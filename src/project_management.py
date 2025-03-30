# src/project_management.py
import os
import sys
import json
from src.chatbot.core import ChatBot

class ProjectManager:
    def __init__(self, chatbot, default_project=None):
        self.chatbot = chatbot
        self.project_dir = 'projekt'
        self.projekt_file = os.path.join(self.project_dir, 'projekt.txt')
        self.aufgabe_file = os.path.join(self.project_dir, 'aufgabe.txt')
        self.default_project = default_project
        
        # Verzeichnis erstellen, falls nicht existiert
        os.makedirs(self.project_dir, exist_ok=True)
    
    def initialize_project(self):
        # Prüfe, ob Projektdatei existiert
        if not os.path.exists(self.projekt_file):
            # Projekt-Idee holen
            if self.default_project:
                projekt_idee = self.default_project
            else:
                # Nur in interaktiver Umgebung
                if sys.stdin.isatty():
                    print("Es wurde noch kein Projekt definiert.")
                    projekt_idee = input("Beschreiben Sie Ihr Projektvorhaben: ")
                else:
                    # Fallback für Tests
                    projekt_idee = "Ein Softwareprojekt zur Prozessoptimierung"
            
            # Generiere Projekt-Prompt
            projekt_prompt = (
                f"Entwickle einen strukturierten Projektplan für folgende Projektidee: '{projekt_idee}'. "
                "Erstelle einen umfassenden Projektplan mit folgender Struktur:\n\n"
                "# Projekttitel\n"
                "# Projektziel\n"
                "# Problemstellung\n"
                "# Lösungsansatz\n"
                "# Projektphasen\n"
                "# Meilensteine\n"
                "# Benötigte Ressourcen\n"
                "Antworte im vorgegebenen Markdown-Format und sei detailliert."
            )
            
            # Hole Projektplan vom Chatbot
            projekt_beschreibung = self.chatbot.generate_response(projekt_prompt)
            
            # Speichere Projekt-Beschreibung
            with open(self.projekt_file, 'w', encoding='utf-8') as f:
                f.write(projekt_beschreibung)
            
            print("Projektplan wurde generiert und gespeichert.")
        
        # Generiere erste Aufgabe
        self.generate_next_task()
    
    def generate_next_task(self):
        # Lese Projektbeschreibung
        with open(self.projekt_file, 'r', encoding='utf-8') as f:
            projekt_beschreibung = f.read()
        
        # Generiere Aufgabe basierend auf Projektbeschreibung
        task_prompt = (
            f"Basierend auf folgendem Projektplan:\n{projekt_beschreibung}\n\n"
            "Definiere die nächste konkrete Entwicklungsaufgabe. "
            "Die Aufgabe sollte:\n"
            "- Spezifisch und klar umrissen sein\n"
            "- Zum Projektfortschritt beitragen\n"
            "- Messbare Ergebnisse liefern\n\n"
            "Verwende das vorgegebene Markdown-Format."
        )
        
        # Hole Aufgabe vom Chatbot
        naechste_aufgabe = self.chatbot.generate_response(task_prompt)
        
        # Speichere Aufgabe
        with open(self.aufgabe_file, 'w', encoding='utf-8') as f:
            f.write(naechste_aufgabe)
        
        print("Nächste Aufgabe wurde generiert und gespeichert.")
    
    def get_current_task(self):
        # Lese aktuelle Aufgabe
        if os.path.exists(self.aufgabe_file):
            with open(self.aufgabe_file, 'r', encoding='utf-8') as f:
                return f.read()
        return "Keine Aufgabe gefunden."
