import csv
from datetime import datetime
from tempfile import NamedTemporaryFile
from typing import TypedDict
from zoneinfo import ZoneInfo

import pytest

from desafio_mirante.infra.file_parser import SaleParser
from desafio_mirante.application.calculation_use_case import CalculationUseCase
from desafio_mirante.app import App
from tests.factories import ProductFactory, ArgumentsFactory


class Row(TypedDict):
    name: str
    price: float
    sold_at: datetime
    quantity: int


@pytest.fixture
def csv_factory():
    def _csv_factory(rows: list[Row], path: str, headers: list[str]):
        with open(path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            writer.writerows(
                {
                    key: (
                        value.isoformat() if isinstance(value, datetime) else value
                    )
                    for key, value in row.items()
                }
                for row in rows
            )

    return _csv_factory


@pytest.fixture
def temp_csv_file(csv_factory):
    def temp_csv_file_factory(rows):
        with NamedTemporaryFile(mode='w', suffix='.csv') as temp_file:
            headers = list(
                filter(
                    lambda attr: not attr.startswith('_'),
                    vars(ProductFactory),
                )
            )
            csv_factory(rows, temp_file.name, headers)

            temp_file.flush()

            yield temp_file

    return temp_csv_file_factory


@pytest.fixture
def app():
    use_case = CalculationUseCase(parser=SaleParser())
    return App(use_case=use_case)


@pytest.fixture
def make_product_for_date():
    def _make_product_for_date(year: int, month: int, day: int) -> dict:
        product = ProductFactory(
            sold_at=datetime(year, month, day, tzinfo=ZoneInfo('UTC'))
        )

        return {
            'name': product['name'],
            'price': product['price'],
            'sold_at': product['sold_at'].isoformat(),
            'quantity': product['quantity'],
        }

    return _make_product_for_date


@pytest.fixture
def make_arguments_for_date_range():
    def _make_arguments_for_date_range(start: datetime, end: datetime, file_path: str, format:str) -> dict:
        arguments = ArgumentsFactory(file=file_path)
        arguments['start'] = start
        arguments['end'] = end
        arguments['format'] = format
        return arguments

    return _make_arguments_for_date_range
