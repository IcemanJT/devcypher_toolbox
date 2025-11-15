from base import AbstractEncoder
import hashlib

class Sha256(AbstractEncoder):

    _instance = None

    def encode(self, data: str, key: str = None, **kwargs) -> str:
        sha256_hash = hashlib.sha256()
        sha256_hash.update(data.encode('utf-8'))
        return sha256_hash.hexdigest()

    def decode(self, data: str, key: str = None, **kwargs) -> str:
        raise NotImplementedError("SHA-256 is a one-way hash function and cannot be decoded")