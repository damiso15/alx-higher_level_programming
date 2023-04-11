#!/usr/bin/python3
"""
A Rectangle that inherits from BaseGeometry
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


class Rectangle(BaseGeometry):
    """
    A Rectangle that inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """
        Instantiation with width and height
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
