#!/usr/bin/python3

'''Class Square defines square'''


class Square:
    try:
        def __init__(self, sizee=0):
            '''initializing and creating private instance attributee'''
            self.__size = size
    except TypeError:
        '''prints if there is a type error'''
        print("size must be an integer")
    except ValueError:
        '''prints if there was a value error'''
        print("size must be >= 0")
