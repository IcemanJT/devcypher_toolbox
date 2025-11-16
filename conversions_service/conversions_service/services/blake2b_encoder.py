from .base import AbstractEncoder
import hashlib

class Blake2bEncoder(AbstractEncoder):
    name: str = "blake2b"
    is_symmetric: bool = False

    def encode(self, data: str, key: str = None, **kwargs) -> str:
        blake2b_hash = hashlib.blake2b()
        blake2b_hash.update(data.encode('utf-8'))
        return blake2b_hash.hexdigest()  

    def decode(self, data: str, key: str = None, **kwargs) -> str:
        raise NotImplementedError("BLAKE2b is a one-way hash function and cannot be decoded")