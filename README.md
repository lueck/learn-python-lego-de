# Einstieg in die Python-Programmierung mit Lego-Robotern ganz easy #

```{python}
from pyboost.fahrzeug import *

fahrzeug = Einachser()
fahrzeug.fahre_geradeaus(1200, geschwindigkeit = 0.9)
fahrzeug.drehe(180, RECHTS)
fahrzeug.fahre_bogen(180, 600, LINKS)
fahrzeug.ende()
```

Die Roboter-Programmierung mit Python hat verglichen mit grafischen
Programmiersprachen den Vorteil, dass die Eigenschaften z.B. eines
Fahrzeugs wie Raddurchmesser, Übersetzung des Getriebes, Entfaltung,
Spurweite usw. in Objekten definiert und gekapselt werden können. Die
Mathematik zur Berechnung einer Geradeaus- oder Bogenfahrt, die
teilweise Kompetenzen erfordert, die erst Ende der Mittelstufe
vorhanden sind (insbesondere bei der Bogenfahrt), kann dann diesen
Objekten überlassen werden. Beim Bewegen des Fahrzeugs kann deshalb
wie im obigen Beispiel ganz easy in *deklarativer* Weise ausgedrückt
werden, wohin es sich bewegen soll.

Das erleichtert den *Einstieg* in Python ganz erheblich.

Einheiten:
- *mm* (Millimeter) für Längen
- *Grad* bei allen Winkeln
- ein Wert zwischen 0 und 1 für Geschwindigkeit

## Voraussetzungen ##

- Python >= 3.5

## Installation ##

Siehe [Installation (noch englisch)](INSTALL.md).
