# src/main.py
from src.config import get_api_key, get_api_url
from src.chatbot.core import ChatBot

def main():
    # Initialisiere den Chatbot mit den Konfigurationswerten
    bot = ChatBot()
    print("OpenHubertus Chatbot gestartet.")
    
    while True:
        user_input = input("Du: ")
        if user_input.lower() in ['exit', 'quit', 'bye']:
            break
        
        response = bot.generate_response(user_input)
        print("Bot:", response)

if __name__ == "__main__":
    main()
