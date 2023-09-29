#!/usr/bin/python3
"""urllib module"""
if __name__ == "__main__":
    import requests
    import sys
    r = requests.get(sys.argv[1])
    x_requests_id = r.headers.get('X-Request-Id')
    print(x_requests_id)
