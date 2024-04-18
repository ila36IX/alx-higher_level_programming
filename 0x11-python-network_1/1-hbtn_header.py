#!/usr/bin/python3
"""
Script that takes a url as argument and displays the value of the
X-Request-Id variable found in the header of the response
"""

from sys import argv
from urllib.request import urlopen

if __name__ == "__main__":
    link = argv[1]
    with urlopen(link) as response:
        print(response.getheader("X-Request-Id"))
