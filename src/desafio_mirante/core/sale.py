from collections import defaultdict
from dataclasses import dataclass, field

from desafio_mirante.core.sale_item import SaleItem
from desafio_mirante.core.product import Product


@dataclass(frozen=True)
class Sale:
    items: list[SaleItem] = field(default_factory=list)

    def total_by_product(self) -> dict[Product, int]:
        total = defaultdict(int)
        for sale_item in self.items:
            total[sale_item.product] += sale_item.quantity
        return dict(total)

    def total(self):
        return sum(sale_item.total_price() for sale_item in self.items)

    def best_selling_product(self):
        products = self.total_by_product()
        return max(products, key=products.get)
