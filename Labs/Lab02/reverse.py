# COMP1531 Lab 02
# This exercise assumes a single-nested list of strings
#
# Dan Nguyen (z5206032)
# 24/2/2020

def reverse_words(string_list):

    # remove numerical
    string_list = [i for i in string_list if isinstance(i, str)]

    new_list = []

    for string in string_list:
        new_list.append(' '.join(string.split(' ')[::-1]))
        # [::-1] from last element reversed
    
    return new_list

def test_reverse_words():
    assert reverse_words(['Hello World', 'I am here']) == ['World Hello', 'here am I']
    assert reverse_words([]) == []
    assert reverse_words([1, 'I''m a letter']) == ['letter a I''m']
    assert reverse_words(['Hello 23', 32]) == ['23 Hello']
    assert reverse_words([4, 5, ]) == []
    assert reverse_words([None]) == []
