#!/usr/bin/python3
import requests
import sys
payload = {'email': email}
response = requests.post(sys.argv[1], data=payload)
print(response.text)
