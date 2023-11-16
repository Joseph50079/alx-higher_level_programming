#!/usr/bin/python3


"""Module 3-is_kind_of_class.py"""


def is_kind_of_class(obj, a_class):
    """returns True if obj is an instance of a_class or inheritance"""
    return type(obj) is a_class or isinstance(obj, a_class)
