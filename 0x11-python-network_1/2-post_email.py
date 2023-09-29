#!/usr/bin/python3
import urllib.request
import sys
email_encoded = email.replace('@', '%40').replace('.', '%2E')
data = 'email=' + email_encoded
with urllib.request.urlopen(url, data=data.encode('utf-8')) as response:
    content = response.read().decode('utf-8')
    print(content)
