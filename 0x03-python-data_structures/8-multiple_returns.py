#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if (length == 0):
        tup = (0, None)
        return (tup)
    else:
        tup = (length, sentence[0])
        return (tup)
