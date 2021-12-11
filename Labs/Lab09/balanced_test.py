"""
Property based testing
1. for all
2. (x, y, ...)
3. such as precondition (x, y, ...) holds
4. property (x, y, ...) is true
"""

from balanced import balanced
from hypothesis import given, strategies, assume


def is_matched(expression):
    """
    Credit to Peilonrayz
    https://codereview.stackexchange.com/questions/180567/checking-for-balanced-brackets-in-python
    """
    mapping = dict(zip('(', ')'))
    queue = []
    for letter in expression:
        if letter in mapping:
            queue.append(mapping[letter])
        elif not (queue and letter == queue.pop()):
            return False
    return not queue


def test_6():
    assert balanced(6) == {'((()))', '(()())', '(())()', '()(())', '()()()'}


@given(strategies.integers(min_value=0, max_value=10))
def test_different_algorithm(num):
    """
    Test if parantheses are matched using an alternative algorithm.
    """
    assume(num % 2 == 0)
    is_matched(balanced(num))


@given(strategies.integers(min_value=0, max_value=10))
def test_pairs(num):
    """
    There should be same number of left and right brackets.
    """
    assume(num % 2 == 0)
    for string in balanced(num):
        left = right = 0
        for paran in string:
            if paran == "(":
                left += 1
            elif paran == ")":
                right += 1
            else:
                raise ValueError("Not a paranthesis")
        assert left == int(num / 2)
        assert right == int(num / 2)


@given(strategies.integers(min_value=0, max_value=10))
def test_odd(num):
    """
    Odd numbers return empty set
    """
    assume(num % 2 != 0)
    assert balanced(num) == set()


@given(strategies.integers(min_value=0, max_value=10))
def test_duplicate(num):
    """
    Tests if balanced set does not have duplicates.
    """
    bal_set = balanced(num)
    assert len(bal_set) == len(set(bal_set))  # set removes duplicates
