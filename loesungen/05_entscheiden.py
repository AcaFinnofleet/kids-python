# Lösung zu Aufgabe 5: Das Programm entscheidet

antwort = input("Was ist 7 + 5? ")

if antwort == "12":
    print("Richtig! Super gmacht!")
else:
    print("Leider falsch. Die Antwort ist 12.")

antwort = input("Was ist 6 * 7? ")

if antwort == "42":
    print("Genau! Du bist ein Rechenprofi!")
else:
    print("Fast! Die Antwort ist 42.")

alter = int(input("Wie alt bist du? "))

if alter > 12:
    print("Du bist ein Teenager!")
else:
    print("Bald bist du ein Teenager!")
