Hier ist ein erweiterter Eingang für die README:

```markdown
# OpenHubertus Chatbot

## Projektbeschreibung

OpenHubertus ist ein flexibles, modular aufgebautes Chatbot-Projekt, das es Entwicklern und Enthusiasten ermöglicht, einen KI-gestützten Assistenten individuell zu konfigurieren und zu erweitern.

### Vision

Das Ziel des Projekts ist es, einen anpassbaren Chatbot zu entwickeln, der:
- Verschiedene KI-Modelle unterstützt
- Einfach erweiterbar durch Skills ist
- Datenschutz und Benutzerautonomie in den Mittelpunkt stellt
- Als Lernplattform für KI-Interaktionen dient

### Kernfunktionen

- 🤖 Unterstützung verschiedener KI-Modelle
- 🔌 Modulares Skill-System
- 🔒 Lokale Konfiguration und Datenkontrolle
- 🧠 Einfache Erweiterbarkeit

### Technologie-Stack
- Python 3.10+
- OpenAI-kompatible APIs
- Modulare Architektur

Hier ist ein erweiterter Abschnitt für die README, der den Einrichtungsprozess detailliert beschreibt:

```markdown
## Einrichtung und erste Schritte

### 1. Virtuelle Umgebung vorbereiten
```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Abhängigkeiten installieren
```bash
pip install -r requirements.txt
```

### 3. Konfigurationsdatei anlegen
Erstellen Sie eine `.env` Datei mit Ihrem API-Schlüssel:
```
API_KEY=sk-IhrAPISchlüssel
URL=https://litellm.arokeks.de
```

### 4. Verfügbare Modelle auflisten
Nach dem Anlegen der `.env` Datei listen Sie die verfügbaren Modelle auf:
```bash
python3 src/list_models.py
```

Beispiel-Ausgabe:
```
Verfügbare Modelle:
1. gpt-4o-mini
2. groq/mixtral-8x7b-32768
3. claude-3-opus-20240229

Wählen Sie eine Modell-Nummer (oder 'q' zum Beenden): 1
Modell gpt-4o-mini wurde gespeichert.
```

### 5. Chatbot starten
```bash
python3 src/main.py
```

## Hinweise
- Stellen Sie sicher, dass Ihre Umgebungsvariablen korrekt sind
- Der erste Aufruf von `list_models.py` ist wichtig für die Modellkonfiguration
- Bei Problemen überprüfen Sie die `.env` Datei und API-Verbindung
```


