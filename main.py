import bot
from utilities import *
import hmac, hashlib
import os
import meraki_events

#----------------------------------------------------------------------------#
# Check environment variables
#----------------------------------------------------------------------------#

MANDATORY_ENV_VARS = ["BOT_TOKEN", "MERAKI_SECRET"]

for var in MANDATORY_ENV_VARS:
    if var not in os.environ:
        raise EnvironmentError(f'Failed because {var} is not set.')

# Get environment variables
BOT_TOKEN = os.getenv('BOT_TOKEN')
MERAKI_SECRET = os.getenv('MERAKI_SECRET')

# Check for webex room set otherwise return list of rooms
if "WEBEX_ROOM" not in os.environ:
    headers = {
        'authorization': f'Bearer {BOT_TOKEN}'
    }
    rooms = bot.get_rooms(headers)
    alert("Webex Room ID Not Chosen")
    for room in rooms["items"]:
        print(f'Room: {room["title"]} - ID: {room["id"]}')
    alert("------------------------")
    print('\nFailed because WEBEX_ROOM is not set. export WEBEX_ROOM=roomid ')
    quit()
else:
    WEBEX_ROOM = os.getenv('WEBEX_ROOM')

#----------------------------------------------------------------------------#
# Main handler function
#----------------------------------------------------------------------------#

def handler(request):
    """
    When messages come in from the webhook, they are processed here.
    """
    headers = {
        'authorization': f'Bearer {BOT_TOKEN}'
    }
    # Webhook event/metadata received 
    webhook_event = request.get_json()
    message_print("Webhook Received",webhook_event)

    # Meraki Webhook
    if webhook_event['sharedSecret'] == MERAKI_SECRET:
        payload = {'roomId': WEBEX_ROOM}
        message = meraki_events.handler(webhook_event)
        bot.post_message(payload, headers, message)
        return 'success'
        
    # Does Not Match Any Service or Could Not Auth
    else:
        message_print("Unknown Webhook Service",webhook_event)
        return 'failed'


