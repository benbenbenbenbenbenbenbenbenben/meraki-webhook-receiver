# Meraki Webook Receiver
Receive Webhooks from Meraki and Webex Teams. Post to Webex Room.

## Setup
1. Clone Github Repository
```bash
git clone https://github.com/
cd folder
```
2. Now "activate" the python virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```
3. Install project requirements
```bash
pip install Flask
```
4. Export Env Variables
```bash
export BOT_TOKEN=
export BOT_EMAIL= 
export WEBEX_SECRET=
export MERAKI_SECRET=
export WEBEX_ROOM=
```
5. Run App
```bash
python app.py
```

## Further Reading
- [Webex Teams Bot Guide](https://github.com/benbenbenbenbenbenbenbenbenben/webex-teams-bot-guide)
