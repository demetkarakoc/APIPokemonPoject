import rsp as rsp

python -m pip install

import pip
import requests
import json

def main():
    rsq= requests.get('http://pokeapi.co/api/v2/pokemon/1/')
    if rsp.status_ == 200:
        json_rsp = rsp.json()
        poke_name = json_rsp['name']
    print(poke_name)
    print("HTTP Status Code: " + str(req.status_code))
    print(req.headers)
    json_response = json.loads(req.content)
    print("Pokemon Name: " + json_response['name'])
    print(req.status_code)

req = requests.post('http://api/user', data= None, json=None)

if __name__ == '__main__':