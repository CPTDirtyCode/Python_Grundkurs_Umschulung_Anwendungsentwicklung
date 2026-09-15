from random import randint

zahl1 = randint(1, 20)
zahl2 = randint(1, 20)

if zahl1 == zahl2:
    print(f"{zahl1} == {zahl2}")
elif zahl1 > zahl2:
    print(f"{zahl1} > {zahl2}")
elif zahl1 < zahl2:
    print(f"{zahl1} < {zahl2}")

