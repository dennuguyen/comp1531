# COMP1531 Lab 02
#
# Dan Nguyen (z5206032)
# 24/2/2020

from list_exercises import *

def test_reverse():
    l_1 = ["how", "are", "you"]
    l_2 = []
    l_3 = ["list exercise"]
    l_4 = ["python is", "easy"]

    reverse_list(l_1)
    reverse_list(l_2)
    reverse_list(l_3)
    reverse_list(l_4)

    assert l_1 == ["you", "are", "how"]
    assert l_2 == []
    assert l_3 == ["list exercise"]
    assert l_4 == ["easy", "python is"]

def test_min():
    assert minimum([1, 2, 3, -10]) == -10
    assert minimum([]) == None
    assert minimum([0]) == 0
    assert minimum(['a', 1]) == 1

def test_sum():
    assert sum_list([7, 7, 7]) == 21
    assert sum_list([0, 0]) == 0
    assert sum_list([]) == None
    assert sum_list([-1, -1, -2]) == -4
    assert sum_list(['a']) == None
