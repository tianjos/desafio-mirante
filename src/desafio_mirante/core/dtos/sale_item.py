from dataclasses import dataclass

@dataclass(frozen=True)
class SaleItemDTO:
    name: str
    price: float
    quantity: int
    sold_at: str