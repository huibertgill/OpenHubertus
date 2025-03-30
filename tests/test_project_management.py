# tests/test_project_management.py
import os
import pytest
from src.chatbot.core import ChatBot
from src.project_management import ProjectManager

def test_project_initialization():
    bot = ChatBot()
    
    # Test mit vordefiniertem Projekt
    project_manager = ProjectManager(
        bot, 
        default_project="Ein Testprojekt zur Systemintegration"
    )
    
    # Lösche existierende Dateien für Test
    if os.path.exists(project_manager.projekt_file):
        os.remove(project_manager.projekt_file)
    if os.path.exists(project_manager.aufgabe_file):
        os.remove(project_manager.aufgabe_file)
    
    # Initialisiere Projekt
    project_manager.initialize_project()
    
    # Überprüfe Dateien
    assert os.path.exists(project_manager.projekt_file)
    assert os.path.exists(project_manager.aufgabe_file)
    
    # Lese Inhalte
    with open(project_manager.projekt_file, 'r') as f:
        projekt_beschreibung = f.read()
    
    with open(project_manager.aufgabe_file, 'r') as f:
        aufgabe = f.read()
    
    assert len(projekt_beschreibung) > 0
    assert len(aufgabe) > 0
