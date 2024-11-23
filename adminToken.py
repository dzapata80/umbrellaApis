import requests
import base64

# URL to get the token
token_url = "https://api.umbrella.com/auth/v2/token"

# Your credentials for basic authentication
apiKey = "Your API Key"
apiSecret = "Your API Secret"

# Encode the credentials in base64
credentials = f"{apiKey}:{apiSecret}"
encoded_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')

# Basic authentication header
headers = {
    'Authorization': f'Basic {encoded_credentials}',
    'Content-Type': 'application/x-www-form-urlencoded'  # Ensure you use the correct content type
}

# Request body (may vary depending on your API)
data = {
        'grant_type': 'client_credentials'
}

# Make the request to obtain the token
response = requests.post(token_url, headers=headers, data=data)

print('Status code:', response.status_code)

if response.status_code == 200:
    token_data = response.json()

    # Extract the token and its expiration time (usually 3600 seconds)
    access_token = token_data['access_token']
    expires_in = token_data['expires_in']

