import requests
from config import get_api_key, get_api_url, get_model

def test_api_connection():
    api_key = get_api_key()
    api_url = get_api_url()
    api_model = get_model()
    
    print(f"Testing API Connection to: {api_url}/chat/completions")
    print(f"Using Model: {api_model}")
    
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
        
        print("Status Code:", response.status_code)
        print("Response Content:", response.text)
    except Exception as e:
        print(f"Connection Error: {e}")

if __name__ == "__main__":
    test_api_connection()
