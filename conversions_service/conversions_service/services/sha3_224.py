from base import AbstractEncoder
import hashlib

class Sha3_224(AbstractEncoder):
    name: str = "sha3_224"
    is_symmetric: bool = False
    _instance = None

    def encode(self, data: str, key: str = None, **kwargs) -> str:
        sha3_224_hash = hashlib.sha3_224()
        sha3_224_hash.update(data.encode('utf-8'))
        return sha3_224_hash.hexdigest()

    def decode(self, data: str, key: str = None, **kwargs) -> str:
        raise NotImplementedError("SHA3-224 is a one-way hash function and cannot be decoded")