#!/usr/bin/python3
"""
A module function that appends a string at the end of a text file (UTF8) and
returns the number of characters added
"""


def append_write(filename="", text=""):
    """
    function that appends a string at the end of a text file (UTF8) and
    returns the number of characters added

    Args:
        filename (str): The name of the file to write to.
        text (str): The text to write to the file.

    Returns:
        The number of characters added to the file.
    """

    with open(filename, 'a+', encoding="utf-8") as f:
        f.write(text)
    return len(text)
