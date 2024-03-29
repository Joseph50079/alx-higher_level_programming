#!/usr/bin/python3

from sys import stderr


def safe_function(fct, *args):
    try:
        res = fct(*args)
        return res
    except Exception as ex:
        stderr.write("Exception: {}\n".format(ex))
        return None
