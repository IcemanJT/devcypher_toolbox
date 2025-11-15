from base import AbstractEncoder
import hashlib  

class MD5(AbstractEncoder):

    _instance = None

    def encode(self, data: str, key: str = None, **kwargs) -> str:
        md5 = hashlib.md5(data.encode())
        return md5.hexdigest()

    def decode(self, data: str, key: str = None, **kwargs) -> str:
        raise NotImplementedError("MD5 is a one-way hash function and cannot be decoded")