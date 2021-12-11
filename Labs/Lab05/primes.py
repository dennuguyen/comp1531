"""
All integers, n > 1, have prime factors
"""


def factors(num):
    """
    This function factorises the prime factors of all integers that have prime
    factors.
    """

    # Prime numbers can only be whole
    if not isinstance(num, int):
        raise TypeError

    # Negative numbers, 0 and 1 are not prime numbers
    if num < 2:
        raise ValueError

    factors_list = []

    # Algorithm to factorise prime number
    i = 2
    while i**2 <= num:
        while num % i == 0:
            factors_list.append(i)
            num //= i
        i += 1

    # Single left over prime number is factored with 1
    if not factors_list:
        factors_list.append(1)

    # Left over prime number
    if num > 1:
        factors_list.append(num)

    # Format list without ',' or '[' or ']'
    return str(factors_list).replace(',', '')[1:-1]
