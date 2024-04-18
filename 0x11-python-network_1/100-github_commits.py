#!/usr/bin/python3
"""
List 10 commits (from the most recent to oldest) of the repository
“rails” by the user “rails” You must use the GitHub API, here is the
documentation https://developer.github.com/v3/repos/commits/ Print all
commits by: `<sha>: <author name>` (one by line)
"""

from sys import argv
import requests

if __name__ == "__main__":
    repo_name = argv[1]
    owner_name = argv[2]

    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    r = requests.get(url, data=headers)
    response_json = r.json()
    for commit in response_json[:10]:
        print(f"{commit.get('sha')}:", commit.get("commit").get("author").get("name"))
