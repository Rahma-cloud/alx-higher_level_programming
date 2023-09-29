#!/usr/bin/python3
"""urllib module"""
if __name__ == "__main__":
    import requests
    import sys
    auth = (sys.argv[1], sys.argv[2])
    r = requests.get(f"https://api.github.com/user", auth=auth)
    user_data = r.json()
    user_id = user_data.get('id')
    print(user_id)
