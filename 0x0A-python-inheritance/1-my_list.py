#!/usr/bin/python
"""
A class MyList that inherits from list
"""


class MyList(list):
    """
    MyList inherits from builtin list class
    """

    def print_sorted(self):
        """
        A public instance that prints the list, but sorted (ascending sort)
        """
        sorted_list = sorted(self)
        print(sorted_list)
