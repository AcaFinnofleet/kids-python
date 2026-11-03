# ==========================================
#  Aufgabe 4: Das Programm stellt Fragen
# ==========================================
#
# In Scratch:  «frage Wie heisst du? und warte»  und dann der Block «Antwort»
# In Python:   name = input("Wie heisst du? ")
#
# input() wartet, bis du etwas eintippst und Enter drückst.
# Deine Antwort wird in der Variable gespeichert.
#
# Achtung: input() gibt immer TEXT zurück.
# Um damit zu rechnen, machen wir mit int() eine Zahl daraus:
#   alter = int(input("Wie alt bist du? "))
#
# Deine Aufgaben:
#   1. Starte das Programm (F5) und beantworte die Fragen.
#   2. Frage nach dem Lieblingsessen und gib eine lustige Antwort aus.
#      Beispiel:  Pizza? Mmmh, das esse ich auch gern!
#   3. Frage nach zwei Zahlen und zeige ihre Summe an.
#      Vergiss int() nicht!
#
# ------------------------------------------

name = input("Wie heisst du? ")
print("Grüezi", name + "!")

alter = int(input("Wie alt bist du? "))
print("Nächstes Jahr bist du", alter + 1)

# Schreibe deine Zeilen hier:

