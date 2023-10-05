#!/usr/bin/python3

from magic_calculation_102 import add, sub


def magic_calculation(a, b):
    if a < b:
        add(a, b)
        c = add(a, b)
        for i in range(4, 7):
            c = add(c, i)
        return c
    else:
        sub(a - b)
        return sub(a, b)
