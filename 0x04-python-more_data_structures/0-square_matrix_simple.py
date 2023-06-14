#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []
    for col in matrix:
        square = list(map(lambda x: x*x, col))
        new_matrix.append(square)
    return new_matrix
