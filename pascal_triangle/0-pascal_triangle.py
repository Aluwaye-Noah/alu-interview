#!/usr/bin/python3
""" Pascal triangle method"""


def pascal_triangle(n):
    """Function that returns a list of lists of integers"""
    triangle = []
    if n <= 0:
        return triangle
    for i in range(1, n + 1):
        row = []
        for j in range(i):
            if j == 0 or j == i-1:
                row.append(1)
            else:
                row.append(triangle[i-2][j-1] + triangle[i-2][j])
        triangle.append(row)
    return triangle
