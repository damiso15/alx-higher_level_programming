#!/usr/bin/python3
"""
A module that returns a list of lists of integers representing the Pascal’s
triangle of n
"""


def pascal_triangle(n):
    """
    A function that returns a list of lists of integers representing the
    Pascal’s triangle of n

    Args:
        n (int): The integer to return the list of lists of integers

    Return:
        The list of lists of integers representing the Pascal’s
    triangle of n
    """

    my_list = []
    if n <= 0:
        return my_list

    tri_list = [[1]]
    for num in range(1, n):
        row = [1]
        for num2 in range(1, num):
            row.append(tri_list[num - 1][num2 - 1] + tri_list[num - 1][num2])
        row.append(1)
        tri_list.append(row)

    return tri_list
