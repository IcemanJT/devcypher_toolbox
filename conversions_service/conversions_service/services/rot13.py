from cesar import Cesar

class Rot13(Cesar):

    _instance = None

    def encode(self, data: str, key: str = None, **kwargs) -> str:
        return super().encode(data, '13')

    def decode(self, data: str, key: str = None, **kwargs) -> str:
        return super().decode(data, '13')