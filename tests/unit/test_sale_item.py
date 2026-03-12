from datetime import datetime
from decimal import Decimal

import pytest

from desafio_mirante.core.entities.sale_item import SaleItem
from desafio_mirante.core.entities.product import Product
from desafio_mirante.core.entities.money import Money


@pytest.mark.unit
def test_sale_item_total_price():
    product = Product(name='Test Product', price=Money(Decimal('15.50')))
    sale_item = SaleItem(
        product=product, sold_at=datetime.fromisoformat('2024-01-01'), quantity=2
    )

    assert sale_item.total_price == Money(Decimal('31.00'))


@pytest.mark.unit
def test_simple_sale_item_ordering():
    product1 = Product(name='Product 1', price=Money(Decimal('10.00')))
    product2 = Product(name='Product 2', price=Money(Decimal('20.00')))

    sale_item1 = SaleItem(
        product=product1, sold_at=datetime.fromisoformat('2024-01-01'), quantity=1
    )
    sale_item2 = SaleItem(
        product=product2, sold_at=datetime.fromisoformat('2024-01-02'), quantity=1
    )

    assert sale_item1 < sale_item2


@pytest.mark.unit
def test_sale_complex_item_ordering():
    productA = Product(name='Test Product', price=Money(Decimal('10.00')))
    productB = Product(name='Another Product', price=Money(Decimal('15.00')))

    sale_item1 = SaleItem(
        product=productA, sold_at=datetime.fromisoformat('2024-01-01'), quantity=2
    )
    sale_item2 = SaleItem(
        product=productB, sold_at=datetime.fromisoformat('2024-01-01'), quantity=1
    )   

    assert sale_item1 > sale_item2
