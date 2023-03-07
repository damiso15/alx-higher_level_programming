#!/usr/bin/python3

def remove_char_at(str, n):
    string = ""
    for char in range(len(str)):
        if char != n:
            string += str[char]
    return string

