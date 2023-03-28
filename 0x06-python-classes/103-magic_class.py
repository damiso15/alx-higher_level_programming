#!/usr/bin/python3
import math

"""
A class MagicClass
"""


class MagicClass:
    def __init__(self, radius=0):
        """ Instantiation with radius """

        self.__radius = 0

        if type(value) not in [int, float]:
            raise TypeError('radius must be a number')
        self.__radius = value

    def area(self):
        """ A public instance method that returns the current square area """

        return self.__radius ** 2 * math.pi

    def circumference(self):
        """ A public instance method that returns the current circumference """

        return 2 * math.pi * self.__radius
