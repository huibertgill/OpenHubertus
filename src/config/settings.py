import os
from dotenv import load_dotenv

# Lädt die .env Datei
load_dotenv()

def get_api_key():
    return os.getenv('API_KEY')

def get_api_url():
    return os.getenv('URL')

def get_model():
    # Fallback-Wert, falls kein Modell gesetzt
    return os.getenv('MODEL', 'gpt-4o-mini')
