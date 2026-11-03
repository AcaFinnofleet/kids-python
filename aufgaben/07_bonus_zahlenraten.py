# ==========================================
#  Bonus-Aufgabe 7: Zahlenraten
# ==========================================
#
# Der Computer denkt sich eine Zahl zwischen 1 und 100 aus.
# Du musst sie erraten!
#
# Neu:
#   import random                  lädt die Zufalls-Werkzeuge
#   random.randint(1, 100)         Zufallszahl von 1 bis 100
#                                  (In Scratch: «Zufallszahl von 1 bis 100»)
#
#   while tipp != geheim:          wiederhole, solange der Tipp NICHT stimmt
#                                  (In Scratch: «wiederhole bis ...»)
#   !=                             bedeutet «ist nicht gleich»
#
# Deine Aufgaben:
#   1. Starte das Programm (IDLE: F5, VS Code: Ctrl+F5). Es merkt, ob du richtig liegst,
#      aber es gibt noch keine Tipps!
#   2. Ergänze an der markierten Stelle zwei Tipps:
#        falls tipp < geheim:  print("Zu klein!")
#        falls tipp > geheim:  print("Zu gross!")
#   3. Profi-Aufgabe: Zähle die Versuche mit einer Variable "versuche"
#      und zeige am Schluss an, wie viele Versuche du gebraucht hast.
#
# ------------------------------------------

import random

geheim = random.randint(1, 100)
tipp = 0

print("Ich denke an eine Zahl zwischen 1 und 100.")

while tipp != geheim:
    tipp = int(input("Dein Tipp: "))

    # Hier kommen deine Tipps hin (eingerückt!):


print("Juhui! Die Zahl war", geheim)
