from base import AbstractEncoder
import hashlib

class shake_256(AbstractEncoder):
    name: str = "shake_256"
    is_symmetric: bool = False
    _instance = None

    def encode(self, data: str, key: str = None, **kwargs) -> str:
        shake_256_hash = hashlib.shake_256()
        shake_256_hash.update(data.encode('utf-8'))
        # Default output length for SHAKE256 is 64 bytes (512 bits)
        output_length = kwargs.get('output_length', 64)
        return shake_256_hash.hexdigest(output_length)  

    def decode(self, data: str, key: str = None, **kwargs) -> str:
        raise NotImplementedError("SHAKE-256 is a one-way hash function and cannot be decoded")