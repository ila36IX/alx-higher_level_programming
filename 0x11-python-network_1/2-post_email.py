#!/usr/bin/python3
"""
Takes in a URL and an email, sends a POST request to the passed URL with the
email as a parameter, and displays the body of the response
"""

from sys import argv
from urllib.request import urlopen
from urllib.parse import urlencode


if __name__ == "__main__":
    link = argv[1]
    parameter = urlencode({"email": argv[2]}).encode("ascii")
    with urlopen(link, parameter) as response:
        response = response.read().decode("utf-8")
