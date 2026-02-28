from decimal import Decimal

from desafio_mirante.core.product import Product
from desafio_mirante.core.money import Money


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


def test_product_serialization():
    product = Product(name='Test Product', price=Money(Decimal('15.50')))
    assert product.as_text() == 'Test Product - BRL 15.50'
    assert (
        product.as_json()
        == '{"name": "Test Product", "price": {"amount": "15.50", "currency": "BRL"}}'
    )
