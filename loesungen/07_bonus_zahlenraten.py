# Lösung zu Bonus-Aufgabe 7: Zahlenraten

import random

geheim = random.randint(1, 100)
tipp = 0
versuche = 0

print("Ich denke an eine Zahl zwischen 1 und 100.")

while tipp != geheim:
    tipp = int(input("Dein Tipp: "))
    versuche = versuche + 1

    if tipp < geheim:
        print("Zu klein!")
    if tipp > geheim:
        print("Zu gross!")

print("Juhui! Die Zahl war", geheim)
print("Du hast", versuche, "Versuche gebraucht.")
