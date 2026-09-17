

def teilersumme_kleiner(zahl):

    summe = 0

    print("Teiler:")

    for teiler in range(1, zahl):

        if zahl % teiler == 0:
            print(teiler, end=" ")
            summe += teiler

    print(f"\nTeilersumme: {summe}")

    return summe < zahl


zahl = int(input("Gib eine Zahl ein: "))

print("Ergebnis:", teilersumme_kleiner(zahl))