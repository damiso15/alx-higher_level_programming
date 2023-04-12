#!/usr/bin/python3
"""
A class MyInt that inherits from int
"""


class MyInt(int):
    """
    A class MyInt that inherits from int
    """

    def __eq__(self, value):
        return super().__ne__(value)

    def __ne__(self, value):
        return super().__eq__(value)
