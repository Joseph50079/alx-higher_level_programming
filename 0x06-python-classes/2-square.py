#!/usr/bin/python3

'''Class Square defines square'''


class Square:
    '''define the class attribute to private'''
    def __init__(self, size=0):
        '''initializing and creating private instance attributee'''
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be integer")
            self.__size = size
        else:
            raise TypeError("size must be integer")
