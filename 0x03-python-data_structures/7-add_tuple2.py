#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    a, b = tuple_a, tuple_b
    t = ()
    idx = 0
    if idx < len(a) and idx < len(b):
        t += a[0] + b[0],
    elif idx > len(a):
        t += 0 + b[0],
    elif idx > len(b):
        t += a[0] + 0,
    else:
        t += 0 + 0,
    idx += 1
    if idx < len(a) and idx < len(b):
        t += a[1] + b[1],
    elif idx >  len(a):
        t += 0 + b[1],
    elif idx > len(b):
        t += a[1] + 0,
    else:
        t += 0 + 0,
    return t
