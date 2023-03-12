import requests
import json
import pprint

url = "https://api.tvmaze.com/singlesearch/shows"
params = {"q": "the walking dead"}

response = requests.get(url, params)

if response.status_code == 200:
    # data - dictionary
    data = json.loads(response.text)
    pprint.pprint(data)

    name = data['name']
    premiered = data['premiered']
    summary = data['summary']

    print()
    print(f"{name} premiered on {premiered}")
    print(summary)
else:
    print(f"Error: {response.status_code}")