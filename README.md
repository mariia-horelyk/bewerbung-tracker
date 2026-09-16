# Bewerbung Tracker

Ein einfaches Kommandozeilen-Programm zur Verwaltung von Bewerbungen. 
Dieses Projekt ist mein erstes eigenständiges Lernprojekt während meiner Umschulung 
zur Fachinformatikerin Anwendungsentwicklung.

## Funktionen

- Neue Bewerbung hinzufügen (Firma, Datum, Stelle)
- Alle gespeicherten Bewerbungen anzeigen
- Status einer Bewerbung ändern (z. B. "gesendet" → "Vorstellungsgespräch")
- Bewerbung löschen
- Daten werden automatisch in einer JSON-Datei gespeichert und bleiben 
  auch nach dem Beenden des Programms erhalten

## Verwendete Technologien

- Python 3
- Eingebautes `json`-Modul zur Datenspeicherung

## Installation und Start

**Einfachste Methode (Windows):**
1. Repository herunterladen: Auf GitHub oben auf den grünen Button "Code" klicken, dann "Download ZIP" auswählen
2. ZIP-Datei entpacken (Rechtsklick → "Alle extrahieren")
3. Im entpackten Ordner doppelklick auf die Datei `start.bat` - das Programm startet automatischDoppelklick auf die Datei `start.bat` im Projektordner - das Programm startet automatisch.

**Alternative (über die Kommandozeile):**
1. Python 3 muss installiert sein
2. Repository herunterladen oder klonen
3. Im Terminal in den Projektordner wechseln
4. Programm starten mit:

python tracker.py


## Beispiel

1 - Bewerbung hinzufügen
2 - Alle Bewerbungen anzeigen
3 - Status einer Bewerbung ändern
4 - Bewerbung löschen
5 - Beenden
Was möchtest du tun?


## Mögliche Erweiterungen

- Grafische Benutzeroberfläche (GUI)
- Suche und Filter nach Status oder Firma
- Speicherung in einer Datenbank statt JSON-Datei