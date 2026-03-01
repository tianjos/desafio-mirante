from dataclasses import dataclass
from decimal import ROUND_HALF_UP, Decimal
from typing import Self


@dataclass(frozen=True, order=True)
class Money:
    amount: Decimal

    def __abs__(self):
        return Money(abs(self.amount))

    def __bool__(self):
        return self.amount != 0

    def __add__(self, other: Self):
        return Money(self.amount + other.amount)

    def __radd__(self, other):
        if other == 0:
            return self
        if isinstance(other, Money):
            return self.__add__(other)

        return NotImplemented

    def __sub__(self, other: Self):
        return Money(self.amount - other.amount)

    def __mul__(self, other: Self):
        return Money(self.amount * other.amount)

    def __truediv__(self, other: Self):
        if other.amount == 0:
            return Money(Decimal('0.00'))
        return Money(self.amount / other.amount)

    def __neg__(self):
        return Money(-self.amount)

    def __str__(self):
        return f'{self.amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)}'
