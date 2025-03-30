# src/list_models.py
import requests
import os
from dotenv import load_dotenv

def get_available_models(api_key, api_url):
    try:
        response = requests.get(
            f"{api_url}/models",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            }
        )
        
        if response.status_code == 200:
            # Annahme: Die API gibt eine Liste von Modellen zurück
            return response.json().get('models', [])
        else:
            print(f"Fehler beim Abrufen der Modelle: {response.status_code}")
            print(response.text)
            return None
    
    except Exception as e:
        print(f"Fehler: {str(e)}")
        return None

def select_and_save_model(models):
    if not models:
        return None
    
    print("Verfügbare Modelle:")
    for i, model in enumerate(models, 1):
        print(f"{i}. {model}")
    
    while True:
        try:
            choice = int(input("Wählen Sie eine Modell-Nummer: "))
            if 1 <= choice <= len(models):
                selected_model = models[choice-1]
                
                # Modell in .env speichern
                with open('.env', 'r') as f:
                    lines = f.readlines()
                
                with open('.env', 'w') as f:
                    model_line_found = False
                    for line in lines:
                        if line.startswith('MODEL='):
                            f.write(f"MODEL={selected_model}\n")
                            model_line_found = True
                        else:
                            f.write(line)
                    
                    if not model_line_found:
                        f.write(f"\nMODEL={selected_model}\n")
                
                print(f"Modell {selected_model} wurde gespeichert.")
                return selected_model
            else:
                print("Ungültige Auswahl. Bitte erneut versuchen.")
        
        except ValueError:
            print("Bitte geben Sie eine gültige Zahl ein.")

def main():
    load_dotenv()
    api_key = os.getenv('API_KEY')
    api_url = os.getenv('URL')
    
    models = get_available_models(api_key, api_url)
    if models:
        select_and_save_model(models)

if __name__ == "__main__":
    main()

