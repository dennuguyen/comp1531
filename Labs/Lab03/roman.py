import sys, pytest


def test_single_digit():
    assert roman('III') == 3
    assert roman('X') == 10


def test_double_digit():
    assert roman('II') == 2
    assert roman('IV') == 4
    assert roman('IX') == 9
    assert roman('XX') == 20
    assert roman('IC') == 99


def test_more():
    assert roman('XIX') == 19
    assert roman('XXX') == 30
    assert roman('XLIX') == 49
    assert roman('MDCCLXXVI') == 1776
    assert roman('MMXIX') == 2019


def test_empty():
    assert roman('') == 0


def test_incorrect_format():
    with pytest.raises(KeyError):
        roman('A')
    with pytest.raises(KeyError):
        roman('123')
    with pytest.raises(KeyError):
        roman(' ')


def test_incorrect_format_repeated():
    with pytest.raises(KeyError):
        roman('IIII')
    with pytest.raises(KeyError):
        roman('IIIIIIIII')
    with pytest.raises(KeyError):
        roman('XXXXV')


def test_repeated_V():
    with pytest.raises(KeyError):
        roman('VV')


def roman(input):

    roman_arabic = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    count = 1

    # parse roman numeral for errors
    #   - too many repeated roman numerals
    #   - VV
    #   - char not in roman_arabic
    for i in range(len(input)):
        try:
            if i + 1 < len(input) and roman_arabic[input[i]] == roman_arabic[
                    input[i + 1]]:
                count += 1

                if count == 4 or (count == 2 and input[i] == 'V'):
                    raise KeyError
            else:
                count = 1

        except KeyError:
            raise

    answer = 0

    # parse roman numeral from left to right
    for i in range(len(input)):

        # i + 1 < len(input) protects against IndexError in last case
        # if next number is greater than current number then subtract
        # e.g. IX = 1 10 = 9
        if i + 1 < len(input) and roman_arabic[input[i]] < roman_arabic[input[
                i + 1]]:
            answer -= roman_arabic[input[i]]
        else:
            answer += roman_arabic[input[i]]

    return answer


test_single_digit()
test_double_digit()
test_more()
test_empty()
test_incorrect_format()
test_incorrect_format_repeated()
test_repeated_V()