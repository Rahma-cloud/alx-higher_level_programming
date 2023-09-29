#!/usr/bin/python3
"""urllib module"""
if __name__ == "__main":
    import requests
    import sys
    if len(sys.argv) == 2:
        letter = sys.argv[1]
    else:
        letter = ""
    payload = {'q': letter}
    try:
        r = requests.post('http://0.0.0.0:5000/search_user', data=payload)
        r_data = r.json()
        if r_data:
            print("[{}] {}".format(r_data.get('id'), r_data.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
    except Exception as e:
        print(f"Error: {e}")
