#!/usr/bin/python3
import urllib.request
import sys
with urllib.request.urlopen(sys.argv[1]) as response:
    answer = response.getheader('X-Request-Id')
print(answer)
