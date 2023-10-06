#!/usr/bin/python3
from sys import argv
if __name__=="__main__":
    sumof = 0
    for i in argv[1:]:
        sumof += int(i)
    print("{}".format(sumof))
