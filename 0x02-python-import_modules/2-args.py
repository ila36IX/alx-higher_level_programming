#!/usr/bin/python3
from sys import argv
if __name__=="__main__":
    if (len(argv) == 1):
        print("0 arguments.")
    else:
        length = len(argv)
        print("{} argument{}:".format(length - 1, "s" if length > 2 else ""))
        for i in range(1, length):
            print("{}: {}".format(i, argv[i]))
