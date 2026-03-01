import csv
import logging

from desafio_mirante.core.ports.file_parser import FileParser
from desafio_mirante.core.dtos.sale_item import SaleItemDTO

logger = logging.getLogger(__name__)


class SaleParser(FileParser[SaleItemDTO]):
    def from_csv(self, file_path: str) -> list[SaleItemDTO]:
        with open(file_path, 'r', encoding='utf-8', newline='') as csv_file:
            reader = csv.DictReader(csv_file)
            try:
                return [SaleItemDTO(**row) for row in reader]
            except TypeError as e:
                logger.error(f'Error parsing CSV file: {e}')
                raise ValueError('Missing required fields in CSV file')
