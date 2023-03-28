#!/usr/bin/python3
"""
A class Square that defines a square
"""


class Square:
    """
    A Square with the following attributes:
    Private instance attribute: size
    Public instance method: def area(self):
    Instantiation with size: def __init__(self, size=0):
    """

    def __init__(self, size=0):
        """ Initialize size """
        self.size = size

    @property
    def size(self):
        """ The property for the size method to retrieve it """
        return self.__size

    @size.setter
    def size(self, value):
        """ The property setter for the size method to set it """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ A public instance method that returns the current square area """
        return self.__size ** 2

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()
