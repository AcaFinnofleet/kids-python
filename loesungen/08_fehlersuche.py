# Lösung zu Aufgabe 8: Fehlersuche (Debugging)
#
# Die 6 Fehler, in der Reihenfolge, in der Python sie meldet:
#   1. Zeile mit «Hallo»:        Anführungszeichen am Ende fehlt.
#   2. Zeile mit «if antwort»:   Doppelpunkt fehlt.
#   3. Zeile mit «Schade»:       Einrückung fehlt.
#   4. Zeile mit «if zahl»:      = statt ==
#   5. Zeile mit «prnit»:        Tippfehler, richtig ist print.
#   6. Zeile mit «alter»:        int() fehlt, sonst ist alter ein Text.
#
# Python meldet zuerst alle Fehler in der Schreibweise (1 bis 4),
# weil es das Programm vor dem Start ganz durchliest.
# Die Fehler 5 und 6 bemerkt Python erst, wenn es die Zeile ausführt.

print("Hallo, ich bin Robo, der Roboter!")

name = input("Wie heisst du? ")
print("Freut mich,", name)

alter = int(input("Wie alt bist du? "))
print("Nächstes Jahr bist du", alter + 1)

antwort = input("Magst du Roboter? (ja/nein) ")
if antwort == "ja":
    print("Ich mag dich auch!")
else:
    print("Schade! Ich mag dich trotzdem.")

zahl = int(input("Rate meine Lieblingszahl (1 bis 5): "))
if zahl == 3:
    print("Richtig! Meine Lieblingszahl ist 3.")
else:
    print("Nein, meine Lieblingszahl ist 3.")

print("Programm fertig! Danke, dass du mich repariert hast!")
