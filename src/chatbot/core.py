import requests

class ChatBot:
    def __init__(self, api_key, api_url):
        self.api_key = api_key
        self.api_url = api_url
    
    def generate_response(self, user_input):
        try:
            response = requests.post(
                self.api_url,
                headers={
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json"
                },
                json={
                    "messages": [{"role": "user", "content": user_input}]
                }
            )
            return response.json()['choices'][0]['message']['content']
        except Exception as e:
            return f"Fehler: {str(e)}"
