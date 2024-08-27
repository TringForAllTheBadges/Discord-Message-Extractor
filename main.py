import requests
import json

BASE_URL = "https://discord.com/api/v9"
TOKEN = "TOKEN HERE"

headers = {
    "Authorization": TOKEN,
    "Content-Type": "application/json"
}

def get_messages(channel_id, limit=100):
    url = f"{BASE_URL}/channels/{channel_id}/messages?limit={limit}"
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        messages = response.json()
        return messages
    else:
        return None

def save_messages(messages, filename):
    with open(filename, 'w') as f:
        json.dump(messages, f, indent=4)

channel_id = "TARGET CHANNEL ID"
messages = get_messages(channel_id)

if messages:
    save_messages(messages, "messages.json")
    print(f"Got {len(messages)} messages")
else:
    print("Failed to get messages")
