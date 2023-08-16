#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result_matrix = []

    for row in matrix:
        result_row = []
        for elelment in row:
            result_row.append(element ** 2)
        result_matrix.append(result_row)

    return(result_matrix)
