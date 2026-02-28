from datetime import datetime
from decimal import Decimal

from desafio_mirante.core.sale_item import SaleItem
from desafio_mirante.core.product import Product
from desafio_mirante.core.money import Money


def test_sale_item_serialization():
    product = Product(name='Test Product', price=Money(Decimal('15.50')))
    sale_item = SaleItem(
        product=product, sold_at=datetime.fromisoformat('2024-01-01'), quantity=2
    )

    assert sale_item.as_text() == 'Test Product - 2 x BRL 15.50 = BRL 31.00'
    assert (
        sale_item.as_json()
        == f'{{"product": {product.as_json()}, "sold_at": "2024-01-01T00:00:00", "quantity": 2}}'
    )
