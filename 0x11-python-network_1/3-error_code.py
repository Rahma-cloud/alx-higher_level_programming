#!/usr/bin/python3
"""urllib module"""
import urllib.request
import sys
if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            content = response.read().decode('utf-8')
            print(content)
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
