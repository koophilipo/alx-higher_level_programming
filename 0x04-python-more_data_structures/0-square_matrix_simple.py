#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    if matrix:
        if len(matrix) > 0:
            new_matrix = []
            row = []
            for i in range(len(matrix)):
                for j in range(len(matrix[i])):
                    row.append(matrix[i][j]**2)
                new_matrix.append(row.copy())
                row.clear()
            return (new_matrix)
    return (matrix)
