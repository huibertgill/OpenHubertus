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

def get_system_prompt(file_path='src/config/prompt.txt'):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read().strip()
    except FileNotFoundError:
        print(f"Systemprompt-Datei nicht gefunden: {file_path}")
        return "Du bist ein hilfreicher KI-Assistent."
    except Exception as e:
        print(f"Fehler beim Lesen des Systemprompts: {e}")
        return "Du bist ein hilfreicher KI-Assistent."
