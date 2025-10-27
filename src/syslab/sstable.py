import hashlib,json
from .common import atomic_json,dumps
from .bloom import Bloom

def write_table(path,records):
    entries={k:records[k] for k in sorted(records)};bloom=Bloom(max(2048,len(entries)*16))
    for key in entries:bloom.add(key)
    payload={'records':entries,'bloom':{'bits':bloom.bits,'hashes':bloom.hashes,'bitmap':list(bloom.bitmap)}}
    atomic_json(path,{'payload':payload,'sha256':hashlib.sha256(dumps(payload).encode()).hexdigest()})
def read_table(path):
    value=json.loads(path.read_text());payload=value['payload']
    if hashlib.sha256(dumps(payload).encode()).hexdigest()!=value['sha256']:raise ValueError('SST checksum mismatch')
    info=payload['bloom'];return payload['records'],Bloom(info['bits'],info['hashes'],info['bitmap'])
