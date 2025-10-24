import os,json,hashlib
from pathlib import Path
from .common import atomic_json,dumps
from .wal import WAL
from .sstable import read_table,write_table
class LSM:
    """Single-writer local disk engine. No multi-process writer locking."""
    def __init__(self,directory,mem_limit=16):
        if mem_limit<1:raise ValueError('positive memtable limit required')
        self.directory=Path(directory);self.directory.mkdir(parents=True,exist_ok=True);self.limit=mem_limit;self.mem={};self.manifest=self.directory/'manifest.json'
        state={'tables':[],'checkpoint':0,'generation':0}
        if self.manifest.exists():
            e=json.loads(self.manifest.read_text());state=e['state']
            if hashlib.sha256(dumps(state).encode()).hexdigest()!=e['sha256']:raise ValueError('manifest checksum mismatch')
        self.tables=state['tables'];self.checkpoint=state['checkpoint'];self.generation=state['generation'];self.seq=self.checkpoint
        for name in self.tables:
            if Path(name).name!=name:raise ValueError('invalid table filename')
            read_table(self.directory/name)
        self.wal=WAL(self.directory/'wal.bin');self.sync_directory()
        for record in self.wal.recover():
            self.seq=max(self.seq,record['seq'])
            if record['seq']>self.checkpoint:self.mem[record['key']]=[record['seq'],record['value'],record['deleted']]
    def sync_directory(self):
        if hasattr(os,'O_DIRECTORY'):
            fd=os.open(self.directory,os.O_RDONLY|os.O_DIRECTORY)
            try:os.fsync(fd)
            finally:os.close(fd)
    def save_manifest(self):
        state={'tables':self.tables,'checkpoint':self.checkpoint,'generation':self.generation}
        atomic_json(self.manifest,{'state':state,'sha256':hashlib.sha256(dumps(state).encode()).hexdigest()});self.sync_directory()
    def mutate(self,key,value,deleted):
        if not isinstance(key,str) or not key or len(key)>1024:raise ValueError('invalid key')
        dumps(value);seq=self.seq+1;record={'seq':seq,'key':key,'value':value,'deleted':deleted}
        self.wal.append(record);self.seq=seq;self.mem[key]=[seq,value,deleted]
        if len(self.mem)>=self.limit:self.flush()
    def put(self,key,value):self.mutate(key,value,False)
    def delete(self,key):self.mutate(key,None,True)
    def get(self,key):
        best=self.mem.get(key)
        for name in reversed(self.tables):
            records,bloom=read_table(self.directory/name)
            if bloom.may_contain(key):
                found=records.get(key)
                if found and (best is None or found[0]>best[0]):best=found
        return None if best is None or best[2] else best[1]
    def flush(self):
        if not self.mem:return
        self.generation+=1;name=f'sst-{self.generation:08d}.json';write_table(self.directory/name,self.mem);self.sync_directory()
        self.tables.append(name);self.checkpoint=max(self.checkpoint,max(v[0] for v in self.mem.values()));self.save_manifest();self.mem.clear();self.wal.reset()
    def compact(self):
        if len(self.tables)<2:return
        merged={};old=list(self.tables)
        for name in old:
            records,_=read_table(self.directory/name)
            for key,value in records.items():
                if key not in merged or value[0]>merged[key][0]:merged[key]=value
        self.generation+=1;name=f'sst-{self.generation:08d}.json';write_table(self.directory/name,merged);self.sync_directory();self.tables=[name];self.save_manifest()
        for filename in old:(self.directory/filename).unlink()
        self.sync_directory()
