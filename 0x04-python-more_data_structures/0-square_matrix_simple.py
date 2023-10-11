#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    square = []
    for i in range(len(matrix)):
        a = list(map((lambda x: x * x) , matrix[i]))
        square.append(a)
    return square
