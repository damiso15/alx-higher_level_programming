#!/usr/bin/python3
"""
A class Square that defines a square
"""


class Square:
    """A Square with a size"""

    def __init__(self, size=0):
        """Initialize size"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """A public instance method that returns the current square area"""
        return self.__size ** 2
