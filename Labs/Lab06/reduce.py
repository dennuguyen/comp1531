"""
Implementation of reduce similar to the function of reduce from the functools
module.
"""
import inspect


def reduce(_f, _xs):
    """
    Applies a function _f on the first two elements of the list _xs.
    This reoccurs until _xs is "reduced" into the base case.
    """
    # assert _if is a callable function with 2 arguments
    try:
        assert inspect.isfunction(_f)
        assert len(inspect.signature(_f).parameters) == 2
    except AssertionError:
        raise AssertionError

    # assert _xs is a list if not then return whatever _xs was
    try:
        assert isinstance(_xs, list)
    except AssertionError:
        return _xs

    # base case
    if not _xs:
        return None

    # base case
    if len(_xs) == 1:
        return _xs[0]

    # perform lambda on first two elements of list
    _xs[1] = _f(_xs[0], _xs[1])
    del _xs[0]

    return reduce(_f, _xs)
