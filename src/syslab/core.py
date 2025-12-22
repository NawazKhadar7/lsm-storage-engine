import tempfile
from pathlib import Path
from .common import validate_case
from .lsm import LSM
FAMILIES=('overwrite','delete','flush','compact','recover','torn-wal')
def run_case(case):
    validate_case(case)
    if case['family'] not in FAMILIES:raise ValueError('unknown storage family')
    n=case['size'];f=case['family'];model={};reads=0
    with tempfile.TemporaryDirectory() as directory:
        db=LSM(directory,8 if f in ('flush','compact') else n+1)
        for i in range(n):
            key=f'k{i%(max(1,n//4))}' if f=='overwrite' else f'k{i}';db.put(key,i);model[key]=i
        if f=='delete':
            for i in range(0,n,3):db.delete(f'k{i}');model.pop(f'k{i}')
        if f=='compact':db.flush();db.compact()
        if f in ('recover','torn-wal'):
            if f=='torn-wal':
                with (Path(directory)/'wal.bin').open('ab') as file:file.write(b'\x00\x00\x00')
            db=LSM(directory,n+1)
            # A post-recovery append must survive a second restart.
            db.put('recovered',123);model['recovered']=123;db=LSM(directory,n+2)
        matches=True
        for i in range(n):
            key=f'k{i}';value=db.get(key);reads+=1;matches=matches and value==model.get(key)
        matches=matches and all(db.get(k)==v for k,v in model.items())
        tables=len(db.tables)
    return {'metrics':{'writes':n,'reads':reads,'live_keys':len(model),'model_matches':matches,'tables':tables,'recovered':f in ('recover','torn-wal')},'output':{'sample':dict(list(model.items())[:8]),'single_writer':True}}
