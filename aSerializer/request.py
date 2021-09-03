import requests
from datetime import datetime
import json

url = "http://127.0.0.1:8000/create/"

data = {
    'name': 'Rudra',
    'age': 13,
    'pass_date': '2012-09-04 06:00'
}

data = json.dumps(data)

r = requests.post(url=url, data=data)

data = r.json()

print(data)