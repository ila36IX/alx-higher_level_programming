#!/usr/bin/python3
"""
featch a website
"""
from urllib.request import urlopen

if __name__ == "__main__":
    link = "https://alx-intranet.hbtn.io/status"
    with urlopen(link) as response:
        byte_content = response.read()
        print("Body response:")
        print(f"\t- type: {type(byte_content)}")
        print(f"\t- content: {byte_content}")
        print(f"\t- utf8 content: {byte_content.decode('utf8')}")
