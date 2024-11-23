import requests
import json

url = "https://s-platform.api.opendns.com/1.0/domains?customerKey=6818a0ce-eaa5-4363-9226-7ea105d142d2"

payload = None

headers = {"Accept": "application/json"}

response = requests.request('GET', url, headers=headers, data=payload)

# Iterate over each item in the data list
for item in response.json()['data']:
    domain = item['name']
    domainId = item['id']
    print(f"Domain: {domain}, ID: {domainId}")

#print(json.dumps(response.json(), indent=2))

