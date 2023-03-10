#!/usr/bin/python3


def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None

    new_item = my_list[0]

    for element in my_list:
        if element > new_item:
            new_item = element
    return new_item
