import requests
from src.config import get_api_key, get_api_url, get_model, get_system_prompt
from src.config.logging_config import setup_chat_logging, log_chat_interaction


class ChatBot:
    def __init__(self):
        self.api_key = get_api_key()
        self.api_url = get_api_url()
        self.model = get_model()
        self.system_prompt = get_system_prompt()    
        self.logger = setup_chat_logging()

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
                        {"role": "system", "content": self.system_prompt},
                        {"role": "user", "content": user_input}
                    ]
                }
            )
            
            if response.status_code == 200:
                response_data = response.json()
                output_text = response_data['choices'][0]['message']['content']
                
                # Logging der Interaktion
                log_chat_interaction(
                    self.logger, 
                    user='User', 
                    model=self.model, 
                    input_text=user_input, 
                    output_text=output_text
                )
                return output_text
            else:
                return f"API Error: {response.status_code} - {response.text}"
        
        except Exception as e:
            return f"Fehler: {str(e)}"
