from base import AbstractEncoder
import hashlib

class Sha3_512(AbstractEncoder):
    name: str = "sha3_512"
    is_symmetric: bool = False
    _instance = None

    def encode(self, data: str, key: str = None, **kwargs) -> str:
        sha3_512_hash = hashlib.sha3_512()
        sha3_512_hash.update(data.encode('utf-8'))
        return sha3_512_hash.hexdigest()

    def decode(self, data: str, key: str = None, **kwargs) -> str:
        raise NotImplementedError("SHA3-512 is a one-way hash function and cannot be decoded")