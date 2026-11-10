# Python-Spickzettel

Zum Ausdrucken: [CHEAT-SHEET.pdf](CHEAT-SHEET.pdf), zwei A4-Seiten, beidseitig drucken.

## So schreibst du Python

### Programm starten

- Knopf ▶ oben rechts in VS Code.
- Oder im Terminal: `py 01_hallo.py` und Enter.
- Tipp: `py 01` und die Tab-Taste ergänzt den Namen.

**Wo ist das Resultat?** Unten im Terminal, unter der langen Zeile, die VS Code für dich getippt hat.

**Zeilen mit `#`** sind Notizen für Menschen. Python überspringt sie. Dort steht deine Aufgabe.

**Stoppen:** ins Terminal klicken, dann Ctrl + C.

### 01 Text anzeigen

In Scratch: «sage Hallo!»

| Du schreibst | Das Terminal zeigt |
|---|---|
| `print("Hallo Welt!")` | `Hallo Welt!` |
| `print("\\o/")` | `\o/` |

Text steht immer zwischen "Anführungszeichen". Jedes `print` macht eine neue Zeile.
Für ein `\` im Text schreibst du zwei: `\\`

### 02 Rechnen

In Scratch: «( ) + ( )»

| `+` | `-` | `*` | `/` |
|---|---|---|---|
| plus | minus | mal | geteilt |

| Du schreibst | Das Terminal zeigt |
|---|---|
| `print(3 + 4)` | `7` |
| `print("3 + 4")` | `3 + 4` |
| `print(10 / 2)` | `5.0` |

Zum Rechnen **keine** Anführungszeichen.
Mit `/` zeigt Python immer eine Kommazahl, mit Punkt statt Komma.

### 03 Variablen

In Scratch: «setze alter auf 11»

Eine Variable ist eine Box mit Namen. Der Name hat keine Leerzeichen: `lieblingszahl`

```python
name = "Lena"   # Text: mit ""
alter = 11      # Zahl: ohne ""
print(name, "ist", alter)
```

Das Terminal zeigt: `Lena ist 11`

Das Komma zeigt mehrere Dinge nacheinander, mit Abstand.

### 04 Fragen stellen

In Scratch: «frage … und warte»

```python
name = input("Wie heisst du? ")
print("Grüezi", name + "!")
```

Im Terminal (`Lena` tippst du selbst):

```text
Wie heisst du? Lena
Grüezi Lena!
```

Das Programm wartet, bis du tippst und Enter drückst.
Mit `+` klebt Python Text ohne Abstand zusammen.

> **Achtung:** `input()` gibt immer **Text**. Zum Rechnen machst du mit `int()` eine Zahl daraus:
> `alter = int(input("Wie alt bist du? "))`

### 05 Entscheiden

In Scratch: «falls … dann … sonst»

```python
antwort = input("Was ist 7 + 5? ")
if antwort == "12":         # ← Doppelpunkt!
    print("Richtig!")       # ← eingerückt
else:
    print("Leider falsch.")
```

**Einrücken** = 4 Leerzeichen oder Tab-Taste. Das ist wie das Innere eines Scratch-Blocks.
`if` geht auch ohne `else`.

| `==` | `!=` | `>` | `<` |
|---|---|---|---|
| ist gleich | ist nicht gleich | grösser als | kleiner als |

> **Ein = oder zwei?** `alter = 11` speichert. `alter == 11` fragt: Ist das gleich?

Die Antwort von `input()` ist Text, also vergleichst du mit `"12"`.
Mit `int()` wird sie eine Zahl, dann ohne Anführungszeichen: `if alter > 12:`

### 06 Punkte zählen

In Scratch: «ändere punkte um 1»

```python
punkte = 0                  # am Anfang
punkte = punkte + 1         # bei «Richtig!»
if antwort.lower() == "bern":
```

`.lower()` macht alle Buchstaben klein. So sind Bern, BERN und bern alle richtig.
Schreibe die richtige Antwort im Code deshalb klein!

### 07 Zahlenraten (Bonus)

In Scratch: «wiederhole bis …»

```python
import random                    # ganz oben
geheim = random.randint(1, 100)  # 1 bis 100
tipp = 0
while tipp != geheim:
    tipp = int(input("Dein Tipp: "))
```

> **Andersrum!** Scratch wiederholt, **bis** es stimmt. Python wiederholt, **solange** es **nicht** stimmt. Darum steht hier `!=`.

## Wenn etwas nicht klappt

Fehler sind normal. Auch Profis korrigieren einen nach dem anderen.

### So liest du eine Fehlermeldung

```text
  File "...\08_fehlersuche.py", line 31
    print("Hallo, ich bin Robo, der Roboter!)
          ^
SyntaxError: unterminated string literal (detected at line 31)
```

1. `line 31` heisst Zeile 31. Dort oder kurz davor steckt der Fehler.
2. Das Dach `^` zeigt ungefähr auf die Stelle.
3. Die letzte Zeile sagt, was falsch ist. Die Tabelle unten übersetzt sie.
4. Python zeigt immer nur **einen** Fehler. Korrigiere ihn und starte nochmals.

### Fehler-Wörterbuch

| Python meldet | Das heisst | Falsch | Richtig |
|---|---|---|---|
| `SyntaxError: unterminated string literal` | Ein Anführungszeichen `"` fehlt. Steht direkt davor ein `\`? Dann schreibe `\\`. | `print("Hallo)` | `print("Hallo")` |
| `SyntaxError: expected ':'` | Ein Doppelpunkt `:` fehlt am Ende der Zeile mit `if`, `else` oder `while`. | `if antwort == "ja"` | `if antwort == "ja":` |
| `IndentationError: expected an indented block` | Die Zeile unter `if`, `else` oder `while` braucht 4 Leerzeichen oder Tab. | `print("Schade")` ganz links | 4 Leerzeichen, dann `print("Schade")` |
| `SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?` | Beim Vergleichen braucht es zwei Gleichheitszeichen `==`. | `if zahl = 3:` | `if zahl == 3:` |
| `NameError: name 'prnit' is not defined` | Ein Wort ist falsch geschrieben. Oft rät Python: *Did you mean: 'print'?* | `prnit("Hallo")` | `print("Hallo")` |
| `TypeError: can only concatenate str (not "int") to str` | Text und Zahl sind gemischt. `input()` gibt Text, es fehlt `int()`. | `alter = input("Alter? ")` | `alter = int(input("Alter? "))` |
| `ValueError: invalid literal for int() with base 10: 'elf'` | Du hast Buchstaben getippt, wo eine Zahl verlangt ist. Starte nochmals und tippe Ziffern. | Eingabe `elf` | Eingabe `11` |

### Hilfe!

**Es passiert nichts?**
Das Programm wartet auf deine Antwort. Klicke ins Terminal unten, tippe und drücke Enter.

**Es hört nicht mehr auf?**
Klicke ins Terminal und drücke Ctrl + C.

**VS Code fragt nach einem Debugger?**
Du hast F5 gedrückt. Drücke Esc und starte mit dem Knopf ▶.

**Rot unterstrichen?**
VS Code hat schon vor dem Start einen Fehler gefunden. Schau dir diese Stelle genau an.

**Richtig geantwortet, aber das Programm sagt «falsch»?**
Hier zeigt Python keinen Fehler.
Steht die richtige Antwort im Code klein, also `"bern"`?
Vergleichst du mit `"12"` statt mit `12`?

### Wo ist die Taste?

Schweizer Tastatur. Shift (⇧) gedrückt halten, dann die zweite Taste tippen.

| Zeichen | Tasten |
|---|---|
| `"` | Shift + 2 |
| `:` | Shift + Punkt |
| `(` und `)` | Shift + 8 und Shift + 9 |
| `=` | Shift + 0 |
| `+` | Shift + 1 |
| `*` | Shift + 3 |
| `/` | Shift + 7 |
| `!` | Shift + ¨ (rechts neben ü) |
| `-` | eigene Taste rechts neben dem Punkt |
| `<` | eigene Taste links neben Y |
| `>` | Shift + < |
| `\` | AltGr + < |
