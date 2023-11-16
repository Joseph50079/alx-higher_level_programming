#!/usr/bin/python3


"""Module 4-inherits_from.py"""


def inherit_from(obj, a_class):
    """ Inherit_from a class check for object inheritance
    Args:
        obj: (class or object type):
        a_class: (class type):
    Return:
        True if inherited else False
    """
    return issubclass(obj, a_class)
