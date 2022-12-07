#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix:
        if len(matrix) > 0:
            for i in range(len(matrix)):
                for b in range(len(matrix[i])):
                    if b == 0:
                        pass
                    else:
                        print("", end=' ')
                    print("{:d}".format(matrix[i][b]), end='')
                print("\n", end='')
