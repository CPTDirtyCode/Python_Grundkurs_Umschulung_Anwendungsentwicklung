
# Durchschnitt

"""
Schreibe eine Funktion, die drei Zahlen entgegennimmt,
den Durchschnitt berechnet und diesen zurückgibt.
"""

def durchschnitt(a, b, c):
    return (a + b + c) / 3


zahl1 = float(input("Gib die erste Zahl ein: "))
zahl2 = float(input("Gib die zweite Zahl ein: "))
zahl3 = float(input("Gib die dritte Zahl ein: "))

ergebnis = durchschnitt(zahl1, zahl2, zahl3)

print(f"\nDer Durchschnitt beträgt: {ergebnis}")