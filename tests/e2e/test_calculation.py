import json
from datetime import datetime
from zoneinfo import ZoneInfo

import pytest

from desafio_mirante.core.dtos.args import ArgsDTO


@pytest.mark.e2e
def test_calculation_json_output(
    tmp_path, csv_factory, app, make_product_for_date, make_arguments_for_date_range
):
    file_path = tmp_path / 'sales.csv'
    product = make_product_for_date(year=2025, month=10, day=1)
    csv_factory(
        [product], file_path, headers=['name', 'price', 'sold_at', 'quantity']
    )
    arguments = make_arguments_for_date_range(
        start=datetime(2025, 1, 1, tzinfo=ZoneInfo('UTC')),
        end=datetime(2026, 1, 1, tzinfo=ZoneInfo('UTC')),
        file_path=str(file_path),
        format='json'
    )
    dto = ArgsDTO(**arguments)

    result = app.run(args_dto=dto)
    
    assert json.loads(result)

