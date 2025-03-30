import requests
from src.config import get_api_key, get_api_url, get_model

class ChatBot:
    def __init__(self):
        self.api_key = get_api_key()
        self.api_url = get_api_url()
        self.model = get_model()
    
    def generate_response(self, user_input):
        try:
            response = requests.post(
                f"{self.api_url}/chat/completions",
                headers={
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": self.model,
                    "messages": [
                        {"role": "system", "content": "You are a helpful assistant named OpenHubertus."},
                        {"role": "user", "content": user_input}
                    ]
                }
            )
            
            if response.status_code == 200:
                response_data = response.json()
                return response_data['choices'][0]['message']['content']
            else:
                return f"API Error: {response.status_code} - {response.text}"
        
        except Exception as e:
            return f"Fehler: {str(e)}"
