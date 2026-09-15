

import random
import time

zeichen = "23456789abcdefghijkmnopqrstuvwxyz"

print("===================================")
print("   Buchverlag Web-Code Generator")
print("===================================")

for nummer in range(1, 6):

    print(f"\nErzeuge Web-Code #{nummer}...")
    time.sleep(1)

    code = ""

    for _ in range(8):
        code += random.choice(zeichen)

    print(f" Web-Code: {code}")

print("\n 5 Web-Codes erfolgreich erstellt!")