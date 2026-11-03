# Lösung zu Aufgabe 6: Euer eigenes Quiz!

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
antwort = input("Wie viele Beine hat eine Spinne? ")
if antwort == "8":
    print("Richtig!")
    punkte = punkte + 1
else:
    print("Leider falsch. Eine Spinne hat 8 Beine.")

# ----- Frage 3 -----
antwort = input("Wie heisst der höchste Berg der Schweiz? ")
if antwort.lower() == "dufourspitze":
    print("Richtig!")
    punkte = punkte + 1
else:
    print("Leider falsch. Es ist die Dufourspitze.")

# ----- Frage 4 -----
antwort = input("Was ist 9 * 9? ")
if antwort == "81":
    print("Richtig!")
    punkte = punkte + 1
else:
    print("Leider falsch. Die Antwort ist 81.")

print("==============================")
print("Du hast", punkte, "von 4 Punkten!")
