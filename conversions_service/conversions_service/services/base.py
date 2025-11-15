from abc import ABC, abstractmethod


class AbstractEncoder(ABC):
    name: str = None
    is_symmetric: bool = False

    @classmethod
    def get_instance(cls):
        if not hasattr(cls, "_instance"):
            cls._instance = cls.__new__(cls)
        return cls._instance

    @abstractmethod
    def encode(self, data: str, key: str, **kwargs) -> str:
        raise NotImplementedError("Subclasses must implement this method")

    @abstractmethod
    def decode(self, data: str, key: str, **kwargs) -> str:
        raise NotImplementedError("Subclasses must implement this method")