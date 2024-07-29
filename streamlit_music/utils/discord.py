# utils/discord.py
import requests

WEBHOOK_URL = 'YOUR_DISCORD_WEBHOOK_URL'

def post_to_discord(message):
    data = {
        "content": message
    }
    response = requests.post(WEBHOOK_URL, json=data)
    if response.status_code != 204:
        raise Exception(f"Error posting to Discord: {response.status_code}, {response.text}")
