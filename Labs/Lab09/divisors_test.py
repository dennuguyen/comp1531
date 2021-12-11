"""
Property based testing
1. for all
2. (x, y, ...)
3. such as precondition (x, y, ...) holds
4. property (x, y, ...) is true
"""

from divisors import divisors
from hypothesis import given, strategies
import pytest


def test_12():
    assert divisors(12) == {1, 2, 3, 4, 6, 12}


@given(strategies.integers(min_value=0, max_value=1000))
def test_divisible(num):
    """
    Every integer in the set returned by divisors wholly divises num.
    """
    for n in divisors(num):
        assert num % n == 0


@given(strategies.integers(min_value=-1000, max_value=-1))
def test_negative(num):
    """
    Negative numbers raise ValueError.
    """
    with pytest.raises(ValueError):
        for _ in divisors(num):
            pass


@given(strategies.integers(min_value=1, max_value=1000))
def test_1_and_itself(num):
    """
    Check if 1 and the integer passed is in the set returned.
    """
    assert any(n == 1 or n == num for n in divisors(num))
