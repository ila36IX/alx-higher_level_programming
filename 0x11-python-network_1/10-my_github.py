#!/usr/bin/python3
"""
Takes your GitHub credentials (username and password) and uses the GitHub API
to display your id
"""

from sys import argv
import requests

username = argv[1]
pass_token = argv[2]
headers = {"Authorization": f"token {pass_token}", "X-GitHub-Api-Version": "2022-11-28"}
r = requests.get(f"https://api.github.com/users/ila36IX", data=headers)
print(r.json().get("id"))
