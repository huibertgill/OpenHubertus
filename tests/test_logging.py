import os
from src.config.logging_config import setup_chat_logging, log_chat_interaction

def test_logging_setup():
    logger = setup_chat_logging()
    assert logger is not None
    
    log_file = 'logs/chats.log'
    assert os.path.exists(log_file)

def test_log_interaction():
    logger = setup_chat_logging()
    log_chat_interaction(
        logger, 
        user='User', 
        model='test-model', 
        input_text='Hallo', 
        output_text='Welt'
    )
    
    # Optional: Log-Datei überprüfen
    with open('logs/chats.log', 'r') as f:
        content = f.read()
        assert 'User' in content
        assert 'test-model' in content
