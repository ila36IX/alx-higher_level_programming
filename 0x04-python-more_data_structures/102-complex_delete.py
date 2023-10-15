#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    items = list(a_dictionary.items())[:]
    for i, j in items:
        if j == value:
            del a_dictionary[i]
    return (a_dictionary)
