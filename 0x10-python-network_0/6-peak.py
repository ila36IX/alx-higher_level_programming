#!/usr/bin/python3
# finds a peak in a list of unsorted integers
def find_peak(list_of_integers):
    if type(list_of_integers) is not list:
        return None
    if len(list_of_integers) == 0:
        return None
    num = list_of_integers
    l, r = 0, len(list_of_integers) - 1
    while l <= r:
        m = l + ((r - l + 1) // 2)
        if m > 0 and num[m - 1] >= num[m]:
            r = m - 1
        elif m < len(num) - 1 and num[m] < num[m + 1]:
            l = m + 1
        else:
            return num[m]


print(find_peak([1, 2, 4, 6, 3]))
print(find_peak([4, 2, 1, 2, 3, 1]))
print(find_peak([2, 2, 2]))
print(find_peak([]))
print(find_peak([-2, -4, 2, 1]))
print(find_peak([4, 2, 1, 2, 2, 2, 3, 1]))
