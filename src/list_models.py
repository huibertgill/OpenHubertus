# src/list_models.py
import sys
import os
import requests

# Pfad-Anpassung für Imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.config import get_api_key, get_api_url

def get_available_models():
    api_key = get_api_key()
    api_url = get_api_url()
    
    print(f"Hole Modelle von: {api_url}/models")
    
    try:
        response = requests.get(
            f"{api_url}/models",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            }
        )
        
        print(f"Status Code: {response.status_code}")
        print(f"Response Headers: {response.headers}")
        print(f"Response Content: {response.text}")
        
        if response.status_code == 200:
            # Parsen der Modellantwort
            models_data = response.json()
            
            # Extrahiere Modellnamen 
            # Die genaue Struktur hängt von der API-Antwort ab
            if isinstance(models_data, dict) and 'data' in models_data:
                models = [model.get('id', model) for model in models_data['data']]
            elif isinstance(models_data, list):
                models = [model.get('id', model) for model in models_data]
            else:
                models = [str(models_data)]
            
            return models
        else:
            print(f"Fehler beim Abrufen der Modelle: {response.status_code}")
            print(response.text)
            return []
    
    except Exception as e:
        print(f"Verbindungsfehler: {e}")
        return []

def select_and_save_model(models):
    if not models:
        print("Keine Modelle gefunden.")
        return None
    
    print("Verfügbare Modelle:")
    for i, model in enumerate(models, 1):
        print(f"{i}. {model}")
    
    while True:
        try:
            choice = input("Wählen Sie eine Modell-Nummer (oder 'q' zum Beenden): ")
            
            if choice.lower() == 'q':
                return None
            
            choice = int(choice)
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
            print("Bitte geben Sie eine gültige Zahl ein oder 'q' zum Beenden.")

def main():
    models = get_available_models()
    if models:
        select_and_save_model(models)

if __name__ == "__main__":
    main()
