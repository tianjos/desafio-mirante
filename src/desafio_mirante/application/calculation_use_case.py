from datetime import datetime
from decimal import Decimal

from desafio_mirante.core.entities.money import Money
from desafio_mirante.core.entities.product import Product
from desafio_mirante.core.entities.sale import Sale
from desafio_mirante.core.entities.sale_item import SaleItem
from desafio_mirante.core.entities.report import Report
from desafio_mirante.core.dtos.args import ArgsDTO
from desafio_mirante.core.entities.format import Format
from desafio_mirante.infra.file_parser import SaleParser
from desafio_mirante.infra.text_format import TextFormat
from desafio_mirante.infra.json_format import JsonFormat


class CalculationUseCase:
    def __init__(self, parser: SaleParser):
        self.parser = parser

    def execute(self, args_dto: ArgsDTO):
        items = self.parser.from_csv(args_dto.file)

        sale_items = []
        for item in items:
            product = Product(name=item.name, price=Money(Decimal(item.price)))
            sale_items.append(
                SaleItem(
                    product=product,
                    sold_at=datetime.fromisoformat(item.sold_at),
                    quantity=int(item.quantity),
                )
            )

        sale = Sale(
            items=sale_items,
            start_at=args_dto.start, 
            end_at=args_dto.end
        )

        report = Report(
            total_sales=sale.total(),
            most_sold_product=sale.most_sold_product(),
            total_by_product=sale.total_by_product(),
        )

        if args_dto.format == Format.TEXT:
            return TextFormat(report).format()

        return JsonFormat(report).format()
