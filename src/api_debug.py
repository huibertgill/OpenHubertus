# src/api_debug.py
import requests
import os
from dotenv import load_dotenv

load_dotenv()

def test_api_connection():
    api_key = os.getenv('API_KEY')
    api_url = os.getenv('URL')
    api_model = os.getenv('MODEL')
    print(f"Testing API Connection to: {api_url}/chat/completions")
    
    try:
        response = requests.post(
            f"{api_url}/chat/completions",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            },
            json={
                "model": api_model,
                "messages": [
                    {"role": "user", "content": "Hello, who are you?"}
                ]
            }
        )
        
        print("Request: :", requests)
        print("Status Code:", response.status_code)
        print("Response Headers:", response.headers)
        print("Response Content:", response.text)
        
    except Exception as e:
        print(f"Connection Error: {e}")

if __name__ == "__main__":
    test_api_connection()
