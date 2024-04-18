#!/usr/bin/python3
"""
Takes in a URL and an email, sends a POST request to the passed URL with the
email as a parameter, and displays the body of the response
"""

from sys import argv
from urllib.request import urlopen
from urllib.parse import urlencode

link = argv[1]
parameter = urlencode({"email": argv[2]})
print(parameter)

if __name__ == "__main__":
    with urlopen(url, parameter) as response:
        response = response.read().encode("utf-8")
