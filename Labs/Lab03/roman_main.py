import sys
from roman import roman


def test_roman():
    assert roman('II') == 2
    assert roman('IV') == 4
    assert roman('IX') == 9
    assert roman('X') == 10
    assert roman('XIX') == 19
    assert roman('XX') == 20
    assert roman('XLIX') == 49
    assert roman('MDCCLXXVI') == 1776
    assert roman('MMXIX') == 2019


if __name__ == '__main__':
    test_roman()
