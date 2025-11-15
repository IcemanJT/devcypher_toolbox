from base import AbstractEncoder
import hashlib

class Sha3_256(AbstractEncoder):
    name: str = "sha3_256"
    is_symmetric: bool = False
    _instance = None

    def encode(self, data: str, key: str = None, **kwargs) -> str:
        sha3_256_hash = hashlib.sha3_256()
        sha3_256_hash.update(data.encode('utf-8'))
        return sha3_256_hash.hexdigest()

    def decode(self, data: str, key: str = None, **kwargs) -> str:
        raise NotImplementedError("SHA3-256 is a one-way hash function and cannot be decoded")