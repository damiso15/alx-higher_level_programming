#!/usr/bin/python3
"""
A class BaseGeometry
"""


class BaseGeometry:
    """
    A class BaseGeometry
    """

    def area(self):
        """
        A Public Instance that raises an Exception with the message area() is
        not implemented
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        A Public Instance that validates value
        """

        if type(value) != int:
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
