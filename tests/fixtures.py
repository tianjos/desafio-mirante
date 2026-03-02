import csv
from tempfile import NamedTemporaryFile

import pytest

from desafio_mirante.infra.file_parser import SaleParser
from desafio_mirante.application.calculation_use_case import CalculationUseCase
from desafio_mirante.app import App
from tests.factories import ProductFactory


@pytest.fixture
def csv_factory():
    def _csv_factory(rows, path, headers):
        with open(path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            writer.writerows(rows)
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
