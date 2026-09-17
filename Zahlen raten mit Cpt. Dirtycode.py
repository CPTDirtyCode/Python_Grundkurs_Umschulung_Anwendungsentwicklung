

import random

geheime_zahl = random.randint(1, 100)
versuche = 0

print("Ich habe mir eine Zahl zwischen 1 und 100 ausgedacht!")

while True:

    try:
        tipp = int(input("Dein Tipp: "))
        versuche += 1

        if tipp < geheime_zahl:
            print("Zu niedrig!")

        elif tipp > geheime_zahl:
            print("Zu hoch!")

        else:
            print(f"\nRichtig geraten!")
            print(f"Du hast {versuche} Versuche gebraucht.")
            break

    except ValueError:
        print(" Bitte eine gültige Zahl eingeben!")