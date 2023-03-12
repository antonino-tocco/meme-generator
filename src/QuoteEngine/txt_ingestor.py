from typing import List

from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel



class TxtIngestor(IngestorInterface):
    """Ingestor for .txt files."""

    allowed_extensions = ["txt"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse a .txt file and return a list of QuoteModel objects."""
        if not cls.can_ingest(path):
            raise Exception("Cannot ingest exception.")

        quotes = []

        with open(path, "r") as file:
            for line in file.readlines():
                body, author = line.split(" - ")
                quotes.append(QuoteModel(body, author))

        return quotes