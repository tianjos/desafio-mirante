from dataclasses import dataclass

from desafio_mirante.core.entities.money import Money
from desafio_mirante.core.entities.product import Product


@dataclass(frozen=True)
class Report:
    total_sales: Money
    most_sold_product: list[Product]
    total_by_product: dict[Product, int]

    def to_dict(self):
        return {
            'total_sales': self.total_sales,
            'most_sold_product': ', '.join([p.name for p in self.most_sold_product]),
            'total_by_product': {
                p.name: q for p, q in self.total_by_product.items()
            },
        }
