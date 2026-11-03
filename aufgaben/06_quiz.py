# ==========================================
#  Aufgabe 6: Euer eigenes Quiz!
# ==========================================
#
# Jetzt seid ihr die Entwicklerinnen und Entwickler!
# Baut ein Quiz mit eigenen Fragen. Am Ende zeigt das Programm die Punkte.
#
# Neu:
#   punkte = punkte + 1    erhöht die Punkte um 1
#                          (In Scratch: «ändere punkte um 1»)
#
#   .lower()               macht alle Buchstaben klein.
#                          So ist «Bern», «BERN» und «bern» alles richtig.
#                          Schreibe deshalb die richtige Antwort klein!
#
# Deine Aufgaben:
#   1. Starte das Programm (Knopf ▶) und spiele die erste Frage.
#   2. Kopiere den Block von Frage 1 und mache daraus Frage 2, 3 und 4.
#      Ändere jeweils die Frage, die Antwort und die Nachrichten.
#   3. Passe die Zahl in der letzten Zeile an, wenn du mehr Fragen hast.
#   4. Am Schluss: Lasst ein anderes Team euer Quiz spielen!
#
# ------------------------------------------

print("==============================")
print("   Willkommen zu unserem Quiz!")
print("==============================")

punkte = 0

# ----- Frage 1 -----
antwort = input("Was ist die Hauptstadt der Schweiz? ")
if antwort.lower() == "bern":
    print("Richtig!")
    punkte = punkte + 1
else:
    print("Leider falsch. Die Antwort ist Bern.")

# ----- Frage 2 -----


# ----- Frage 3 -----


# ----- Frage 4 -----


print("==============================")
print("Du hast", punkte, "von 4 Punkten!")
