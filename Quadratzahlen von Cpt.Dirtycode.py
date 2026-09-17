
# Quadratzahlen

zahl = 1
anzahl = 0

print("Quadratzahlen kleiner als 100:")

while zahl ** 2 < 100:
    quadratzahl = zahl ** 2
    print(quadratzahl, end=" ")

    anzahl += 1
    zahl += 1

print("\n")
print("Anzahl der gefundenen Quadratzahlen:", anzahl)