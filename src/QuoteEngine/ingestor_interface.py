from abc import ABC, abstractmethod


class IngestorInterface(ABC):
    """Interface for ingestors."""
    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path):
        extension = path.split('.')[-1]
        return extension in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path):
        pass