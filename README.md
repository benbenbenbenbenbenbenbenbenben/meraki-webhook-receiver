# Meraki Webook Receiver
Receive Webhooks from Meraki Dashboard and post to Webex Room.

# Table of Contents
- [Requirements](#requirements)
- [Setup](#setup)


# Requirements

* Webex Bot and Token
* Python
* Ngrok (Or similar if running locally)
* Meraki Dashboard

# Setup

## Webex Bot 
Skip if you already have a Bot and Token.
1. Login to Webex Developer site https://developer.webex.com/my-apps
2. Create a Bot (Create a new App > Create a new Bot)
    1. Give your bot a name, username and description
    2. Copy the generated Access Token (store somewhere safe for later)
3. Add your Bot to a Webex Teams Space
    1. In Webex Teams click the + button and create a space
    2. Give your space a name and add your Bot (i.e. yourbot@webex.bot)
    3. Click Create
    4. Say “Hello” if you want :)


## Ngrok
Exposes your development environment to the Internet using a public URL so we can receive Webhooks.
1. Signup for Free Ngrok Account https://ngrok.com/ and download Ngrok
2. Follow instructions in Ngrok to link authtoken 
3. Start Ngrok
```bash
$ ./ngrok http 5000
```
4. Copy the Ngrok Forwarding URL for later use (ie. https://zzzzzzzz.ngrok.io)


## Setup Webhook Server In Meraki Dashbboard
Configure the webhook server in your Meraki Dashboard. Network-wide > Alerts

![Image of webhook](https://i.ibb.co/wsLVz4Z/meraki-webhook-setup.png)  

[Meraki Webooks Documentation](https://developer.cisco.com/meraki/webhooks/)

## Setup Receiver
1. Clone Github Repository
```bash
git clone https://github.com/benbenbenbenbenbenbenbenbenben/meraki-webhook-receiver.git
cd meraki-webhook-receiver
```
2. Now "activate" the python virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```
3. Install project requirements
```bash
pip install Flask requests
```
4. Export Env Variables
```bash
export BOT_TOKEN=
export MERAKI_SECRET=
```
5. Run The App.
Initially this will return a list of webex rooms the bot has been added to. Copy the room Id for your room and export.
```bash
python app.py
```
```bash
export WEBEX_ROOM=
```
```bash
python app.py
```

## Test
Send a test webhook from Network-wide > Alerts Page or using the new Environmental > Alert Profiles test buttons. 


