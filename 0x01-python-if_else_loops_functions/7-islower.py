#!/usr/bin/python3

def islower(c):
    for i in range(97, 123):
        a = chr(i)
        if c == a:
            return True
        else:
            return False
