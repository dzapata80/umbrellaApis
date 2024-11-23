import requests

url = "https://s-platform.api.opendns.com/1.0/events?customerKey=6818a0ce-eaa5-4363-9226-7ea105d142d2"

payload = '''[
    {
        "alertTime": "2024-02-08T09:30:26Z",
        "deviceId": "device ID",
        "deviceVersion": "version of device",
        "dstDomain": "www.syssa.com",
        "dstUrl": "https://www.syssa.com",
        "protocolVersion": "1.0a",
        "eventTime": "2024-02-08T09:29:26Z",
        "providerName" : "Security Platform",
        "disableDstSafeguards" : false
    }
]'''

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

response = requests.request('POST', url, headers=headers, data = payload)

print(response.text.encode('utf8'))
print("Status code:" + str(response.status_code))