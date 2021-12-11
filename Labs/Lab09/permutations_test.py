"""
Property based testing
1. for all
2. (x, y, ...)
3. such as precondition (x, y, ...) holds
4. property (x, y, ...) is true
"""

from permutations import permutations
from hypothesis import given, strategies, assume


@given(strategies.text(min_size=0, max_size=5))
def test_unordered(text):
    """
    Tests if string returned from permutation is unorderly equivalent to text.
    """
    for string in permutations(text):
        assert sorted(string) == sorted(text)


@given(strategies.text(min_size=0, max_size=1))
def test_empty_singular(text):
    """
    Tests that empty and singular text returns itself.
    """
    for string in permutations(text):
        assert string == text


@given(strategies.text(min_size=2, max_size=5))
def test_duplicate(text):
    """
    Tests if perm_set does not have duplicates.
    """
    perm_set = permutations(text)
    assert len(perm_set) == len(set(perm_set))  # set removes duplicates
