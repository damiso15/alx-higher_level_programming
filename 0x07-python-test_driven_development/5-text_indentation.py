#!/usr/bin/python3
"""
text_indentation

This function prints a text with 2 new lines after each of these
characters: ., ? and :
"""


def text_indentation(text):
    """ prints a text with 2 new lines after each of these
    characters: ., ? and :
    - Prototype: def text_indentation(text):
    - text must be a string, otherwise raise a TypeError exception with
    the message text must be a string
    - There should be no space at the beginning or at the end of
    each printed line
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    char = ['.', '?', ':']
    # split the text into a list of lines using the given char as separator
    # iterates over each line in the list
    lines = []
    line_start = 0
    for i in range(len(text)):
        if text[i] in char:
            lines.append(text[line_start:i+1].strip())
            line_start = i+1
    if line_start < len(text):
        lines.append(text[line_start:].strip())

    for line in lines:
        # if the line is not empty, print it with two newlines after the char
        if line != "":
            print(line)
            print()
