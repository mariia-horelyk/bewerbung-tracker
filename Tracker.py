import json # Modul zum Speichern der Daten in einer Datei
from datetime import datetime  # Modul für Datumsberechnungen

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
    print("5 - Statistik anzeigen ")
    print("6 - Erinnerungen")
    print("7 - LinkedIn-Kontakte")
    print("8 - LinkedIn-Kontakt ändern") 
    print("9 - Beenden")

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
            "status": "gesendet",
            "linkedin": "noch nicht gesucht"
        }

        bewerbungen.append(new_bewerbung)
        speichern() # Änderung sofort in der Datei sichern

# Punkt 2: alle Bewerbungen anzeigen
    elif auswahl == "2":
        print("Insgesamt:", len(bewerbungen), "Bewerbungen")  
        for i, b in enumerate(bewerbungen): 
            print("Bewerbung Nr. ", i+1)
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
        
# Punkt 5: Statistik anzeigen       
    elif auswahl == "5":
        gesamt = len(bewerbungen)
        absagen = 0 
        for b in bewerbungen:
            if b["status"] == "Absage":
                absagen = absagen + 1
        print("Insgesamt:", gesamt, "Bewerbungen")
        print("Absagen:", absagen)
        if gesamt > 0:
            quote = (absagen / gesamt) * 100
            print("Absagequote:", round(quote, 1), "%")
            
# Punkt 6: Erinnerungen
    elif auswahl == "6":
            heute = datetime.now()
            print("Erinnerung fällig:")
            for b in bewerbungen:
                if b["status"] == "gesendet":
                    try:
                        datum=datetime.strptime(b["datum"], "%d.%m.%Y")
                    except ValueError:
                        continue
                    tage = (heute - datum).days
                    if tage >= 14:
                        print("Firma:", b["firma"], "| gesendet am", b["datum"], "| vor", tage, "Tagen")
                        
# Punkt 7: LinkedIn-Kontakte pro Firma anzeigen
    elif auswahl == "7":
        for i, b in enumerate(bewerbungen):
            print(i+1, "-", b["firma"], "|", b.get("linkedin", "noch nicht gesucht"))                     
                        
# Punkt 8: LinkedIn-Kontakt einer Firma ändern
    elif auswahl == "8":
        for i, b in enumerate(bewerbungen):
            print(i+1, "-", b["firma"], "|", b.get("linkedin", "noch nicht gesucht"))

        nummer = input("Welche Nummer möchtest du ändern? ")
        print("1 - Kontakt gefunden")
        print("2 - Kein Kontakt gefunden")
        print("3 - noch nicht gesucht")
        wahl = input("Neuer Status: ")

        if wahl == "1":
            neuer_status = "Kontakt gefunden"
        elif wahl == "2":
            neuer_status = "Kein Kontakt gefunden"
        elif wahl == "3":
            neuer_status = "noch nicht gesucht"

        bewerbungen[int(nummer)-1]["linkedin"] = neuer_status
        speichern()
                                
# Punkt 9: Programm beenden
    elif auswahl == "9":
        print("Bis bald!")
        break

 
    