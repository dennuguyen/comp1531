"""
Assuming there will only be 5 inputs.

Obtaining a -> e was condensed into a list comprehension with an f-string to
keep the original output stream syntax with the range from 'a' to 'f'.

my_min and its for loop was removed in favour of python's inbuilt min().

To get the product of the first 4 and last 4 numbers in the list, reduce
(from functools) allows a function (mul from operator) to be applied to the
list (like a lambda function). The list is parsed using slicing.
"""

from operator import mul
import functools

if __name__ == '__main__':
    L = []
    L = [int(input(f'Enter {chr(x)}: ')) for x in range(ord('a'), ord('f'))]

    print('Minimum: ' + str(min(L)))
    print('Product of first 4 numbers: ' + str(functools.reduce(mul, L[:4])))
    print('Product of last 4 numbers: ' + str(functools.reduce(mul, L[-4:])))
