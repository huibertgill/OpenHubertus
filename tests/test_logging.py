import logging
import os
from src.config.logging_config import setup_chat_logging, log_chat_interaction

def test_logging():
    logger = setup_chat_logging()
    log_file = "chat.log"
    log_chat_interaction(logger, "User", "gpt-4o-mini", "Hallo", "Hallo Welt")
    assert os.path.exists(log_file)
    with open(log_file, "r") as f:
        assert "Hallo" in f.read()
