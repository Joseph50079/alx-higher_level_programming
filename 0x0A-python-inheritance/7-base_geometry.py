#!/usr/bin/python3
"""
Module 6-base geometry.py
"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """area returns area value
        """
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """validate value"""

        self.name = name
        self.value = value
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
