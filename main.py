from chatbot import *
from utilities import *
import hmac, hashlib
import os
import meraki_events, webex_events

# Check environment variables set
MANDATORY_ENV_VARS = ["BOT_EMAIL", "BOT_TOKEN", "MERAKI_SECRET", "WEBEX_ROOM", "WEBEX_SECRET"]

for var in MANDATORY_ENV_VARS:
    if var not in os.environ:
        raise EnvironmentError(f"Failed because {var} is not set.")

# Get environment variables
BOT_EMAIL = os.getenv('BOT_EMAIL')
BOT_TOKEN = os.getenv('BOT_TOKEN')
MERAKI_SECRET = os.getenv('MERAKI_SECRET')
WEBEX_ROOM = os.getenv('WEBEX_ROOM')
WEBEX_SECRET = str.encode(os.getenv('WEBEX_SECRET'))

# Main handler function
def handler(request):
    """
    When messages come in from the webhook, they are processed here.
    """

    headers = {
        'authorization': f'Bearer {BOT_TOKEN}'
    }

    # Webhook event/metadata received 
    webhook_event = request.get_json()

    # Validate Request If From Webex Teams
    raw = request.data
    hashed = hmac.new(WEBEX_SECRET, raw, hashlib.sha1)
    validatedSignature = hashed.hexdigest()

    # Webex Teams Webhook
    if validatedSignature == request.headers.get('X-Spark-Signature'):
        data = webhook_event['data']
        payload = {'roomId': data['roomId']}
        try:
            message = webex_events.handler(headers, webhook_event, BOT_EMAIL)
            post_message(payload, headers, message)
            return 'success'
        except ValueError as e:
            print(e)
            return 'failed'
        
    # Meraki Webhook
    elif webhook_event['sharedSecret'] == MERAKI_SECRET:
        payload = {'roomId': WEBEX_ROOM}
        message = meraki_events.handler(webhook_event)
        post_message(payload, headers, message)
        return 'success'
        
    # Does Not Match Any Service or Could Not Auth
    else:
        message_print("Unknown Webhook Service",webhook_event)
        return 'failed'


