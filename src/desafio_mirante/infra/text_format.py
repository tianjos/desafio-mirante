from desafio_mirante.core.entities.money import Money
from desafio_mirante.core.entities.sale import Sale


class TextFormat:
    def __init__(self, sale: Sale):
        self.sale = sale

    def format(self) -> str:
        total = self.sale.total()
        most_sold_product = self.sale.most_sold_product()
        total_by_product = self.sale.total_by_product()

        lines = []
        for product, quantity in total_by_product.items():
            total_price = Money(product.price.amount * quantity)
            lines.append(
                f'{product.name} - {quantity} x BRL {product.price} = BRL {total_price}'
            )
        lines.append(f'Total: BRL {total}')
        lines.append(f'Most sold product: {most_sold_product.name}')
        return '\n'.join(lines)
