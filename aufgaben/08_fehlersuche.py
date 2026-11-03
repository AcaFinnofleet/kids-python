# ==========================================
#  Aufgabe 8: Fehlersuche (Debugging)
# ==========================================
#
# Robo der Roboter hat ein Problem: In seinem Programm stecken 6 Fehler!
# Findet und korrigiert alle Fehler.
#
# So geht ihr vor:
#   1. Starte das Programm (Knopf ▶).
#   2. Python zeigt eine Fehlermeldung mit der Nummer der Zeile, in der der Fehler steckt.
#      VS Code unterstreicht manche Fehler schon vor dem Start rot.
#   3. Korrigiere den Fehler und starte nochmals.
#   4. Wiederhole, bis Robo «Programm fertig!» sagt.
#
# Python zeigt immer nur EINEN Fehler auf einmal.
# Das ist normal. Auch Profis korrigieren einen Fehler nach dem anderen.
#
# Fehler-Wörterbuch (die Meldungen sind auf Englisch):
#
#   unterminated string literal   Ein Anführungszeichen " fehlt.
#   expected ':'                  Ein Doppelpunkt : fehlt.
#   Maybe you meant '=='          Beim Vergleichen braucht es == statt =
#   expected an indented block    Die Zeile muss eingerückt sein (4 Leerzeichen).
#   name '...' is not defined     Ein Wort ist falsch geschrieben.
#   can only concatenate str      Text und Zahl gemischt. Tipp: int(input(...))
#
# Hilfe: Schau in den SPICKZETTEL!
#
# ------------------------------------------

print("Hallo, ich bin Robo, der Roboter!)

name = input("Wie heisst du? ")
prnit("Freut mich,", name)

alter = input("Wie alt bist du? ")
print("Nächstes Jahr bist du", alter + 1)

antwort = input("Magst du Roboter? (ja/nein) ")
if antwort == "ja"
    print("Ich mag dich auch!")
else:
print("Schade! Ich mag dich trotzdem.")

zahl = int(input("Rate meine Lieblingszahl (1 bis 5): "))
if zahl = 3:
    print("Richtig! Meine Lieblingszahl ist 3.")
else:
    print("Nein, meine Lieblingszahl ist 3.")

print("Programm fertig! Danke, dass du mich repariert hast!")
