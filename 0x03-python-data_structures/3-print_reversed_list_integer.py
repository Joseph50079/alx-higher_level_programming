#!/usr/bin/python3
'''
this module prints alist reversed
'''
rev_list = []
def print_reversed_list_integer(my_list=[]):
    rev_list = my_list.reverse()
    for i in rev_list:
        print("{:d}".format(i))
