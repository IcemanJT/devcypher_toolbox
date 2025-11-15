from base import AbstractEncoder

class Atbash(AbstractEncoder):
    name: str = "atbash"
    is_symmetric: bool = True
    _instance = None

    def encode(self, data: str, key: str = None, **kwargs) -> str:
        result = ""
        for char in data:
            if char.isalpha():
                if char.isupper():
                    result += chr(90 - (ord(char) - 65))
                else:
                    result += chr(122 - (ord(char) - 97))
            else:
                result += char
        return result

    def decode(self, data: str, key: str = None, **kwargs) -> str:
        return self.encode(data)