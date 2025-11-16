from .base import AbstractEncoder

class CesarEncoder(AbstractEncoder):
    name: str = "cesar"
    is_symmetric: bool = True

    def encode(self, data: str, key: str, **kwargs) -> str:
        shift = int(key)

        result = ""
        for char in data:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                result += chr((ord(char) - base + shift) % 26 + base)
            else:
                result += char
        return result


    def decode(self, data: str, key: str, **kwargs) -> str:
        return self.encode(data, str(-int(key)))