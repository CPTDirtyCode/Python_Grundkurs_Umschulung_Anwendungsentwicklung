

def berechne_kosten(preis, anzahl=100, waehrung="€"):
    return f"{preis * anzahl} {waehrung}"


print("🏴‍☠️ Piraten-Kostenrechner 🏴‍☠️")

preis = float(input("Preis pro Kanonenkugel: "))
anzahl = input("Anzahl (Enter = 100): ")
waehrung = input("Währung (Enter = €): ")

if anzahl == "":
    anzahl = 100
else:
    anzahl = int(anzahl)

if waehrung == "":
    waehrung = "€"

print()
print("Gesamtkosten:")
print(berechne_kosten(preis, anzahl, waehrung))