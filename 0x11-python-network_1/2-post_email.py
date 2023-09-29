#!/usr/bin/python3
"""urllib module"""
import urllib.request
import sys
if __name__ == "__main__":
    email_encoded = sys.argv[2].replace('@', '%40').replace('.', '%2E')
    data = 'email=' + email_encoded
    with urllib.request.urlopen(
        sys.argv[1], data=data.encode('utf-8')
    ) as response:
        content = response.read().decode('utf-8')
        print(content)
