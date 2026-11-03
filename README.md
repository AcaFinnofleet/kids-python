# kids-python

Python-Aufgaben für Kinder von 10 bis 12 Jahren mit Scratch-Erfahrung.
Die Lektion dauert etwa eine Stunde.

## Struktur

| Pfad | Inhalt |
|---|---|
| `aufgaben/` | Dateien für die Kinder, zum Ergänzen |
| `aufgaben/SPICKZETTEL.txt` | Übersicht Scratch → Python und typische Fehler |
| `loesungen/` | Lösungen für die Leitung |

## Aufgaben

| Datei | Thema | Entsprechung in Scratch |
|---|---|---|
| `01_hallo.py` | `print` | «sage» |
| `02_rechnen.py` | Operatoren `+ - * /` | Operator-Blöcke |
| `03_variablen.py` | Variablen | «setze ... auf» |
| `04_fragen.py` | `input()`, `int()` | «frage ... und warte» |
| `05_entscheiden.py` | `if` / `else` | «falls ... dann ... sonst» |
| `06_quiz.py` | Quiz mit Punkten, Schlussaufgabe | Kombination der vorherigen Blöcke |
| `07_bonus_zahlenraten.py` | `random`, `while`; Bonus für schnelle Gruppen | «Zufallszahl», «wiederhole bis» |
| `08_fehlersuche.py` | Debugging: sechs absichtliche Fehler korrigieren | — |

## Vorbereitung der PCs

1. Installiere Python:
   ```
   winget install Python.Python.3.13
   ```
2. Öffne ein neues Terminal und prüfe die Installation mit `python --version`.
3. Installiere die Python-Erweiterung von Microsoft für VS Code:
   ```
   code --install-extension ms-python.python
   ```
4. Kopiere den Ordner `aufgaben/` auf den Desktop jedes PCs.
   Kopiere den Ordner `loesungen/` nicht.
5. Lege in VS Code die Taste F5 auf «Run Python File» fest:
   Ctrl+Shift+P → «Preferences: Open Keyboard Shortcuts (JSON)», dann einfügen:
   ```json
   [
     {
       "key": "f5",
       "command": "python.execInTerminal",
       "when": "editorLangId == python"
     }
   ]
   ```
6. Öffne in VS Code den Ordner `aufgaben/` mit «File → Open Folder…».
7. Öffne `01_hallo.py` und starte es mit F5 als Test.

## Programme starten in VS Code

- F5 führt die Datei, die im Editor offen ist, mit `python.execInTerminal` aus.
  Dieser Befehl startet Python direkt im Terminal, ohne Debugger.
- Ohne den Eintrag aus Schritt 5 startet F5 den Debugger von VS Code.
  Der Projektordner enthält keine Debug-Konfiguration, deshalb fragt VS Code dann nach einem Debugger.
- Das Programm läuft im Terminal unten, dort funktioniert auch `input()`.
- Ctrl+C im Terminal stoppt ein laufendes Programm.
- `aufgaben/.vscode/settings.json` setzt die Eingabeaufforderung (Command Prompt) als Terminal.
  Die Eingabeaufforderung startet schneller als PowerShell und lädt kein PowerShell-Profil.
- VS Code liest `.vscode/settings.json` nur aus dem geöffneten Ordner.
  Das Projekt enthält deshalb eine zweite Kopie in `.vscode/settings.json` für den Fall, dass das ganze Projekt geöffnet wird.

## Ablauf

| Minuten | Aktivität |
|---|---|
| 0–10 | Einführung: Was macht ein Entwickler? Vergleich Scratch → Python mit dem `SPICKZETTEL` |
| 10–50 | Aufgaben in Gruppen, im eigenen Tempo, von `01` bis `06` |
| 50–60 | Jede Gruppe lässt eine andere Gruppe ihr Quiz spielen |

## Hinweise für die Leitung

- Jede Gruppe soll mindestens `06_quiz.py` erreichen, weil die Schlusspräsentation diese Datei verwendet.
- Wird die Zeit knapp, überspringe `02_rechnen.py` und `03_variablen.py`.
  `04_fragen.py` führt Variablen nochmals ein.
- `07_bonus_zahlenraten.py` ist für Gruppen, die früher fertig sind.
- `08_fehlersuche.py` enthält sechs Fehler.
  Python meldet zuerst die vier Syntaxfehler, weil es die ganze Datei vor dem Ausführen liest.
  Danach meldet Python `NameError` und `TypeError`, wenn es die betroffenen Zeilen ausführt.
  Die Reihenfolge der Meldungen steht in `loesungen/08_fehlersuche.py`.
- Setze `08_fehlersuche.py` als Alternative zu `07_bonus_zahlenraten.py` ein, oder gemeinsam nach der Einführung, um die Fehlermeldungen zu zeigen.
- `int(input(...))` erzeugt einen `ValueError`, wenn jemand Text statt einer Zahl eingibt.
  Zeige den Fehler den Kindern: Eine Fehlermeldung lesen gehört zur Arbeit eines Entwicklers.
- `06_quiz.py` vergleicht Textantworten mit `.lower()`.
  Deshalb muss die erwartete Antwort im Code kleingeschrieben sein.
