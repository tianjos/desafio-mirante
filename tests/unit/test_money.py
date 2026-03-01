from decimal import Decimal

import pytest

from desafio_mirante.core.entities.money import Money


@pytest.mark.unit
def test_money_ordering():
    money1 = Money(Decimal('10.00'))
    money2 = Money(Decimal('20.00'))
    money3 = Money(Decimal('5.00'))

    assert money1 < money2
    assert money3 < money1
    assert sorted([money1, money2, money3]) == [money3, money1, money2]


@pytest.mark.unit
def test_money_equality():
    money1 = Money(Decimal('10.00'))
    money2 = Money(Decimal('10.00'))
    money3 = Money(Decimal('20.00'))

    assert money1 == money2
    assert money1 != money3


@pytest.mark.unit
def test_money_comparison():
    money1 = Money(Decimal('10.00'))
    money2 = Money(Decimal('20.00'))

    assert money1 < money2
    assert money2 > money1


@pytest.mark.unit
def test_money_serialization():
    money = Money(Decimal('15.50'))

    assert str(money) == '15.50'
    assert f'{money}' == '15.50'


@pytest.mark.unit
def test_money_addition():
    money1 = Money(Decimal('10.00'))
    money2 = Money(Decimal('5.00'))

    result = money1 + money2

    assert result == Money(Decimal('15.00'))


@pytest.mark.unit
def test_money_subtraction():
    money1 = Money(Decimal('10.00'))
    money2 = Money(Decimal('5.00'))

    result = money1 - money2

    assert result == Money(Decimal('5.00'))


@pytest.mark.unit
def test_money_multiplication():
    money1 = Money(Decimal('10.00'))
    money2 = Money(Decimal('2.00'))

    result = money1 * money2

    assert result == Money(Decimal('20.00'))


@pytest.mark.unit
def test_money_division():
    money1 = Money(Decimal('10.00'))
    money2 = Money(Decimal('2.00'))

    result = money1 / money2

    assert result == Money(Decimal('5.00'))


@pytest.mark.unit
def test_money_division_by_zero():
    money1 = Money(Decimal('10.00'))
    money2 = Money(Decimal('0.00'))

    result = money1 / money2

    assert result == Money(Decimal('0.00'))


@pytest.mark.unit
def test_money_negation():
    money = Money(Decimal('10.00'))

    result = -money

    assert result == Money(Decimal('-10.00'))


@pytest.mark.unit
def test_money_abs():
    money = Money(Decimal('-10.00'))

    result = abs(money)

    assert result == Money(Decimal('10.00'))


@pytest.mark.unit
def test_money_bool():
    money1 = Money(Decimal('0.00'))
    money2 = Money(Decimal('10.00'))

    assert not money1
    assert money2
