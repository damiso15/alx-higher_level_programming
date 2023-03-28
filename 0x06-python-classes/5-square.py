#!/usr/bin/python3
"""
A class Square that defines a square
"""


class Square:
    """A Square with a size"""

    def __init__(self, size=0):
        """Initialize size"""
        self.size = size

    @property
    def size(self):
        """The property for the size method to retrieve it"""
        return self.__size

    @size.setter
    def size(self, value):
        """The property setter for the size method to set it"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """A public instance method that returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """A public instance method that prints in stdout the square with
        the character #"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
