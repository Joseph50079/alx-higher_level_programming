#!/usr/bin/python3

'''
This script output addtion of all arguments given as integer
'''
if __name__ == "__main__":
    from sys import argv

    if len(argv) != 1:
        num = 0
        for i in list(argv[1:]):
            i = int(i)
            num  += i
        print("{:d}".format(num))
