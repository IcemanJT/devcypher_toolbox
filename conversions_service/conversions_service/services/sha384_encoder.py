from .base import AbstractEncoder
import hashlib

class Sha384Encoder(AbstractEncoder):
    name: str = "sha384"
    is_symmetric: bool = False

    def encode(self, data: str, key: str = None, **kwargs) -> str:
        sha384_hash = hashlib.sha384()
        sha384_hash.update(data.encode('utf-8'))
        return sha384_hash.hexdigest()  

    def decode(self, data: str, key: str = None, **kwargs) -> str:
        raise NotImplementedError("SHA-384 is a one-way hash function and cannot be decoded")