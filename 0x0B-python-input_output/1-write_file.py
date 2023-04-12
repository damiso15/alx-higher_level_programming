#!/usr/bin/python3
"""
A module that writes a string to a text file (UTF8) and returns
the number of characters written
"""


def write_file(filename="", text=""):
    """
    a function that writes a string to a text file (UTF8) and returns
    the number of characters written

    Args:
        filename (str): The name of the file to write to.
        text (str): The text to write to the file.

    Returns:
        The number of characters written to the file.
    """

    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text)
    return len(text)
