#!/usr/bin/python3
"""
A module that returns the JSON representation of an object (string)
"""
import json


def to_json_string(my_obj):
    """

    Args:
        my_obj (str): The object.

    Returns:
        The JSON representation of an object (string).
    """

    json_obj = json.dumps(my_obj)
    return json_obj
