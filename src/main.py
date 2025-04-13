import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.config import get_api_key, get_api_url
from src.chatbot.core import ChatBot
from src.project_management import ProjectManager

def main():
    # Initialisiere Chatbot
    bot = ChatBot()
    
    # Initialisiere Projektmanagement
    project_manager = ProjectManager(bot)
    project_manager.initialize_project()
    
    # Aktuelle Aufgabe anzeigen
    current_task = project_manager.get_current_task()
    print("Aktuelle Aufgabe:")
    print(current_task)
    
    # Optional: Interaktive Chatbot-Schleife
    while True:
        user_input = input("Du: ")
        if user_input.lower() in ['exit', 'quit', 'bye', '/bye', '/exit']:
            break
        
        response = bot.generate_response(user_input)
        print("Bot:", response)

if __name__ == "__main__":
    main()
