#!usr/bin/python3

"""

MyList that inherits from list

"""
import doctest


class MyList(list):
    """MyLIst is child that inharted from list"""

    def __init__(self):
        super().__init__(self)

    def print_sorted(self):
        """Print the sorted list"""
        print(sorted(self))


if __name__ == "__main__":
    doctest.testfile("./tests/1-my_list.txt")
