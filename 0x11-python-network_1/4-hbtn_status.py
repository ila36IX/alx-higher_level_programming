#!/usr/bin/python3
# etches https://alx-intranet.hbtn.io/status
import requests

r = requests.get("https://alx-intranet.hbtn.io/status")
print("Body response:")
print(f"\t - {type(r.text)}")
print(f"\t - {r.text}")
