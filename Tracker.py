import json # Modul zum Speichern der Daten in einer Datei

# Versuche, beim Programmstart vorhandene Bewerbungen aus der Datei zu laden.
# Falls die Datei noch nicht existiert (erster Start), wird eine leere Liste erstellt.

try:
    with open("bewerbungen.json", "r") as datei:
        bewerbungen = json.load(datei)
except FileNotFoundError:
    bewerbungen = [] # Liste, in der alle Bewerbungen während der Programmlaufzeit gespeichert werden
# Diese Funktion speichert die aktuelle Liste der Bewerbungen in einer Datei,
# damit die Daten beim nächsten Programmstart nicht verloren gehen

def speichern():
    with open("bewerbungen.json", "w") as datei:
        json.dump(bewerbungen, datei)

# Hauptschleife des Programms - läuft, bis der Nutzer "Beenden" wählt
while True:
# Menü anzeigen
    print("1 - Bewerbung hinzufügen")
    print("2 - Alle Bewerbungen anzeigen")
    print("3 - Status einer Bewerbung ändern")
    print("4 - Bewerbung löschen")
    print("5 - Beenden")

    auswahl = input("Was möchtest du tun? ")

# Punkt 1: neue Bewerbung hinzufügen
    if auswahl == "1":
        firma = input("Name der Firma: ")
        datum = input("Datum der Bewerbung (TT.MM.JJJJ): ")
        stelle = input("Name der Stelle: ")

        new_bewerbung = {
            "firma": firma,
            "datum": datum,
            "stelle": stelle,
            "status": "gesendet"
        }

        bewerbungen.append(new_bewerbung)
        speichern() # Änderung sofort in der Datei sichern

# Punkt 2: alle Bewerbungen anzeigen
    elif auswahl == "2":
        for b in bewerbungen:   
            print("Firma:", b['firma'])
            print("Datum:", b['datum'])
            print("Stelle:", b['stelle'])
            print("Status:", b['status'])
            print("--------------------")

# Punkt 3: Status einer bestimmten Bewerbung ändern
    elif auswahl == "3":
        for i, b in enumerate(bewerbungen):
            print(i+1, "-", b["firma"])

        nummer = input("Welche Nummer möchtest du ändern?  ")
        neuer_status = input("Neuer Status: ")
        bewerbungen[int(nummer)-1]["status"] = neuer_status
        speichern() # Änderung sofort in der Datei sichern

# Punkt 4: Bewerbung anhand der Nummer löschen
    elif auswahl == "4":
        for i, b in enumerate(bewerbungen):
            print(i+1, "-", b["firma"])

        nummer = input("Welche Nummer möchtest du löschen?  ")

        bewerbungen.pop(int(nummer)-1)
        speichern() # Änderung sofort in der Datei sichern

# Punkt 5: Programm beenden
    elif auswahl == "5":
            print("Bis bald!")
            break

 
    