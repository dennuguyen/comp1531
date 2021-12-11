"""
Property based testing
1. for all
2. (x, y, ...)
3. such as precondition (x, y, ...) holds
4. property (x, y, ...) is true
"""

from factors import factors, is_prime
from hypothesis import given, strategies
import inspect
from functools import reduce


def test_generator():
    '''
    Ensure it is generator function
    '''
    assert inspect.isgeneratorfunction(
        factors), "factors does not appear to be a generator"


@given(strategies.integers(min_value=2, max_value=1000))
def test_divisible(num):
    """
    All numbers in set returned by factors() wholly divises num.
    """
    for n in factors(num):
        assert num % n == 0


@given(strategies.integers(min_value=2, max_value=1000))
def test_multiple(num):
    """
    Multiplying all numbers in set returned by factors() yields num.
    """
    assert reduce(lambda x, y: x * y, factors(num)) == num