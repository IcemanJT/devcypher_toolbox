from .base import AbstractEncoder
import hashlib

class Sha512Encoder(AbstractEncoder):
    name: str = "sha512"
    is_symmetric: bool = False

    def encode(self, data: str, key: str = None, **kwargs) -> str:
        sha512_hash = hashlib.sha512()
        sha512_hash.update(data.encode('utf-8'))
        return sha512_hash.hexdigest()  
    
    def decode(self, data: str, key: str = None, **kwargs) -> str:
        raise NotImplementedError("SHA-512 is a one-way hash function and cannot be decoded")