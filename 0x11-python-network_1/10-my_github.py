#!/usr/bin/python3
"""
Takes your GitHub credentials (username and password) and uses the GitHub API
to display your id
"""

from sys import argv
import requests

if __name__ == "__main__":
    username = argv[1]
    pass_token = argv[2]
    headers = {"Authorization": f"Bearer {pass_token}", "X-GitHub-Api-Version": "2022-11-28"}
    r = requests.get(f"https://api.github.com/users/{username}", headers=headers)
    print(r.json().get("id"))
