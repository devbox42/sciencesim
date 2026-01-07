# Workflow: Spanisch-Materialien

**Version:** 2.8 (2026-01-05)
**Für:** Klasse 7-9 (regulär) | Klasse 10-12 (Spätbeginner)

---

## 0. Grundkonfiguration

### Stundenkontingent

| Klassenstufe | WStd | Format | DS/Woche |
|--------------|------|--------|----------|
| **7-9 (regulär)** | **4** | 2×90 Min | **2** |
| 10-12 (Spätbeginner) | 4 | 2×90 Min | 2 |

### Lehrwerk-Zuordnung

| Klassenstufe | Lehrwerk | Referenz-Datei |
|--------------|----------|----------------|
| **7-8** | **Qué pasa 1** | `knowledge/Spanisch-Que-Pasa-1/que-pasa-1-referenz.md` |
| **9** | **Qué pasa 2** | `knowledge/Spanish-Que-Pasa-2/` |
| 10-12 | A_tope.com | `knowledge/Spanisch-A_tope_Spaetbeginner/` |

### Planungs-Modi

| Modus | Format | Tokens | Score | Wann verwenden |
|-------|--------|--------|-------|----------------|
| **KOMPAKT** | Planungsnotiz (.md) | ~250 | **≥9.5** | **DEFAULT** – Regulärer Unterricht |
| Tier 1 | Langentwurf (.tex) | ~2500 | ≥9.0 | Unterrichtsbesuche, Dokumentation |
| Tier 2 | Langentwurf (.tex) | ~800 | — | Formale Anforderung |
| Tier 3 | Langentwurf (.tex) | ~500 | — | Minimale Dokumentation |

**KOMPAKT ist Default.** Tier 1-3 nur bei expliziter Anfrage ("erstelle einen Langentwurf").

**Score-Schwellen:**
- **KOMPAKT: ≥9.5** (strenger, da weniger Dokumentation → höhere Qualitätsanforderung)
- **Tier 1: ≥9.0** (vollständige Dokumentation kompensiert)

### Planungsnotiz-Format (KOMPAKT)

```markdown
# Planung: [Thema] (Kl. [X], DS [Y])

## Feinziele
- FZ1: [Verb] ... (AFB I)
- FZ2: [Verb] ... (AFB II)
- FZ3: [Verb] ... (AFB II/III)

## Voraussetzungen
[Was SuS bereits können]

## Neue Inhalte
- Vokabeln: [Liste, max. 15]
- Grammatik: [Struktur]
- Redemittel: [Phrasen]

## Verlauf (90 Min)
| Min | Phase | Aktivität | SF | Material |
|-----|-------|-----------|-----|----------|
| 10 | Einstieg | ... | PL | — |
| 25 | Erarbeitung | ... | EA | LB |
| 20 | Übung | ... | PA/GA | AB 1-2 |
| 25 | Anwendung | ... | PA | AB 3-4 |
| 10 | Sicherung | ... | PL | AB 5 |

## Differenzierung
- [B]: ...
- [S]: ...
- [E]: ...

## Output
AB ([X] BE), LB, LP, SLIDES
```

### Tier-System (nur bei expliziter Anfrage)

| Tier | Umfang | Seiten | Inhalt |
|------|--------|--------|--------|
| **Tier 1** | Vollständig | 8-12 | Bedingungsanalyse, Sachanalyse, Didaktik, Verlauf |
| **Tier 2** | Standard | 4-6 | Feinziele, Verlauf, Differenzierung |
| **Tier 3** | Minimal | 2-3 | Feinziele, Verlauf-Kurzform |

---

## 1. Materialerstellungs-Workflow

### Übersicht

```
PHASE 0: KONTEXTAUFNAHME
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    User-Input erfassen und strukturieren:
    ├─ A) VORWISSEN → Was wurde bereits unterrichtet?
    ├─ B) LERNZIELE → Was soll gelernt werden?
    ├─ C) AKTIVITÄTEN → Konkrete Vorstellungen?
    └─ D) KONTEXT → Besonderheiten, Einschränkungen?
        │
        ↓

PHASE 1: ANFRAGE + MODUS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    Pflichtangaben erfassen:
    ├─ Klassenstufe (7/8/9)
    ├─ Unidad/Thema
    └─ Position (DS X von Y)

    Modus bestimmen:
    ├─ DEFAULT: KOMPAKT (Planungsnotiz)
    └─ Bei "Langentwurf" / "LE" / "Tier X": Formaler LE
        │
        ↓

PHASE 2: PLANUNG
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    KOMPAKT-Modus (Default):
    ├─ Planungsnotiz erstellen (PLANUNG-xxx.md)
    ├─ Didaktik-Score ausgeben
    └─ FREIGABE bei Score ≥9.5

    ODER Tier 1-3 (bei Anfrage):
    ├─ Langentwurf erstellen (LE-xxx.tex)
    ├─ Didaktik-Score (nur Tier 1)
    └─ FREIGABE bei Score ≥9.0
        │
        ↓

PHASE 3: CONTENT-MATERIALIEN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    Stufe 3.1: AB (zuerst!)
    Stufe 3.2: LB, LP, SLIDES (parallel)
    Stufe 3.3: ML, LH, MT (parallel)
        │
        ↓

PHASE 4: KOMPILIERUNG & PRÜFUNG
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    pdflatex für alle .tex
    Seitenlimits prüfen
    Checklisten durchgehen
```

---

## 1a. Phase 0: Kontextaufnahme (Detail)

### Zweck

User-Input erfassen und in LE-Struktur überführen, bevor Materialien erstellt werden.

### Die 4 Kontext-Kategorien

```
┌─────────────────────────────────────────────────────────────────┐
│  A) VORWISSEN                                                   │
│     "Ich habe bisher ... unterrichtet"                          │
│     "Die SuS können bereits ..."                                │
│     → Wird zu: Voraussetzungen im LE                            │
├─────────────────────────────────────────────────────────────────┤
│  B) LERNZIELE                                                   │
│     "Ich möchte ... einführen"                                  │
│     "Die SuS sollen lernen ..."                                 │
│     "Grammatik: ... / Wortfeld: ..."                            │
│     → Wird zu: Feinziele FZ1-FZ4 im LE                          │
├─────────────────────────────────────────────────────────────────┤
│  C) AKTIVITÄTEN                                                 │
│     "Ich stelle mir vor ..."                                    │
│     "Ich möchte eine Rallye / ein Spiel / einen Dialog ..."     │
│     "Die SuS sollen ... machen"                                 │
│     → Wird zu: Verlaufsphasen im LE                             │
├─────────────────────────────────────────────────────────────────┤
│  D) KONTEXT                                                     │
│     "Besonderheit: ..."                                         │
│     "Ich habe nur 45 Min / Die Klasse ist unruhig / ..."        │
│     "Kein Lehrwerk / Anderes Lehrwerk / ..."                    │
│     → Wird zu: Didaktische Hinweise im LE                       │
└─────────────────────────────────────────────────────────────────┘
```

### Mapping: User-Input → LE-Element

| User sagt... | Kategorie | Wird im LE zu... |
|--------------|-----------|------------------|
| "Ich habe ser/estar gemacht" | A) Vorwissen | `\voraussetzungen{ser, estar bekannt}` |
| "Jetzt möchte ich hay einführen" | B) Lernziel | `FZ1: SuS verwenden hay korrekt (AFB I)` |
| "SuS sollen Klassenraum beschreiben" | B) Lernziel | `FZ2: SuS beschreiben Räume (AFB II)` |
| "Ich stelle mir eine Rallye vor" | C) Aktivität | Erarbeitungsphase: Rallye-Aktivität |
| "Gruppenarbeit bevorzugt" | C) Aktivität | Sozialform: GA in Verlaufsplan |
| "Nur 45 Minuten" | D) Kontext | Zeitplanung anpassen, Tier 3 empfehlen |
| "Klasse ist unruhig" | D) Kontext | Mehr Struktur, kürzere Phasen |
| "Kein Lehrwerk" | D) Kontext | Eigenständige Vokabeln/Grammatik |

### Verarbeitung im LE

**Beispiel-Anfrage:**
> "Ich habe ser/estar gemacht. Jetzt möchte ich hay einführen.
> Die SuS sollen ihr Klassenzimmer beschreiben.
> Ich stelle mir eine Rallye durch den Klassenraum vor."

**Extrahierter Kontext:**

| Kategorie | Extrahiert | LE-Element |
|-----------|------------|------------|
| A) Vorwissen | ser, estar | Voraussetzungen |
| B) Lernziel 1 | hay einführen | FZ1: hay verwenden (AFB I) |
| B) Lernziel 2 | Klassenraum beschreiben | FZ2: Räume beschreiben (AFB II) |
| C) Aktivität | Rallye | Erarbeitung: Klassenraum-Rallye |

**Resultat im LE:**

```latex
\section{Voraussetzungen}
Die SuS kennen bereits: ser, estar (aus vorherigen Stunden)

\section{Feinziele}
\begin{itemize}
    \item[\textbf{FZ1}] SuS \textbf{verwenden} hay korrekt in Sätzen (AFB I)
    \item[\textbf{FZ2}] SuS \textbf{beschreiben} ihren Klassenraum (AFB II)
\end{itemize}

\section{Verlauf}
\begin{tabular}{|p{2cm}|p{8cm}|p{2cm}|}
\hline
\textbf{Phase} & \textbf{Aktivität} & \textbf{SF} \\
\hline
Erarbeitung & \textbf{Klassenraum-Rallye:} SuS gehen durch
               den Raum und notieren "Hay un/una..." & GA \\
\hline
\end{tabular}
```

### Fallback: Kein User-Kontext

Wenn User nur sagt: "Erstelle Material für Unidad 2"

```
A) Vorwissen:   → Aus Lehrwerksreferenz ableiten (Unidad 1)
B) Lernziele:   → Aus Lehrwerksreferenz übernehmen
C) Aktivitäten: → Standard-Aktivitäten (Input → Übung → Produktion)
D) Kontext:     → Defaults (90 Min, heterogene Klasse, Tablets)
```

### Rückfragen bei Unklarheit

Wenn Kontext unklar oder widersprüchlich:

```
User: "Ich möchte Pretérito machen"

Claude fragt nach:
├─ "Pretérito indefinido oder imperfecto?"
├─ "Was haben die SuS bereits gelernt?"
└─ "Gibt es eine konkrete Aktivität die du dir vorstellst?"
```

---

## 2. Material-Hierarchie: AB als Zentrum

### Kernprinzip

**Das AB (Arbeitsblatt) ist das zentrale Schülerdokument.**

Alle anderen Materialien führen durch das AB:

```
                    ┌─────────────────────────────────────────┐
                    │              AB                         │
                    │        (Arbeitsblatt)                   │
                    │                                         │
                    │   Das zentrale Schülerdokument          │
                    │         zum Abheften                    │
                    └─────────────────────────────────────────┘
                                      ↑
                    ┌─────────────────┼─────────────────┐
                    │                 │                 │
               ┌────┴────┐      ┌─────┴─────┐     ┌─────┴─────┐
               │   LB    │      │    LP     │     │  SLIDES   │
               │Lernblatt│      │ Lernpfad  │     │  Beamer   │
               └─────────┘      └───────────┘     └───────────┘
                    │                 │                 │
                    └─────────────────┴─────────────────┘
                                      │
                        ALLE FÜHREN DURCH AB
```

### Drei Unterrichtsszenarien

| Szenario | Führungsinstrument | Wann? |
|----------|-------------------|-------|
| **Analog** | **LB** führt durch AB | Kein Tablet, klassisch |
| **Digital** | **LP** führt durch AB | Schüler arbeiten selbstständig |
| **Frontal** | **SLIDES** führt durch AB | Lehrervortrag, gemeinsam |

**In allen Szenarien:** AB ist das Ergebnis, das im Hefter landet.

---

## 3. Abhängigkeiten und Erstellungsreihenfolge

### Abhängigkeitsgraph

```
                    ┌─────┐
                    │ LE  │  ← Basis für alles
                    └──┬──┘
                       │
                       ↓
                    ┌─────┐
                    │ AB  │  ← ZENTRAL (definiert Aufgaben-Struktur)
                    └──┬──┘
                       │
     ┌─────────────────┼─────────────────────────┐
     │                 │                         │
     ↓                 ↓                         ↓
  ┌─────┐          ┌─────┐                   ┌─────┐
  │ LB  │          │ LP  │                   │SLIDES│
  │→AB 1│          │→AB 1│                   │→AB 1│
  │→AB 2│          │→AB 2│                   │→AB 2│
  └─────┘          └─────┘                   └─────┘
     │                 │                         │
     └─────────────────┼─────────────────────────┘
                       │
     ┌─────────────────┼─────────────────┐
     ↓                 ↓                 ↓
  ┌─────┐          ┌─────┐           ┌─────┐
  │ ML  │          │ LH  │           │ MT  │
  └─────┘          └─────┘           └─────┘
```

### Detaillierte Erstellungsreihenfolge

```
STUFE 3.1: AB ZUERST (definiert Struktur)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    AB erstellen:
    ├─ Aufgabe 1: [Typ] ([X] BE)
    ├─ Aufgabe 2: [Typ] ([X] BE)
    ├─ Aufgabe 3: [Typ] ([X] BE)
    ├─ Aufgabe 4: [Typ] ([X] BE)
    └─ Merkkästen (leer, zum Ausfüllen)

    → Aufgaben-Nummern stehen jetzt fest!
        │
        ↓

STUFE 3.2: FÜHRUNGSINSTRUMENTE (parallel möglich)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    LB (Lernblatt):
    ├─ Abschnitt 1: Vokabeln        → AB Aufgabe 1
    ├─ Abschnitt 2: Grammatik       → AB Aufgabe 2
    ├─ Abschnitt 3: Redemittel      → AB Aufgabe 3
    └─ Abschnitt 4: Anwendung       → AB Aufgabe 4

    LP (Lernpfad):
    ├─ Schritt 1-3: Vokabel-Input   → Hefter: AB Aufgabe 1
    ├─ Schritt 4-6: Grammatik       → Hefter: AB Aufgabe 2
    ├─ Schritt 7-8: Dialog          → Hefter: AB Aufgabe 3
    └─ Schritt 9-10: Produktion     → Hefter: AB Aufgabe 4

    SLIDES (Beamer LaTeX):
    ├─ Folie 3-5: Vokabeln          → Jetzt: AB Aufgabe 1
    ├─ Folie 6-8: Grammatik         → Jetzt: AB Aufgabe 2
    ├─ Folie 9-10: Dialog           → Jetzt: AB Aufgabe 3
    └─ Folie 11-12: Produktion      → Jetzt: AB Aufgabe 4
        │
        ↓

STUFE 3.3: ABGELEITETE MATERIALIEN (parallel möglich)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    ML ─── AB + rote Lösungen
    LH ─── Kurzplan + AB-Lösungen + Differenzierung [B]/[S]/[E]
    MT ─── Prüft Inhalte (basierend auf AB-Aufgaben)
```

### Zusammenfassung: Linearer Flow

```
LE → AB → (LB | LP | SLIDES) → (ML | LH | MT)
```

**Keine zirkulären Abhängigkeiten!**

---

## 4. Material-Übersicht pro Doppelstunde

| # | Kürzel | Typ | Max. Seiten | Abhängig von |
|---|--------|-----|-------------|--------------|
| 1 | **LE** | LaTeX→PDF | 8-12 (T1) / 4-6 (T2) / 2-3 (T3) | — |
| 2 | **AB** | LaTeX→PDF | **2** | LE |
| 3 | **LB** | LaTeX→PDF | **2** | LE, AB |
| 4 | **ML** | LaTeX→PDF | 2 | AB |
| 5 | **LH** | LaTeX→PDF | **3** | LE, AB |
| 6 | **LP** | HTML | — | LE, AB |
| 7 | **SLIDES** | LaTeX→PDF | 10-15 Folien | LE, AB |
| 8 | **MT** | HTML+PDF | — | LE, AB |
| 9 | **PLATZKARTEN** | LaTeX→PDF | 2 (24 Karten) | MT/TEST |
| 10 | **QR-TEST** | HTML→PDF | 1 | MT/TEST |

---

## 4a. Templates und Layout-Spezifikationen

### Template-Dateien

Alle Templates liegen in `templates/spanisch/`:

| Template | Datei | Beschreibung |
|----------|-------|--------------|
| Arbeitsblatt | `arbeitsblatt-spanisch.tex` | AB mit Punkteformat `_/X` |
| Lernblatt | `lernblatt-spanisch.tex` | LB zweispaltig, Lehrbuch-Stil |
| Musterlösung | `musterloesung-spanisch.tex` | ML mit roten Lösungen |
| Lehrerhinweise | `lehrerhinweise-spanisch.tex` | LH mit [B]/[S]/[E] |
| Langentwurf | `langentwurf-spanisch.tex` | LE Tier 1/2/3 |
| Platzkarten | `platzkarten-spanisch.tex` | 24 Karten für Tests |
| QR-Test | `qr-test-spanisch.tex` | Großer QR für Beamer |
| QR-Lernpfad | `qr-lernpfad-spanisch.tex` | Großer QR für LP |

### Schrift-Spezifikationen

| Material | Schrift | Größe | Paket |
|----------|---------|-------|-------|
| **AB** | Helvetica (serifenlos) | 11pt | `\usepackage{helvet}` |
| **LB** | Palatino (Serifen) | 10pt | `\usepackage{palatino}` |
| **ML** | wie AB | 11pt | `\usepackage{helvet}` |
| **LH** | wie AB | 11pt | `\usepackage{helvet}` |
| **LE** | wie AB | 11pt | `\usepackage{helvet}` |

### Farb-Schema

```latex
% Fachfarbe Spanisch
\definecolor{spanisch-color}{HTML}{c41e3a}  % Karminrot

% SW-Modus (für Druck)
\swmodustrue  % Setzt alle Farben auf Schwarz/Grau
```

### Befehle (in Templates definiert)

| Befehl | AB | LB | Funktion |
|--------|:--:|:--:|----------|
| `\es{text}` | ✓ | ✓ | Spanisch hervorheben (fett, farbig) |
| `\de{text}` | — | ✓ | Deutsch (kursiv) |
| `\gram{text}` | — | ✓ | Grammatikbegriff (Kapitälchen) |
| `\abmark{X}` | — | ✓ | AB-Verweis: "→ AB X" |
| `\punktebox{X}` | ✓ | — | Punktebox: `_/X` |
| `\luecke{Xcm}` | ✓ | — | Lücke zum Ausfüllen |
| `\antwortzeilen{X}` | ✓ | — | X Antwortzeilen |

### Box-Typen

**AB (arbeitsblatt-spanisch.tex):**
- `merkkasten[Titel]` — Merkkasten mit farbigem Rahmen
- `vokabelkasten` — Vokabel-Box ohne Titel
- `hinweis` — Orange Hinweis-Box
- `aufgabe{X}` — Aufgaben-Umgebung (verhindert Seitenumbruch)

**LB (lernblatt-spanisch.tex):**
- `lernzielbox` — "Das lernst du:" (oben)
- `grammatikbox[Titel]` — Grauer Hintergrund
- `merkbox[Titel]` — Dicker schwarzer Rahmen
- `vokabelbox[Titel]` — Dünner Rahmen
- `tippbox` — Randlinie links
- `zusatzbox[Titel]` — Zusatzaufgaben

### Aufgabentypen-Gestaltung

| Aufgabentyp | Layout | Beschreibung |
|-------------|--------|--------------|
| **Zuordnung** | TikZ-Boxen + Linien | Linke Spalte: Regeln/Begriffe, Rechte Spalte: Beispiele → SuS verbinden mit Linien |
| **Lückentext** | `\luecke{Xcm}` | Inline-Lücken im Fließtext |
| **Multiple Choice** | Checkboxen | `$\square$ Option A` |
| **Freie Antwort** | `\antwortzeilen{X}` | Leere Zeilen |

**Zuordnungsaufgaben (Matching) – IMMER so gestalten:**
- TikZ-Boxen verwenden (KEINE Buchstaben-/Ziffernzuordnung wie "1-c, 2-d")
- Linke Spalte: Begriffe/Regeln mit deutschem Untertitel (klein, grau)
- Rechte Spalte: Beispiele (gemischte Reihenfolge)
- SuS verbinden visuell mit Linien
- ML: Rote Verbindungslinien (`\draw[loesung, thick]`)

```latex
% TikZ-Zuordnung Vorlage
\begin{tikzpicture}[
    regelbox/.style={draw, rectangle, minimum width=2.6cm, minimum height=1.1cm,
                     font=\small, align=center},
    beispielbox/.style={draw, rectangle, minimum width=3.2cm, minimum height=0.65cm,
                        font=\small}
]
% Linke Spalte: Regeln (mit deutscher Erklärung)
\node[regelbox] (R1) at (0,0) {hay + un/una\\[-1pt]{\tiny\textcolor{mittelgrau}{unbest. Artikel}}};
\node[regelbox] (R2) at (0,-1.3) {hay + número\\[-1pt]{\tiny\textcolor{mittelgrau}{Zahl}}};

% Rechte Spalte: Beispiele (gemischt)
\node[beispielbox] (B1) at (4.8,0) {Hay tres sillas.};
\node[beispielbox] (B2) at (4.8,-1.3) {Hay una mesa.};

% NUR in ML: Lösungslinien in Rot
% \draw[loesung, thick] (R1.east) -- (B2.west);
% \draw[loesung, thick] (R2.east) -- (B1.west);
\end{tikzpicture}
```

### Verwendung

```bash
# 1. Template kopieren
cp templates/spanisch/arbeitsblatt-spanisch.tex AB-05-ropa.tex

# 2. Variablen anpassen
# \newcommand{\thema}{La ropa}
# \newcommand{\sequenz}{05}
# \newcommand{\klasse}{8}
# \newcommand{\maxpunkte}{25}

# 3. Kompilieren (2× für Referenzen)
pdflatex AB-05-ropa.tex && pdflatex AB-05-ropa.tex
```

---

## 5. Deutsche Sprache in Materialien

### Umlaute und ß – IMMER korrekt!

| Richtig | Falsch | Beispiel |
|---------|--------|----------|
| ä | ae | Ergänze (nicht: Ergaenze) |
| ö | oe | Wörter (nicht: Woerter) |
| ü | ue | Prüfen (nicht: Pruefen) |
| ß | ss | außerdem, fleißig, groß |
| Ä, Ö, Ü | Ae, Oe, Ue | Übung (nicht: Uebung) |

**Ausnahme:** Dateinamen dürfen `ae, oe, ue` verwenden (Kompatibilität).

### Prüf-Befehl (nach Erstellung)

```bash
# Suche nach falschen Umlauten in deutschem Text:
grep -oE "(Ergaenz|Woert|Pruef|Ueb|Laend|fleiss|gross|weiss|muss|dass)" *.html *.tex
# Sollte LEER sein!

# Zähle korrekte Umlaute:
grep -oh "ä\|ö\|ü\|Ä\|Ö\|Ü\|ß" *.html | sort | uniq -c
```

---

## 6. Spanische Eingabe-Toleranz

### Problem
Schüler haben deutsche Tastaturen ohne einfachen Zugang zu:
- ñ (n mit Tilde)
- á, é, í, ó, ú (Akzente)
- ¿, ¡ (führende Satzzeichen)

### Lösung: Tolerante Eingabeprüfung

**Utility-Datei:** `templates/spanisch/spanish-input-tolerance.js`

#### Toleriert werden:
| Eingabe | Akzeptiert als |
|---------|----------------|
| `espanol` | `español` |
| `como estas` | `¿Cómo estás?` |
| `manana` | `mañana` |
| `simpatico` | `simpático` |
| `Que tal` | `¿Qué tal?` |

#### Nicht toleriert (muss korrekt sein):
- Falsche Wörter (z.B. "ser" statt "estar")
- Falsche Verbformen (z.B. "soy" statt "es")
- Fehlende Wörter

### Implementierung in HTML

```html
<!-- 1. Script einbinden -->
<script src="../../../templates/spanisch/spanish-input-tolerance.js"></script>

<!-- 2. Input mit korrekter Antwort + Alternative -->
<input type="text"
       class="fill-blank"
       data-answer="simpático"
       data-alt="simpatico"
       id="q1">

<!-- 3. Prüfung (ES5-kompatibel!) -->
<script>
function checkAnswer(inputId) {
    var input = document.getElementById(inputId);
    var answer = input.getAttribute('data-answer');
    var alt = input.getAttribute('data-alt');

    if (spanishMatch(input.value, answer, alt)) {
        // Korrekt!
    } else {
        // Falsch
    }
}
</script>
```

### Die `spanishMatch()` Funktion

```javascript
function spanishMatch(input, correct, alt) {
    var normalized = normalize(input);  // Entfernt Akzente, ¿¡, lowercase
    return normalized === normalize(correct) ||
           (alt && normalized === normalize(alt));
}
```

### Multiple-Choice: Keine Toleranz nötig
Bei Radio-Buttons/Selects ist keine Toleranz erforderlich, da Schüler nur auswählen.

---

## 7. Bewertungsskalen

### Übersicht

| Klassenstufe | Leistungsart | Skala | Status |
|--------------|--------------|-------|--------|
| 7-9 (Sek I) | Sonstige Leistungen | 14-NP | ✅ Bekannt |
| 7-9 (Sek I) | Klassenarbeit | — | ⚠️ **ABFRAGE** |
| 10-12 (Sek II) | Sonstige Leistungen | 15-NP | ✅ Bekannt |
| 10-12 (Sek II) | Klausur | 15-NP (Klausur) | ✅ Bekannt |

---

### ⚠️ WARNUNG: Klassenarbeit/Klausur-Erstellung

> **Bei Erstellung von Klassenarbeiten (Sek I) oder Klausuren:**
>
> 1. **Sek I (Kl. 7-9) Klassenarbeit:**
>    - Maßstab ist NICHT im Workflow hinterlegt
>    - **PFLICHT:** User nach Bewertungsmaßstab fragen!
>    - Frage: *"Welchen Notenschlüssel verwendest du für Klassenarbeiten? Bitte Prozentgrenzen angeben."*
>
> 2. **Sek II (Kl. 10-12) Klausur:**
>    - Maßstab ist hinterlegt (siehe unten)
>    - Trotzdem bestätigen lassen: *"Klausur-Maßstab (15-NP, 5%-Schritte) verwenden?"*

---

### 14-NP Sonstige Leistungen (Sek I, Kl. 7-9)

**Für:** Minitests, Sequenztests, mündliche Leistungen

| NP | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
|----|----|----|----|----|----|----|---|---|---|---|---|---|---|---|---|
| **%** | 100 | ≥96 | ≥90,67 | ≥86 | ≥80 | ≥73,33 | ≥66,67 | ≥60 | ≥53,33 | ≥46,67 | ≥40 | ≥33,33 | ≥26,67 | ≥20 | <20 |
| **Note** | 1+ | 1 | 1- | 2+ | 2 | 2- | 3+ | 3 | 3- | 4+ | 4 | 4- | 5+ | 5 | 6 |

---

### 15-NP Sonstige Leistungen (Sek II, Kl. 10-12)

**Für:** Minitests, Sequenztests, mündliche Leistungen

| NP | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
|----|----|----|----|----|----|----|---|---|---|---|---|---|---|---|---|---|
| **%** | ≥98,67 | ≥97,33 | ≥96 | ≥90,67 | ≥85,33 | ≥80 | ≥73,33 | ≥66,67 | ≥60 | ≥53,33 | ≥46,67 | ≥40 | ≥33,33 | ≥26,67 | ≥20 | <20 |
| **Note** | 1+ | 1 | 1- | 2+ | 2 | 2- | 3+ | 3 | 3- | 4+ | 4 | 4- | 5+ | 5 | 5- | 6 |

---

### 15-NP Klausur (Sek II, Kl. 10-12)

**Für:** Klausuren (freundlicherer Maßstab!)

| NP | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
|----|----|----|----|----|----|----|---|---|---|---|---|---|---|---|---|---|
| **%** | ≥95 | ≥90 | ≥85 | ≥80 | ≥75 | ≥70 | ≥65 | ≥60 | ≥55 | ≥50 | ≥45 | ≥40 | ≥33 | ≥27 | ≥20 | <20 |
| **Note** | 1+ | 1 | 1- | 2+ | 2 | 2- | 3+ | 3 | 3- | 4+ | 4 | 4- | 5+ | 5 | 5- | 6 |

**Vergleich (obere Noten):**

| Note | Klausur | Sonstige | Differenz |
|------|---------|----------|-----------|
| 1+ (15 NP) | 95% | 98,67% | −3,67% |
| 1 (14 NP) | 90% | 97,33% | −7,33% |
| 1- (13 NP) | 85% | 96% | −11% |

---

## 8. Differenzierung

### Intern (nur in Lehrermaterialien!)

| Niveau | Marker (nur LH/LE) | Zielgruppe |
|--------|-------------------|------------|
| **[B]** Basis | grün | Berufsreife |
| **[S]** Standard | blau | Mittlere Reife |
| **[E]** Erweiterung | lila | Gymnasium |

**WICHTIG:** Keine Sternchen oder Niveaumarkierungen auf Schülermaterial!

### Online-Materialien: A/B-Gruppen

```html
<!-- Niveau-Auswahl -->
<button onclick="showSection('A')">Gruppe A (A2)</button>
<button onclick="showSection('B')">Gruppe B (B1)</button>

<!-- Inhalte -->
<div id="sectionA" class="lernpfad-section">
    <!-- Einfachere Übungen -->
</div>

<div id="sectionB" class="lernpfad-section">
    <!-- Komplexere Übungen -->
</div>
```

### Unterschiede A vs. B

| Aspekt | Gruppe A (A2) | Gruppe B (B1) |
|--------|---------------|---------------|
| Wörterzahl | 60-80 | 100-120 |
| Grammatik | Grundformen | Komplexe Strukturen |
| Vokabeln | Basiswortschatz | Erweiterter Wortschatz |
| Konnektoren | también, pero | además, sin embargo, por eso |
| Aufgabentyp | Lückentext, Zuordnung | Freie Textproduktion |

---

## 9. LocalStorage – Fortschritt speichern

### Pflicht für alle Online-Materialien

```javascript
var STORAGE_KEY = 'lp-05a-ropa';  // Eindeutig pro Material!

// Speichern
function saveData() {
    var data = {
        inputs: {},
        textareas: {},
        checkboxes: [],
        timestamp: new Date().toISOString()
    };
    // ... Daten sammeln ...
    localStorage.setItem(STORAGE_KEY, JSON.stringify(data));
}

// Laden
function loadData() {
    var saved = localStorage.getItem(STORAGE_KEY);
    if (saved) {
        var data = JSON.parse(saved);
        // ... Daten wiederherstellen ...
    }
}

// Auto-Save bei Eingabe (ES5-kompatibel)
var inputs = document.querySelectorAll('input, textarea');
for (var i = 0; i < inputs.length; i++) {
    inputs[i].addEventListener('input', saveData);
}

// Laden beim Start
loadData();
```

---

## 10. Export für itslearning

### Standard-Export-Funktion

```javascript
function exportResults() {
    var text = '=== [TITEL] ===\n';
    text += 'Name: _________________\n';
    text += 'Datum: ' + new Date().toLocaleDateString('de-DE') + '\n\n';

    // ... Ergebnisse sammeln ...

    document.getElementById('exportArea').style.display = 'block';
    document.getElementById('exportText').value = text;
}

function copyExport() {
    document.getElementById('exportText').select();
    document.execCommand('copy');
    alert('Text kopiert! Füge ihn jetzt in itslearning ein.');
}
```

---

## 11. Seitenlimits für Print-Materialien

### PFLICHT: Maximale Seitenzahlen

| Dokument | Max. Seiten | Begründung |
|----------|-------------|------------|
| **LB** (Lernblatt) | **2 A4** | Übersichtlichkeit, Heftung |
| **AB** (Arbeitsblatt) | **2 A4** | Kopierkosten, Bearbeitungszeit |
| **ML** (Musterlösung) | 2 A4 | Entspricht AB-Länge |
| **LH** (Lehrerhinweise) | 3 A4 | Mehr Platz für Lösungen |
| **LE** (Langentwurf) | unbegrenzt | Tier 1 erfordert Vollständigkeit |

### Strategien zur Einhaltung

**Bei LB (Lernblatt):**
- Zweispaltig mit `\begin{multicols}{2}`
- Schriftgröße 10pt (nicht kleiner!)
- Kompakte Boxen, wenig Whitespace
- Nur essentielle Vokabeln (max. 20)

**Bei AB (Arbeitsblatt):**
- Max. 5-6 Aufgaben pro AB
- Zusatzaufgaben in separate Box (optional)
- Antwortzeilen sparsam (max. 4-5 pro Aufgabe)
- Merkkästen kompakt halten

### Prüf-Befehl (nach PDF-Erstellung)

```bash
# Seitenzahl prüfen:
pdfinfo LB-*.pdf AB-*.pdf | grep -E "(File:|Pages:)"

# Erwartete Ausgabe:
# File: LB-01-thema.pdf
# Pages: 2
# File: AB-01-thema.pdf
# Pages: 2
```

### Bei Überschreitung

1. **Aufgaben priorisieren:** AFB I/II behalten, AFB III in Zusatzbox
2. **Vokabeln reduzieren:** Nur Kernwortschatz (8-12 Wörter)
3. **Layout optimieren:** Zweispaltig, kompaktere Abstände
4. **Inhalte auslagern:** Zusatzaufgaben → Lernpfad (digital)

---

## 12. Dateinamens-Konvention

```
LE-05a-mi-ropa.tex      # Langentwurf
AB-05a-mi-ropa.tex      # Arbeitsblatt
LB-05a-mi-ropa.tex      # Lernblatt
ML-05a-mi-ropa.tex      # Musterlösung
LH-05a-mi-ropa.tex      # Lehrerhinweise
LP-05a-mi-ropa.html     # Lernpfad
SLIDES-05a-mi-ropa.tex  # Beamer-Folien
MT-05a-mi-ropa.html     # Minitest (digital)
MT-05a-mi-ropa.tex      # Minitest (Papier)
```

**Regeln:**
- Keine Umlaute in Dateinamen
- Kleinschreibung
- Bindestriche statt Leerzeichen
- Sequenz + DS-Buchstabe im Namen (z.B. `05a`)

---

## 13. Platzkarten und QR-Codes

### Systemübersicht

Das Platzkarten-System ermöglicht digitale Stundenleistungen (Tests) mit analoger Identifizierung:

```
TEST.html (online) → PLATZKARTEN.tex (24 Karten) → SuS scannen QR
                                                        ↓
                                    Ergebnis notieren auf Karte
```

### Komponenten

| Datei | Zweck | Format |
|-------|-------|--------|
| `TEST-xxx.html` | Der digitale Test | HTML |
| `PLATZKARTEN.tex` | 24 Karten (2×A4, 4×3 Grid) | LaTeX→PDF |
| `QR-TEST.html` | Großer QR für Beamer | HTML→PDF |

### Aufbau einer Platzkarte (45mm × 88mm)

```
┌─────────────────────────┐
│        P1               │  ← Platznummer (groß, fett, #c41e3a)
│                         │
│  ─────────────────────  │  ← Namenslinie
│        Name             │
│                         │
│  ┌─────────────────┐    │
│  │    Punkte       │    │  ← Punkte-Feld (handschriftlich)
│  │    ___ / 28     │    │     Max. aus Test übernehmen!
│  └─────────────────┘    │
│                         │
│  ┌─────────────────┐    │
│  │   Note (NP)     │    │  ← Notenfeld (handschriftlich)
│  │    ___          │    │
│  └─────────────────┘    │
│                         │
│      ┌─────────┐        │
│      │ QR-Code │        │  ← Link zum Online-Test
│      └─────────┘        │
└─────────────────────────┘
```

### Templates (alle LaTeX → PDF)

| Template | Datei | Zweck |
|----------|-------|-------|
| Platzkarten | `templates/spanisch/platzkarten-spanisch.tex` | 24 Karten mit QR für Tests |
| QR-Test | `templates/spanisch/qr-test-spanisch.tex` | Großer QR für Stundenleistung |
| QR-Lernpfad | `templates/spanisch/qr-lernpfad-spanisch.tex` | Großer QR für Lernpfad |

**WICHTIG:** QR-Dokumente werden IMMER als LaTeX→PDF erstellt (keine HTML-Varianten).

**Verwendung:**
```bash
# 1. Template kopieren
cp templates/spanisch/qr-test-spanisch.tex QR-TEST.tex

# 2. Konfiguration anpassen (Titel, URL)
# → \newcommand{\testtitel}{...}
# → \newcommand{\testurl}{...}

# 3. Kompilieren
pdflatex QR-TEST.tex
```

### Hosting & Publish

**URL-Schema:**
```
https://devbox42.github.io/sciencesim/spanisch/[klasse]/[unidad]/[DATEI].html
```

**Publish-Skript:** `projects/spanisch/publish.sh`

```bash
cd projects/spanisch

# Einzelne Datei publizieren
./publish.sh kl08/unidad5-repaso-numeros/LP-repaso-numeros.html

# Ganzer Ordner (alle .html Dateien)
./publish.sh kl08/unidad5-repaso-numeros/

# Alle bereits online vorhandenen Dateien aktualisieren
./publish.sh
```

**Output:**
- `neu erstellt` → Datei war noch nicht online
- `aktualisiert` → Datei wurde geändert
- `unverändert` → Keine Änderung nötig

**Voraussetzung:** GitHub CLI (`gh`) muss authentifiziert sein.

**WICHTIG:** URL muss VOR dem Drucken der Platzkarten/QR-Codes online sein!

### Workflow im Unterricht

```
VORBEREITUNG:
1. TEST-xxx.html erstellen (mit Platznummer-Auswahl P1-P30)
2. Test auf GitHub Pages hosten
3. URL in PLATZKARTEN.tex eintragen
4. PLATZKARTEN.pdf drucken und schneiden → 24 Karten
5. QR-TEST.html für Beamer vorbereiten

DURCHFÜHRUNG:
1. Platzkarten verteilen (jeder SuS eine Karte)
2. SuS schreiben Namen auf Karte
3. QR-Code auf Beamer zeigen ODER SuS scannen eigene Karte
4. SuS wählen ihre Platznummer (P1-P24) im Test
5. SuS bearbeiten Test digital
6. Ergebnis wird angezeigt → SuS notieren Punkte auf Karte

NACHBEREITUNG:
1. Karten einsammeln
2. Punkte/NP kontrollieren und ggf. korrigieren
3. Karten zurückgeben oder abheften
```

### Vorteile

| Aspekt | Vorteil |
|--------|---------|
| Identifizierung | Analog über Platzkarte (kein Login nötig) |
| Flexibilität | Test auf jedem Gerät (BYOD) |
| Papierersparnis | Test digital, nur Karten drucken |
| Wiederverwendbar | Template für alle Tests |
| Betrugsschutz | Platznummer muss VOR Testbeginn gewählt werden |

### Digitaler Test (MT.html) – Implementierung

#### Platznummer-Auswahl (Dropdown + OK)

**NICHT als Kacheln**, sondern als Dropdown mit expliziter Bestätigung:

```html
<div class="seat-field">
    <label>Wähle deine Platznummer:</label>
    <div class="seat-warning">
        ⚠️ Die Platznummer kann nach Bestätigung nicht mehr geändert werden!
    </div>
    <select id="seatSelect"><!-- P1-P24 per JS --></select>
    <button onclick="confirmSeat()">OK</button>
</div>
```

**Ablauf:** Dropdown → OK → `confirm()`-Dialog → gesperrt

#### Auto-Reset nach Klassenstufe

| Klassenstufe | Auto-Reset | Begründung |
|--------------|------------|------------|
| **6-7** | ✅ 24h | iPads werden geteilt |
| **8+** | ❌ Nein | Eigene Geräte, Permanenz |

#### PDF-Export: NUR Ergebnisteil

```css
@media print {
    .header, .seat-field, .hinweis, #testContent, .actions { display: none !important; }
    .result { display: block !important; }
}
```

---

## 14. Checkliste vor Freigabe

### Phase 0: Kontextaufnahme

**User-Input strukturieren:**
- [ ] A) VORWISSEN erfasst? ("Ich habe ... unterrichtet") → Voraussetzungen im LE
- [ ] B) LERNZIELE erfasst? ("Ich möchte ... einführen") → Feinziele FZ1-FZ4 im LE
- [ ] C) AKTIVITÄTEN erfasst? ("Ich stelle mir vor ...") → Verlaufsphasen im LE
- [ ] D) KONTEXT erfasst? (Zeit, Klasse, Besonderheiten) → Didaktische Hinweise im LE

**Bei fehlendem Kontext:**
- [ ] Fallback auf Lehrwerksreferenz (wenn vorhanden)?
- [ ] Fallback auf Standard-Aktivitäten?
- [ ] Rückfrage an User gestellt (bei Unklarheit)?

### Phase 1: Vorbereitung (vor LE)

**Lehrwerk (optional):**
- [ ] Lehrwerk angegeben? → Referenz-Datei lesen, Seiten/Vokabeln/Grammatik übernehmen
- [ ] Kein Lehrwerk? → OK, eigenständige Stunde erstellen

**Progression (optional):**
- [ ] Vorgängerstunde bekannt? → Darauf aufbauen, Voraussetzungen dokumentieren
- [ ] Vorgänger unklar? → User fragen: "Was wurde bereits eingeführt?"
- [ ] Kaltstart gewünscht? → OK, keine Voraussetzungen annehmen

**Rahmenplan (flexibel anstreben):**
- [ ] Rahmenplan-Kompetenz identifiziert? (Hören/Sprechen/Lesen/Schreiben)
- [ ] Im LE dokumentieren (wenn passend)
- [ ] Kein Blocker wenn nicht 100% passt

### Phase 2: Langentwurf (LE)
- [ ] Tier-Stufe entspricht Anforderung?
- [ ] Didaktik-Score ≥9.0 (nur Tier 1)?
- [ ] Lehrwerk-Seiten referenziert (falls Lehrwerk angegeben)?
- [ ] Voraussetzungen dokumentiert (falls Vorgänger bekannt)?
- [ ] Differenzierung [B]/[S]/[E] vorhanden?

### Phase 3: Content-Materialien

**AB (Arbeitsblatt):**
- [ ] Max. 2 Seiten?
- [ ] Mind. 25 BE?
- [ ] Punkteformat `_/X`?
- [ ] Merkkästen zum Ausfüllen?

**LB (Lernblatt):**
- [ ] Max. 2 Seiten?
- [ ] `\abmark{X}` Verweise korrekt?
- [ ] Vokabeln, Grammatik, Redemittel?

**LP (Lernpfad):**
- [ ] 10-15 Schritte?
- [ ] Hefter-Hinweise "→ AB Aufgabe X"?
- [ ] ES5-kompatibles JavaScript?
- [ ] localStorage implementiert?
- [ ] spanish-input-tolerance.js eingebunden?

**SLIDES (Beamer LaTeX):**
- [ ] 10-15 Folien?
- [ ] AB-Referenzen "→ AB Aufgabe X"?
- [ ] pdflatex kompiliert fehlerfrei?

**ML, LH, MT:**
- [ ] Konsistent mit AB?
- [ ] Lösungen vollständig?

**PLATZKARTEN und QR (nur bei Stundenleistungen/Tests):**
- [ ] TEST online gehostet?
- [ ] QR-Code-URL in PLATZKARTEN.tex korrekt?
- [ ] Maximalpunkte auf Karte = Punkte im Test?
- [ ] 24 Karten auf 2 Seiten (4×3 Grid)?
- [ ] QR-TEST.html für Beamer vorbereitet?

### Sprache

**Deutsch:**
- [ ] Umlaute korrekt (ä, ö, ü, ß)?
- [ ] Keine "ae", "oe", "ue" in deutschem Text?

**Spanisch-Korrektheit (PFLICHT):**
- [ ] Akzente korrekt (á, é, í, ó, ú, ñ)?
- [ ] Grammatik geprüft (Kongruenz, Verbformen, ser/estar)?
- [ ] Genus korrekt (el problema, la mano)?
- [ ] Natürlich klingend (nicht wörtlich aus Deutsch übersetzt)?

> **Typische Fehler vermeiden:**
> - `esta` vs `está` (diese vs ist)
> - `el problema` nicht `la problema`
> - `está cansado` nicht `es cansado`
> - `los niños comen` nicht `los niños come`

### Technisch
- [ ] Alle PDFs kompiliert?
- [ ] Seitenlimits eingehalten?

### Phase 4: Material-QA (nach Kompilierung)

> **Vollständige QA-Dokumentation:** Siehe `/CLAUDE.md` → Abschnitt "Material-QA"

**Kurzversion für Spanisch:**

**Traceability (LE → Materialien):**
- [ ] Jedes Feinziel FZ1-FZ4 hat eine AB-Aufgabe?
- [ ] LP-Schritte decken alle LE-Verlaufsphasen ab?
- [ ] Differenzierung [B]/[S]/[E] in LH = LE?

**Konsistenz (Material ↔ Material):**
- [ ] AB-Verweise in LB, LP, SLIDES korrekt? ("→ AB Aufgabe X")
- [ ] ML-Lösungen = Lösungen aus LE?
- [ ] Fachfarbe `#c41e3a` durchgängig?

**Layout-QA (PDF visuell):**
- [ ] Alle PDFs geöffnet und durchgesehen?
- [ ] Keine Aufgaben über Seitenumbruch zerrissen?
- [ ] Boxen-Titel vollständig sichtbar?
- [ ] Genug Antwortplatz für SuS?

**Bei Problemen:** `\newpage`, `\needspace{Xem}`, `\vspace{Xpt}` → neu kompilieren → erneut prüfen.

---

## 14. Halbjahres-/Jahresplanung

### Stundenplan-Template

Für visuelle Übersichten: `templates/stundenplan-template.html`

**Dokumentation:** `templates/README-STUNDENPLAN.md`

**Workflow:**
1. Template kopieren → `projects/spanisch/KLASSE/STUNDENPLAN-XXX.html`
2. Fachfarbe setzen: `--fach-color: #c41e3a;` (Karminrot)
3. Kalender-Monate + Ferien eintragen
4. Stunden mit Feinzielen + Material einfügen
5. Im Browser öffnen / drucken

**Beispiel:** `projects/physik/kl12-GK/STUNDENPLAN-Q4-2526.html`

---

## Versionshistorie

| Datum | Version | Änderung |
|-------|---------|----------|
| 2026-01-05 | **2.9** | **Stundenplan-Template hinzugefügt (§14)** |
| 2024-12-31 | 1.0 | Initiale Version |
| 2026-01-05 | **2.0** | **Workflow komplett überarbeitet:** AB als Zentrum, Tier-System, Abhängigkeiten, Wochenstunden korrigiert (4 statt 3), Lehrwerk-Zuordnung (QP1 für 7-8, QP2 für 9) |
| 2026-01-05 | **2.1** | **Material-QA ergänzt:** Traceability, Konsistenz, Layout-QA mit Verweis auf CLAUDE.md |
| 2026-01-05 | **2.2** | **Phase 1 + Spanisch-Korrektheit:** Lehrwerk (optional), Progression (optional), Rahmenplan (flexibel), Spanisch-Korrektheit (Pflicht) |
| 2026-01-05 | **2.3** | **Phase 0 Kontextaufnahme:** User-Input (Vorwissen, Lernziele, Aktivitäten, Kontext) → LE-Struktur, Fallback-Logik, Rückfragen |
| 2026-01-05 | **2.4** | **Platzkarten & QR-Codes dokumentiert (§13):** 24-Karten-System für digitale Tests, Komponenten, LaTeX-Template, Unterrichts-Workflow, Checkliste ergänzt |
| 2026-01-05 | **2.5** | **Publish-Workflow ergänzt (§13):** publish.sh Dokumentation, URL-Schema, GitHub-Hosting |
| 2026-01-05 | **2.6** | **Templates & Layout-Spezifikationen (§4a):** Schriftarten (Helvetica/Palatino), Befehle, Box-Typen, Farb-Schema, Verwendung |
| 2026-01-05 | **2.7** | **KOMPAKT-Modus als Default:** Planungsnotiz (~250 Tokens) statt LE (~2500), Tier 1-3 für formale Anforderungen beibehalten |
| 2026-01-05 | **2.8** | **Didaktik-Score für KOMPAKT:** Score ≥9.5 Pflicht (strenger als Tier 1 mit ≥9.0), Qualitätssicherung für alle Planungs-Modi |
| 2026-01-07 | **2.9** | **Aufgabentypen-Gestaltung (§4a):** Zuordnungsaufgaben IMMER mit TikZ-Boxen + Linien (keine Buchstaben-/Ziffernzuordnung), deutsche Untertitel, ML mit roten Verbindungslinien |
