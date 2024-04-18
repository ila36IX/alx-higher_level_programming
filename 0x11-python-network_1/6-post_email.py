#!/usr/bin/python3
# Takes in a URL and an email address, sends a POST request to the passed URL
# with the email as a parameter, and finally displays the body of the

from sys import argv
import requests

r = requests.post(argv[1], {"email": argv[2]})
print(r.text)
