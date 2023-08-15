#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in marix:
        for col_idx, value in enumerate(row):
            if col_idx == len(row) -1:
                print("{:d}".format(value), end="")
            else:
                print("{:d}".format(value), end=" ")
        print()
