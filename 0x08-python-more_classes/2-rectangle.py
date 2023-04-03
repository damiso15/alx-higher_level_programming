#!/usr/bin/python3
"""
A class that defines a rectangle
"""


class Rectangle:
    """ Returns the Area and Perimeter of a rectangle
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
    - Public instance method: def area(self): that returns the rectangle area
    - Public instance method: def perimeter(self): that returns the
    rectangle perimeter:
        - if width or height is equal to 0, perimeter is equal to 0
    """

    def __init__(self, width=0, height=0):
        """ Initialize width and height """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ The property for the width module to retrieve it """

        return self.__width

    @property
    def height(self):
        """ The property for the height module to retrieve it """

        return self.__height

    @height.setter
    def height(self, value):
        """ The property setter for the width module to set it """

        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value < 0:
            raise TypeError("height must be >= 0")

        self.__height = value

    @width.setter
    def width(self, value):
        """ The property setter for the width module to set it """

        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise TypeError("width must be >= 0")

        self.__width = value

    def area(self):
        """ A public instance method that returns the rectangle area """

        return self.__width * self.__height

    def perimeter(self):
        """ A public instance method that returns the rectangle perimeter """

        return (2 * self.__width) + (2 * self.__height)
