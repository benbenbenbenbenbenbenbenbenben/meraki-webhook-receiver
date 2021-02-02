import json
import requests

# Send a message in Webex Teams
def post_message(payload, headers, message):
    payload['markdown'] = message
    response = requests.post('https://api.ciscospark.com/v1/messages/',headers=headers,json=payload)

# Get a list of rooms the webex bot is in
def get_rooms(headers):
    url = 'https://api.ciscospark.com/v1/rooms'
    response = requests.get(url, headers=headers)
    return response.json()
