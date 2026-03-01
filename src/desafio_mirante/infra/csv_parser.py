import csv
from dataclasses import dataclass
from decimal import Decimal
from datetime import datetime
from pathlib import Path

from desafio_mirante.core.money import Money
from desafio_mirante.core.product import Product
from desafio_mirante.core.sale_item import SaleItem
from desafio_mirante.core.sale import Sale


@dataclass(frozen=True, kw_only=True)
class CsvParser:
    file_path: Path
    strict: bool = True

    def as_dict(self) -> list[dict[str, str]]:
        with self.file_path.open('r', encoding='utf-8', newline='') as csv_file:
            reader = csv.DictReader(csv_file)
            return [row for row in reader]

    def as_sales(self) -> Sale:
        with self.file_path.open('r', encoding='utf-8', newline='') as csv_file:
            reader = csv.DictReader(csv_file)

            sale_items = []
            for row in reader:
                try:
                    product = Product(name=row['name'], price=Money(Decimal(row['price'])))
                    sale_items.append(
                        SaleItem(
                            product=product,
                            sold_at=datetime.fromisoformat(row['sold_at']),
                            quantity=int(row['quantity']),
                        )
                    )
                except (TypeError, KeyError, ValueError):
                    if self.strict:
                        raise ValueError(f'Error parsing row: {row}')

            return Sale(items=sale_items)

    def as_products(self) -> list[Product]:
        with self.file_path.open('r', encoding='utf-8', newline='') as csv_file:
            reader = csv.DictReader(csv_file)

            products = []
            for row in reader:
                try:
                    products.append(Product(**row))
                except TypeError:
                    if self.strict:
                        raise ValueError(f'Error parsing row: {row}')
            return products
