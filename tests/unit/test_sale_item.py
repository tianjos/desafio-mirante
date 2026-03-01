from datetime import datetime
from decimal import Decimal

import pytest

from desafio_mirante.core.sale_item import SaleItem
from desafio_mirante.core.product import Product
from desafio_mirante.core.money import Money


@pytest.mark.unit
def test_sale_item_total_price():
    product = Product(name='Test Product', price=Money(Decimal('15.50')))
    sale_item = SaleItem(
        product=product, sold_at=datetime.fromisoformat('2024-01-01'), quantity=2
    )

    assert sale_item.total_price() == Money(Decimal('31.00'))
