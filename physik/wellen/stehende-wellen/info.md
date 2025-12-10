---
titel: Stehende Wellen
fach: Physik
thema: Wellen
unterthema: Interferenz
klassenstufe: 11-12
kurzbeschreibung: Interaktive Simulation zur Entstehung stehender Wellen durch Superposition und virtuelles Mikrowellenexperiment zur Wellenlängenbestimmung.
stichworte: stehende Welle, Superposition, Knoten, Bäuche, Interferenz, Mikrowellen, Wellenlänge, Kohärenz
---

## Beschreibung

Diese Simulation visualisiert die Entstehung stehender Wellen durch Überlagerung zweier gegenläufiger harmonischer Wellen gleicher Frequenz und Amplitude. 

**Tab 1: Superposition** zeigt:
- Zwei gegenläufige Wellen (blau: nach rechts, rot: nach links)
- Die resultierende stehende Welle (grün)
- Knoten (gelb) und Bäuche (violett) mit Markierungen
- Einstellbare Parameter: Wellenlänge (2–8 cm), Amplitude (0,5–2 cm), Frequenz (0,3–2 Hz)

**Tab 2: Mikrowellenexperiment** simuliert:
- Versuchsaufbau mit Sender (10 GHz), Reflektor und beweglichem Detektor
- Signalstärke-Anzeige zur Lokalisierung von Knoten und Bäuchen
- Messfunktion zur Bestimmung des Knotenabstands
- Automatische Berechnung von λ und Ausbreitungsgeschwindigkeit

## Lernziele

- Erklären der Entstehung stehender Wellen durch Superposition kohärenter Wellen
- Definieren der Begriffe Knoten und Bauch
- Angeben der Abstände: Knoten–Knoten = λ/2, Knoten–Bauch = λ/4
- Experimentelles Bestimmen der Wellenlänge aus dem Knotenabstand
- Erkennen, dass Mikrowellen elektromagnetische Wellen sind (v = c)

## Fachlicher Hintergrund

Treffen zwei harmonische Wellen gleicher Frequenz f, gleicher Amplitude A und gleicher Wellenlänge λ aufeinander, die sich in entgegengesetzter Richtung ausbreiten, so überlagern sie sich zu einer stehenden Welle:

**Hinlaufende Welle:** y₁(x,t) = A · sin(kx − ωt)  
**Reflektierte Welle:** y₂(x,t) = A · sin(kx + ωt)  
**Stehende Welle:** y(x,t) = y₁ + y₂ = 2A · sin(kx) · cos(ωt)

Die Orte mit sin(kx) = 0 heißen **Knoten** (dauerhaft y = 0).  
Die Orte mit |sin(kx)| = 1 heißen **Bäuche** (maximale Schwingungsamplitude 2A).

Der Abstand benachbarter Knoten beträgt λ/2, der Abstand Knoten–Bauch beträgt λ/4.

## Bedienung

### Tab 1: Superposition
1. Wellenlänge, Amplitude und Frequenz mit den Reglern einstellen
2. Einzelne Wellen oder die Resultierende ein-/ausblenden
3. Knoten und Bäuche markieren lassen
4. Mit Pause/Start die Animation anhalten
5. Messwerte (Knotenabstand, Knoten–Bauch-Abstand) in der Info-Box ablesen

### Tab 2: Mikrowellenexperiment
1. Detektor mit dem Regler entlang der Strecke bewegen
2. Signalstärke beobachten (Minimum = Knoten, Maximum = Bauch)
3. Bei einem Minimum "Knoten 1 markieren" klicken
4. Zum nächsten Minimum fahren und "Knoten 2 markieren" klicken
5. "λ berechnen" klicken für Ergebnis

## Bezug zum Rahmenplan MV

**Rahmenplan Physik Sek II (Erprobungsfassung), S. 30:**

*Stehende Wellen*
- Konstruktive und Destruktive Superposition
- Kohärenz, Kohärenzbedingung
- DE: Wellenlängenbestimmung mittels einer durch Reflexion erzeugten stehenden Welle

*Hinweise:* Der Schwerpunkt liegt auf eindimensionalen stehenden Wellen.

## Technische Hinweise

- Optimiert für iPad (Querformat) und Desktop
- Keine externen Abhängigkeiten
- Läuft offline nach einmaligem Laden
