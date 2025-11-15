import importlib
import logging

logger = logging.getLogger(__name__)

class EncodeApi:

    def __init__(self):
        self.services = None

    @classmethod
    def get_instance(cls):
        if not hasattr(cls, "_instance"):
            cls._instance = cls.__new__(cls)
            cls._instance.initialize()
        return cls._instance


    def initialize(self):
        native_dir = importlib.import_module(f"conversions_service.services")
        self.services = {}
        for service_name in dir(native_dir):
            if service_name.endswith("Encoder"):
                service_class = getattr(native_dir, service_name)
                service_instance = service_class.get_instance()
                self.services[service_instance.name]= service_instance
        logger.info(f"Loaded encoding services: {list(self.services.keys())}")



    def encode(self,data: dict) -> str:
        if not data.get("method") or not data.get("data"):
            raise ValueError("Cipher and data must be provided for encoding.")
        return self.services[data["method"]].encode(data["data"], data.get("key", ""), **data.get("options", {}))

    def decode(self,data: dict) -> str:
        if not data.get("method") or not data.get("data"):
            raise ValueError("Cipher and data must be provided for decoding.")
        return self.services[data["method"]].decode(data["data"], data.get("key", ""), **data.get("options", {}))

    @property
    def available_decode_ciphers(self):
        return list(filter(lambda encoder: encoder.is_symmetric, self.services.keys()))

    @property
    def available_encode_ciphers(self):
        return list(self.services.keys())