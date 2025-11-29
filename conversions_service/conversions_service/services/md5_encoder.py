import hashlib
from .base import AbstractEncoder
import hashlib

class MD5Encoder(AbstractEncoder):
    name: str = "md5"
    is_symmetric: bool = False

    def encode(self, data: str, key: str, **kwargs) -> str:
        md5_hash = hashlib.md5(data.encode('utf-8'))
        return md5_hash.hexdigest()

    def decode(self, data: str, key: str, **kwargs) -> str:
        raise NotImplementedError("MD5 is a one-way hash function and cannot be decoded.")