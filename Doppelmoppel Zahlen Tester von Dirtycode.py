

# def hat_doppelte_zahl(liste):
#     return len(liste) != len(set(liste))
#
# print()
# eingabe = input("Gib mehrere Zahlen ein (mit Leerzeichen getrennt): ")
# zahlen = list(map(int, eingabe.split()))
#
# print("\nDeine Liste:")
# print(zahlen)
#
# if hat_doppelte_zahl(zahlen):
#     print("\nDoppelte Zahlen gefunden!")
# else:
#     print("\nKeine doppelten Zahlen gefunden!")

#Besser:

# Doppelte Zahl mit Wort-Unterstützung


def text_zu_zahl(text):

    # Prüfen, ob der Benutzer eine Zahl eingegeben hat
    try:
        return int(text)

    except ValueError:

        # Wort in ASCII-/Unicode-Summe umwandeln
        wert = 0

        for buchstabe in text:
            wert += ord(buchstabe)

        return wert


def hat_doppelte_zahl(liste):
    return len(liste) != len(set(liste))

print()
print("=== Doppelte Zahl Prüfer ===")
print("Du kannst Zahlen und Wörter eingeben.")
print("Beispiel: 42 Hund Katze 99 Hund")
print()

eingabe = input("Gib mehrere Zahlen ein (mit Leerzeichen getrennt):")

teile = eingabe.split()

werte = []

print("\n--- Umwandlungen ---")

for eintrag in teile:

    try:
        zahl = int(eintrag)

        print(f"{eintrag} ist bereits eine Zahl.")

        werte.append(zahl)

    except ValueError:

        wortzahl = text_zu_zahl(eintrag)

        print(f"{eintrag} -> {wortzahl}")

        werte.append(wortzahl)

print("\n--- Ergebnisliste ---")
print(werte)

if hat_doppelte_zahl(werte):

    print("\nDoppelte Werte gefunden!")

    doppelte = []

    for wert in set(werte):

        if werte.count(wert) > 1:
            doppelte.append(wert)

    print("Doppelte Werte:", doppelte)

else:

    print("\nKeine doppelten Werte gefunden!")