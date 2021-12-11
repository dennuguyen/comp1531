"""
Property based testing
1. for all
2. (x, y, ...)
3. such as precondition (x, y, ...) holds
4. property (x, y, ...) is true
"""

from inverse import inverse
from hypothesis import given, strategies
from hypothesis.strategies import dictionaries, integers, characters, text


def test_inverse():
    assert inverse({1: 'A', 2: 'B', 3: 'A'}) == {'A': [1, 3], 'B': [2]}


@given(dictionaries(characters(), integers()))
def test_types(d):
    """
    Knowing that keys are str and values are int, the inverted dictionary has
    keys that are int and values that are str.
    """
    for key, val in inverse(d).items():
        assert isinstance(key, int) and all(isinstance(x, str) for x in val)


@given(dictionaries(text(), integers()))
def test_swapped(d):
    for key, val in inverse(d).items():
        assert key in d.values()
        assert all(x in d.keys() for x in val)
