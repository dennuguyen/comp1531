"""
Transpose a matrix
"""
import pytest


def transpose(matrix):
    """
    Given a matrix, calculate its transpose. Transposing a matrix swaps its rows
    with its columns, so the element at position (i,j) of the matrix is now at
    position (j,i).

    Params:
        matrix (list): A matrix represented as a list of lists, where each inner
        list is of the same length.

    Returns:
        (list): The transposed matrix, represented as a lists of lists where
        each inner list is the same length.

    Raises:
        ValueError: If the inner lists of the argument are not all of the same
        length.
    """

    # Check if the matrix is empty
    if not any(matrix):
        return matrix

    # Check if invalid matrix
    if len(set(map(len, matrix))) not in (0, 1):
        raise ValueError("Invalid matrix")

    # Code Flow
    #
    # 1. *matrix initialises matrix as a tuple
    #
    # 2. zip(*matrix) gets the first iterable from each element of tuple and
    #    returns a zip object (that is also a tuple)
    #
    # 3. map each element in the tuple to a list
    #
    # 4. typecast whole expression to a list
    return list(map(list, zip(*matrix)))


def test_0x0():
    """
    0x0
    """
    assert transpose([[]]) == [[]]


def test_1x1():
    """
    1x1
    """
    assert transpose([[1]]) == [[1]]


def test_2x1():
    """
    2x1
    """
    assert transpose([[1, 2]]) == [[1], [2]]


def test_2x2():
    """
    2x2
    """
    assert transpose([[1, 2], [3, 4]]) == [[1, 3], [2, 4]]


def test_2x3():
    """
    2x3
    """
    assert transpose([[1, 2], [3, 4], [5, 6]]) == [[1, 3, 5], [2, 4, 6]]


def test_3x3():
    """
    3x3
    """
    assert transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [[1, 4,
                                                             7], [2, 5, 8],
                                                            [3, 6, 9]]


def test_unequal_list():
    """
    Invalid matrix
    """
    with pytest.raises(ValueError):
        transpose([[1], [3, 4]])
