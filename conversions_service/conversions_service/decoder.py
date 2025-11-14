class Decoder:
    _instance = None
    
    def __init__(self):
        raise RuntimeError("Decoder class is made in Singleton manner, use get_instance instead!")
    
    @classmethod
    def get_instance(cls):
        if cls._instance == None:
            cls._instance = cls.__new__(cls)
        return cls._instance

    #to do
