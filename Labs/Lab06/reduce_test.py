"""
Unit test file for reduce.py
"""
import pytest
from reduce import reduce


def test_empty_list():
    """
    Test the empty list case
    """
    assert reduce(lambda x, y: x + y, []) is None


def test_none():
    """
    Test case where None is given instead of list
    """
    assert reduce(lambda x, y: x + y, None) is None


def test_dictionary():
    """
    Test case where dict is given instead of list
    """
    assert reduce(lambda x, y: x + 3, {'key': []}) == {'key': []}


def test_int():
    """
    Test case where int is given instead of list
    """
    assert reduce(lambda x, y: x + 3, 1) == 1


def test_string():
    """
    Test case where string is given instead of list
    """
    assert reduce(lambda x, y: x + y, "hello") == "hello"


def test_single_element():
    """
    Test the single element in list case
    """
    assert reduce(lambda x, y: x + y, [1]) == 1
    assert reduce(lambda x, y: x * y, [2]) == 2
    assert reduce(lambda x, y: x // y, [3]) == 3


def test_simple_addition():
    """
    Test a simple lambda addition
    """
    assert reduce(lambda x, y: x + y, [1, 2, 3, 4, 5]) == 15


def test_constant_addition():
    """
    Test a constant lambda addition
    """
    assert reduce(lambda x, y: x + 3, [1, 2, 3, 4, 5]) == 13


def test_constant():
    """
    Test a lambda that returns a constant
    """
    assert reduce(lambda x, y: -21, [1, 2, 3, 4, 5]) == -21


def test_simple_multiplication():
    """
    Test a simple lambda multiplication
    """
    assert reduce(lambda x, y: x * y, [1, 2, 3, 4, 5]) == 120


def test_simple_power():
    """
    Test a simple lambda power
    """
    assert reduce(lambda x, y: x**y, [1, 2, 3, 4, 5]) == 1


def test_zero():
    """
    Test a simple lambda 0th root
    """
    with pytest.raises(ArithmeticError):
        reduce(lambda x, y: x // y, [0, 0])


def test_lambda_1_arg():
    """
    Test a lambda with 1 argument
    """
    with pytest.raises(AssertionError):
        reduce(lambda x: x + 3, [1, 2, 3, 4, 5])


def test_lambda_3_arg():
    """
    Test a lambda with 3 arguments
    """
    with pytest.raises(AssertionError):
        reduce(lambda x, y, z: x + y + z, [1, 2, 3, 4, 5])


def test_no_lambda():
    """
    Test with no given callable function
    """
    with pytest.raises(AssertionError):
        reduce(1, [1, 2, 3, 4, 5])


if __name__ == '__main__':
    test_empty_list()
    test_none()
    test_dictionary()
    test_int()
    test_string()
    test_single_element()
    test_simple_addition()
    test_constant_addition()
    test_constant()
    test_simple_multiplication()
    test_simple_power()
    test_zero()
    test_lambda_1_arg()
    test_lambda_3_arg()
    test_no_lambda()
