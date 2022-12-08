#!/usr/bin/python3
# checks if c is a lower case character
def islower(c):
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
