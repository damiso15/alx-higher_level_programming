#!/usr/bin/python3


def matrix_mul(m_a, m_b):
    """Multiplies two matrices.
    Args:
        m_a: list of lists representing a matrix.
        m_b: list of lists representing a matrix.
    Returns:
        A new matrix representing the multiplication of m_a and m_b.
    Raises:
        TypeError: if m_a or m_b is not a list or a list of lists, or if an
        element is not an int or float.
        ValueError: if m_a or m_b is empty or not a rectangle, or if matrices
        can't be multiplied.
    """
    if type(m_a) != list:
        raise TypeError("m_a must be a list")
    elif type(m_b) != list:
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    elif not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if len(m_a) == 0 or len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")
    elif len(m_b) == 0 or len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")

    if not all(isinstance(elem, (int, float)) for row in m_a for elem in row):
        raise TypeError("m_a should contain only integers or floats")
    elif not all(isinstance(elem, (int, float))for row in m_b for elem in row):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    elif not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            elem = 0
            for k in range(len(m_a[0])):
                elem += m_a[i][k] * m_b[k][j]
            row.append(elem)
        result.append(row)
    return result
