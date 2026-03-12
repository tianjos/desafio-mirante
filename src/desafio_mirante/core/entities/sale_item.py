
from dataclasses import dataclass, field
from datetime import datetime
from .product import Product
from .money import Money


@dataclass(frozen=True, slots=True)
class SaleItem:
    product: Product
    sold_at: datetime = field(compare=False)
    quantity: int

    @property
    def total_price(self):
        return Money(self.product.price.amount * self.quantity)

    def __eq__(self, other):
        if not isinstance(other, SaleItem):
            return NotImplemented
        return (
            self.product == other.product and
            self.quantity == other.quantity and
            self.sold_at == other.sold_at
        )

    def __lt__(self, other):
        if not isinstance(other, SaleItem):
            return NotImplemented
        return self.total_price < other.total_price

    def __le__(self, other):
        if not isinstance(other, SaleItem):
            return NotImplemented
        return self.total_price <= other.total_price
    
    def __gt__(self, other):
        if not isinstance(other, SaleItem):
            return NotImplemented
        return self.total_price > other.total_price
    
    def __ge__(self, other):
        if not isinstance(other, SaleItem):
            return NotImplemented
        return self.total_price >= other.total_price