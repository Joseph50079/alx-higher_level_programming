#!/usr/bin/python3

'''Class Square defines square'''


class Square:
    '''define the class attribute to private'''
    def __init__(self, size=0):
        '''initializing and creating private instance attributee'''
        if not isinstance(size, int):
            raise TypeError('size must be integer')
            '''prints if there is a type error'''
        else:
            if size < 0:
                raise ValueError('size must be >= 0')
                '''prints if there was a value error'''
            else:
                self.__size = size
