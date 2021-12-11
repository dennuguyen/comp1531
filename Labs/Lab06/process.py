"""
Module docstring to keep pylint happy
"""
import json
import unpickle


def wrap(data):
    """
    Put the most common data and raw data into a dictionary
    """
    return {
        "mostCommon": {
            "colour": unpickle.most_common(data)[0][0],
            "shape": unpickle.most_common(data)[1][0],
        },
        "rawData": [data],
    }


if __name__ == '__main__':
    DATA = unpickle.unpickle()
    with open('processed.json', 'w') as file_:
        json.dump(wrap(DATA), file_)
