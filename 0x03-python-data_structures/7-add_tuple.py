#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    result = ()
    for i in range(2):
        sum_a = tuple_a[i] if i < len(tuple_a) else 0
        sum_b = tuple_b[i] if i < len(tuple_b) else 0
        result += (sum_a + sum_b,)
    return result
