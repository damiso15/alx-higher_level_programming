#!/usr/bin/python3
"""
The module returns True if the object is exactly an instance of
the specified class
"""


def is_same_class(obj, a_class):
    """
    returns True if the object is exactly an instance of the specified
    class; otherwise False
    """

    obj_type = type(obj)
    if obj_type == a_class:
        return True
    else:
        return False
