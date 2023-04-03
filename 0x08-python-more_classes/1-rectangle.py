#!/usr/bin/python3
"""
A class that defines a rectangle
"""


class Rectangle:
    """
    A class Rectangle that defines a rectangle
    - Private instance attribute: width:
        - property def width(self): to retrieve it
        - property setter def width(self, value): to set it:
            - width must be an integer, otherwise raise a TypeError exception
            with the message width must be an integer
            - if width is less than 0, raise a ValueError exception with the
            message width must be >= 0
    - Private instance attribute: height:
        - property def height(self): to retrieve it
        - property setter def height(self, value): to set it:
            - height must be an integer, otherwise raise a TypeError exception
            with the message height must be an integer
            - if height is less than 0, raise a ValueError exception with the
            message height must be >= 0
    - Instantiation with optional width and height:
    def __init__(self, width=0, height=0):
    """

    def __init__(self, width=0, height=0):
        """ Initialize width and height """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ The property for the width module to retrieve it """

        return self.__width

    @width.setter
    def width(self, value):
        """ The property setter for the width module to set it """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise TypeError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ The property for the height module to retrieve it """

        return self.__height

    @height.setter
    def height(self, value):
        """ The property setter for the width module to set it """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise TypeError("height must be >= 0")
        else:
            self.__height = value
