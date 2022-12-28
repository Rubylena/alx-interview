#!/usr/bin/python3
"""Pascal Triangle Challenge"""


def pascal_triangle(n):
    """returns a list of lists of numbers
    representing the pascals triangle"""
    if n <= 0:
        return []

    # gives a complete list with zero values or n [0, 0, 0, 0, 0]
    pascal_triangle = [0] * n

    for i in range(n):
        # define a row and fill first and last idx with 1

        # breakdown the list into a triangle
        new_row = [0] * (i+1)
        # replace all the index[0] with 1
        new_row[0] = 1
        # replace zero with 1 for all the last index in a row
        new_row[len(new_row) - 1] = 1

        for j in range(1, i):
            if j > 0 and j < len(new_row):
                a = pascal_triangle[i - 1][j]
                b = pascal_triangle[i - 1][j - 1]
                new_row[j] = a + b

        pascal_triangle[i] = new_row

    return pascal_triangle
