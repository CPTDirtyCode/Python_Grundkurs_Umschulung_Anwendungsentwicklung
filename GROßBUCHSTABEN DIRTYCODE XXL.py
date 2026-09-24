
# Großbuchstaben

# Schreibe ein Python-Programm, das sämtliche existierenden Kombinationen
# aus zwei großen Buchstaben auf den Bildschirm schreibt.

#ord("A")  -> "Wie viele Goldmünzen ist das Zeichen wert?"
#chr(65)   -> "Welches Zeichen versteckt sich hinter 65?"

for erster_buchstabe in range(ord("A"), ord("Z") + 1):

    for zweiter_buchstabe in range(ord("A"), ord("Z") + 1):

        print(chr(erster_buchstabe) + chr(zweiter_buchstabe), end=" ")

    print()  # Zeilenumbruch nach jeder Reihe

#oder:
print()
print()
buchstaben = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for erster in buchstaben:
    for zweiter in buchstaben:
        print(erster + zweiter, end=" ")
    print()