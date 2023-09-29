#!/usr/bin/python3
"""urllib module"""
import urllib.request
import sys
if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        answer = response.getheader('X-Request-Id')
    print(answer)
