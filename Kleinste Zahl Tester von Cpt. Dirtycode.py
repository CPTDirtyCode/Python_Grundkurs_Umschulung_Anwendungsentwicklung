

# Kleinste von drei unterschiedlichen Zahlen

import random

# Drei unterschiedliche Zufallszahlen erzeugen:
zahlen = random.sample(range(1, 999), 3)

a = zahlen[0]
b = zahlen[1]
c = zahlen[2]

print("Zahl 1:", a)
print("Zahl 2:", b)
print("Zahl 3:", c)

# Kleinste Zahl ermitteln
if a < b and a < c:
    kleinste = a
elif b < a and b < c:
    kleinste = b
else:
    kleinste = c

print("\nDie kleinste Zahl ist:", kleinste)