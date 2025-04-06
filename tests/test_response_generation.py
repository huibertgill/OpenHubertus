from src.chatbot.core import ChatBot

def test_response_generation():
    bot = ChatBot()
    response = bot.generate_response("Hallo")
    assert isinstance(response, str)
    assert len(response) > 0