#!/usr/bin/python3

BaseGeometry = __import__("7-base_geometry").BaseGeometry
"""
Module 8-rectangle.py
"""


class Rectangle(BaseGeometry):
    """
    Rectangle class computes for rectangle

    Args:
        width: (int): width if rectangle
        height: (int): height of rectangle
    """

    def __init__(self, width, height):
        self.integer_validator("height", height)
        self.integer_validator("width", width)
        self.__width = height
        self.__height = width
