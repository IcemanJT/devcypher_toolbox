import base64

class Encoder:
    _instance = None
    
    def __init__(self):
        raise RuntimeError("Encoder class is made in Singleton manner, use get_instance instead!")
    
    @classmethod
    def get_instance(cls):
        if cls._instance == None:
            cls._instance = cls.__new__(cls)
        return cls._instance

    @property
    def available_ciphers(self):
        return ["cesar", "atbash", "rot13", "base64"]

    def cesar(self, text: str, key: str):
        shift = int(key) #using key argument as shift value

        result = ""
        for char in text:
            if char.isalpha():
                ascii_offset = 65 if char.isupper() else 97
                result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            else:
                result += char
        
        return result

    def atbash(self, text: str, key = None):
        result = ""
        for char in text:
            if char.isalpha():
                if char.isupper():
                    result += chr(90 - (ord(char) - 65))
                else:
                    result += chr(122 - (ord(char) - 97))
            else:
                result += char
        return result

    def rot13(self, text, key = None):
        return self.cesar(text, 13)