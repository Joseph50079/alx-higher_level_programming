#!/usr/bin/python3

"""Module 10-square.py"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Square computes for square"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """computes square area"""
        return self.__size ** 2

    def __str__(self):
        return ("[{}] {}/{}".format("Square", self.__size, self.__size))
