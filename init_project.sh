#!/bin/bash

# Projektverzeichnis
PROJECT_DIR="/Users/huibertgill/code/openhubertus"

# Erstelle Hauptverzeichnis
mkdir -p $PROJECT_DIR

# Wechsle in Projektverzeichnis
cd $PROJECT_DIR

# Erstelle Unterverzeichnisse
mkdir -p src/chatbot/skills
mkdir -p tests

# Erstelle .env Datei
cat << EOF > .env
API_KEY=sk-YOUR_API_KEY_HERE
URL=https://litellm.arokeks.de
EOF

# Erstelle requirements.txt
cat << EOF > requirements.txt
python-dotenv
openai
requests
pytest
EOF

# Erstelle README.md
cat << EOF > README.md
# OpenHubertus Chatbot

## Setup
1. Create virtual environment
\`\`\`
python3 -m venv venv
source venv/bin/activate
\`\`\`

2. Install dependencies
\`\`\`
pip install -r requirements.txt
\`\`\`
EOF

# Erstelle __init__.py Dateien
touch src/__init__.py
touch src/chatbot/__init__.py
touch src/chatbot/skills/__init__.py
touch tests/__init__.py

# Erstelle Basis-Skripte
cat << EOF > src/config.py
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
API_URL = os.getenv('URL')
EOF

cat << EOF > src/main.py
from config import API_KEY, API_URL
from chatbot.core import ChatBot

def main():
    bot = ChatBot(api_key=API_KEY, api_url=API_URL)
    print("OpenHubertus Chatbot gestartet.")
    
    while True:
        user_input = input("Du: ")
        if user_input.lower() in ['exit', 'quit', 'bye']:
            break
        
        response = bot.generate_response(user_input)
        print("Bot:", response)

if __name__ == "__main__":
    main()
EOF

cat << EOF > src/chatbot/core.py
import requests

class ChatBot:
    def __init__(self, api_key, api_url):
        self.api_key = api_key
        self.api_url = api_url
    
    def generate_response(self, user_input):
        try:
            response = requests.post(
                self.api_url,
                headers={
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json"
                },
                json={
                    "messages": [{"role": "user", "content": user_input}]
                }
            )
            return response.json()['choices'][0]['message']['content']
        except Exception as e:
            return f"Fehler: {str(e)}"
EOF

# Erstelle ein einfaches Test-Skript
cat << EOF > tests/test_core.py
import pytest
from src.chatbot.core import ChatBot
from src.config import API_KEY, API_URL

def test_chatbot_initialization():
    bot = ChatBot(api_key=API_KEY, api_url=API_URL)
    assert bot.api_key == API_KEY
    assert bot.api_url == API_URL

def test_generate_response():
    bot = ChatBot(api_key=API_KEY, api_url=API_URL)
    response = bot.generate_response("Hallo, wie geht es dir?")
    assert isinstance(response, str)
    assert len(response) > 0
EOF

# Setze Berechtigungen
chmod +x $0

echo "Projektstruktur für OpenHubertus Chatbot wurde erstellt!"
