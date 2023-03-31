#!/usr/bin/python3
"""
This is a function that adds 2 integers together.

The function takes 2 integer arguments. For example,

>>> add_integer(1, 2)
3
"""


def add_integer(a, b=98):
    """ Returns the addition of 2 integers

    >>> [add_integer(a, b) for a, b in [(i, i+2) for i in range(6)]]
    [2, 4, 6, 8, 10, 12]
    >>> add_integer(1, 5)
    6
    >>> add_integer(5)
    103
    >>> add_integer(1.2, 3.12)
    4
    >>> add_integer("a", 2)
    Traceback (most recent call last):
        ...
    TypeError: a must be an integer
    >>> add_integer(2, "b")
    Traceback (most recent call last):
        ...
    TypeError: b must be an integer

    A function that adds 2 integers
    - a and b must be integers or floats, otherwise raise a TypeError
    exception with the message a must be an integer or b must be an integer
    - a and b must be first casted to integers if they are float
    - Returns an integer: the addition of a and b
    - You are not allowed to import any module
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    if type(a) is float or type(b) is float:
        return int(a + b)

    return a + b
