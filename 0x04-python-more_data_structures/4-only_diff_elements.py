#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    ll = list(filter(lambda x: x in set_1, set_2))
    return set(filter(lambda x: x not in ll, list(set_1) + list(set_2)))
