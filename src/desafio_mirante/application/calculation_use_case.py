from datetime import datetime
from decimal import Decimal

from desafio_mirante.core.money import Money
from desafio_mirante.core.product import Product
from desafio_mirante.core.sale import Sale
from desafio_mirante.core.sale_item import SaleItem
from desafio_mirante.core.dtos.args import ArgsDTO
from desafio_mirante.core.format import Format
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
            items=sale_items, start_at=args_dto.start, end_at=args_dto.end
        )

        if args_dto.format == Format.TEXT:
            return TextFormat(sale).format()

        return JsonFormat(sale).format()
