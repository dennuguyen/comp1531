"""
Module docstring or pylint will complain
"""
import pickle
from collections import Counter


def unpickle():
    """
    unpickling 'shapecolour.p' returns a list of dictionaries with 'shape' and
    'colour' keys
    """
    file_ = open('shapecolour.p', 'rb')
    data = pickle.load(file_)
    file_.close()

    return data


def most_common(data):
    """
    1. List comprehension splits the list into two lists by dictionary key.

    2. Counter from collections module orders the lists by occurence of value in
       dictionary format (key = key, value = number of occurences).

    3. most_common() converts the dictionary into a list of tuples (str, occur).

    4. [0] gets the first element which is the most common value.

    5. Tuple is returned. Output is a tuple of tuple
       (('rectangle', 1283), ('aqua', 1082))
    """
    return (Counter([i['shape'] for i in data]).most_common()[0],
            Counter([i['colour'] for i in data]).most_common()[0])


if __name__ == '__main__':
    DATA = unpickle()
    print(f"Colour: {most_common(DATA)[0][0]}")
    print(f"Shape: {most_common(DATA)[1][0]}")
