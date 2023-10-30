#!/usr/bin/python3
"""

This module contains a function that divides all elements of a matrix.

"""


def matrix_divided(matrix, div):
    """Return a new matrix that divides all elements of a matrix
    Args:
        matrix: List of lists that have the some size
        div: Non-zero integer or float
    """
    not_list = "matrix must be a matrix (list of lists) of integers/floats"
    not_some_size_error = "Each row of the matrix must have the same size"

    if not isinstance(matrix, list):
        raise TypeError(not_list)

    row_len = len(matrix[0])
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(not_list)
        if len(row) != row_len:
            raise TypeError(not_some_size_error)

        for n in row:
            if type(n) not in [int, float]:
                raise TypeError(not_list)

        if type(div) not in [int, float]:
            raise TypeError("div must be a number")

        if div == 0:
            raise ZeroDivisionError("division by zero")

    matrix_clone = []
    for row in matrix:
        matrix_clone.append([round(num / div, 2) for num in row])
    return matrix_clone
