#!/usr/bin/python3

def best_score(a_dictionary):
    if (a_dictionary is None):
        return None
    if (len(a_dictionary.items()) == 0):
        return None
    big_value = 0
    key = ""
    for i, j in a_dictionary.items():
        if big_value < j:
            big_value = j
            key = i
    return (key)
