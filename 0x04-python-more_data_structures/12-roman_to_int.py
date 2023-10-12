#!/usr/bin/python3

def roman_to_int(roman_string):
    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = roman_string
    t = 0
    res = 0
    prev = 0
    if not num:
        return 0
    if len(num) == 0 or num is None:
        return 0
    if not isinstance(num, str):
        return 0
    for n in reversed(num):
        t = dic[n]
        if prev > t:
            res -= t
        else:
            res += t
        prev = t
    return res
