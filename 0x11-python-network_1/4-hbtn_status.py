#!/usr/bin/python3
import requests
<<<<<<< HEAD
r = requests.get('https://alx-intranet.hbtn.io/status')
print(r.text)
=======
r = requests.get('https://alx-intranet.hbtn.io/status', auth=('user', 'pass'))
r.status_code
>>>>>>> 66e7130f41ba9442c2e8bcacab55d333aa37568f
