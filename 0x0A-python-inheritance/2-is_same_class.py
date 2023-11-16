#!/usr/bin/python3


"""Module is_same_class check for attribute instance"""


def is_same_class(obj, a_class):
    """ is_same_class check if obj is an instance of a_class

    Args:
        obj: (object: any type): attribute object
        a_class: (class type): any class type

    Return:
        returns true if obj is class instance else false
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
