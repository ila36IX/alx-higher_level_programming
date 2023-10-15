#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dic = list(a_dictionary.items())[:]
    for i, j in dic:
        if (j & 1 != 0):
            a_dictionary.pop(i)
    return (a_dictionary)
