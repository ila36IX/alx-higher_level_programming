#!/usr/bin/python3
"""
Takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

from sys import argv
import requests

if __name__ == "__main__":
    post_letter = ""

    if len(argv) == 2:
        post_letter = argv[1]
    r = requests.post("http://0.0.0.0:5000/search_user", data={"q": post_letter})

    try:
        json_r = r.json()
        if len(json_r) == 0:
            print("No result")
        else:
                print(f"[{json_r.get('id')}] {json_r.get('name')}")
    except expression as e:
        print("Not a valid JSON")
