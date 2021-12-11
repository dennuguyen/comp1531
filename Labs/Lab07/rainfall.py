"""
Calculate average of rainfall if rainfall is greater than 0.
"""
import functools
import pytest


def rainfall(nums):
    """
    Calculate rainfall without use of for, while or additional modules.
    """
    try:
        nums = list(filter(lambda x: x > 0, nums))
        return functools.reduce(lambda x, y: x + y, nums) / len(nums)
    except:
        raise ValueError


def test_simple():
    """
    test_simple
    """
    assert rainfall([1, 2, 3]) == 2


def test_negative():
    """
    test_negative
    """
    assert rainfall([1, -5, 3, 4, 4]) == 3


def test_zero():
    """
    test_zero
    """
    assert rainfall([1, 0, 2, 3]) == 2


def test_all_negative():
    """
    test_all_negative
    """
    with pytest.raises(ValueError):
        rainfall([-1, -2, -3])


def test_simple_again():
    """
    test_simple_again
    """
    assert rainfall([1, 2, 3, 4, 5, 6]) == 3.5


def test_negative_zero():
    """
    test_negative_zero
    """
    with pytest.raises(ValueError):
        rainfall([0, -2, -4])


def test_simple_again_again():
    """
    test_simple_again_again
    """
    assert rainfall([1, 28, -1]) == 14.5


def test_empty():
    """
    test_empty
    """
    with pytest.raises(ValueError):
        rainfall([])


def test_float():
    """
    test_float
    """
    assert rainfall([0.4, 1.5, -6.2, 1.0]) == 29 / 30
