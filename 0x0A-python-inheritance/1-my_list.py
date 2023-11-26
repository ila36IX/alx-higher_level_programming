#!/usr/bin/python3

"""

MyList that inherits from list

"""


class MyList(list):
    """MyLIst is child that inharted from list"""

    def print_sorted(self):
        """Print the sorted list"""
        print(sorted(self))
