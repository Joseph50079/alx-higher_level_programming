#!/usr/bin/python3

'''
Class Square defines square
'''


class Square:
    '''define the class attribute to private
    Attribute:
        size: The size of Square
    '''
    def __init__(self, size=0):
        '''initializing and creating private instance attribute
        Args:
            size(int): This size of squares
        '''

        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
        else:
            raise TypeError("size must be an integer")

    def area(self):
        '''This is class method returns area
        Attribute:
            Args:
                self attribute to objects
            Return:
                area of Square
        '''
        self.__size *= self.__size
        return self.__size

    def my_print(self):
        '''my_print prints square using '#'
        if size is less than zeeero it should print a new line
        else print square
        '''
        if self.__size <= 0:
            print('')
        else:
            for i in range(self.__size):
                for n in range(self.__size):
                    print('#', end='')
                print('')

    @property
    def size(self):
        '''This will get the attribute of Square
        Return:
            returns the attribute of Square
        '''
        return self.__size

    @size.setter
    def size(self, value):
        '''This will set a value of square
        Args:
            value: value of square
        Return:
            returns the value (new square value)
        '''
        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value
        else:
            raise TypeError("size must be an integer")
        return self.__size
