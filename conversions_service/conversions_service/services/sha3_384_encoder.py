from .base import AbstractEncoder
import hashlib

class Sha3_384Encoder(AbstractEncoder):
    name: str = "sha3_384"
    is_symmetric: bool = False

    def encode(self, data: str, key: str = None, **kwargs) -> str:
        sha3_384_hash = hashlib.sha3_384()
        sha3_384_hash.update(data.encode('utf-8'))
        return sha3_384_hash.hexdigest()

    def decode(self, data: str, key: str = None, **kwargs) -> str:
        raise NotImplementedError("SHA3-384 is a one-way hash function and cannot be decoded")