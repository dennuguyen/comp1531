# Tutorial 9

## Code review

In groups of 3 to 5, review your solutions to `rainfall.py` and `transpose.py` from the last lab. For `rainfall.py`, compare the different ways `filter()` and `reduce()` can be used to solve this exercise. Is it possible to do it with only one call to `reduce()`, and no use of `filter()` or `map()`? Is that solution "better" than other solutions?

## Generators

Run-length encoding is a technique for compressing data with many adjacent repeated values. It works by converting a string into a series of tuples, `(c,n)`, where `c` is the character and `n` is the number of times it is repeated. For example, the string `Helllloooooo!` is encoded as `[('H',1), ('e',1), ('l', 4), ('o', 6), ('!',1)]`.

Write a *generator*, `encode(string)`, that generates the run-length encoding of the given string.

Why this is better than a conventional iterator or a function that returns a list?

Write a function, `decode(encoded)`, that converts the encoded data back to a string.

## Property-based testing

What property do the `encode()` and `decode()` functions have that can be expressed as a property-based test?

Write this test using hypothesis in python.

Does this property form a complete definition of this pair of functions? i.e. Assuming that the functions satisfy this property, is that sufficient to guarantee they work correctly?
