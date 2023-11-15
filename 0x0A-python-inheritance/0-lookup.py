#!/usr/bin/python3

""" Module lookup """


def lookup(obj):
    """ returns list of attributes and method obj

    Args:
        obj: (object: any type):

    """
    return dir(obj)
