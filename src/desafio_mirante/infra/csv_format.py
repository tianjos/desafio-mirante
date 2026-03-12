
import csv
from io import StringIO
from desafio_mirante.core.entities.report import Report

class CSVFormat:
    def __init__(self, report: Report):
        self.report = report

    def format(self) -> str:
        buffer = StringIO()
        fieldnames = ['Product', 'Total Sales']
        writer = csv.DictWriter(buffer, fieldnames=fieldnames)

        # Cabeçalho e totais por produto
        writer.writeheader()
        for product, total in self.report.total_by_product.items():
            writer.writerow({'Product': product.name, 'Total Sales': total})

        # Linha de total geral
        writer.writerow({'Product': '', 'Total Sales': ''})
        writer.writerow({'Product': 'Total Sales', 'Total Sales': self.report.total_sales})

        # Produtos mais vendidos
        buffer.write('Most Sold Product(s),\n')
        for product in self.report.most_sold_product:
            buffer.write(f',{product.name}\n')

        return buffer.getvalue()