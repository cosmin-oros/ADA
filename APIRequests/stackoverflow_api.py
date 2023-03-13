import requests
import json

response = requests.get('https://api.stackexchange.com/2.3/badges?order=desc&sort=rank&site=stackoverflow')

for data in response.json()['items']:
    print("Name: ", data['name'])
    print("Rank: ", data['rank'])
    print()