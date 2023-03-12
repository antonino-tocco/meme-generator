import os
import subprocess

from typing import List

from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel


class PDFIngestor(IngestorInterface):
    """Ingestor for .pdf files."""
    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []
        full_path = os.path.abspath(path)
        lines = subprocess.Popen(['pdftotext', full_path, '-'], stdout=subprocess.PIPE)\
            .communicate()[0].decode('utf-8').split('\f')
        for line in lines:
            if line != "":
                parse = line.split(' - ')
                new_quote = QuoteModel(parse[0], parse[1])
                quotes.append(new_quote)
        return quotes