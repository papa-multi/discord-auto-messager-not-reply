import requests
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Authentication token and channel ID
TOKEN = input("Enter your Discord Auth Token: ")
CHANNEL_ID = input("Enter your Discord Channel ID: ")
DELAY_MINUTES = float(input("Enter delay between messages (in minutes): "))
DELAY = DELAY_MINUTES * 60  # Convert minutes to seconds

# Read sentences from a text file
with open('sentences.txt', 'r') as file:
    sentences = file.read().splitlines()

# URL to send messages to the Discord channel
url = f'https://discord.com/api/v9/channels/{CHANNEL_ID}/messages'

# Request headers
headers = {
    'Authorization': TOKEN,
    'Content-Type': 'application/json'
}

# Send messages with a time delay
for sentence in sentences:
    data = {
        'content': sentence
    }
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        logging.info(f'Message sent: {sentence}')
    else:
        logging.error(f'Error sending message: {response.status_code} - {response.text}')
    
    time.sleep(DELAY)
