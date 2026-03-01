from dataclasses import dataclass

from desafio_mirante.core.dtos.sale_item import SaleItemDTO


@dataclass(frozen=True, kw_only=True)
class SaleDTO:
    items: list[SaleItemDTO]
