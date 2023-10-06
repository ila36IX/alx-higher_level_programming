#!/usr/bin/python3
import hidden_4
if __name__=="__main__":
    for string in dir(hidden_4):
        if (string[0] != "_"):
            print(string)
