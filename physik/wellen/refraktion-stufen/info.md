---
titel: Wellenrefraktion – Stufenmodell
fach: Physik
thema: Wellen
unterthema: Brechung
klassenstufe: 9-12
kurzbeschreibung: Simulation zur Brechung von Wasserwellen an diskreten Tiefenstufen. Zeigt, wie kontinuierliche Brechung durch viele kleine diskrete Brechungen modelliert werden kann.
stichworte: Wellenrefraktion, Brechung, Snellius, Stufenmodell, Wasserwellen, Strand, Tiefenverlauf, Wellengeschwindigkeit
---

## Beschreibung

Diese Simulation modelliert die Brechung von Wasserwellen beim Auflaufen auf einen Strand als diskrete Stufenfolge. Der kontinuierliche Tiefenverlauf wird in 2-40 Stufen unterteilt, an deren Grenzen jeweils das Snellius-Gesetz angewendet wird.

Die Simulation zeigt anschaulich, wie die Summe vieler kleiner Brechungen an den Stufengrenzen zur kontinuierlichen Kruemmung der Wellenfront fuehrt.

## Lernziele

- Das Snellius-Gesetz auf Wasserwellen anwenden
- Den Zusammenhang zwischen Wassertiefe und Wellengeschwindigkeit verstehen
- Kontinuierliche Brechung als Grenzfall diskreter Brechungen begreifen
- Erklaeren, warum Wellen am Strand parallel ankommen

## Fachlicher Hintergrund

Fuer Flachwasserwellen gilt die Dispersionsrelation:

    v = sqrt(g * h)

Die Wellengeschwindigkeit haengt von der Wassertiefe ab. An jeder Stufengrenze gilt das Snellius-Gesetz:

    sin(theta_1) / sin(theta_2) = v_1 / v_2

Da v_2 < v_1 (flacheres Wasser), folgt theta_2 < theta_1 – die Wellen werden zum Lot hin gebrochen.

Die Simulation verwendet einen exponentiellen Tiefenverlauf von h_max (tiefes Wasser) bis h_min (Strand). Der depthFactor wird berechnet als:

    depthFactor = (h_min / h_max)^t

wobei t = 0 am Anfang (tief) und t = 1 am Ende (flach).

## Bedienung

**Simulationsparameter:**
- Einfallswinkel: 5-70 Grad
- Anzahl Stufen: 2-40 (bei wenigen Stufen sieht man die einzelnen Brechungen, bei vielen die kontinuierliche Kurve)
- Wellenabstand: Abstand zwischen den Wellenkaemmen
- Geschwindigkeit: Animationsgeschwindigkeit
- Tiefe: Wassertiefe im tiefen Bereich (h_max) und am Strand (h_min)

**Anzeige-Optionen:**
- Wellennormalen (rot): Zeigt die Ausbreitungsrichtung in jeder Stufe
- Winkel anzeigen (gelb): Brechungswinkel an den Stufen
- Geschwindigkeiten (gruen): Relative Geschwindigkeit v/v_0
- Tiefenwerte: Wassertiefe in jeder Stufe
- Strahlengang: Ein einzelner "Lichtstrahl" mit Brechung an jeder Grenzflaeche
- Stufengrenzen: Gestrichelte Linien zwischen den Stufen

## Didaktische Hinweise

Mit wenigen Stufen (2-5) sind die einzelnen Brechungen an den Grenzflaechen deutlich sichtbar. Erhoehe schrittweise die Stufenzahl, um zu zeigen, wie sich die Gesamtbrechung dem kontinuierlichen Fall annaehert.

Bei 40 Stufen ergibt sich eine fast perfekt gekruemmte Wellenfront – die diskrete Naeherung entspricht dann dem kontinuierlichen Tiefenverlauf.
