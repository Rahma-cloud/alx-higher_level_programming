#!/usr/bin/python3
"""urllib module"""
if __name__ == "__main__":
    import requests
    import sys
    payload = {'email': sys.argv[2]}
    response = requests.post(sys.argv[1], data=payload)
    print(response.text)
