from encoder import Encoder
import base64

class Decoder:
    _instance = None
    _encoder_instance = None
    
    def __init__(self):
        raise RuntimeError("Decoder class is made in Singleton manner, use get_instance instead!")
    
    @classmethod
    def get_instance(cls):
        if cls._instance == None:
            cls._instance = cls.__new__(cls)
            cls._encoder_instance = Encoder.get_instance()
        return cls._instance

    @property
    def available_ciphers(self):
        return ["cesar", "atbash", "rot13", "base64"]

    def cesar(self, text: str, key: str):
        shift = int(key) #using key argument as shift value
        #using encoder to reverse decode
        return self._encoder_instance.cesar(text, str(-shift))

    def atbash(self, text: str, key = None):
        #atbash is symetic
        return self._encoder_instance.atbash(text)

    def rot13(self, text, key = None):
        return self.cesar(text, 13)