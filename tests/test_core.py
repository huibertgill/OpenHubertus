import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from src.chatbot.core import ChatBot
from src.config import get_api_key, get_api_url, get_model

def test_chatbot_initialization():
    bot = ChatBot()
    assert bot.api_key == get_api_key()
    assert bot.api_url == get_api_url()
    assert bot.model == get_model()

def test_generate_response():
    bot = ChatBot()
    response = bot.generate_response("Hallo, wie geht es dir?")
    assert isinstance(response, str)
    assert len(response) > 0
