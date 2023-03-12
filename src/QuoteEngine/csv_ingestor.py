import csv
from typing import List

from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel


class CSVIngestor(IngestorInterface):
    """Ingestor for .csv files."""
    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest exception')

        quotes = []
        with open(path, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                new_quote = QuoteModel(row[0], row[1])
                quotes.append(new_quote)
        return quotes