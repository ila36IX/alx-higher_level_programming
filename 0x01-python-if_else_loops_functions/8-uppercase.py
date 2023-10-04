#!/usr/bin/python3
def uppercase(str):
    for c in str:
        char = c
        if (ord(c) >= 97 and ord(c) <= 122):
            char = chr(ord(c) - 32)
        print("{}".format(char), end="")
    print()
