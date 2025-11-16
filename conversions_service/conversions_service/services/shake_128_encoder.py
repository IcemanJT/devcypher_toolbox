from .base import AbstractEncoder
import hashlib

class Shake_128Encoder(AbstractEncoder):
    name: str = "shake_128"
    is_symmetric: bool = False

    def encode(self, data: str, key: str = None, **kwargs) -> str:
        shake_128_hash = hashlib.shake_128()
        shake_128_hash.update(data.encode('utf-8'))
        # Default output length for SHAKE128 is 32 bytes (256 bits)
        output_length = kwargs.get('output_length', 32)
        return shake_128_hash.hexdigest(output_length)  

    def decode(self, data: str, key: str = None, **kwargs) -> str:
        raise NotImplementedError("SHAKE-128 is a one-way hash function and cannot be decoded")