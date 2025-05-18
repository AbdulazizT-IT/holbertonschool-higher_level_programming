#!/usr/bin/python3
"""
This module defines the function matrix_divided
which divides all elements of a matrix by a number.
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by div.

    Args:
        matrix: list of lists of integers/floats.
        div: number to divide the matrix elements by.

    Returns:
        A new matrix with the result of the division.

    Raises:
        TypeError: If matrix is not a list of lists of ints/floats,
                   if rows are not the same size,
                   or if div is not a number.
        ZeroDivisionError: If div is 0.
    """
    # Check if matrix is a list of lists of ints/floats
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for row in matrix:
        if not all(isinstance(x, (int, float)) for x in row):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check that all rows have the same size
    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Check div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check div is not zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide each element and round to 2 decimal places
    new_matrix = [[round(x / div, 2) for x in row] for row in matrix]
    return new_matrix
