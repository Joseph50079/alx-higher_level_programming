#!/usr/bin/python3

# checks if c is a lower upper case

def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            a = ord(str[i])
            a -= 32
        else:
            a = ord(str[i])
        str1 += chr(a)
    print("{:s}".format(str1))
