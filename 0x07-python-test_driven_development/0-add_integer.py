#!/usr/bin/python3
'''This module will return addition of two integers
Example:
    >>> add_integer(1, 2)
    3
'''


def add_integer(a, b=98):
    """Returns addition of a and b
    Args:
        a:
        b:
    Return:
        a + b
    """
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')
    if a is None or not a:
        raise TypeError("a must be an integer")
    else:
        return int(a) + int(b)
