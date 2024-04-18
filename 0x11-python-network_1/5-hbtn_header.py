#!/usr/bin/python3
# Takes in a URL, sends a request to the URL and displays the value of the
# variable X-Request-Id in the response header

from sys import argv
import requests

r = requests.get(argv[1])
print(r.headers.get("X-Request-Id"))
r = requests.get("http://getalien.tech")
