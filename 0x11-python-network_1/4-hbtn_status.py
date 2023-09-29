#!/usr/bin/python3
import requests
r = requests.get('https://alx-intranet.hbtn.io/status')
content = r.text
print("Body response:")
print(f"\t- type: {type(content)}")
print(f"\t- content: {content}")
