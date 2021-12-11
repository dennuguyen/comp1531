"""
Annoying docstring
"""
import urllib
import json
import pytest

BASE_URL = 'http://127.0.0.1:5000/'


@pytest.fixture(autouse=True)
def reset_state():
    """
    This pytest fixture automatically runs for every test function call
    """
    headers = {'Content-Type': 'application/json'}
    req_obj = urllib.request.Request(f"{BASE_URL}/reset",
                                     headers=headers,
                                     method='POST')
    urllib.request.urlopen(req_obj)


def test_list_names_empty():
    """
    Test the listing of an empty payload
    """

    # Check that payload is an empty dictionary
    payload = json.load(urllib.request.urlopen(f"{BASE_URL}/name"))
    assert payload == {'name': []}


def test_add_name_single():
    """
    Test the case of adding a single name and listing
    """
    # Add a John Doe via the /name/add route
    data = json.dumps({'name': 'John Doe'}).encode('utf-8')
    headers = {'Content-Type': 'application/json'}
    req_obj = urllib.request.Request(f"{BASE_URL}/name/add",
                                     data=data,
                                     headers=headers,
                                     method='POST')

    # Successful name add returns empty dictionary
    assert json.load(urllib.request.urlopen(req_obj)) == {}

    # Check the payload
    payload = json.load(urllib.request.urlopen(f"{BASE_URL}/name"))
    assert payload == {'name': ['John Doe']}


def test_add_name_multiple():
    """
    Test the case of adding multiple names and listing it
    """
    # Add a John Doe via the /name/add route
    data1 = json.dumps({'name': 'John Doe'}).encode('utf-8')
    headers = {'Content-Type': 'application/json'}
    req_obj1 = urllib.request.Request(f"{BASE_URL}/name/add",
                                      data=data1,
                                      headers=headers,
                                      method='POST')

    # Successful name add returns empty dictionary
    assert json.load(urllib.request.urlopen(req_obj1)) == {}

    # Add second person
    data2 = json.dumps({'name': 'Max Powers'}).encode('utf-8')
    req_obj2 = urllib.request.Request(f"{BASE_URL}/name/add",
                                      data=data2,
                                      headers=headers,
                                      method='POST')

    # Successful name add returns empty dictionary
    assert json.load(urllib.request.urlopen(req_obj2)) == {}

    # Check the payload
    payload = json.load(urllib.request.urlopen(f"{BASE_URL}/name"))
    assert payload == {'name': ['John Doe', 'Max Powers']}


def test_add_name_repeated():
    """
    Test the case of adding the same name multiple times
    """
    # Add a John Doe via the /name/add route
    data1 = json.dumps({'name': 'John Doe'}).encode('utf-8')
    headers = {'Content-Type': 'application/json'}
    req_obj1 = urllib.request.Request(f"{BASE_URL}/name/add",
                                      data=data1,
                                      headers=headers,
                                      method='POST')

    # Successful name add returns empty dictionary
    assert json.load(urllib.request.urlopen(req_obj1)) == {}

    # Add second person
    data2 = json.dumps({'name': 'John Doe'}).encode('utf-8')
    req_obj2 = urllib.request.Request(f"{BASE_URL}/name/add",
                                      data=data2,
                                      headers=headers,
                                      method='POST')

    # Successful name add returns empty dictionary
    assert json.load(urllib.request.urlopen(req_obj2)) == {}

    # Check the payload
    payload = json.load(urllib.request.urlopen(f"{BASE_URL}/name"))
    assert payload == {'name': ['John Doe', 'John Doe']}


def test_remove_name_once():
    """
    Test the removal of the name once
    """
    # Add a John Doe via the /name/add route
    data1 = json.dumps({'name': 'John Doe'}).encode('utf-8')
    headers = {'Content-Type': 'application/json'}
    req_obj1 = urllib.request.Request(f"{BASE_URL}/name/add",
                                      data=data1,
                                      headers=headers,
                                      method='POST')

    # Open the URL to add the name
    json.load(urllib.request.urlopen(req_obj1))

    data2 = json.dumps({'name': 'John Doe'}).encode('utf-8')
    req_obj2 = urllib.request.Request(f"{BASE_URL}/name/remove",
                                      data=data2,
                                      headers=headers,
                                      method='DELETE')

    # Successful name removal returns empty dictionary
    assert json.load(urllib.request.urlopen(req_obj2)) == {}

    # Check the payload
    payload = json.load(urllib.request.urlopen(f"{BASE_URL}/name"))
    assert payload == {'name': []}


def test_remove_name_repeated():
    """
    Test removal of a name that was repeated which should only remove it once
    """
    # Add a John Doe via the /name/add route
    data1 = json.dumps({'name': 'John Doe'}).encode('utf-8')
    headers = {'Content-Type': 'application/json'}
    req_obj1 = urllib.request.Request(f"{BASE_URL}/name/add",
                                      data=data1,
                                      headers=headers,
                                      method='POST')

    # Open the URL twice to add the name twice
    json.load(urllib.request.urlopen(req_obj1))
    json.load(urllib.request.urlopen(req_obj1))

    data2 = json.dumps({'name': 'John Doe'}).encode('utf-8')
    req_obj2 = urllib.request.Request(f"{BASE_URL}/name/remove",
                                      data=data2,
                                      headers=headers,
                                      method='DELETE')

    # Successful name removal returns empty dictionary
    assert json.load(urllib.request.urlopen(req_obj2)) == {}

    # Check the payload
    payload = json.load(urllib.request.urlopen(f"{BASE_URL}/name"))
    assert payload == {'name': ['John Doe']}


def test_remove_empty():
    """
    Test removing an empty dictionary
    """
    data = json.dumps({'name': 'John Doe'}).encode('utf-8')
    headers = {'Content-Type': 'application/json'}
    req_obj = urllib.request.Request(f"{BASE_URL}/name/remove",
                                     data=data,
                                     headers=headers,
                                     method='DELETE')

    # Exception should raise on removal of empty list
    with pytest.raises(Exception):
        json.load(urllib.request.urlopen(req_obj))


if __name__ == '__main__':
    test_list_names_empty()
    test_remove_name_once()
    test_add_name_multiple()
    test_add_name_repeated()
    test_remove_name_once()
    test_remove_name_repeated()
    test_remove_empty()
