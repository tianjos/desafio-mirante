from decimal import Decimal

import pytest

from desafio_mirante.core.product import Product
from desafio_mirante.core.money import Money


@pytest.mark.unit
def test_product_sort():
    products = [
        Product(name='Product 3', price=Money(Decimal('30.00'))),
        Product(name='Product 1', price=Money(Decimal('10.00'))),
        Product(name='Product 2', price=Money(Decimal('20.00'))),
    ]

    assert sorted(products) == [
        Product(name='Product 1', price=Money(Decimal('10.00'))),
        Product(name='Product 2', price=Money(Decimal('20.00'))),
        Product(name='Product 3', price=Money(Decimal('30.00'))),
    ]
