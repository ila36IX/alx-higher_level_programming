#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    for i,j in a_dictionary.items():
        if (j & 1 != 0):
            a_dictionary.pop(i)
        return (a_dictionary)
