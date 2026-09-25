"""import math?"""


# Fibonacci

"""
Schreibe ein Programm, das per for-Schleife die ersten 10 Zahlen der
Fibonacci-Folge ausgibt: 0 1 1 2 3 5 8 13 21 34

Zusatz: Gib alle Fibonacci Zahlen unter 500 aus

Bonus:
Zeige die Fibonacci-Zahlen in einem ASCII-Koordinatensystem.
"""


print("Erste 10 Fibonacci-Zahlen:")

fib = [0, 1]

print(0, 1, end=" ")

for i in range(8):
    neue_zahl = fib[-1] + fib[-2]
    fib.append(neue_zahl)
    print(neue_zahl, end=" ")

print("\n")


# Alle Fibonacci-Zahlen unter 500

print("Alle Fibonacci-Zahlen unter 500:")

a = 0
b = 1

while a < 500:
    print(a, end=" ")
    a, b = b, a + b

print("\n")


# ASCII-Koordinatensystem mit der Hilfe von KI:

print("ASCII-Diagramm der ersten 10 Fibonacci-Zahlen:")
print("(X = Position in der Folge, Y = Fibonacci-Wert)\n")

werte = fib

max_y = max(werte)

# Skalierung, damit das Diagramm nicht riesig wird
skalierung = 2

for y in range(max_y // skalierung + 1, -1, -1):

    print(f"{y*skalierung:>2}|", end="")

    for x in range(len(werte)):
        if werte[x] // skalierung == y:
            print("●", end=" ")
        else:
            print("  ", end="")

    print()

print("  +" + "--" * len(werte))

print("   ", end="")
for x in range(len(werte)):
    print(x, end=" ")

print("\n   X-Achse (Index der Fibonacci-Zahl)")