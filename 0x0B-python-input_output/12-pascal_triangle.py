#!/usr/bin/python3
"""Define a pascal triangle"""


def pascal_triangle(n):
    """
    Function that returns a list of lists of integers
    representing the Pascal's triangle of n

    Args:
        n (int): Number

    Returns:
        List of list of integers
    """
    if n <= 0:
        return []

    matrix = [[1]]
    while len(matrix) != n:
        mat = matrix[-1]
        tmp = [1]
        for i in range(len(mat) - 1):
            tmp.append(mat[i] + mat[i + 1])
        tmp.append(1)
        matrix.append(tmp)
    return matrix
