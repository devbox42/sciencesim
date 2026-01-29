# Workflow Learnings & Standards: Spanisch-Materialerstellung

**Stand:** Januar 2026
**Projekt:** Lernpfade

---

## 1. Lehrbuch-Zuordnung

| Klassenstufe | Lehrbuch | NP-Skala | Status |
|--------------|----------|----------|--------|
| Kl. 7-8 | ¿Qué pasa? 1 | 14-NP | verfügbar |
| Kl. 9 | ¿Qué pasa? 2 | 14-NP | kommt demnächst |
| Kl. 10 Spätbeginner | A_tope | **15-NP** | verfügbar |
| Kl. 11-12 Spätbeginner | A_tope | 15-NP | verfügbar |

**Wichtig:** Klasse 10 Spätbeginner verwendet 15-NP-Skala (wie Abiturstufe)!

---

## 1b. Referenz-Regeln (KRITISCH!)

```
SCHÜLERMATERIALIEN (AB, ML, LB, LP, TEST):
┌─────────────────────────────────────────────────────────────┐
│ ❌ KEINE Schulnamen (z.B. "XY-Schule")                       │
│ ❌ KEINE Lehrbuchnamen (z.B. "¿Qué pasa?", "A_tope")        │
│                                                             │
│ ✓ Stattdessen: "Lehrbuch" oder "Lehrbuch, Lektion X"        │
│ ✓ Oder: Keine Referenz, wenn nicht nötig                    │
└─────────────────────────────────────────────────────────────┘

LEHRERMATERIALIEN (LH, PPTX, README):
┌─────────────────────────────────────────────────────────────┐
│ ✓ Schulname erlaubt (XY-Schule)                             │
│ ✓ Lehrbuchnamen erlaubt (¿Qué pasa? 1, S. 78-85)            │
│ ✓ Detaillierte Seitenreferenzen                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 2. Standard-Dokumente (Materialpaket)

### Übersicht

```
MATERIALPAKET PRO UNTERRICHTSEINHEIT
════════════════════════════════════

PFLICHT (immer erstellen):
├── AB-xxx.pdf      Arbeitsblatt (Schüler)
├── ML-xxx.pdf      Musterlösung (Lehrer)
├── LB-xxx.pdf      Lernblatt (Offline-Input)
└── PPTX-xxx.pptx   Präsentation (Beamer)

DIGITAL (wenn Geräte verfügbar):
├── LP-xxx.html     Lernpfad (interaktiv)
└── TEST-xxx.html   Stundenleistung (online)

ZUSATZ:
├── LH-xxx.pdf      Lehrerhinweise
├── PLATZKARTEN.pdf QR + Notizfeld
├── QR-LERNPFAD.pdf Einzelblatt QR
└── QR-TEST.pdf     Einzelblatt QR

ORDNER:
└── LEHRER-MATERIALIEN/
    ├── README.md   Quick Reference
    └── [alle PDFs + PPTX]
```

### Kürzel-Legende

| Kürzel | Name | Zweck |
|--------|------|-------|
| **AB** | Arbeitsblatt | Aufgaben für Schüler (Hefter) |
| **ML** | Musterlösung | AB mit Lösungen (rot) |
| **LB** | Lernblatt | Offline-Input, ersetzt Lehrbuch |
| **LP** | Lernpfad | Interaktiver digitaler Lernpfad |
| **TEST** | Stundenleistung | Online-Prüfung |
| **PPTX** | Präsentation | Beamer-Folien |
| **LH** | Lehrerhinweise | Stundenverlauf + Tipps |
| **PLATZ** | Platzkarten | QR + Notizfeld |

---

## 3. Dokument-Spezifikationen

### AB (Arbeitsblatt)

```
FORMAT: A4, 1-2 Seiten, LaTeX → PDF
SCHRIFT: Serifenlos (Helvetica), 11pt
FARBE: Fachfarbe für Überschriften, sonst S/W-druckbar

STRUKTUR:
┌─────────────────────────────────────────────────────────────┐
│ Header: Fach Kl. X | Arbeitsblatt | Seite X/Y               │
├─────────────────────────────────────────────────────────────┤
│ Titel: Arbeitsblatt: [Thema]                                │
│ Kopfzeile: Name ___ | Klasse ___ | Datum ___                │
├─────────────────────────────────────────────────────────────┤
│ Aufgabe 1: [Titel]                             [_/X Punkte] │
│ Instruktion + Aufgabeninhalt                                │
│ ...                                                         │
│ Aufgabe N: [Titel]                             [_/X Punkte] │
├─────────────────────────────────────────────────────────────┤
│ Merkkasten (wenn Input nötig)                               │
├─────────────────────────────────────────────────────────────┤
│ ─────────────────────────────────────────                   │
│ Punkte: ___/[MAX]                                           │
├─────────────────────────────────────────────────────────────┤
│ Extension Tasks (★★★) - Für Schnelle [unbewertet]           │
│ E1: ... (+X BE)  E2: ... (+X BE)  E3: ...  E4: ...          │
└─────────────────────────────────────────────────────────────┘

AUFGABENTYPEN:
• Zuordnung: Linien zeichnen (KEIN A/B/C, nur Platz)
• Lückentext: \luecke{Xcm}
• Konjugation: Tabelle mit Lücken
• Dialog: Zeilen ergänzen
• Freies Schreiben: Linien

EXTENSION: Min. 4 Aufgaben, ~10-15 BE, UNBEWERTET
PUNKTE: Basis 25-35 BE (45min), 40-50 BE (90min)
```

### ML (Musterlösung)

```
FORMAT: Identisch mit AB

UNTERSCHIEDE:
• Header: "MUSTERLÖSUNG" in Rot
• Lösungen in Rot: \lsg{...}
• Punkte ausgefüllt
• NP-Skala am Ende

NP-SKALEN:
┌─────────────────────────────────────────────────────────────┐
│ 14-NP: Klasse 5-9 (normale Klassen)                         │
│ 15-NP: Klasse 10-12 Spätbeginner + Sek II                   │
└─────────────────────────────────────────────────────────────┘
```

### LB (Lernblatt) — Best-Practice-Design

```
ZWECK:
• Offline-Ersatz für Lehrwerk
• Alternative zum digitalen Lernpfad
• Enthält alle Inputs für AB-Bearbeitung
• Kann später zu Buch kompiliert werden

FORMAT: A4, 2 Seiten (Doppelseite), LaTeX → PDF
SCHRIFT: Helvetica (Sans-Serif) primär, Palatino (Serif) für ES-Vokabeln
FARBE: Konservativ, NUR didaktisch begründet

QUELLEN (Best Practice Research):
• Zeka Design: Typography in Learning Materials
• Pomona College: Visual Hierarchy for Effective Learning
• ERIC: Visual Aids in Vocabulary Acquisition
• Colorín Colorado: Using Visuals for ELL

DESIGN-PRINZIPIEN (Best Practice):
┌─────────────────────────────────────────────────────────────┐
│ TYPOGRAFIE (Dual-Font-System):                              │
│ • Fließtext: Sans-Serif (Helvetica) - modern, lesbar        │
│ • Spanisch: Serif (Palatino) + fett → visuelle Distinktion  │
│ • Deutsch: Sans-Serif kursiv, grau - dezent                 │
│ • Grammatikbegriffe: \gram{...} → KAPITÄLCHEN               │
│                                                             │
│ BOX-HIERARCHIE (minimal, kein "visual noise"):              │
│ • Lernzielbox: Grauer Hintergrund, KEIN Rahmen              │
│ • Grammatikbox: Nur linke Linie (3pt) - Einzug              │
│ • Merkbox: Grauer Hintergrund + obere Linie                 │
│ • KEINE vollständigen Rahmen um Textblöcke!                 │
│                                                             │
│ FARBE (didaktisch begründet = ERWÜNSCHT!):                  │
│ • Farbmuster bei Farbvokabeln (quadratisch, 8pt)            │
│ • Rot für "unregelmäßig"-Markierung (Zahlenstrahl)          │
│ • ROT für Stammwechsel: qu[ie]ro, p[ue]do (EXZELLENT!)      │
│ • Blau im Beispieldialog ("jersey azul")                    │
│ • Grau für dezente Elemente (DE-Text, Verweise)             │
│                                                             │
│ FARBPRINZIP bei Grammatik:                                  │
│ • Stammwechsel (e→ie, o→ue) IMMER farbig hervorheben        │
│ • Unregelmäßige Formen farbig markieren                     │
│ • Endungen bei Genus-Anpassung ggf. unterstreichen          │
│ • Farbe hier EXPLIZIT erwünscht (nicht "visual noise")      │
│                                                             │
│ VISUALS (konservativ):                                      │
│ • TikZ NUR für einfache Grafiken (Zahlenstrahl, Farbmuster) │
│ • KEINE automatischen Bild-Downloads                        │
│ • Bilder nur nach expliziter Recherche-Empfehlung           │
│ • Bei Bedarf: User nach Bildwunsch fragen                   │
└─────────────────────────────────────────────────────────────┘

STRUKTUR (Lehrbuch-Stil):
┌─────────────────────────────────────────────────────────────┐
│ Lektion X: [Spanischer Titel]                               │
│ [Deutscher Untertitel]                                      │
├─────────────────────────────────────────────────────────────┤
│ [Motivierender Einleitungstext, 2-3 Sätze]                  │
│ "Stell dir vor, du bist in Madrid..."                       │
├─────────────────────────────────────────────────────────────┤
│ ┌─────────────────────────────────────────────────────────┐ │
│ │ Das lernst du:                                          │ │
│ │ • Lernziel 1  • Lernziel 2  • Lernziel 3  • Lernziel 4  │ │
│ └─────────────────────────────────────────────────────────┘ │
├─────────────────────────────────────────────────────────────┤
│ 1. [Spanisch] -- [Deutsch]                                  │
│ [Erklärender Fließtext]                                     │
│ ┌────────────────────┐                                      │
│ │ Vokabelbox         │                                      │
│ │ fett = ES, kursiv = DE │                                  │
│ └────────────────────┘                                      │
│ ┌ Tippbox ─────────────────────────────────────────────────┐│
│ │ Tipp: Merkhilfe...                                       ││
│ └──────────────────────────────────────────────────────────┘│
│ → AB Aufgabe 1                                              │
├─────────────────────────────────────────────────────────────┤
│ [Weitere nummerierte Abschnitte...]                         │
└─────────────────────────────────────────────────────────────┘

KOPF-/FUSSZEILE:
• Links: SPANISCH | Klasse X (Kapitälchen)
• Rechts: Thema (z.B. "De compras") -- KEINE Lektionsnummer!
• Mitte unten: Seite X/Y
• KEINE Lehrbuch-/Schulreferenzen!

REFERENZEN:
• AB-Verweise: "→ AB X" (LINKSBÜNDIG nach jedem Abschnitt)
• Keine Lehrbuch-Verweise auf Schülermaterialien

BUCHKOMPILATION (für spätere Zusammenstellung):
• Lektionsnummer im Header
• Einheitliche Ränder (1.8cm)
• Zentrale Seitennummern
• Konsistente Box-Definitionen (in Preamble)

LaTeX-BEFEHLE (Preamble):
% Dual-Font-System
\usepackage{helvet}
\renewcommand{\familydefault}{\sfdefault}
\usepackage{palatino}
\newcommand{\seriftext}[1]{{\fontfamily{ppl}\selectfont #1}}

% Spanisch: Serif + fett (visuelle Distinktion)
\newcommand{\es}[1]{\seriftext{\textbf{#1}}}
% Deutsch: Sans-Serif kursiv, grau
\newcommand{\de}[1]{\textit{\textcolor{akzent}{#1}}}
% Grammatik: Kapitälchen
\newcommand{\gram}[1]{\textsc{#1}}
% AB-Verweis: dezent, LINKSBÜNDIG
\newcommand{\abmark}[1]{{\footnotesize\textcolor{akzent}{$\rightarrow$ AB #1}}}
% Farbmuster (für Farbvokabeln)
\newcommand{\farbmuster}[1]{\tikz[baseline=-0.5ex]\fill[#1] (0,0) rectangle (8pt,8pt);}

BOX-DEFINITIONEN (minimal, kein visual noise):
% Lernziel-Box: Grauer Hintergrund, KEIN Rahmen
\newtcolorbox{lernzielbox}{
    colback=hellgrau, colframe=hellgrau, boxrule=0pt, arc=0pt,
    left=10pt, right=10pt, top=8pt, bottom=8pt
}
% Grammatik-Box: Nur linke Linie
\newtcolorbox{grammatikbox}[1][]{
    colback=white, colframe=white, boxrule=0pt, arc=0pt,
    left=10pt, right=6pt, top=6pt, bottom=6pt,
    borderline west={3pt}{0pt}{akzent}
}
% Merksatz-Box: Grauer Hintergrund + obere Linie
\newtcolorbox{merkbox}[1][]{
    colback=hellgrau, colframe=hellgrau, boxrule=0pt, arc=0pt,
    left=10pt, right=10pt, top=8pt, bottom=8pt,
    borderline north={2pt}{0pt}{colornegro}
}

INHALTLICHE QUALITÄT:
• Seiten sinnvoll füllen (nicht künstlich strecken)
• Fun Facts / ¿Sabías que? einbauen (Motivation!)
• Etymologie erklären (z.B. warum quinientos statt cincocientos)
• Kulturelle Hinweise (z.B. Rebajas, ¿Me cobra?)
• Eselsbrücken / Merksätze anbieten
• KEINE leeren Seiten am Ende!

SCORE-ZIEL: ≥ 9.8/10
```

### LP (Lernpfad)

```
FORMAT: Single-file HTML, ES5-kompatibel (kein let/const/=>)
RESPONSIVE: Mobile-first, Tablet-optimiert

STRUKTUR:
┌─────────────────────────────────────────────────────────────┐
│ HEADER                                                      │
│ • Titel + Thema                                             │
│ • Fortschrittsbalken                                        │
│ • Punkte: X/Y                                               │
├─────────────────────────────────────────────────────────────┤
│ NAVIGATION                                                  │
│ • Abschnitte als Tabs/Accordion                             │
│ • Visueller Status (✓ erledigt / ● aktiv / ○ offen)         │
├─────────────────────────────────────────────────────────────┤
│ CONTENT                                                     │
│ • Input (Text, Tabellen, Beispiele)                         │
│ • Interaktive Übungen mit Sofort-Feedback                   │
│ • Hefter-Hinweise: "→ AB Aufgabe X"                         │
├─────────────────────────────────────────────────────────────┤
│ FOOTER                                                      │
│ • Weiter/Zurück-Buttons                                     │
│ • Reset-Button (mit Bestätigung)                            │
└─────────────────────────────────────────────────────────────┘

FEATURES:
• localStorage-Persistenz (LP_[ID]_ Präfix)
• Fuzzy-Matching: norm() entfernt Akzente, normalisiert Leerzeichen
• Feldweise Feedback: .field-ok (grün), .field-wrong (rot)
• Akzeptierte Varianten in Arrays (z.B. ["blanca", "blanco"])

FARBEN:
• Fachfarbe: Header, Akzente
• Grün #2a7a4b: korrekt
• Rot #c62828: falsch
• Hellgrau #f5f5f5: Boxen
```

### TEST (Stundenleistung)

```
FORMAT: Single-file HTML, ES5-kompatibel

STRUKTUR:
┌─────────────────────────────────────────────────────────────┐
│ HEADER                                                      │
│ • "Stundenleistung: [Thema]"                                │
│ • Klasse, Datum                                             │
│ • Namensfeld (PFLICHT vor Start)                            │
├─────────────────────────────────────────────────────────────┤
│ AUFGABEN                                                    │
│ • Nummeriert mit Punktangabe                                │
│ • KEIN Sofort-Feedback während Test                         │
├─────────────────────────────────────────────────────────────┤
│ ABGABE                                                      │
│ • "Test abgeben"-Button                                     │
│ • Bestätigung erforderlich                                  │
├─────────────────────────────────────────────────────────────┤
│ ERGEBNIS (nach Abgabe)                                      │
│ • Punkte: X/Y                                               │
│ • Notenpunkte (14-NP oder 15-NP)                            │
│ • Korrektur sichtbar                                        │
├─────────────────────────────────────────────────────────────┤
│ ⚠️ EXPORT-HINWEIS (PFLICHT, prominent!)                     │
│ ┌─────────────────────────────────────────────────────────┐ │
│ │ WICHTIG: Exportiere dein Ergebnis als PDF!              │ │
│ │ 1. Drücke Strg+P (oder Cmd+P auf Mac)                   │ │
│ │ 2. Wähle "Als PDF speichern"                            │ │
│ │ 3. Lade das PDF in der Bildungscloud hoch               │ │
│ │                                                         │ │
│ │ [PDF exportieren] ← Button öffnet Druckdialog           │ │
│ └─────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘

LEHRER-FEATURES:
• PIN-Reset: Standard 2024
• localStorage: TEST_[ID]_ Präfix
• Automatische Auswertung mit Fuzzy-Matching
```

### PPTX (Präsentation)

```
FORMAT: PowerPoint, 16:9 (10" × 5.625"), python-pptx generiert

FOLIEN-STRUKTUR:
┌─────────────────────────────────────────────────────────────┐
│ 1. TITELFOLIE                                               │
│    • Thema (groß, Fachfarbe)                                │
│    • Untertitel (Inhalte)                                   │
│    • Klasse + Fach                                          │
├─────────────────────────────────────────────────────────────┤
│ 2. EINSTIEG / WARM-UP                                       │
│    • Aktivierung (Spiel, Rätsel, Schätzfrage)               │
│    • Spanische Motivation                                   │
├─────────────────────────────────────────────────────────────┤
│ 3-N. PRO AB-AUFGABE (Dreier-Block):                         │
│                                                             │
│    A) INPUT-FOLIE                                           │
│       Header: "[Thema] | [Buch] S.XX / LB Kasten X"         │
│       • Vokabeln / Grammatik / Redemittel                   │
│       • Max. 8-10 Zeilen                                    │
│                                                             │
│    B) AUFGABEN-FOLIE                                        │
│       Header: "Aufgabe X: [Titel] | AB • X Punkte"          │
│       • Instruktion (1-2 Sätze)                             │
│       • Tipps                                               │
│       • Zeit ("Du hast X Minuten")                          │
│       • Motivation (¡Vamos! etc.)                           │
│       • KEINE Lösungen!                                     │
│                                                             │
│    C) LÖSUNGS-FOLIE                                         │
│       Header: "Aufgabe X: [Titel] | Lösung"                 │
│       Badge: "LÖSUNG" (grün, oben rechts)                   │
│       • Alle korrekten Antworten in Grün                    │
├─────────────────────────────────────────────────────────────┤
│ N+1. EXTENSION AUFGABEN                                     │
│      Header: "Extension (★★★) | Für Schnelle"               │
├─────────────────────────────────────────────────────────────┤
│ N+2. EXTENSION LÖSUNGEN                                     │
│      Mit grünem Badge                                       │
├─────────────────────────────────────────────────────────────┤
│ N+3. ZUSAMMENFASSUNG                                        │
│      "Das hast du heute gelernt:"                           │
│      • Vokabeln • Grammatik • Kommunikation                 │
├─────────────────────────────────────────────────────────────┤
│ N+4. BEWERTUNG (für Lehrkraft)                              │
│      • BE-Verteilung                                        │
│      • Extension (unbewertet)                               │
│      • NP-Skala                                             │
└─────────────────────────────────────────────────────────────┘

DESIGN:
• Header: 1.1" hoch, Fachfarbe ausgefüllt
• Titel: 32pt weiß fett
• Body: 18pt dunkelgrau
• Spanisch: Fachfarbe
• Lösungen: Grün #2a7a4b
• Badge: Abgerundetes Rechteck

REFERENZEN (PFLICHT auf Input-Folien):
• Lehrbuch: "[Buch] S. XX"
• Lernblatt: "LB Kasten X"
• Beide Quellen angeben!

SPRACHE:
• Du-Form
• Imperativ ("Verbinde", "Schreibe")
• Spanische Motivationsphrasen

MOTIVATIONS-POOL:
¡Vamos! ¡Adelante! ¡Mucha suerte! ¡Buena suerte!
¡Inténtalo! ¡Es fácil! ¡Muy bien! ¡Perfecto!
```

### LH (Lehrerhinweise)

```
FORMAT: A4, 2-4 Seiten, LaTeX → PDF

⚠️ DESIGN: DEZENT!
• KEINE voll ausgefüllten Header
• NUR farbige Rahmen (Pastelltöne)
• Fachfarbe nur als Akzent/Linie
• Hauptsächlich schwarz/grau

STRUKTUR:
┌─────────────────────────────────────────────────────────────┐
│ 1. ÜBERBLICK                                                │
│    • Thema, Klasse, Dauer                                   │
│    • Lernziele (Rahmenplan-Bezug)                           │
│    • Materialien                                            │
├─────────────────────────────────────────────────────────────┤
│ 2. STUNDENVERLAUF                                           │
│    Tabelle: Zeit | Phase | Inhalt | Sozialform | Material   │
│    5-Minuten-Raster                                         │
├─────────────────────────────────────────────────────────────┤
│ 3. DIFFERENZIERUNG                                          │
│    • ★ Basisniveau                                          │
│    • ★★ Mittleres Niveau                                    │
│    • ★★★ Erweitertes Niveau                                 │
├─────────────────────────────────────────────────────────────┤
│ 4. HÄUFIGE FEHLER                                           │
│    • Typische Schülerfehler                                 │
│    • Reaktionen/Hilfestellungen                             │
├─────────────────────────────────────────────────────────────┤
│ 5. LÖSUNGEN (Kurzform)                                      │
│    Alle AB-Lösungen kompakt                                 │
└─────────────────────────────────────────────────────────────┘

FARBEN (dezent):
• Rahmen: Pastellversion der Fachfarbe
• Text: Schwarz/Dunkelgrau
• Überschriften: Fachfarbe (nur Text, kein Hintergrund)
```

### PLATZKARTEN

```
FORMAT: A4, 12 Karten/Seite (2 Seiten = 24 Karten)

EINZELNE KARTE:
┌─────────────────────────────────────────┐
│ [Thema]              [QR-Code]          │
│ Klasse: ___                             │
│ Name: _____________                     │
│ Punkte: ___/___ | NP: ___               │
└─────────────────────────────────────────┘

WORKFLOW:
1. Karte verteilen
2. Schüler scannt QR → macht Test
3. Schüler zeigt Ergebnis + exportiert PDF
4. Lehrer notiert Punkte/NP auf Karte
5. Karte einsammeln → Papiernachweis
```

### QR-Einzelblätter

```
FORMAT: A4, 1 Seite

VARIANTEN:
• QR-LERNPFAD.pdf
• QR-TEST.pdf

LAYOUT:
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│              [GROSSER QR-CODE]                              │
│                 (ca. 12cm)                                  │
│                                                             │
│           [Thema] - [Typ]                                   │
│                                                             │
│              [URL als Text]                                 │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 4. Erkannte Probleme & Learnings

### Buchreferenzen
**Problem:** Seitenangaben waren NICHT verifiziert
**Lösung:**
- Buchreferenzen MÜSSEN aus `knowledge/` stammen
- Wenn unsicher: Platzhalter `[Buch S. ???]`
- Verifizierung als separater Workflow-Schritt

### Extension Tasks
**Problem:** Nur 2 Aufgaben
**Lösung:**
- Minimum 4-5 Extension Tasks
- Verschiedene Typen: Rechnen, Schreiben, Transfer, Kreativ
- ~10-15 BE zusätzlich
- UNBEWERTET (weder Note noch Bonus)

### Matching-Aufgaben
**Problem:** Buchstaben-Zuordnung statt Linien
**Lösung:**
- Platz für Linien: `\hspace{1.8cm}`
- KEINE Buchstaben (A, B, C)
- KEINE Einsetzstriche

### PPTX Lösungen
**Problem:** Lösungen auf gleicher Folie wie Aufgabe
**Lösung:**
- Lösungen IMMER auf separater Folgefolie
- Grünes "LÖSUNG"-Badge

### Test-Export
**Problem:** Kein Hinweis zur PDF-Abgabe
**Lösung:**
- Prominenter Export-Hinweis nach Abgabe
- Button für Druckdialog
- Anleitung für Bildungscloud-Upload

---

## 5. Workflow: Stundenerstellung

### Phase 1: Vorbereitung
```
□ Thema aus Sequenzplan identifizieren
□ Lehrbuch-Seiten in knowledge/ prüfen
□ Lernziele aus Rahmenplan notieren
□ Zeitrahmen festlegen (45/90 Min)
```

### Phase 2: Basis-Materialien
```
□ AB erstellen
  □ 6-8 Aufgaben (Basis)
  □ Merkkasten wenn nötig
  □ Extension Tasks (min. 4)
  □ Punkteverteilung prüfen

□ ML erstellen
  □ AB kopieren
  □ Lösungen einfügen (rot)
  □ NP-Skala hinzufügen (14 oder 15)

□ LB erstellen
  □ Vokabelkästen mit Bildern
  □ Grammatik-Tabellen
  □ Redemittel
  □ AB-Verweise
  □ Buchseiten-Referenzen (VERIFIZIERT!)
  □ Score prüfen (≥ 9.8)
```

### Phase 3: Präsentation
```
□ PPTX erstellen
  □ Titelfolie
  □ Einstieg/Warm-up
  □ Pro Aufgabe: Input → Aufgabe → Lösung
  □ Referenzen: Buch UND LB auf Input-Folien
  □ Extension + Lösungen
  □ Zusammenfassung
  □ Bewertungsfolie

□ Validierung
  □ Buchreferenzen verifiziert?
  □ Lösungen NIE auf Aufgaben-Folie?
  □ Grünes Badge auf allen Lösungs-Folien?
  □ Zeitangaben bei allen Aufgaben?
  □ Spanische Motivation vorhanden?
```

### Phase 4: Digital (optional)
```
□ LP erstellen
  □ Alle AB-Aufgaben abgedeckt
  □ Sofort-Feedback implementiert
  □ localStorage-Persistenz
  □ Hefter-Hinweise

□ TEST erstellen
  □ Aufgaben ohne Feedback
  □ Abgabe-Bestätigung
  □ Ergebnisanzeige
  □ ⚠️ PDF-Export-Hinweis (PFLICHT!)
  □ Bildungscloud-Anleitung
  □ PIN-Reset (2024)
```

### Phase 5: Zusatzmaterialien
```
□ LH erstellen
  □ Stundenverlauf (5-Min-Raster)
  □ Differenzierung
  □ Häufige Fehler
  □ Kurzlösungen
  □ DESIGN: Dezent, nur Rahmen!

□ PLATZKARTEN erstellen
  □ QR zum Test
  □ Notizfelder

□ QR-Einzelblätter
  □ QR-LERNPFAD.pdf
  □ QR-TEST.pdf
```

### Phase 6: Finalisierung
```
□ Alle PDFs kompilieren
□ LEHRER-MATERIALIEN/ Ordner erstellen
□ README.md mit Quick Reference

□ STIMMIGKEITSPRÜFUNG (PFLICHT!):
  ┌─────────────────────────────────────────────────────────────┐
  │ LB und LP müssen BEIDE in AB münden!                        │
  │                                                             │
  │ 1. LEHRBUCH-ABGLEICH (knowledge/*.txt lesen!):              │
  │    • Entsprechende Lektion im Volltext prüfen               │
  │    • Vokabeln mit Lehrbuch abgleichen                       │
  │    • Grammatik-Erklärungen verifizieren                     │
  │    • Keine erfundenen Inhalte!                              │
  │                                                             │
  │ 2. Prüfe für JEDE AB-Aufgabe:                               │
  │    • Hat LB den passenden Input? (Vokabeln, Grammatik)      │
  │    • Hat LB einen "→ AB X" Verweis?                         │
  │    • Hat LP den passenden Input + Übung?                    │
  │    • Sind Vokabeln/Phrasen IDENTISCH? (keine Abweichungen!) │
  │                                                             │
  │ Beispiel-Check für AB Aufgabe 3 (Modalverben):              │
  │ ✓ Lehrbuch-TXT: Konjugation geprüft                         │
  │ ✓ LB: Konjugationstabelle querer/poder/tener que            │
  │ ✓ LB: "→ AB 3" Verweis vorhanden                            │
  │ ✓ LP: Gleiche Tabelle + interaktive Übung                   │
  │ ✓ Alle Formen identisch (quiero, puedo, tengo que...)       │
  └─────────────────────────────────────────────────────────────┘

□ Selbsttest: Alle Dokumente konsistent?
  □ Punktzahlen stimmen überein?
  □ Aufgabennummern konsistent?
  □ Lösungen korrekt?
  □ Referenzen verifiziert?
  □ LB ↔ AB Alignment geprüft?
  □ LP ↔ AB Alignment geprüft?
```

---

## 6. Validierungs-Checkliste (Selbsttest)

### AB
- [ ] Alle Aufgaben nummeriert mit Punkten
- [ ] Summe = maxpunkte Variable
- [ ] Extension Tasks vorhanden (min. 4)
- [ ] Merkkasten wenn nötig
- [ ] S/W-druckbar

### ML
- [ ] Identisches Layout wie AB
- [ ] Alle Lösungen in Rot
- [ ] Punkte ausgefüllt
- [ ] NP-Skala korrekt (14 oder 15)

### LB
- [ ] Alle AB-Inputs vorhanden
- [ ] AB-Verweise korrekt (LINKSBÜNDIG)
- [ ] Header: Thema statt Lektionsnummer
- [ ] KEINE Lehrbuch-/Schulreferenzen
- [ ] Seiten sinnvoll gefüllt (Fun Facts, Etymologie, Kultur)
- [ ] Stammwechsel/Unregelmäßiges FARBIG hervorgehoben
- [ ] Bilder nur wenn vom User gewünscht
- [ ] Score ≥ 9.8

### LP
- [ ] Alle AB-Aufgaben abgedeckt
- [ ] Fuzzy-Matching implementiert
- [ ] localStorage funktioniert
- [ ] Punkte-Summe korrekt

### TEST
- [ ] Name-Pflichtfeld
- [ ] Kein Feedback während Test
- [ ] Ergebnis nach Abgabe
- [ ] ⚠️ PDF-Export-Hinweis vorhanden
- [ ] Bildungscloud-Anleitung
- [ ] PIN-Reset funktioniert

### PPTX
- [ ] Jede AB-Aufgabe: Input + Aufgabe + Lösung
- [ ] Referenzen: Buch + LB
- [ ] Lösungen auf separater Folie
- [ ] Grünes Badge auf Lösungsfolien
- [ ] Zeitangaben vorhanden
- [ ] Spanische Motivation
- [ ] Extension vorhanden
- [ ] Bewertungsfolie korrekt

### LH
- [ ] Design dezent (nur Rahmen)
- [ ] Stundenverlauf vollständig
- [ ] Differenzierung beschrieben
- [ ] Lösungen enthalten

### Ordner
- [ ] LEHRER-MATERIALIEN/ existiert
- [ ] README.md vorhanden
- [ ] Alle PDFs kopiert
- [ ] PPTX kopiert

### STIMMIGKEIT (PFLICHT am Ende!)
- [ ] LB → AB: Jede AB-Aufgabe hat Input im LB
- [ ] LB → AB: "→ AB X" Verweise vollständig
- [ ] LP → AB: Jede AB-Aufgabe hat Input + Übung im LP
- [ ] Vokabeln/Phrasen IDENTISCH in LB, LP, AB
- [ ] Grammatik-Tabellen IDENTISCH (gleiche Formen)
- [ ] LEHRBUCH-ABGLEICH: Volltext (knowledge/*.txt) geprüft
      → Vokabeln stimmen mit Lehrbuch überein?
      → Grammatik-Erklärungen konsistent?
      → Keine erfundenen Inhalte?

---

## 7. Bilder & Lizenzen

### ⚠️ KEINE automatische Bildersuche!
```
WORKFLOW FÜR BILDER:
┌─────────────────────────────────────────────────────────────┐
│ 1. Standardmäßig: KEINE Bilder in LB/AB einfügen            │
│ 2. TikZ nur für einfache Grafiken (Zahlenstrahl, Farbmuster)│
│ 3. Falls Bild didaktisch sinnvoll:                          │
│    → User fragen: "Soll ich passende Bilder recherchieren?" │
│ 4. User entscheidet über Bildintegration                    │
└─────────────────────────────────────────────────────────────┘
```

### Erlaubte Quellen (falls Bilder gewünscht)
| Quelle | Lizenz | Verwendung |
|--------|--------|------------|
| Wikimedia Commons | CC-BY-SA, Public Domain | ✅ |
| Wikipedia | CC-BY-SA | ✅ |
| Pixabay | Pixabay License | ✅ (prüfen) |
| Public Domain Vectors | Public Domain | ✅ |

### Verboten
- Stock-Fotos mit unklarer Lizenz
- Bilder aus Lehrbüchern (Copyright)
- Google-Bildersuche ohne Lizenzprüfung
- Automatisches Herunterladen ohne User-Zustimmung

### Quellenangabe (falls Bilder verwendet)
Bei jedem Bild im LB:
```latex
\footnotesize{Quelle: Wikimedia Commons, CC-BY-SA}
```

---

## 8. Farbschema

### Fachfarben
| Fach | Farbe | Hex |
|------|-------|-----|
| Spanisch | Karminrot | #c41e3a |
| Physik | Blau | #2c5aa0 |
| Chemie | Grün | #2a7a4b |
| Informatik | Orange | #b35c00 |

### Feedback-Farben
| Bedeutung | Farbe | Hex |
|-----------|-------|-----|
| Korrekt | Grün | #2a7a4b |
| Falsch | Rot | #c62828 |
| Warnung | Orange | #b35c00 |

### LH-Pastelltöne (dezent!)
| Fach | Rahmenfarbe | Hex |
|------|-------------|-----|
| Spanisch | Helles Rosa | #f8d7da |
| Physik | Helles Blau | #d1e7ff |
| Chemie | Helles Grün | #d4edda |

---

*Zuletzt aktualisiert: Januar 2026*
