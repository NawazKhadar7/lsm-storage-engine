import json,struct,zlib,os
from pathlib import Path
from .common import dumps
MAX_RECORD=1024*1024
class WAL:
    def __init__(self,path):self.path=Path(path);self.path.parent.mkdir(parents=True,exist_ok=True);self.path.touch(exist_ok=True)
    def append(self,record):
        data=dumps(record).encode()
        if len(data)>MAX_RECORD:raise ValueError('record too large')
        frame=struct.pack('>II',len(data),zlib.crc32(data))+data
        with self.path.open('ab') as f:f.write(frame);f.flush();os.fsync(f.fileno())
    def recover(self):
        records=[];data=self.path.read_bytes();offset=0
        while offset<len(data):
            if len(data)-offset<8:break
            length,checksum=struct.unpack_from('>II',data,offset)
            if length>MAX_RECORD:raise ValueError('invalid WAL frame length')
            if offset+8+length>len(data):break
            payload=data[offset+8:offset+8+length]
            if zlib.crc32(payload)!=checksum:raise ValueError('WAL checksum mismatch')
            records.append(json.loads(payload));offset+=8+length
        # Remove an incomplete final record so future appends remain recoverable.
        if offset<len(data):
            with self.path.open('r+b') as f:f.truncate(offset);f.flush();os.fsync(f.fileno())
        return records
    def reset(self):
        with self.path.open('wb') as f:f.flush();os.fsync(f.fileno())
