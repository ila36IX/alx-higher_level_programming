#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    sumof = 0
    for i in argv[1:]:
        sumof += int(i)
    print("{}".format(sumof))
