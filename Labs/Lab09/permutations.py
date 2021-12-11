"""
Permutation answer obtained from:
https://stackoverflow.com/questions/104420/how-to-generate-all-permutations-of-a-list
"""


def iter2set(fn):
    def wrapper(*args):
        return set(fn(*args))

    return wrapper


@iter2set
def permutations(string):
    '''
    For the given string, compute the set of all permutations of the characters of that string. For example:
    >>> permutations('ABC')
    {'ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA'}

    Params:
      string (str): The string to permute

    Returns:
      (set of str): Each string in this set should be a permutation of the input string.
    '''
    if len(string) <= 1:
        yield string
        return

    for perm in permutations(string[1:]):
        for i in range(len(string)):
            yield perm[:i] + string[0:1] + perm[i:]
