from .cesar_encoder import CesarEncoder

class Rot13Encoder(CesarEncoder):
    name: str = "rot13"
    is_symmetric: bool = True

    def encode(self, data: str, key: str = None, **kwargs) -> str:
        return super().encode(data, '13')

    def decode(self, data: str, key: str = None, **kwargs) -> str:
        return super().decode(data, '13')