# Stunde 5: Halbwertszeit

> Einzelstunde (45 min) | Klasse 10 | Kernphysik

---

## Lernziele

| Nr | Lernziel | AFB | Überprüfung |
|----|----------|-----|-------------|
| 3.1 | Den Begriff Halbwertszeit definieren | I | Definition |
| 3.2 | Den exponentiellen Zerfall grafisch darstellen und interpretieren | II | Diagramm |
| 3.3 | Berechnungen mit dem Zerfallsgesetz durchführen | II | Rechenaufgaben |
| 3.4 | Die C-14-Methode zur Altersbestimmung erklären | II | Anwendung |

---

## Motivation & Relevanz

### Warum Halbwertszeit lernen?

| Frage | Antwort |
|-------|---------|
| **Wozu braucht man das?** | Altersbestimmung (Mumien, Dinosaurier, Erde!), Medizin (Wie lange bleibt Kontrastmittel im Körper?), Atomkraft (Wie lange strahlt Müll?) |
| **Was hat das mit mir zu tun?** | Wenn du je ein MRT oder CT brauchst, wird die HWZ bestimmen, wie lange du "strahlen" wirst |

### Alltagsanwendungen

| Anwendung | Isotop | Halbwertszeit | Bedeutung |
|-----------|--------|---------------|-----------|
| **Ötzi-Datierung** | C-14 | 5730 a | Funde bis ~50.000 Jahre alt |
| **Schilddrüsen-Scan** | I-131 | 8 d | Nach 24 d: nur noch 12,5% |
| **Atommüll** | Pu-239 | 24.000 a | Problem für 240.000+ Jahre! |
| **PET-Scan** | F-18 | 110 min | Schnell weg → wenig Belastung |

### Einstiegs-Hook (für Lernpfad)

> **"Die Alpen-Mumie Ötzi ist exakt 5300 Jahre alt. Woher wissen wir das so genau?"**
>
> Die Antwort steckt in jedem Atom: Radioaktiver Zerfall ist wie eine tickende Uhr.
> Heute lernst du, diese "Atomuhr" zu lesen!

---

## Fachlicher Hintergrund

### Radioaktiver Zerfall

- Radioaktiver Zerfall ist ein **statistischer Prozess**
- Man kann nicht vorhersagen, WANN ein einzelner Kern zerfällt
- Aber: Bei großen Mengen ist die Zerfallsrate vorhersagbar

### Halbwertszeit T₁/₂

**Definition:** Die Halbwertszeit ist die Zeit, nach der die Hälfte der ursprünglich vorhandenen Kerne zerfallen ist.

**Wichtig:**
- Halbwertszeit ist **stoffspezifisch** (für jedes Isotop konstant)
- Unabhängig von: Temperatur, Druck, chemischer Bindung
- Kann nicht beeinflusst werden!

### Zerfallsgesetz

**Formel:**
```
N(t) = N₀ · (½)^(t/T₁/₂)
```

| Symbol | Bedeutung |
|--------|-----------|
| N(t) | Anzahl der Kerne zum Zeitpunkt t |
| N₀ | Anzahl der Kerne zum Zeitpunkt t=0 |
| t | vergangene Zeit |
| T₁/₂ | Halbwertszeit |

**Alternative Schreibweise:**
```
N(t) = N₀ · e^(-λt)    mit λ = ln(2)/T₁/₂
```
(Für Klasse 10: nur die Halbwertszeit-Formel verwenden)

### Beispiel-Halbwertszeiten

| Isotop | T₁/₂ | Verwendung |
|--------|------|------------|
| ¹⁴C | 5730 Jahre | Altersbestimmung |
| ¹³¹I | 8 Tage | Schilddrüsentherapie |
| ⁶⁰Co | 5,3 Jahre | Strahlentherapie |
| ²³⁸U | 4,5 Mrd. Jahre | Gesteinsalter |
| ²²²Rn | 3,8 Tage | Radonbelastung |
| ²¹⁰Po | 138 Tage | Giftstoff |

### C-14-Methode (Radiokarbon-Datierung)

**Prinzip:**
1. Lebende Organismen nehmen ¹⁴C aus der Atmosphäre auf (konstantes Verhältnis ¹⁴C/¹²C)
2. Nach dem Tod: kein neues ¹⁴C mehr, vorhandenes zerfällt
3. Aus dem ¹⁴C/¹²C-Verhältnis → Alter bestimmbar

**Reichweite:** ~50.000 Jahre (danach zu wenig ¹⁴C übrig)

---

## Stundenverlauf

### Phase 1: Einstieg – Würfelexperiment (10 min)

**Simulation des radioaktiven Zerfalls**

| Zeit | Lehrer | Schüler | Medium |
|------|--------|---------|--------|
| 2' | Erklärt: "Jeder Würfel = 1 Atomkern, 6 = Zerfall" | Zuhören | Würfel |
| 5' | Leitet Durchführung | Würfeln, "6er" entfernen, zählen | EA/GA |
| 3' | Sammelt Ergebnisse, trägt in Diagramm ein | Ergebnisse nennen | Tafel |

**Erwartetes Ergebnis:**
- Start: 100 Würfel
- Runde 1: ~83 übrig
- Runde 2: ~69 übrig
- usw. → exponentielle Abnahme

**Alternativ:** PhET-Simulation "Radioaktiver Zerfall"

---

### Phase 2: Erarbeitung I – Zerfallsgesetz (15 min)

**Lernpfad-Abschnitt 1-3**

| Zeit | Inhalt | Methode |
|------|--------|---------|
| 5' | Definition Halbwertszeit | Lernpfad |
| 5' | Zerfallskurve: Diagramm lesen | Lernpfad + interaktiv |
| 5' | Formel: N(t) = N₀ · (½)^(t/T₁/₂) | Lernpfad |

**Lernpfad-Inhalte:**

> **Halbwertszeit:**
> Nach einer Halbwertszeit ist die Hälfte der Kerne zerfallen.
>
> | Zeit | Anteil übrig |
> |------|--------------|
> | 0 | 100% |
> | 1 · T₁/₂ | 50% |
> | 2 · T₁/₂ | 25% |
> | 3 · T₁/₂ | 12,5% |
> | 4 · T₁/₂ | 6,25% |

**Diagramm im Lernpfad:**
```
N/N₀
  │
1 ┼────┐
  │    └───┐
½ ┼────────└───┐
  │            └───┐
¼ ┼────────────────└───
  │
  └──┼──────┼──────┼──────► t
     T₁/₂  2T₁/₂  3T₁/₂
```

---

### Phase 3: Übung – Berechnungen (12 min)

**Lernpfad-Abschnitt 4**

| Zeit | Inhalt | Methode |
|------|--------|---------|
| 3' | Beispielrechnung vorführen | Lernpfad |
| 9' | Übungsaufgaben (4 Stück) | EA |

**Beispielrechnung:**

> **Aufgabe:** Ein Präparat enthält 800 radioaktive Kerne. Die Halbwertszeit beträgt 4 Tage. Wie viele Kerne sind nach 12 Tagen noch vorhanden?
>
> **Lösung:**
> - Gegeben: N₀ = 800, T₁/₂ = 4 d, t = 12 d
> - Gesucht: N(t)
> - Anzahl Halbwertszeiten: 12 d ÷ 4 d = 3
> - N(t) = 800 · (½)³ = 800 · ⅛ = **100 Kerne**

**Übungsaufgaben (kopfrechenbar!):**

| Nr | N₀ | T₁/₂ | t | Lösung N(t) |
|----|-----|------|---|-------------|
| 1 | 400 | 2 h | 6 h | 50 |
| 2 | 1000 | 5 d | 10 d | 250 |
| 3 | 200 | 8 a | 24 a | 25 |
| 4 | 640 | 10 min | 40 min | 40 |

---

### Phase 4: Anwendung – C-14-Methode (8 min)

**Lernpfad-Abschnitt 5**

| Zeit | Inhalt | Methode |
|------|--------|---------|
| 4' | Prinzip der Radiokarbon-Datierung | Lernpfad |
| 4' | Beispiel: Ötzi, Mumien | Lernpfad + Bild |

**Lernpfad-Inhalt:**

> **C-14-Datierung:**
>
> 1. Lebewesen nehmen ¹⁴C auf (aus CO₂ der Luft)
> 2. Nach dem Tod: ¹⁴C zerfällt, kein neues kommt nach
> 3. Je weniger ¹⁴C übrig → desto älter
>
> **Beispiel Ötzi:**
> - Gefunden 1991 in den Alpen
> - ¹⁴C-Gehalt: ~53% des ursprünglichen
> - T₁/₂ = 5730 Jahre
> - Alter: ~5300 Jahre

---

### Phase 5: Sicherung (5 min)

| Zeit | Inhalt | Methode |
|------|--------|---------|
| 5' | AB: Formel + 2 Aufgaben | EA → Hefter |

---

## Arbeitsblatt: Halbwertszeit

### Merksatz (in Hefter übertragen)

```
┌─────────────────────────────────────────────────────────────┐
│  HALBWERTSZEIT T₁/₂                                         │
│                                                             │
│  Definition: Zeit, nach der die Hälfte der Kerne            │
│              zerfallen ist.                                 │
│                                                             │
│  Formel:  N(t) = N₀ · (½)^(t/T₁/₂)                         │
│                                                             │
│  N₀ = Anfangsanzahl    t = Zeit    T₁/₂ = Halbwertszeit    │
└─────────────────────────────────────────────────────────────┘
```

---

### Aufgabe 1: Zerfallskurve (4 BE)

Ein radioaktives Präparat hat eine Halbwertszeit von 2 Stunden. Zu Beginn sind 800 Kerne vorhanden.

a) Fülle die Tabelle aus (2 BE):

| Zeit (h) | 0 | 2 | 4 | 6 | 8 |
|----------|---|---|---|---|---|
| Kerne | 800 | ___ | ___ | ___ | ___ |

b) Zeichne die Zerfallskurve in das Diagramm (2 BE):

```
N
 │
800┼─
   │
600┼
   │
400┼
   │
200┼
   │
  0┼──┼──┼──┼──┼──┼─► t (h)
     2  4  6  8
```

**Lösung:**
- a) 800 → 400 → 200 → 100 → 50
- b) Exponentiell fallende Kurve durch diese Punkte

---

### Aufgabe 2: Berechnung (4 BE)

Iod-131 hat eine Halbwertszeit von 8 Tagen und wird in der Medizin verwendet.

a) Ein Patient erhält ein Präparat mit 400 mg ¹³¹I. Wie viel ist nach 24 Tagen noch vorhanden? (2 BE)

_______________________________________________

b) Nach wie vielen Tagen sind nur noch 25 mg übrig? (2 BE)

_______________________________________________

**Lösung:**
- a) 24 d ÷ 8 d = 3 Halbwertszeiten → 400 · (½)³ = 400 · ⅛ = **50 mg**
- b) 400 → 200 → 100 → 50 → 25 = 4 Halbwertszeiten → 4 · 8 d = **32 Tage**

---

### Aufgabe 3: Transfer – C-14-Datierung (4 BE)

In einer Holzprobe aus einem archäologischen Fund ist nur noch 12,5% des ursprünglichen ¹⁴C-Gehalts vorhanden.

a) Wie viele Halbwertszeiten sind vergangen? (2 BE)

_______________________________________________

b) Wie alt ist die Probe? (T₁/₂ von ¹⁴C = 5730 Jahre) (2 BE)

_______________________________________________

**Lösung:**
- a) 100% → 50% → 25% → 12,5% = **3 Halbwertszeiten**
- b) 3 · 5730 a = **17.190 Jahre**

---

## Lernpfad-Struktur (Stunde 5)

```
Step 1: Einstieg – Würfelexperiment (content + Simulation)
Step 2: Was ist Halbwertszeit? (content)
Step 3: Zerfallskurve lesen (content + interaktiv)
Step 4: Formel anwenden (content + Beispiel)
Step 5: Übung: Berechnungen (exercise: numeric, 4 Aufgaben)
Step 6: C-14-Methode (content)
Step 7: AB-Hinweis + Quiz (test: 4 Fragen)
```

---

## Erwartungshorizont Lernpfad-Quiz

| Frage | Typ | Inhalt | Lösung |
|-------|-----|--------|--------|
| Q1 | MC | Definition Halbwertszeit | Zeit, nach der die Hälfte zerfallen ist |
| Q2 | Numeric | N₀=200, T₁/₂=5d, t=15d → N(t)=? | 25 |
| Q3 | MC | Wie viel % nach 2 Halbwertszeiten? | 25% |
| Q4 | Numeric | 12,5% übrig → wie viele T₁/₂? | 3 |

---

## Differenzierung (qualitativ)

### ★ Basis – Verstehen & Ablesen
| Aufgabentyp | Beispiel |
|-------------|----------|
| Tabelle | Zerfallstabelle ausfüllen (halbieren) |
| Diagramm | "Lies ab: Wie viele Kerne nach 2 Halbwertszeiten?" |
| Beschreibung | "Erkläre mit eigenen Worten, was nach 3 HWZ passiert ist" |

### ★★ Standard – Berechnen & Anwenden
| Aufgabentyp | Beispiel |
|-------------|----------|
| Vorwärts | N₀ = 800, T½ = 4h, t = 12h → N(t) = ? |
| Rückwärts | N₀ = 400, N(t) = 25 → Wie viele HWZ? |
| Anwendung | "Iod-131 (T½ = 8d): Wann sind 75% zerfallen?" |

### ★★★ Erweitert – Modellieren & Bewerten
| Aufgabentyp | Beispiel |
|-------------|----------|
| C-14-Problem | "Probe hat 12,5% C-14. Wie alt ist sie?" |
| Reflexion | "Warum funktioniert C-14 nur bis ~50.000 Jahre?" |
| Modellkritik | "Welche Unsicherheiten hat die Radiokarbonmethode?" |

---

## Scaffolding (gestufte Hilfen)

### Für Halbwertszeit-Berechnungen

```
[Hilfe 1 – Impuls]
"Wie oft passt die Halbwertszeit in die Gesamtzeit?"

[Hilfe 2 – Strategie]
"Teile t durch T½. Das ist die Anzahl der Halbierungen."

[Hilfe 3 – Beispiel]
"Bei t = 12h und T½ = 4h: 12 ÷ 4 = 3 Halbwertszeiten"

[Hilfe 4 – Rechenschritt]
"N(t) = N₀ · (½)³ = N₀ · ⅛. Jetzt einsetzen!"
```

### Für C-14-Datierung

```
[Hilfe 1] "Wie viel Prozent C-14 ist noch da?"
[Hilfe 2] "100% → 50% → 25% → 12,5% = wie viele Halbierungen?"
[Hilfe 3] "Anzahl HWZ × 5730 Jahre = Alter"
```

---

## Inklusion & UDL

### Repräsentationsformen
| Inhalt | Text | Bild | Interaktiv | Audio |
|--------|------|------|------------|-------|
| Halbwertszeit | ✓ Definition | ✓ Zerfallskurve | ✓ Würfel-Simulation | ○ TTS |
| Berechnung | ✓ Formel + Beispiel | ✓ Rechenschema | ✓ Numeric-Übung | ○ Video |
| C-14 | ✓ Erklärtext | ✓ Ötzi-Bild | ✓ Altersberechnung | ○ Doku-Clip |

### Barrierefreiheit
- [ ] Schriftgröße AB: ≥11pt
- [ ] Diagramm: Achsenbeschriftung groß genug
- [ ] Formel: Brüche alternativ als Dezimalzahl (½ = 0,5)
- [ ] Tabellen: Klare Linien, ausreichend Platz
- [ ] Rechenwege: Schrittweise, nicht komprimiert

### Alternative Zugänge
| Kanal | Umsetzung |
|-------|-----------|
| Visuell | Zerfallskurve, Würfel-Demo |
| Auditiv | Erklärvideo, Lehrermoderation |
| Haptisch | Würfelexperiment selbst durchführen |
| Lesend | Lernpfad, AB mit Beispielrechnungen |

### Konkrete Alternativmaterialien

| Material | Standard | Alternative A | Alternative B |
|----------|----------|---------------|---------------|
| **Lernpfad-Text** | HTML-Version | PDF (14pt) | Audio-TTS |
| **AB Halbwertszeit** | Formelbasiert | Tabellenbasiert (nur Halbieren) | Fertige Beispiele nachrechnen |
| **Würfelexperiment** | Real (Würfel) | PhET-Simulation | Fertige Datentabelle |
| **C-14-Anwendung** | Lernpfad-Text | Ötzi-Video (5 min) | Infografik |

### Video-Alternativen (mit Untertiteln)

| Thema | Link | Länge | UT |
|-------|------|-------|-----|
| Halbwertszeit | SimpleClub | 6 min | ✓ |
| C-14-Datierung | Terra X Lesch | 8 min | ✓ |

---

## Praktikabilität & Zeitmanagement

### Zeitpuffer

| Phase | Geplant | Minimum | Puffer |
|-------|---------|---------|--------|
| Würfelexperiment | 10 min | 7 min | 3 min |
| Zerfallsgesetz | 15 min | 12 min | 3 min |
| Berechnungen | 12 min | 10 min | 2 min |
| C-14-Methode | 8 min | 5 min | 3 min |
| **Gesamt** | **45 min** | **34 min** | **11 min** |

### Notfallplan

| Problem | Lösung |
|---------|--------|
| **Keine Würfel** | PhET-Simulation "Radioactive Dating Game" |
| **Schüler zu schnell** | Rückwärts-Aufgabe: "Probe hat 6,25% C-14. Alter?" |
| **Schüler zu langsam** | C-14 nur qualitativ, Formel-Anwendung als HA |
| **Rechenschwierigkeiten** | Tabellen-Methode (nur Halbieren, keine Formel) |

### Backup-Material

- [ ] Offline-PDF: `backup-lernpfad-halbwertszeit.pdf`
- [ ] AB Papier-Set: 30× vorgedruckt
- [ ] Würfel-Set: 30 Würfel (Alternative: Online-Würfel-Tool)

### Mixed-Ability-Konzept

```
┌─────────────────────────────────────────────────────────────┐
│  TEMPO-DIFFERENZIERUNG (45 min = eng!)                     │
│                                                             │
│  PHASE 1: Alle gemeinsam (Würfelexperiment)                │
│  └─ Aktive Beteiligung aller                               │
│                                                             │
│  PHASE 2: Differenziertes Üben                             │
│  ├─ ★ Langsame: Tabellen-Methode (nur Halbieren)          │
│  ├─ ★★ Mittlere: Formel mit ganzzahligen HWZ              │
│  └─ ★★★ Schnelle: Rückwärts-Aufgaben + C-14               │
│                                                             │
│  PHASE 3: C-14 für alle (qualitativ)                       │
└─────────────────────────────────────────────────────────────┘
```

### Begabtenförderung (Enrichment)

| Für wen | Material | Inhalt |
|---------|----------|--------|
| **Schnell fertig** | Lernpfad-Erweiterung | Nicht-ganzzahlige HWZ (mit ln) |
| **Mathe-affin** | Zusatz | Herleitung: N(t) = N₀ · e^(-λt) |
| **Hochbegabt** | Challenge | "Berechne das Alter der Erde (U-Pb-Methode)" |

### Enrichment-Aufgaben im Lernpfad

```
[Nach dem Quiz erscheint für Schüler mit >90%:]

🚀 BONUS: Die Exponentialfunktion

Die Formel N(t) = N₀ · (½)^(t/T½) ist eigentlich:
N(t) = N₀ · e^(-λt)   mit λ = ln(2)/T½

Aufgabe (Mathe Klasse 11 voraus!):
1. Zeige: (½)^(t/T½) = e^(-ln(2)·t/T½)
2. Nach welcher Zeit sind 90% zerfallen (nicht 50%)?
   Tipp: Setze N(t) = 0,1 · N₀ und löse nach t auf.

💡 Das brauchst du im Physik-LK!
```

### Realistische Klassenraumszenarien

| Szenario | Häufigkeit | Lösung |
|----------|------------|--------|
| Würfel reichen nicht (30 SuS) | möglich | Gruppen à 4 mit je 25 Würfeln |
| Formel zu abstrakt für 10 SuS | häufig | Tabellen-Methode als Fallback |
| Zeit reicht nicht für C-14 | möglich | C-14 als Einstieg nächste Stunde |
| Schüler fragt nach Pu-239 (Atommüll) | wahrscheinlich | Vorgriff auf Stunde 6-7 |

---

## Kopfrechenbare Werte

**Halbwertszeiten:** 2, 4, 5, 8, 10 (Tage/Stunden/Jahre/Minuten)

**Startmengen:** 100, 200, 400, 500, 800, 1000

**Zeiten:** Vielfache der Halbwertszeit (1, 2, 3, 4 × T₁/₂)

**Ergebnisse:** Immer durch Halbieren:
- ½ = 50%
- ¼ = 25%
- ⅛ = 12,5%
- 1/16 = 6,25%

---

## Aktivierung & Kognitive Aktivität

### Hypothesen-Phasen

| Phase | Schüler-Hypothese | Methode |
|-------|-------------------|---------|
| Vor Würfelexperiment | "Wie viele Würfel bleiben nach 5 Runden?" | Schätzung aufschreiben |
| Nach Experiment | "Ist Zerfall vorhersagbar?" | Think-Pair-Share |
| Vor C-14-Anwendung | "Wie kann man Alter messen?" | Brainstorming (1 min) |

### Würfelexperiment als Aktivierung

```
┌─────────────────────────────────────────────────────────────┐
│  WÜRFEL-ZERFALL (aktive Schülerbeteiligung)                 │
│                                                             │
│  Setup: Jeder Schüler = "Atomkern", Würfel = Zerfallschance │
│                                                             │
│  Runde 1: Alle würfeln. Wer 6 würfelt → "zerfallen" (setzt) │
│  Runde 2: Nur "aktive" Kerne würfeln weiter                 │
│  → Dokumentation: Wie viele sind noch "aktiv"?             │
│                                                             │
│  Erkenntnis: "Nach ~4 Runden ist die Hälfte weg"           │
│              → Das ist die HALBWERTSZEIT!                  │
└─────────────────────────────────────────────────────────────┘
```

### Think-Pair-Share Protokoll

| Frage | Think | Pair | Share |
|-------|-------|------|-------|
| "Wann zerfällt ein einzelner Kern?" | Notiz | Diskussion | "Wissen wir nicht!" |
| "Was bedeutet T½ = 5730 a für C-14?" | Rechnung | Vergleichen | Erklärung |

---

## Metacognition-Prompts

### Lernpfad-Integration

| Nach Abschnitt | Prompt |
|----------------|--------|
| Definition HWZ | "Erkläre HWZ in einem Satz für einen Grundschüler" |
| Zerfallskurve | "Was fällt dir an der Kurvenform auf?" |
| Formel | "Welcher Schritt fällt dir schwer: t/T½ berechnen oder einsetzen?" |
| C-14-Methode | "Was hat dich überrascht?" |

### Selbstcheck vor Rechnung

```
Vor jeder Aufgabe im Lernpfad:
□ Gegeben notiert? (N₀, T½, t)
□ Gesucht klar? (N(t) oder Anzahl HWZ)
□ Strategie gewählt? (Tabelle oder Formel)
```

---

## Diagnostisches Feedback (Lernpfad)

### Fehlerkategorien HWZ-Berechnungen

| Fehlertyp | Typischer Fehler | Feedback |
|-----------|------------------|----------|
| HWZ-Anzahl falsch | t ÷ T½ falsch | "Teile die Gesamtzeit durch die Halbwertszeit" |
| Halbieren vergessen | N₀ · ½ statt (½)^n | "Halbiere für JEDE Halbwertszeit" |
| Einheiten gemischt | Tage und Stunden | "Achte auf gleiche Einheiten!" |
| Formel falsch | N₀ ÷ 2^n | "Richtig: N₀ · (½)^n – multiplizieren, nicht dividieren!" |

---

## Medien & Material

- [ ] Würfel (100 Stück) oder PhET-Simulation
- [ ] Lernpfad: lernpfad-halbwertszeit.html
- [ ] AB: arbeitsblatt-halbwertszeit.tex
- [ ] Millimeterpapier für Zerfallskurve
- [ ] Klassenliste für Würfel-Dokumentation
