# kids-python

Esercizi di Python per bambini dai 10 ai 12 anni con esperienza di Scratch.
La sessione dura circa un'ora.
Le istruzioni e i messaggi sono in tedesco con ortografia svizzera.

## Struttura

| Percorso | Contenuto |
|---|---|
| `aufgaben/` | File per i bambini, da completare |
| `aufgaben/SPICKZETTEL.txt` | Promemoria con le corrispondenze Scratch → Python e gli errori tipici |
| `loesungen/` | Soluzioni per l'adulto che guida la sessione |

## Esercizi

| File | Concetto | Equivalente Scratch |
|---|---|---|
| `01_hallo.py` | `print` | «sage» |
| `02_rechnen.py` | Operatori `+ - * /` | Blocchi operatore |
| `03_variablen.py` | Variabili | «setze ... auf» |
| `04_fragen.py` | `input()`, `int()` | «frage ... und warte» |
| `05_entscheiden.py` | `if` / `else` | «falls ... dann ... sonst» |
| `06_quiz.py` | Quiz con punteggio, esercizio finale | Combinazione dei blocchi precedenti |
| `07_bonus_zahlenraten.py` | `random`, `while`; bonus per i gruppi veloci | «Zufallszahl», «wiederhole bis» |
| `08_fehlersuche.py` | Debugging: correggere sei errori voluti | — |

## Preparazione dei PC

1. Installa Python:
   ```
   winget install Python.Python.3.13
   ```
2. Apri un nuovo terminale e verifica l'installazione con `python --version`.
3. Copia la cartella `aufgaben/` sul desktop di ogni PC.
   Non copiare la cartella `loesungen/`.
4. Imposta IDLE come programma predefinito per i file `.py`.
   In alternativa, apri ogni file con un clic destro e scegli «Edit with IDLE».
5. Esegui `loesungen/06_quiz.py` con F5 come prova.

## Scaletta

| Minuti | Attività |
|---|---|
| 0–10 | Introduzione: cosa fa uno sviluppatore, confronto Scratch → Python con il `SPICKZETTEL` |
| 10–50 | Esercizi in gruppo, a ritmo libero, da `01` a `06` |
| 50–60 | Ogni gruppo fa giocare il proprio quiz a un altro gruppo |

## Note per la guida

- Ogni gruppo deve arrivare almeno a `06_quiz.py`, perché la presentazione finale usa quel file.
- Dove il tempo stringe, salta `02_rechnen.py` e `03_variablen.py`.
  `04_fragen.py` ripresenta le variabili.
- `07_bonus_zahlenraten.py` serve ai gruppi che finiscono prima degli altri.
- `08_fehlersuche.py` contiene sei errori.
  Python segnala prima i quattro errori di sintassi, perché analizza tutto il file prima dell'esecuzione.
  Poi segnala `NameError` e `TypeError`, quando esegue le righe colpite.
  L'ordine delle segnalazioni è descritto in `loesungen/08_fehlersuche.py`.
- Usa `08_fehlersuche.py` come alternativa a `07_bonus_zahlenraten.py`, oppure in plenaria dopo l'introduzione per mostrare i messaggi di errore.
- `int(input(...))` produce un `ValueError` quando l'utente inserisce testo al posto di un numero.
  Mostra l'errore ai bambini: leggere una traceback fa parte del lavoro dello sviluppatore.
- `06_quiz.py` confronta le risposte di testo con `.lower()`.
  Per questo la risposta attesa nel codice va scritta in minuscolo.
