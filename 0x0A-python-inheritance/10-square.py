#!/usr/bin/python3

"""Module 10-square.py"""

class Square(Rectangle):
    """Square computes for square"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """computes square area"""
        return self.__size ** 2
