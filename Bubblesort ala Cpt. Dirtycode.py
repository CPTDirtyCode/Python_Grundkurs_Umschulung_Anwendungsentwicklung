

def bubblesort(beute):

    getauscht = True
    runde = 1

    while getauscht:

        print(f"\nSortierrunde {runde}")

        getauscht = False

        for i in range(len(beute) - 1):

            if beute[i] > beute[i + 1]:

                print(f"Tausche {beute[i]} mit {beute[i + 1]}")

                beute[i], beute[i + 1] = beute[i + 1], beute[i]

                getauscht = True

        print("Aktuelle Beute:", beute)

        runde += 1

    return beute


eingabe = input("Gib die Werte deiner Beute ein (Zahlen mit Leerzeichen getrennt: ")

beute = [int(x) for x in eingabe.split()]

print("\nUnsortierte Beute:")
print(beute)

bubblesort(beute)

print("\nPerfekt sortierte Piratenbeute:")
print(beute)