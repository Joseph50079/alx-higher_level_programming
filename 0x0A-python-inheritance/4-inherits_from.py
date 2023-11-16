#!/usr/bin/python3


"""Module 4-inherits_from.py"""


def inherit_from(obj, a_class):
    """inherit_from a class check for object inheritance

    Args:
        obj:
        a_class:

    Return:
        True if inherited else False
    """
    return issubclass(obj, a_class)
