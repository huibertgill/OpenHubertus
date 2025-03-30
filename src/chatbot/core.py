# In core.py
import os
from dotenv import load_dotenv

class ChatBot:
    def __init__(self, api_key, api_url):
        load_dotenv()
        self.api_key = api_key
        self.api_url = api_url
        self.model = os.getenv('MODEL', 'gpt-4o-mini')  # Fallback-Modell
    
    def generate_response(self, user_input):
        try:
            response = requests.post(
                f"{self.api_url}/chat/completions",
                headers={
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": self.model,  # Dynamisches Modell aus .env
                    "messages": [
                        {"role": "system", "content": "You are a helpful assistant named OpenHubertus."},
                        {"role": "user", "content": user_input}
                    ]
                }
            )
            
            print("Raw Response:", response.text)
            
            if response.status_code == 200:
                response_data = response.json()
                return response_data['choices'][0]['message']['content']
            else:
                return f"API Error: {response.status_code} - {response.text}"
        
        except Exception as e:
            return f"Fehler: {str(e)}"
