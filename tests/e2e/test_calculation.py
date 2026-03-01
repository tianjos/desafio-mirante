import pytest


@pytest.mark.e2e
def test_calculation_json_output(args_dto, app):
    expected_output = {
        "Total Sales": 1000.00,
        "Average Sale": 250.00,
        "Total Items Sold": 10
    }
    assert app.run(args_dto=args_dto) == expected_output


@pytest.mark.e2e
def test_calculation_tex_output(e2e_test_runner):
    pass
