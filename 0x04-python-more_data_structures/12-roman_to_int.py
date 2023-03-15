#!/usr/bin/python3


def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string is None:
        return None


    roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            }

    res = 0
    prev_val = 0
    for i in range(len(roman_string) - 1, -1, -1):
        if roman_dict[roman_string[i]] >= prev_val:
            res += roman_dict[roman_string[i]]
        else:
            res -= roman_dict[roman_string[i]]
        prev_val = roman_dict[roman_string[i]]

    return res
