#!/usr/bin/python3
"""
A module that returns the dictionary description with simple data structure
(list, dictionary, string, integer and boolean) for JSON serialization of
an object
"""


def class_to_json(obj):
    """
    A function that returns the dictionary description with simple data
    structure (list, dictionary, string, integer and boolean) for JSON
    serialization of an object

    Args:
        obj (str): The object to convert to a dictionary

    Returns:
        The dictionary description with simple data structure (list, dictionary
        string, integer and boolean) for JSON serialization of an object:
    """

    python_dictionary = {}
    attributes = dir(obj)
    for item in attributes:
        if item.startswith("__"):
            continue

        value = getattr(obj, item)
        if isinstance(value, (list, dict, str, int, bool)):
            python_dictionary[item] = value

    return python_dictionary
