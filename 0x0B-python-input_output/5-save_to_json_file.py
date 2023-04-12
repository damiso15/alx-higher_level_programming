#!/usr/bin/python3
"""
A module that writes an Object to a text file, using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """
    A function that writes an Object to a text file, using a JSON
    representation

    Args:
        my_obj (str): The python object to convert to JSON.
        filename (str): The name of the file to store the JSON.

    Returns:
       An Object to a text file, using a JSON representation
    """

    json_obj = json.dumps(my_obj)

    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(json_obj)
