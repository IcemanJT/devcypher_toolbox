from base import AbstractEncoder
import hashlib

class sha224(AbstractEncoder):
    name: str = "sha224"
    is_symmetric: bool = False
    _instance = None

    def encode(self, data: str, key: str = None, **kwargs) -> str:
        sha224 = hashlib.sha224()
        sha224.update(data.encode('utf-8'))
        return sha224.hexdigest()

    def decode(self, data: str, key: str = None, **kwargs) -> str:
        raise NotImplementedError("SHA-224 is a one-way hash function and cannot be decoded")