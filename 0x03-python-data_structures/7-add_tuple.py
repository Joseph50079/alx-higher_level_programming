#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    a, b = tuple_a, tuple_b
    t = ()
    if a[0] and b[0]:
        t += a[0] + b[0],
    elif not a[0]:
        t += 0 + b[0],
    elif not b[0]:
        t += a[0] + 0,
    else:
        t += 0 + 0,
    if a[1] and b[1]:
        t += a[1] + b[1],
    elif not a[1]:
        t += 0 + b[1],
    elif not b[1]:
        t += a[0] + 0,
    else:
        t += 0 + 0,
