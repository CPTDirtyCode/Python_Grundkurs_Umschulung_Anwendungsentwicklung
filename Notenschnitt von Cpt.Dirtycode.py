

# Notenschnitt

import random

noten = []

# 20 Zufallsnoten erzeugen (1.0 bis 6.0 in Zehntel schritten)

for _ in range(20):
    note = random.randint(10, 60) / 10
    noten.append(note)

print("Erzeugte Noten:")
print(noten)

# Beste und schlechteste Note streichen

noten_ohne_ausreisser = noten.copy()

noten_ohne_ausreisser.remove(min(noten_ohne_ausreisser))
noten_ohne_ausreisser.remove(max(noten_ohne_ausreisser))

print("\nOhne beste und schlechteste Note:")
print(noten_ohne_ausreisser)

# Durchschnitt berechnen

durchschnitt = sum(noten_ohne_ausreisser) / len(noten_ohne_ausreisser)


# Auf halbe Noten runden

gerundet = round(durchschnitt * 2) / 2

print()

print(" Der Käpt'n wertet die Leistungen der Crew aus...")
print(" Die beste und schlechteste Bewertung werden über Bord geworfen!")
print(f" Durchschnitt der Crew: {durchschnitt:.2f}")
print(f" Offizieller Piraten-Notenschnitt: {gerundet:.1f}")