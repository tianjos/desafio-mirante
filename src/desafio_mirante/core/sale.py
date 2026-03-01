from collections import defaultdict
from dataclasses import dataclass, field
from datetime import datetime
from functools import cached_property

from desafio_mirante.core.sale_item import SaleItem
from desafio_mirante.core.product import Product


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
        total = defaultdict(int)
        for sale_item in self.filtered_by_date_range:
            total[sale_item.product] += sale_item.quantity
        return dict(total)

    def total(self):
        return sum(sale_item.total_price() for sale_item in self.filtered_by_date_range)

    def best_selling_product(self):
        products = self.total_by_product()
        return max(products, key=products.get)
    