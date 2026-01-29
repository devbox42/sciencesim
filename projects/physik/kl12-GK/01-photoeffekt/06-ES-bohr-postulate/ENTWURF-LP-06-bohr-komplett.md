# ENTWURF: Lernpfad "Bohr-Atommodell" (Mi 28.01. + Fr 30.01.)

**Status:** ZUR BESPRECHUNG
**Zielgruppe:** Physik 12 GK Gymnasium
**Zeitrahmen:** Mi 45 min (ES) + Fr 90 min (DS mit Recap)

---

## GESAMTKONZEPT

### Epistemische Struktur (Erkenntnisweg)
```
[Motivation] → [Problem] → [Evidenz] → [Hypothese] → [Theorie] → [Verifikation] → [Transfer]
```

### Didaktische Prinzipien
- **Beobachtung VOR Erklärung**: Schüler sehen Phänomene, grübeln, halten fest → dann Auflösung
- **Simulation auf jeder Slide**: Mindestens ein interaktives Element pro Station
- **Gymnasium GK**: Weniger Tipps, mehr eigenständiges Denken
- **Digitale Diagnostik**: Self-Checks im Lernpfad
- **Analoge Sicherung**: Beobachtungen auf AB festhalten

---

## PHASE 0: MOTIVATION – "Wozu ist das gut?" (ca. 5 min)

### Konzept
Interaktives Grid mit ~10 Anwendungsbereichen zum Anklicken. Jeder zeigt ein Bild und eine kurze Teaser-Info (ohne zu viel vorwegzunehmen).

### Elemente (klickbar mit Info-Popup)

| # | Anwendung | Bild/Icon | Teaser-Text |
|---|-----------|-----------|-------------|
| 1 | **Laser** | Laserpointer | "Warum ist Laserlicht so besonders? Es hat nur EINE Wellenlänge..." |
| 2 | **LEDs** | Bunte LEDs | "Warum leuchtet eine rote LED rot und eine blaue blau?" |
| 3 | **Neonröhren** | Leuchtreklame | "Jedes Gas hat seine eigene 'Farb-Signatur'..." |
| 4 | **Sternspektren** | Sternenhimmel | "Wie wissen Astronomen, woraus Sterne bestehen?" |
| 5 | **Feuerwerk** | Buntes Feuerwerk | "Verschiedene Metalle = verschiedene Farben. Warum?" |
| 6 | **Quantencomputer** | Chip-Illustration | "Die Grundlage: Quantisierte Energiezustände" |
| 7 | **MRT-Scanner** | MRT-Gerät | "Medizinische Bildgebung nutzt Quanteneffekte" |
| 8 | **Solarzellen** | Photovoltaik | "Wie 'fängt' man Licht ein?" |
| 9 | **Flammentest** | Bunsenbrenner + Flamme | "Natrium = gelb, Kupfer = grün. Immer!" |
| 10 | **GPS-Satelliten** | Satellit | "Extrem genaue Atomuhren basieren auf Quantenübergängen" |

### Animation
- Grid-Layout mit Hover-Effekt
- Klick öffnet kleine Info-Card (nicht Modal, sondern Expansion)
- Fortschrittsanzeige: "Du hast X von 10 erkundet"
- **Kein Zwang alle anzuklicken** – Weiter-Button immer sichtbar

### Abschluss-Text (nach Grid)
> "All diese Technologien haben eines gemeinsam: Sie nutzen die Tatsache, dass Energie in Atomen nur bestimmte Werte annehmen kann. Wie kommen wir zu dieser Erkenntnis? Das ist unser Weg heute."

---

## PHASE 1: DAS PROBLEM – Rutherford-Modell (Mi, ca. 15 min)

### Station 1.1: "Was wissen wir über Atome?"
**Typ:** Kurze Rekapitulation

**Animation:** Interaktives Rutherford-Atom
- Zeigt: Kern (winzig, positiv) + Elektronen (Kreisbahn)
- Beschriftungen ein-/ausblendbar
- Größenverhältnisse-Slider (Kern vs. Hülle)

**Lernpfad-Frage (Self-Check):**
> "Das Rutherford-Modell beschreibt das Atom als..."
> - [ ] Rosinenkuchen mit eingebetteten Elektronen
> - [x] Winziger positiver Kern + Elektronen auf Bahnen
> - [ ] Gleichmäßig verteilte Ladung

**AB-Bezug:** Kasten 1 – Skizze Rutherford-Modell

---

### Station 1.2: "Das Problem der klassischen Physik"
**Typ:** Beobachtungsaufgabe mit Simulation

**SIMULATION: Rutherford-Kollaps (verbessert)**

Verbesserungen gegenüber SIM-06a:
- **EM-Wellen deutlicher**: Wellenfronten in gelb/orange, die sich vom Elektron ausbreiten
- **Energie-Balken**: Zeigt sinkende Energie des Elektrons
- **Beschriftung**: "Elektromagnetische Strahlung" mit Pfeil
- **Zeitanzeige**: Countdown bis Kollaps

**ABLAUF:**
1. Schüler sehen Atom im Ruhezustand
2. Button: "Simulation starten"
3. Elektron kreist, EM-Wellen werden sichtbar abgestrahlt
4. Elektron spiralt langsam nach innen
5. KOLLAPS nach ~3 Sekunden Animation (= 10⁻¹¹ s simuliert)

**Beobachtungsauftrag (VOR Erklärung):**
> "Starte die Simulation und beobachte genau. Was passiert mit dem Elektron? Was siehst du, das vom Elektron ausgeht?"

**AB-Bezug:** Kasten 1 – "Beobachtung: Ich sehe, dass..."

**Lernpfad-Frage (nach Beobachtung):**
> "Was hast du beobachtet? Das Elektron..."
> - [ ] bleibt stabil auf seiner Bahn
> - [x] sendet Wellen aus und spiralt in den Kern
> - [ ] springt sofort in den Kern

**Info-Box (erst NACH Beobachtung sichtbar):**
> "Du hast es richtig gesehen: Ein Elektron auf einer Kreisbahn ist eine beschleunigte Ladung. Nach der klassischen Elektrodynamik (Maxwell) MUSS es elektromagnetische Strahlung aussenden – und dabei Energie verlieren."

---

### Station 1.3: "Die Konsequenz"
**Typ:** Erkenntnis formulieren

**Animation:** Zeitstrahl-Visualisierung
- Zeigt: 10⁻¹¹ Sekunden = 0,000 000 000 01 s
- Vergleich: Ein Lichtstrahl legt in dieser Zeit nur 3 mm zurück
- Pulsierender Text: "Kein Atom dürfte länger als einen Wimpernschlag existieren!"

**Lernpfad-Frage:**
> "Wenn die klassische Physik recht hätte, dann..."
> - [x] gäbe es keine stabilen Atome
> - [ ] würden Atome ewig existieren
> - [ ] würden nur schwere Atome zerfallen

**Erkenntnis-Box:**
> "ABER: Atome existieren stabil! Du selbst bestehst aus Atomen, die seit Milliarden Jahren existieren. Die klassische Physik kann das nicht erklären. Wir brauchen neue Ideen!"

---

## PHASE 2: DIE EVIDENZ – Wasserstoff-Spektrum (Mi, ca. 15 min)

### Station 2.1: "Licht von Atomen"
**Typ:** Vergleichende Beobachtung

**SIMULATION: Spektren-Vergleich (basiert auf SIM-06b)**

**Aufbau:**
- Oben: Kontinuierliches Spektrum (Glühlampe) – Regenbogen
- Unten: Wasserstoff-Spektrum – schwarzer Hintergrund mit einzelnen Linien

**Beobachtungsauftrag:**
> "Vergleiche die beiden Spektren. Was ist der fundamentale Unterschied?"

**AB-Bezug:** Kasten 2 – Tabelle ausfüllen (kontinuierlich vs. diskret)

**Lernpfad-Frage:**
> "Das Wasserstoff-Spektrum zeigt..."
> - [ ] alle Farben des Regenbogens
> - [x] nur bestimmte, einzelne Farben
> - [ ] nur rotes Licht

---

### Station 2.2: "Die Balmer-Serie"
**Typ:** Interaktive Erkundung

**SIMULATION: Klickbare Spektrallinien**
- Klick auf Linie → zeigt Wellenlänge, Name (Hα, Hβ, ...), Farbe
- Tabelle wird parallel ausgefüllt

**Animation-Feature:**
- "Lupe" über Spektrum ziehen
- Zeigt Wellenlänge in nm an Cursor-Position

**Erkenntnis-Impuls:**
> "Wasserstoff sendet NUR ganz bestimmte Wellenlängen aus – nicht alle! Was sagt uns das über die Energie im Atom?"

**AB-Bezug:** Kasten 2 – Balmer-Tabelle vervollständigen

---

### Station 2.3: "Schlussfolgerung"
**Typ:** Transfer zum Energiebegriff

**Animation:** Energietreppe vs. Rampe
- Links: Rampe (kontinuierlich) – durchgestrichen
- Rechts: Treppe (diskret) – mit Häkchen
- Elektron "hüpft" auf Treppenstufen

**Formel-Vorschau (noch ohne Zahlen):**
> E = nur bestimmte Werte = E₁, E₂, E₃, ...

**Lernpfad-Frage:**
> "Diskrete Spektrallinien bedeuten, dass..."
> - [ ] Licht immer die gleiche Energie hat
> - [x] Energie im Atom nur bestimmte Werte annehmen kann
> - [ ] Wasserstoff nur eine Farbe erzeugen kann

**Zwischen-Sicherung:**
> "ERKENNTNIS: Die Energie im Atom ist QUANTISIERT – sie kann nur bestimmte, diskrete Werte annehmen!"

---

## PHASE 3: DIE HYPOTHESE – Bohrs Postulate (Mi ca. 10 min + Fr)

### Station 3.1: "Bohrs revolutionäre Ideen"
**Typ:** Einführung der Postulate

**Animation:** "Postulat-Karten" zum Aufdecken
- 3 Karten, die nacheinander aufgedeckt werden
- Jede Karte hat Vorder- (Frage) und Rückseite (Postulat)

**Karte 1:**
- Vorne: "Warum stürzt das Elektron nicht in den Kern?"
- Hinten: **1. Postulat** – "Es gibt stabile Bahnen, auf denen das Elektron NICHT strahlt."

**Karte 2:**
- Vorne: "Warum nur bestimmte Wellenlängen?"
- Hinten: **2. Postulat** – "Licht wird nur bei ÜBERGÄNGEN zwischen Bahnen ausgesendet."

**Karte 3:**
- Vorne: "Welche Bahnen sind erlaubt?"
- Hinten: **3. Postulat** – "Nur Bahnen mit bestimmtem Drehimpuls: L = n · ℏ"

**AB-Bezug:** Kasten 3 – Postulate in eigenen Worten

---

### Station 3.2: "Das Bohr-Modell visualisiert"
**Typ:** Interaktive Simulation

**SIMULATION: Bohr-Atommodell (verbessert basierend auf SIM-06c)**

**Features:**
- Wählbare Energieniveaus (n = 1, 2, 3, 4, 5, 6)
- Elektron auf gewählter Bahn
- "Übergang auslösen" → Photon wird emittiert
- Photon-Farbe entspricht Wellenlänge
- Energiedifferenz wird angezeigt

**Beobachtungsauftrag:**
> "Wähle verschiedene Übergänge. Welche Übergänge erzeugen sichtbares Licht? Welche nicht?"

**AB-Bezug:** Kasten 3 – Übergangstabelle (Start-n, End-n, Farbe)

---

## — FREITAG: RECAP + FORTSETZUNG —

## RECAP (Fr, ca. 10 min)

### Station R.1: "Was wissen wir?"
**Typ:** Schnelles Quiz zur Aktivierung

**Mini-Quiz (5 Fragen, je 30 Sekunden):**
1. "Das Rutherford-Modell sagt voraus, dass Atome..." → kollabieren
2. "Das Wasserstoff-Spektrum zeigt..." → diskrete Linien
3. "Quantisierung bedeutet..." → nur bestimmte Werte erlaubt
4. "Bohrs 1. Postulat besagt..." → stabile Bahnen ohne Strahlung
5. "Photonen werden emittiert bei..." → Übergängen zwischen Niveaus

**Animation:** Fortschrittsbalken + Punktestand

---

## PHASE 4: DIE THEORIE – Energieniveaus (Fr, ca. 35 min)

### Station 4.1: "Die Energieformel"
**Typ:** Formel-Einführung mit Anwendung (GK-konform: KEINE Herleitung)

**Präsentation der Formel:**
> "Aus Bohrs Postulaten lässt sich eine Formel für die erlaubten Energien ableiten:"

**Formel-Highlight (groß, zentral):**
```
E_n = −13,6 eV / n²
```

**Erklärung:**
- n = Hauptquantenzahl (1, 2, 3, ...)
- E_n = Energie des Elektrons auf Bahn n
- Negativ = gebundener Zustand
- n = 1 → Grundzustand (tiefste Energie)

**Interaktives Element:** Schieberegler für n (1-6)
- Zeigt E_n Wert sofort berechnet
- Visualisiert Bahn im Atom (Radius wächst mit n²)
- Energie-Balken zeigt: je höher n, desto weniger negativ

**AB-Bezug:** Kasten 4 – Energiewerte berechnen (Tabelle ausfüllen)

---

### Station 4.1b: "Für Interessierte" (OPTIONAL, aufklappbar)
**Typ:** Hintergrundwissen – NICHT prüfungsrelevant

**Aufklappbox:**
> **Woher kommt die Formel?**
>
> Bohr kombinierte zwei Ideen:
> 1. **Kräftegleichgewicht:** Coulomb-Kraft = Zentripetalkraft
> 2. **Quantisierung:** Drehimpuls L = n · ℏ (nur ganzzahlige Vielfache!)
>
> Nach einiger Rechnung folgt daraus die Formel E_n = −13,6 eV/n².
>
> Die Zahl 13,6 eV ergibt sich aus Naturkonstanten (Elektronenmasse, Elementarladung, Planck-Konstante).

**Hinweis-Box:**
> ℹ️ Im Grundkurs musst du die Herleitung NICHT können – nur die Formel anwenden!

---

### Station 4.2: "Energieniveau-Diagramm"
**Typ:** Interaktive Visualisierung + Anwendung

**SIMULATION: Energie-Termschema**
- Horizontale Linien für n = 1, 2, 3, 4, 5, 6, ∞
- Energiewerte in eV beschriftet (aus Formel berechnet)
- Klickbare Übergänge → Pfeil erscheint + Photon
- Balmer-Serie hervorgehoben (sichtbares Licht)

**Beobachtungsauftrag:**
> "Klicke auf verschiedene Übergänge. Was fällt dir auf bei Übergängen, die im sichtbaren Bereich liegen?"

**Lernpfad-Rechnung 1 (mit Sofort-Feedback):**
> "Berechne die Energie des Photons beim Übergang n=3 → n=2:"
> - E₃ = −13,6 eV / 9 = ?
> - E₂ = −13,6 eV / 4 = ?
> - ΔE = E₃ − E₂ = ?
> Eingabefelder → Sofort-Feedback

**AB-Bezug:** Kasten 4 – gleiche Rechnung auf Papier

---

### Station 4.3: "Von Energie zu Wellenlänge"
**Typ:** Anwendung der Formel-Kette

**Formel-Kette visualisiert:**
```
E_n → ΔE = E_ober − E_unter → E_Photon = ΔE → λ = hc/E_Photon
```

**Lernpfad-Rechnung 2 (geführt):**
> "Berechne die Wellenlänge der Hα-Linie (Übergang 3→2):"
> 1. ΔE = 1,89 eV (aus voriger Station)
> 2. Umrechnen: E in Joule (× 1,6·10⁻¹⁹)
> 3. λ = hc/E einsetzen
> 4. Ergebnis: λ = ? nm
> Eingabefeld → Sofort-Feedback

**AB-Bezug:** Kasten 4 – Wellenlängen-Berechnung

---

### Station 4.4: "Theorie trifft Experiment"
**Typ:** Verifikation

**SIMULATION: Spektrum-Vergleich**
- Oben: Berechnete Wellenlängen aus Bohr-Formel
- Unten: Gemessenes Wasserstoff-Spektrum
- Button: "Überlagern" → Linien fahren zusammen

**Animation:** Perfekte Übereinstimmung wird sichtbar!

**Erkenntnis-Box:**
> "Die Bohr-Formel sagt die Spektrallinien auf den Nanometer genau voraus! Das ist eine starke Bestätigung der Theorie."

**Lernpfad-Frage:**
> "Was beweist die Übereinstimmung von Theorie und Experiment?"
> - [ ] Die Formel ist zufällig richtig
> - [x] Die Annahme quantisierter Energien ist korrekt
> - [ ] Wasserstoff ist ein besonderes Element

---

## PHASE 5: TRANSFER & VERTIEFUNG (Fr, ca. 35 min)

### Station 5.1: "Ionisierungsenergie"
**Typ:** Anwendung

**Animation:** Elektron wird "befreit"
- n = 1 → n = ∞ (freies Elektron)
- Energie-Pfeil zeigt 13,6 eV

**Lernpfad-Aufgabe:**
> "Wie viel Energie braucht man, um das Elektron aus dem Grundzustand zu entfernen?"

---

### Station 5.2: "Absorption vs. Emission"
**Typ:** Vertiefung

**SIMULATION: Photon-Absorption**
- Photon trifft Atom
- Elektron "springt" auf höheres Niveau
- Nur wenn E_Photon = ΔE passt!

**Vergleich:** Emission (nach unten, Photon raus) vs. Absorption (nach oben, Photon rein)

---

### Station 5.3: "Grenzen des Modells"
**Typ:** Kritische Reflexion

**Info-Box:**
> "Das Bohr-Modell erklärt Wasserstoff perfekt. ABER: Bei Atomen mit mehreren Elektronen versagt es. Die vollständige Lösung kommt mit der Quantenmechanik..."

**Animation:** Mehrere Elektronen → chaotische Bahnen → Fragezeichen

---

### Station 5.4: "Zusammenfassung"
**Typ:** Abschluss

**Animation:** Erkenntnisweg-Visualisierung
```
Problem → Evidenz → Hypothese → Theorie → Verifikation
   ↓         ↓          ↓          ↓           ↓
Kollaps  Spektrum   Postulate   E_n-Formel  Linien stimmen!
```

**Lernpfad-Abschluss:**
> "Du hast den Erkenntnisweg nachvollzogen, der Niels Bohr 1913 zum Nobelpreis führte!"

---

## NEUE/VERBESSERTE SIMULATIONEN (zu erstellen)

| # | Name | Beschreibung | Priorität |
|---|------|--------------|-----------|
| 1 | **SIM-06a-v2** | Rutherford-Kollaps mit deutlicheren EM-Wellen + Energie-Balken | HOCH |
| 2 | **SIM-06d-anwendungen** | Interaktives Grid mit 10 Anwendungen | HOCH |
| 3 | **SIM-06e-termschema** | Interaktives Energieniveau-Diagramm mit klickbaren Übergängen | HOCH |
| 4 | **SIM-06f-spektrum-vergleich** | Theorie vs. Experiment Überlagerung | MITTEL |
| 5 | **SIM-06g-absorption** | Photon-Absorption Animation | MITTEL |

---

## ARBEITSBLATT-STRUKTUR (AB-06 überarbeitet)

| Kasten | Thema | Aufgaben | BE |
|--------|-------|----------|-----|
| 1 | Rutherford & Kollaps | Skizze + Beobachtung + Erklärung | 3 |
| 2 | Spektrum | Tabelle kontinuierlich/diskret + Balmer-Werte | 3 |
| 3 | Bohr-Postulate | Postulate in eigenen Worten + Übergangstabelle | 4 |
| 4 | Energieformel | Berechnung E_n + Wellenlänge | 4 |
| 5 | Transfer | Ionisierung + Absorption/Emission | 3 |
| **Gesamt** | | | **17 BE** |

---

## ZEITPLAN

### Mittwoch 28.01. (45 min)
| Phase | Zeit | Inhalt |
|-------|------|--------|
| 0 | 5 min | Motivation: Anwendungen-Grid |
| 1 | 15 min | Problem: Rutherford-Kollaps |
| 2 | 15 min | Evidenz: Wasserstoff-Spektrum |
| 3.1 | 10 min | Hypothese: Postulate (Einführung) |

### Freitag 30.01. (90 min)
| Phase | Zeit | Inhalt |
|-------|------|--------|
| R | 10 min | Recap-Quiz (5 Fragen) |
| 3.2 | 10 min | Postulate: Bohr-Modell visualisiert |
| 4.1 | 10 min | Energieformel E_n präsentieren + Tabelle |
| 4.2 | 15 min | Termschema interaktiv + erste Rechnung |
| 4.3 | 15 min | Von Energie zu Wellenlänge (Formel-Kette) |
| 4.4 | 10 min | Theorie trifft Experiment (Verifikation) |
| 5 | 20 min | Transfer: Ionisierung, Absorption/Emission, Grenzen |

**Fokus GK:** Formel anwenden, NICHT herleiten. Mehr Zeit für Übung.

---

## OFFENE FRAGEN ZUR BESPRECHUNG

1. **Anwendungen-Grid:** 10 Beispiele zu viel? Oder genau richtig für optionales Erkunden?

2. ~~**Mathematik-Tiefe:**~~ ✅ GEKLÄRT: Herleitung nur als optionaler "Für Interessierte"-Kasten. GK = Formel anwenden, nicht herleiten.

3. **Lyman/Paschen-Serien:** Am Freitag mit behandeln oder nur Balmer? (Empfehlung: Nur erwähnen, Fokus auf Balmer)

4. **AB-Umfang:** 17 BE realistisch für beide Stunden oder kürzen?

5. **Simulationen:** Alle 5 neuen Simulationen erstellen oder mit Kompromissen arbeiten?

---

**NÄCHSTE SCHRITTE nach Freigabe:**
1. Neue Simulationen erstellen (SIM-06a-v2, 06d, 06e, 06f, 06g)
2. LP-06-bohr-postulate.html überarbeiten
3. AB-06-bohr-postulate.tex überarbeiten
4. Arbeitspfad ARBEITSPFAD-06-bohr-postulate.md erstellen
5. QR-Codes generieren
