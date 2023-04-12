#!/usr/bin/python3
"""
A module that creates an Object from a “JSON file”
"""
import json


def load_from_json_file(filename):
    """
    A function that creates an Object from a “JSON file”

    Args:
        filename (str): The name of the file to create the python Object from

    Returns:
        Object from a “JSON file” 
    """

    with open(filename, 'r', encoding="utf-8") as f:
        python_obj = json.load(f)
    return python_obj
