from decimal import Decimal

import pytest

from desafio_mirante.core.product import Product
from desafio_mirante.core.sale import Sale
from desafio_mirante.core.sale_item import SaleItem
from desafio_mirante.core.money import Money


@pytest.mark.unit
def test_total_sales_by_product():
    sale = Sale(
        items=[
            SaleItem(
                product=Product(name='Product A', price=Money(Decimal('10.0'))),
                sold_at='2024-01-01',
                quantity=2,
            ),
            SaleItem(
                product=Product(name='Product B', price=Money(Decimal('20.0'))),
                sold_at='2024-01-02',
                quantity=1,
            ),
            SaleItem(
                product=Product(name='Product A', price=Money(Decimal('10.0'))),
                sold_at='2024-01-03',
                quantity=3,
            ),
        ]
    )

    assert sale.total_by_product() == {
        Product(name='Product A', price=Money(Decimal('10.0'))): 5,
        Product(name='Product B', price=Money(Decimal('20.0'))): 1,
    }


@pytest.mark.unit
def test_total_sales():
    sale = Sale(
        items=[
            SaleItem(
                product=Product(name='Product A', price=Money(Decimal('10.0'))),
                sold_at='2024-01-01',
                quantity=2,
            ),
            SaleItem(
                product=Product(name='Product B', price=Money(Decimal('20.0'))),
                sold_at='2024-01-02',
                quantity=1,
            ),
            SaleItem(
                product=Product(name='Product A', price=Money(Decimal('10.0'))),
                sold_at='2024-01-03',
                quantity=3,
            ),
        ]
    )

    assert sale.total() == Money(Decimal('70.0'))


@pytest.mark.unit
def test_best_selling_product():
    sale = Sale(
        items=[
            SaleItem(
                product=Product(name='Product B', price=Money(Decimal('20.0'))),
                sold_at='2024-01-01',
                quantity=2,
            ),
            SaleItem(
                product=Product(name='Product B', price=Money(Decimal('20.0'))),
                sold_at='2024-01-02',
                quantity=2,
            ),
            SaleItem(
                product=Product(name='Product A', price=Money(Decimal('20.0'))),
                sold_at='2024-01-03',
                quantity=1,
            ),
            SaleItem(
                product=Product(name='Product B', price=Money(Decimal('20.0'))),
                sold_at='2024-01-03',
                quantity=3,
            ),
        ]
    )

    assert sale.most_sold_product() == Product(
        name='Product B', price=Money(Decimal('20.0'))
    )
