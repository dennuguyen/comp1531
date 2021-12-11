# COMP1531 Lab 02
#
# Dan Nguyen (z5206032)
# 25/2/2020

from count import count_char

def test_empty():
    assert count_char("") == {}

def test_simple():
    assert count_char("abc") == {"a": 1, "b": 1, "c": 1}

def test_double():
    assert count_char("aa") == {"a": 2}

def test_sentence():
    assert count_char("Hello World!") == {"H": 1, "e": 1, "l": 3, "o": 2, "W": 1,
                                         "r": 1, "d": 1, " ": 1, "!": 1}

def test_cases():
    assert count_char("aA AaA") == {"a": 2, "A": 3, " ": 1}

def test_digits():
    assert count_char("1 2 3") == {"1": 1, "2": 1, "3": 1, " ": 2}