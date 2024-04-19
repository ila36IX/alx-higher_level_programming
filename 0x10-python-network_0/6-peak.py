#!/usr/bin/python3
"""
Finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """Using binary algorithm"""
    if type(list_of_integers) is not list:
        return None
    if len(list_of_integers) == 0:
        return None
    num = list_of_integers
    left, right = 0, len(list_of_integers) - 1
    while left <= right:
        m = left + ((right - left + 1) // 2)
        if m > 0 and num[m - 1] >= num[m]:
            right = m - 1
        elif m < len(num) - 1 and num[m] < num[m + 1]:
            left = m + 1
        else:
            return num[m]
