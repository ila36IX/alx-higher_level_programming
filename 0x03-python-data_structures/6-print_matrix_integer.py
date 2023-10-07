#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for j, i in enumerate(row):
            print("{}".format(i), end="")
            if (j != len(row) - 1):
                print(" ", end="")
        print()
