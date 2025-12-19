import hashlib
class Bloom:
    def __init__(self,bits=2048,hashes=4,bitmap=None):
        if bits<8 or hashes<1:raise ValueError('invalid bloom dimensions')
        self.bits,self.hashes=bits,hashes;self.bitmap=bytearray(bitmap) if bitmap is not None else bytearray((bits+7)//8)
        if len(self.bitmap)!=(bits+7)//8:raise ValueError('invalid bitmap')
    def positions(self,key):
        digest=hashlib.sha256(key.encode()).digest();a=int.from_bytes(digest[:16],'big');b=int.from_bytes(digest[16:],'big')|1
        return [(a+i*b)%self.bits for i in range(self.hashes)]
    def add(self,key):
        for p in self.positions(key):self.bitmap[p//8]|=1<<(p%8)
    def may_contain(self,key):return all(self.bitmap[p//8]&(1<<(p%8)) for p in self.positions(key))
