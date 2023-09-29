#!/usr/bin/python3
import requests
import sys
headers = {'Authorization': f'Basic {sys.argv[1]}:{sys.argv[2]}'}
r = requests.get(f"https://api.github.com/user", headers=headers)
r.raise_for_status()
user_data = r.json()
user_id = user_data.get('id')
