import json
import requests

# Get the event (most recent message) that triggered the webhook
def get_message(event, headers):
    url = f'https://api.ciscospark.com/v1/messages/{event["data"]["id"]}'
    response = requests.get(url, headers=headers)
    return response.json()['text']

# Send a message in Webex Teams
def post_message(payload, headers, message):
    payload['markdown'] = message
    response = requests.post('https://api.ciscospark.com/v1/messages/',headers=headers,json=payload)

# Get a person in Webex Teams
def get_person(event, headers):
    url = f'https://api.ciscospark.com/v1/people/{event["data"]["personId"]}'
    response = requests.get(url, headers=headers)
    return response.json()

# Delete a message in Webex Teams
def delete_message(event, headers):
    url = f'https://api.ciscospark.com/v1/messages/{event["data"]["messageId"]}'
    response = requests.delete(url, headers=headers)

# Check whether message contains one of multiple possible options
def message_contains(text, options):
    message = text.lower()
    print(message)
    for option in options:
        if option in message:
            return True
    return False