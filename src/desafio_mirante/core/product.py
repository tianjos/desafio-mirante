from dataclasses import dataclass, field

from .money import Money


@dataclass(frozen=True, slots=True, kw_only=True, order=True)
class Product:
    name: str = field(compare=False)
    price: Money = field(hash=False)
