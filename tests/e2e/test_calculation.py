import json

import pytest

from tests.factories import ProductFactory, ArgumentsFactory
from desafio_mirante.core.dtos.args import ArgsDTO


@pytest.mark.e2e
def test_calculation_json_output2(tmp_path, csv_factory, app):
    file_path = tmp_path / 'sales.csv'
    product = ProductFactory()
    csv_factory([product], file_path, headers=['name', 'price', 'sold_at', 'quantity'])
    arguments = ArgumentsFactory(
        file=file_path, format='json', with_start_and_end=True
    )
    dto = ArgsDTO(**arguments)
    
    result = app.run(args_dto=dto)
    assert result == json.dumps({
        'total_sales': product['price'] * product['quantity'],
        'total_items': product['quantity'],
        'most_sold_product': product['name'],
    })

    assert not tmp_path.exists()

@pytest.mark.skip
def test_calculation_json_output(temp_csv_file, app):
    product = ProductFactory()
    file = next(temp_csv_file([product]))
    
    with open(file.name, 'r', encoding='utf-8') as f:
        print(f.readlines())
    #arguments = ArgumentsFactory(
    #    file=next(file), format='json', with_start_and_end=True
    #)
    #dto = ArgsDTO(**arguments)

    #result = app.run(args_dto=dto)

    #assert result == json.dumps({
    #    'total_sales': product['price'] * product['quantity'],
    #    'total_items': product['quantity'],
    #    'most_sold_product': product['name'],
    #})


@pytest.mark.skip
def test_calculation_text_output(temp_csv_file, app):
    products = ProductFactory.create_batch(10)
    file = temp_csv_file(products)
    arguments = ArgumentsFactory(file=file, format='text', with_start_and_end=True)
    dto = ArgsDTO(**arguments)

    result = app.run(args_dto=dto)

    assert 'Total Sales' in result
