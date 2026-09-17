# Zahlenreihen
# Schaue, welche der 12 Aufgaben du schon lösen kannst.
# Je mehr, desto besser, aber es müssen nicht alle sein.

# 1. Schreibe eine Schleife, die Folgendes ausgibt:
# 1 2 3 4 5

print("Aufgabe 1:")
for i in range(1, 6):
    print(i, end=" ")
print("\n")


# 2. Schreibe eine Schleife, die Folgendes ausgibt:
# 100 90 80 70 60 50 40 30 20 10

print("Aufgabe 2:")
for i in range(100, 0, -10):
    print(i, end=" ")
print("\n")


# 3. Schreibe eine Schleife, die Folgendes ausgibt:
# 2000 3000 4000 5000 6000

print("Aufgabe 3:")
for i in range(2000, 7000, 1000):
    print(i, end=" ")
print("\n")


# 4. Schreibe eine Schleife, die Folgendes ausgibt:
# 13 17 21 25 29

print("Aufgabe 4:")
for i in range(13, 30, 4):
    print(i, end=" ")
print("\n")


# 5. Schreibe eine Schleife, die Folgendes ausgibt:
# 2.0 1.5 1.0 0.5 0.0 -0.5 -1.0

print("Aufgabe 5:")
zahl = 2.0
while zahl >= -1.0:
    print(zahl, end=" ")
    zahl -= 0.5
print("\n")


# 6. Schreibe eine Schleife, die Folgendes ausgibt:
# 1.0 2.2 3.4 4.6 5.8 7.0 8.2 9.4

print("Aufgabe 6:")
zahl = 1.0
while zahl <= 9.4:
    print(round(zahl, 1), end=" ")
    zahl += 1.2
print("\n")


# 7. Schreibe eine Schleife, die Folgendes ausgibt:
# Beachte: die 7 fehlt!
# 1 2 3 4 5 6 8 9 10

print("Aufgabe 7:")
for i in range(1, 11):
    if i != 7:
        print(i, end=" ")
print("\n")


# 8. Schreibe eine Schleife, die Folgendes ausgibt:
# Beachte: die 25 und die 41 fehlen!
# 13 17 21 29 33 37 45

print("Aufgabe 8:")
for i in range(13, 46, 4):
    if i != 25 and i != 41:
        print(i, end=" ")
print("\n")


# 9. Schreibe eine Schleife, die Folgendes ausgibt:
# Z5 Z7 Z9 Z11 Z13

print("Aufgabe 9:")
for i in range(5, 14, 2):
    print(f"Z{i}", end=" ")
print("\n")


# 10. Schreibe eine Schleife, die Folgendes ausgibt:
# a2b3 a12b13 a22b23

print("Aufgabe 10:")
for i in range(2, 23, 10):
    print(f"a{i}b{i+1}", end=" ")
print("\n")


# 11. Schreibe eine Schleife,
# die alle Zahlen von 1 bis 20 addiert
# und danach das Endergebnis ausgibt.

print("Aufgabe 11:")
summe = 0

for i in range(1, 21):
    summe += i

print("Summe =", summe)
print()


# 12. Schreibe EINE Schleife, die Folgendes ausgibt:
# 1 2 3 4 5 4 3 2 1

print("Aufgabe 12:")

for i in range(1, 10):
    if i <= 5:
        print(i, end=" ")
    else:
        print(10 - i, end=" ")

print()