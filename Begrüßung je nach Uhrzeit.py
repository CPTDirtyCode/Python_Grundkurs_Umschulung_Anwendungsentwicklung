import time
import getpass
import sys

aktuelle_zeit = time.localtime()
stunde = aktuelle_zeit.tm_hour
benutzer = getpass.getuser()

print(f"Hallo {benutzer}!")
print(f"Aktuelle Uhrzeit: {stunde}:{aktuelle_zeit.tm_min:02d}")

if stunde >= 22 or stunde < 5:
    begruessung = "Gute Nacht"
elif stunde < 11:
    begruessung = "Guten Morgen"
elif stunde < 15:
    begruessung = "Mahlzeit"
elif stunde < 18:
    begruessung = "Guten Nachmittag"
else:
    begruessung = "Guten Abend"

print(f"{begruessung}, {benutzer}!")

sys.exit()