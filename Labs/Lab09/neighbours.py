def neighbours(iterable):
    '''
    A generator, that, given an iterable, yields the "neighbourhood" of each
    element. The neighbourhood is a tuple containing the element itself as well
    as the one that comes before and the one that comes after. For example,
    >>> list(neighbours([1,2,3,4]))
    [(1,2), (1,2,3), (2,3,4), (3,4)]

    Note that the first and last elements are pairs, while the rest are triples.

    Params:
    iterable (iterable): The iterable being processed. In the event it's empty,
    this generator should not yield anything. In the event it only contains
    one element, only that element should be yielded in a one-tuple.

    Yields:
    (tuple) : The neighbourhood of the current element.
    '''
    # Hint: Don't forget that iterables can produce values infinitely. You can't
    # rely on being able to retrieve all the elements at once.

    it = iter(iterable)

    p = c = None
    try:
        for n in it:
            if p is None and c is not None:
                yield (c, n)
            elif p is not None and c is not None:
                yield (p, c, n)
            p, c = c, n
        raise StopIteration
    except StopIteration:
        if p is None and c is not None:
            yield (c, )
        elif p is not None and c is not None and n is not None:
            yield (p, c)
