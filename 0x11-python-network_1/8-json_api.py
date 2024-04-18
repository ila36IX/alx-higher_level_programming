#!/usr/bin/python3
# Takes in a letter and sends a POST request to
# http://0.0.0.0:5000/search_user with the letter as a parameter.

from sys import argv
import requests

post_letter = ""

if len(argv) == 2:
    post_letter = argv[2]
r = requests.get("http://0.0.0.0:5000/search_user")

try:
    json_r = r.json()
except expression as e:
    json_r = {}
    print("No result")

if len(json_r) == 0:
    print("No result")
else:
    for k, v in json_r:
        print(f"[{k}] {v}")
