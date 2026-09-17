import time

print(" Willkommen beim Hunde-Alters-Orakel! ")
print("Vor dir sitzt ein alter Hund.")
print('"Wuff? Wenn du mein Alter wissen willst, belle mich an!"')

bellen = input("\nWie bellst du den Hund an? ")

while bellen.lower() not in [
    "wuff",
    "wau",
    "wuff wuff",
    "wau wau",
    "kleff",
    "kleff kleff",
    "bork",
    "bork bork"
]:
    print("\n Der Hund schaut dich verwirrt an.")
    bellen = input("Versuch es mit einem richtigen Bellen: ")

print("\n Wuff! Du sprichst meine Sprache!")
time.sleep(1)

hundealter = int(input("\nWie alt ist der Hund in Jahren? "))

if hundealter == 1:
    menschenalter = 14
elif hundealter == 2:
    menschenalter = 22
else:
    menschenalter = 22 + (hundealter - 2) * 5

print("\n Der magische Hund denkt nach...")
time.sleep(2)

print(f"\n Ein Hund von {hundealter} Jahren")
print(f" entspräche ungefähr einem Menschen von {menschenalter} Jahren!")

print("\n Der Hund wedelt mit dem Schwanz.")
print('"Wuff! Danke fürs Spielen!"')