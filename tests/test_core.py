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
