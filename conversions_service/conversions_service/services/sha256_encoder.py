import hashlib
from services.base import AbstractEncoder
class Sha256Encoder(AbstractEncoder):
    name: str = "sha256"
    is_symmetric: bool = False

    def encode(self, data: str, key: str, **kwargs) -> str:
        sha256_hash = hashlib.sha256(data.encode('utf-8'))
        return sha256_hash.hexdigest()

    def decode(self, data: str, key: str, **kwargs) -> str:
        raise NotImplementedError("SHA256 is a one-way hash function and cannot be decoded.")
