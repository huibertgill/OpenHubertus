import pytest
from src.chatbot.core import ChatBot
from unittest.mock import patch

@patch('src.chatbot.core.requests.post')
def test_error_handling(mock_post):
    mock_post.side_effect = Exception("API Error")
    bot = ChatBot()
    response = bot.generate_response("Hallo")
    assert "Fehler" in response