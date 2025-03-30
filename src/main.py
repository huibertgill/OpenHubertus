from config import API_KEY, API_URL
from chatbot.core import ChatBot

def main():
    bot = ChatBot(api_key=API_KEY, api_url=API_URL)
    print("OpenHubertus Chatbot gestartet.")
    
    while True:
        user_input = input("Du: ")
        if user_input.lower() in ['exit', 'quit', 'bye']:
            break
        
        response = bot.generate_response(user_input)
        print("Bot:", response)

if __name__ == "__main__":
    main()
