#!/usr/bin/python3
import requests
r = requests.get('https://alx-intranet.hbtn.io/status')
print(r.text)
