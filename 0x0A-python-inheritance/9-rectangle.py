#!/usr/bin/python3
"""
Module Rectangle
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


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

    def area(self):
        """computes the area of a rectangle"""
        return self.__width * self.__height

    def __str__(self):
        return f"[Rectangle] {self.__height}/{self.__width}"
