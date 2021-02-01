from utilities import *
from chatbot import *

# Meraki Webhook handler function
def handler(headers, webhook, BOT_EMAIL):
    # Check if Webex Webhook
    if 'resource' in webhook:
        message_print('Webhook Received', webhook)
        data = webhook['data']

        help_message = f'Hi **Human**! I can do many functions, just **@mention** me with a keyword. Keywords:\
                            \n- **help:** show all my functions\
                            \n- **share:** share a message to other spaces'

        # Ignore bot's own actions
        if webhook['resource'] == 'messages' and data['personEmail'] == BOT_EMAIL:
            raise ValueError('Bots Own Message')

        # Added To New Space
        if webhook['resource'] == 'memberships' and data['personEmail'] == BOT_EMAIL:
            return help_message

        # Get Message Text From Webhook Alert If Authorised
        if webhook['resource'] == 'messages' and '@cisco.com' in data['personEmail']:
            message = get_message(webhook, headers)
            message_print('Message Text Received', message)

            # Respond To Messages
            # Greetings
            if message_contains(message, ['help', 'hi', 'greetings', 'hello']):
                return help_message

            # Return successful
            else: 
                message_print('No Matching Message From Authorised User')   
                return help_message

    # No events matched or user not authorised 
    else:
        message_print('Event Not Configured')
        raise ValueError('Event Not Configured')