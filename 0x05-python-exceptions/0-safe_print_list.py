#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    many_chars = 0
    try:
        while x != 0:
            x -= 1
            print(my_list[many_chars], end="")
            many_chars += 1
    except:
        pass
    print()
    return many_chars

my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list(my_list, 2)
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))
