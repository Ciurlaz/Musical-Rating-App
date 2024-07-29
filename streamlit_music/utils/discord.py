# utils/discord.py
import requests

WEBHOOK_URL = 'https://discord.com/api/webhooks/1267564483124133931/NXJYjiFPSjWprQTyTtnYOliJQcQKTxmw5GFwOpYfyELstPFsOvpJ2FrD9bIid-kdRjR0'

def post_to_discord(message):
    data = {
        "content": message
    }
    response = requests.post(WEBHOOK_URL, json=data)
    if response.status_code != 204:
        raise Exception(f"Error posting to Discord: {response.status_code}, {response.text}")
