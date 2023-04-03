#!/usr/bin/python3
"""
matrix_divided

This function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """ returns a new matrix
    - Prototype: def matrix_divided(matrix, div):
    - matrix must be a list of lists of integers or floats,
    otherwise raise a TypeError exception with the message
    matrix must be a matrix (list of lists) of integers/floats
    - Each row of the matrix must be of the same size, otherwise
    raise a TypeError exception with the message Each row of
    the matrix must have the same size
    - div must be a number (integer or float), otherwise raise
    a TypeError exception with the message div must be a number
    - div can’t be equal to 0, otherwise raise a ZeroDivisionError
    exception with the message division by zero
    - All elements of the matrix should be divided by div, rounded
    to 2 decimal places
    """

    if matrix is None or len(matrix) == 0:
        raise TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        if not all(isinstance(value, (int, float)) for value in row):
            raise TypeError("matrix must be a matrix "
                            "(list of lists) of integers/floats")
        new_row = [round(value / div, 2) for value in row]
        new_matrix.append(new_row)
    return new_matrix
