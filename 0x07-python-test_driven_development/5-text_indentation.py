#!/usr/bin/python3

"""

prints a text with 2 new lines after each of these
characters: ., ? and :

"""


def text_indentation(text):

    """
    prints a text with 2 new lines after each of
    these characters: ., ? and :
    args:
        taxt: Must be a string

    raise:
        TypeError: If text is not string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    space = False

    for i in text:
        if i != " ":
            space = False

        if space:
            continue

        print(i, end="")
        if i in [".", "?", ":"] and not space:
            print("\n")
            space = True
