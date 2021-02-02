import datetime

#----------------------------------------------------------------------------#
# Meraki Webhook handler function
#----------------------------------------------------------------------------#

def handler(webhook):

    # Dashboard Webhook Test
    if not bool(webhook["alertData"]):
        message = f'**Dashboard Webhook Test** 🎯\
                    \n- **Organization:** {webhook["organizationName"]}\
                    \n- **Network:** {webhook["networkName"]}'
        return message

    # Get Event Timestamp
    try:
        ts = datetime.datetime.utcfromtimestamp(webhook["alertData"]["triggerData"][0]["trigger"]["ts"])
    except:
        ts = datetime.datetime.now()

    # Sensor Alert Webhook Test
    if webhook['alertTypeId'] == 'sensor_alert_test':
        message = f'**Sensor Alert Test** ⚠️\
                    \n- **Network:** {webhook["networkName"]}\
                    \n- **Time:** {time_format(ts)}'
        return message

    elif webhook['alertTypeId'] == 'sensor_alert':
        # Door Sensor Open
        if webhook['deviceModel'] == 'MT20' and webhook["alertData"]["triggerData"][0]["trigger"]["sensorValue"] == 1.0:
            message = f'**Door Opened** 🚪🏃\
                        \n- **Network:** {webhook["networkName"]}\
                        \n- **Sensor:** {webhook["deviceName"]}\
                        \n- **Time:** {time_format(ts)}'
            return message

        # Temperature Sensor
        elif webhook['deviceModel'] == 'MT10':
            message = f'**Temperature Alert** 🌡️\
                        \n- **Network:** {webhook["networkName"]}\
                        \n- **Sensor:** {webhook["deviceName"]}\
                        \n- **Time:** {time_format(ts)}\
                        \n- **Temp:** {round(webhook["alertData"]["triggerData"][0]["trigger"]["sensorValue"],1)}'
            return message

        # Other Alert
        else:
            message = f'**Other Sensor Alert** ⁉️\
                        \n- **Data:** {webhook}'
            return message

    # No Meraki Events Founds
    else:
        message = f'**Unknown Webhook** ⁉️'
        for k, v in webhook.items():
            if k != 'sharedSecret':
                message += f'\n- **{k}:** {v}'
        return message

# Customize Time Format
def time_format(ts):
    # Converts Datetime to Time only
    return datetime.datetime.time(ts)