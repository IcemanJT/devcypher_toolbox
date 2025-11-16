from .base import AbstractEncoder
import hashlib

class Blake2sEncoder(AbstractEncoder):
    name: str = "blake2s"
    is_symmetric: bool = False

    def encode(self, data: str, key: str = None, **kwargs) -> str:
        blake2s_hash = hashlib.blake2s()
        blake2s_hash.update(data.encode('utf-8'))
        return blake2s_hash.hexdigest()  

    def decode(self, data: str, key: str = None, **kwargs) -> str:
        raise NotImplementedError("BLAKE2s is a one-way hash function and cannot be decoded")