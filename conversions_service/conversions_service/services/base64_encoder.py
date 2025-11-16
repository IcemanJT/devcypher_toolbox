
import base64

from .base import AbstractEncoder


class Base64Encoder(AbstractEncoder):
    name: str = "base64"
    is_symmetric: bool = True

    def encode(self, data: str, key: str, **kwargs) -> str:
        encoded_bytes = base64.b64encode(data.encode('utf-8'))
        return encoded_bytes.decode('utf-8')

    def decode(self, data: str, key: str, **kwargs) -> str:
        decoded_bytes = base64.b64decode(data.encode('utf-8'))
        return decoded_bytes.decode('utf-8')

