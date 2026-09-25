

# 🏴‍☠️ Piraten-Beute Rechner

SCHATZ = 8_420_000
kombinationen = 0

print("Arrrrr!")
print(f"Wir haben {SCHATZ:,} Gold-Dublonen geplündert!")
print("Der Schiffscomputer berechnet mögliche Aufteilungen...\n")

for crew1 in range(1, 10000):

    if SCHATZ % crew1 == 0:

        crew2 = SCHATZ // crew1

        if crew2 < 10000 and crew1 <= crew2:

            print(
                f" {crew1} Piraten erhalten je {crew2} Dublonen"
            )

            kombinationen += 1

print("\n Der Schiffscomputer ist fertig.")
print(f" Es wurden {kombinationen} mögliche Beute-Aufteilungen gefunden!")