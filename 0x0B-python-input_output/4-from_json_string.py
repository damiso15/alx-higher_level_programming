#!/usr/bin/python3
"""
A module that returns an object (Python data structure)
represented by a JSON string
"""
import json


def from_json_string(my_str):
    """
    function that returns an object (Python data structure) represented
    by a JSON string

    Args:
        my_str (str): The object.

    Returns:
       An object (Python data structure) represented by a JSON string 
    """

    python_obj = json.loads(my_str)
    return python_obj
