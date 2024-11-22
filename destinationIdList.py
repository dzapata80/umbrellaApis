import requests
from adminToken import access_token
import requests
from adminToken import access_token
import json

url = "https://api.umbrella.com/policies/v2/destinationlists"

payload = {}
headers = {'Authorization': f'Bearer {access_token}'}

# Make a GET request to retrieve the destination lists
response = requests.request("GET", url, headers=headers, data=payload)

# Create a list to store the extracted data
extracted_data = []

# Iterate over each item in the data list
for item in response.json()['data']:
    listId = item['id']
    accessAction = item['access']
    name = item['name']

    # Add the current item's data to the list
    extracted_data.append({
        'listId': listId,
        'accessAction': accessAction,
        'name': name
    })

# Convert the list of extracted data into formatted JSON
json_formatted_str = json.dumps(extracted_data, indent=2)
