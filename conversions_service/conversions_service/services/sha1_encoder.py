from .base import AbstractEncoder
import hashlib

class Sha1Encoder(AbstractEncoder):
    name: str = "sha1"
    is_symmetric: bool = False

    def encode(self, data: str, key: str = None, **kwargs) -> str:
        sha1_hash = hashlib.sha1()
        sha1_hash.update(data.encode('utf-8'))
        return sha1_hash.hexdigest()

    def decode(self, data: str, key: str = None, **kwargs) -> str:
        raise NotImplementedError("SHA-256 is a one-way hash function and cannot be decoded")