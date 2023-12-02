#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    many_chars = 0
    try:
        while x != 0:
            x -= 1
            print(my_list[many_chars], end="")
            many_chars += 1
    except Exception as err:
        print()
        return many_chars
    print()
    return many_chars
