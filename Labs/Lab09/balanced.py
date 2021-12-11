from permutations import permutations
from itertools import accumulate


def iter2set(fn):
    def wrapper(*args):
        return set(fn(*args))

    return wrapper


def is_matched(expr):
    """
    Credit to Alain T.:
    https://stackoverflow.com/questions/38833819/python-program-to-check-matching-of-simple-parentheses
    """
    levels = list(accumulate((c == "(") - (c == ")") for c in expr))
    return all(level >= 0 for level in levels) and levels[-1] == 0


@iter2set
def balanced(n):
    '''
    Given a positive number n, compute the set of all strings of length n, in any order, that only
    contain balanced brackets. For example:
    >>> balanced(6)
    {'((()))', '(()())', '(())()', '()(())', '()()()'}

    Note that, by definition, the only string of length 0 containing balanced brackets is the empty
    string.

    Params:
      n (int): The length of string we want

    Returns:
      (set of str): Each string in this set contains balanced brackets. In the event n is odd, this
      set is empty.

    Raises:
      ValueError: If n is negative
    '''
    if n < 0:
        raise ValueError

    if n % 2 != 0:
        return

    string = "()" * int(n / 2)
    for perm in permutations(string[1:]):
        for i in range(len(string)):
            result = string[0:1] + perm[:i] + perm[i:]
            if is_matched(result):
                yield result
