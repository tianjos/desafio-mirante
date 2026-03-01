from datetime import datetime
from tempfile import NamedTemporaryFile

import pytest

from desafio_mirante.core.dtos.args import ArgsDTO
from desafio_mirante.core.entities.format import Format
from desafio_mirante.infra.file_parser import SaleParser
from desafio_mirante.application.calculation_use_case import CalculationUseCase
from desafio_mirante.app import App

@pytest.fixture
def file_content():
    return """name,price,sold_at,quantity
Notebook,4500.00,2025-03-31,1
Mouse,120.50,2025-03-31,3
Teclado,250.00,2025-03-31,4
Monitor,1899.99,2025-03-31,5
Mouse,120.50,2025-03-31,3
Cadeira Gamer,1399.90,2025-03-31,1
"""


@pytest.fixture
def file_path(file_content):
    with NamedTemporaryFile(mode='w', suffix='.csv') as temp_file:
        temp_file.write(file_content)
        temp_file.flush()
        yield temp_file.name


@pytest.fixture
def args_dto(file_path):
    return ArgsDTO(
        file_path=file_path,
        format=Format.JSON,
        start=datetime.fromisoformat('2025-03-31'),
        end=None
    )

@pytest.fixture
def app(file_path):
    use_case = CalculationUseCase(parser=SaleParser())
    return App(use_case=use_case)
