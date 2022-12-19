#!/usr/bin/python3

'''
this module prints alist reversed
'''

def print_reversed_list_integer(my_list=[]):
    for i in range(len(my_list) -1, -1, -1):
        print("{:d}".format(i))
