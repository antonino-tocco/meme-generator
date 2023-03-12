from typing import List

from .ingestor_interface import IngestorInterface
from .csv_ingestor import CSVIngestor
from .docx_ingestor import DocxIngestor
from .pdf_ingestor import PDFIngestor
from .txt_ingestor import TxtIngestor
from .quote_model import QuoteModel


class Ingestor(IngestorInterface):
    """Ingestor for .txt, .docx, .pdf, and .csv files."""
    ingestors = [TxtIngestor, DocxIngestor, PDFIngestor, CSVIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse a file and return a list of QuoteModel objects."""
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)

        raise Exception("Cannot ingest exception.")