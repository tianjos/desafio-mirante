from dataclasses import dataclass, field
from datetime import datetime

from .product import Product
from .money import Money


@dataclass(frozen=True, slots=True, order=True)
class SaleItem:
    product: Product = field(compare=False)
    sold_at: datetime
    quantity: int

    def total_price(self):
        return Money(self.product.price.amount * self.quantity)
