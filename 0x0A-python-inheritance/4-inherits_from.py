#!/usr/bin/python3

"""Module 4-inherits_from.py"""


def inherits_from(obj, a_class):
    """Inherit from a class check for object inheritance e.g subclass.

    Args:
        obj: (class or object type):
        a_class: (class type):

    Return:
        True if inherited else False

    """
    if issubclass(type(obj), a_class) and not type(obj) is a_class:
        return True
    else:
        return False
