#!/usr/bin/python3


def search_replace(my_list, search, replace):
    new_list = []

    for index in my_list:
        if index == search:
            new_list.append(replace)
        else:
            new_list.append(index)

    return new_list
