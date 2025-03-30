import logging
import os
from datetime import datetime

def setup_chat_logging():
    # Logging-Verzeichnis erstellen, falls nicht vorhanden
    log_dir = 'logs'
    os.makedirs(log_dir, exist_ok=True)

    # Log-Datei mit aktuellem Datum
    log_file = os.path.join(log_dir, 'chats.log')

    # Logger konfigurieren
    logger = logging.getLogger('chat_logger')
    logger.setLevel(logging.INFO)

    # File Handler
    file_handler = logging.FileHandler(log_file, encoding='utf-8')
    file_handler.setLevel(logging.INFO)

    # Formatter
    formatter = logging.Formatter('%(message)s')
    file_handler.setFormatter(formatter)

    # Handler hinzufügen
    logger.addHandler(file_handler)

    return logger

def log_chat_interaction(logger, user, model, input_text, output_text):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    log_entry = f"""
{'='*50}
Zeitstempel: {timestamp}
User Eingabe: {input_text}
Modell: {model}
Ausgabe: {output_text}
{'='*50}
"""
    logger.info(log_entry)
