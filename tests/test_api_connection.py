import pytest
from src.chatbot.core import ChatBot

def test_api_connection():
    bot = ChatBot()
    try:
        response = bot.generate_response("test")
        assert response is not None
    except Exception as e:
        pytest.fail(f"API connection failed: {e}")