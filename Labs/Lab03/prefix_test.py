from prefix import prefix_search
import pytest


def test_documentation():
    assert prefix_search({
        'ac': 1,
        'ba': 2,
        'ab': 3,
    }, 'a') == {
        'ac': 1,
        'ab': 3,
    }


def test_exact_match():
    assert prefix_search({
        'category': 'math',
        'cat': 'animal'
    }, 'cat') == {
        'category': 'math',
        'cat': 'animal'
    }


def test_nested_dictionary():
    president = {
        'name': 'Ian Jacobs',
        'age': 54,
        'staff': ['Sally', 'Bob', 'Rob', 'Hayden'],
        'marks': {
            '20T1': 77,
            '20T2': 88,
            '20T3': 99,
        },
    }

    assert prefix_search(president, "marks") == {
        'marks': {
            '20T1': 77,
            '20T2': 88,
            '20T3': 99,
        }
    }


def test_all_search_results():
    assert prefix_search({
        'ac': 1,
        'ba': 2,
        'ab': 3,
    }, '') == {
        'ac': 1,
        'ba': 2,
        'ab': 3,
    }


def test_no_search_result():
    with pytest.raises(KeyError):
        prefix_search({
            "ac": 1,
            "ba": 2,
            "ab": 3,
        }, 'abc')


def test_suffix():
    with pytest.raises(KeyError):
        prefix_search({
            'category': 'math',
            'cat': 'animal',
        }, 'egory')


def test_no_string():
    assert prefix_search({
        'category': '',
        'cat': 'animal',
    }, 'cate') == {
        'category': '',
    }


def test_all_empty():
    with pytest.raises(KeyError):
        prefix_search({}, '')


def test_empty_dictionary():
    with pytest.raises(KeyError):
        prefix_search({}, 'a')


test_documentation()
test_exact_match()
test_nested_dictionary()
test_all_search_results()
test_no_search_result()
test_suffix()
test_no_string()
test_all_empty()
test_empty_dictionary()