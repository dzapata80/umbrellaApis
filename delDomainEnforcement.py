import requests

url = "https://s-platform.api.opendns.com/1.0/domains/{id}?customerKey=6818a0ce-eaa5-4363-9226-7ea105d142d2"

payload = '''{}'''

headers = {"Accept": "application/json"}

response = requests.request('DELETE', url, headers=headers, data = payload)

print(response.text.encode('utf8'))

