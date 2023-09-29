#!/usr/bin/python3
import requests
import sys
payload = {'email': sys.argv[2]}
response = requests.post(sys.argv[1], data=payload)
print(response.text)
