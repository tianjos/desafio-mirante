from desafio_mirante.core.entities.report import Report


class TextFormat:
    def __init__(self, report: Report):
        self.report = report

    def format(self) -> str:

        lines = []
        for product, total_price in self.report.total_by_product.items():
            lines.append(
                f'{product.name} - unit({product.price}) = total: BRL {total_price}'
            )
        lines.append(f'Total: BRL {self.report.total_sales}')
        lines.append(f'Most sold product: {", ".join([product.name for product in self.report.most_sold_product])}')
        return '\n'.join(lines)
