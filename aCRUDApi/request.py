import requests
import json

url = "http://127.0.0.1:8000/api/student/"

def get(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    data = json.dumps(data)
    r = requests.get(url, data=data)
    res = r.json()
    print(res)

# get(id=1)

def post(data):
    data = json.dumps(data)
    r = requests.post(url, data=data)
    res = r.json()
    print(res)


def put(data):
    data = json.dumps(data)
    r = requests.put(url, data=data)
    res = r.json()
    print(res)

def delete(data):
    data = json.dumps(data)
    r = requests.delete(url, data=data)
    res = r.json()
    print(res)

data = {
    'id': 7,
    'name': 'Fake',
    'roll_no': 106,
    'city': 'undefined'
}

# post(data)
# put(data)
delete(data)