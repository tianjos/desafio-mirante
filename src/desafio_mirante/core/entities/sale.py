from collections import defaultdict
from dataclasses import dataclass, field
from datetime import datetime
from decimal import Decimal
from functools import cached_property

from desafio_mirante.core.entities.sale_item import SaleItem
from desafio_mirante.core.entities.product import Product
from desafio_mirante.core.entities.money import Money


@dataclass(frozen=True)
class Sale:
    items: list[SaleItem] = field(default_factory=list)
    start_at: datetime | None = field(default=None)
    end_at: datetime | None = field(default=None)

    @cached_property
    def filtered_by_date_range(self) -> list[SaleItem]:
        if self.start_at is None and self.end_at is None:
            return self.items

        filtered_items = []
        for item in self.items:
            if self.start_at and item.sold_at < self.start_at:
                continue
            if self.end_at and item.sold_at > self.end_at:
                continue
            filtered_items.append(item)

        return filtered_items

    def total_by_product(self) -> dict[Product, int]:
        total = defaultdict(Decimal)
        for sale_item in self.filtered_by_date_range:
            total[sale_item.product] += sale_item.total_price().amount
        return dict(total)

    def total(self):
        return sum(
            sale_item.total_price() for sale_item in self.filtered_by_date_range
        ) or Money(Decimal('0.00'))

    def most_sold_product(self) -> Product:
        total = defaultdict(int)
        for sale_item in self.filtered_by_date_range:
            total[sale_item.product] += sale_item.quantity

        products = dict(total)

        if not products:
            return Product(name='No products sold', price=Money(Decimal('0.00')))

        return max(products, key=products.get)
