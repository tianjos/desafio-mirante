from decimal import Decimal

from desafio_mirante.core.money import Money


def test_money_ordering():
    money1 = Money(Decimal('10.00'))
    money2 = Money(Decimal('20.00'))
    money3 = Money(Decimal('5.00'))

    assert money1 < money2
    assert money3 < money1
    assert sorted([money1, money2, money3]) == [money3, money1, money2]


def test_money_equality():
    money1 = Money(Decimal('10.00'))
    money2 = Money(Decimal('10.00'))
    money3 = Money(Decimal('20.00'))

    assert money1 == money2
    assert money1 != money3


def test_money_comparison():
    money1 = Money(Decimal('10.00'))
    money2 = Money(Decimal('20.00'))

    assert money1 < money2
    assert money2 > money1


def test_money_serialization():
    money = Money(Decimal('15.50'))
    assert str(money) == '15.50'
    assert f'{money}' == '15.50'
