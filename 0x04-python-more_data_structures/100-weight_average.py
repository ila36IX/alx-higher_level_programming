#!/usr/bin/python3

def weight_average(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return (0)
    score = 0
    weight = 0
    for i, j in my_list:
        score += i * j
        weight += j
    return score / weight
