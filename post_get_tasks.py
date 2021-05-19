import requests
from pprint import pprint

import json

# input your information
user = {'userid': '', 'password': ''}
r = requests.post("http://127.0.0.1:8000/post/get_tasks",
                  params=user)  # POST user data

print(json.dumps(r.json(), ensure_ascii=False))
