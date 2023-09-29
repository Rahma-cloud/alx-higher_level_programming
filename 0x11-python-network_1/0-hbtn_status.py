#!/usr/bin/python3
import urllib.request
"""urlib module"""
with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as response:
    content = response.read()
    utf8_content = content.decode('utf-8')
print("Body response:")
print(f"    - type: {type(content)}")
print(f"    - content: {content}")
print(f"    - utf8 content: {utf8_content}")
