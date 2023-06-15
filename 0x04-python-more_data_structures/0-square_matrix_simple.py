#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    powerMatrix = []
    for row in matrix:
        powerMatrix.append(list(map(lambda x: x ** 2, row)))
    return powerMatrix
