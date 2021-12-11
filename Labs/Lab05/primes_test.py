"""
Testing primes.py
"""
import functools as fntool
from operator import mul
import pytest
from primes import factors


def test_even():
    """
    Test even number case
    """
    assert factors(16) == '2 2 2 2'


def test_odd():
    """
    Test odd number case
    """
    assert factors(21) == '3 7'


def test_char():
    """
    Test char case
    """
    with pytest.raises(TypeError):
        factors('a')


def test_float():
    """
    Test float case
    """
    with pytest.raises(TypeError):
        factors(1.0)


def test_single_digit_prime():
    """
    Test single digit prime number case
    """
    assert factors(3) == '1 3'


def test_wrong_order():
    """
    Check order of numbers in string
    """
    assert factors(3) != '3 1'


def test_zero():
    """
    Test zero case
    """
    with pytest.raises(ValueError):
        factors(0)


def test_one():
    """
    Test one case
    """
    with pytest.raises(ValueError):
        factors(1)


def test_negative():
    """
    Test negative case
    """
    with pytest.raises(ValueError):
        factors(-4)


def test_general():
    """
    General test for all numbers between 2 and 1000 inclusive
    """
    for i in range(2, 1000):
        assert fntool.reduce(mul, list(map(int, factors(i).split(' ')))) == i


if __name__ == '__main__':
    test_even()
    test_odd()
    test_char()
    test_float()
    test_single_digit_prime()
    test_wrong_order()
    test_zero()
    test_one()
    test_negative()
    test_general()
