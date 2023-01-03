#!/usr/bin/python3
'''This module will return addition of two integers'''


def add_integer(a, b=98):
    """Returns addition of a and b
    Args:
        a:
        b:
    Return:
        a + b
    """
    if isinstance(a, float) or isinstance(b, float):
        a = int(a)
        b = int(b)
    if not isinstance(a, int):
        raise TypeError('a must be an integer')
    if not isinstance(b, int):
        raise TypeError('b must be an integer')
    else:
        return a + b
