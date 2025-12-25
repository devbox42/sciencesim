# Langentwurf-Template

Standardisiertes Template für Unterrichtsentwürfe nach den Vorgaben der Fächerübergreifenden Handreichung M-V.

## Tier-System

Das Template verwendet ein 3-Tier-System zur Skalierung des Planungsaufwands:

| Tier | Name | Aufwand | Anwendung |
|------|------|---------|-----------|
| **1** | Vollständig | Hoch | Prüfungsstunden, komplexe Themen, Unterrichtsbesuche |
| **2** | Standard | Mittel | Normale Unterrichtsstunden, neue Themen |
| **3** | Minimal | Niedrig | Übungsstunden, Wiederholung, Routine |

### Tier 1: Vollständig (11 Abschnitte)

Alle Komponenten der M-V Handreichung:

1. Deckblatt
2. Inhaltsverzeichnis
3. Bedingungsanalyse (6 Unterabschnitte)
4. Sachanalyse (vollständig mit Kontrastierung)
5. Didaktische Überlegungen
6. Stundenziele (Grob- und Feinziele)
7. Methodische Überlegungen (8 Unterabschnitte)
8. Ausführlicher Verlaufsplan
9. Reflexion (nach Durchführung)
10. Anlagen
11. Lösungen
12. Publikationsverzeichnis
13. Didaktik-Score (mit Begründungen)

**Verwenden bei:**
- Lehrproben / Unterrichtsbesuche
- Staatsexamensprüfungen
- Komplexe grammatische Strukturen (gustar, subjuntivo, etc.)
- Einführung neuer Konzepte
- Showcase-Stunden

### Tier 2: Standard (8 Abschnitte)

Ohne Reflexion, verkürzte Analysen:

1. Deckblatt
2. Inhaltsverzeichnis
3. Bedingungsanalyse (verkürzt)
4. Sachanalyse (Kernkonzepte)
5. Didaktische Überlegungen
6. Stundenziele
7. Methodische Überlegungen
8. Ausführlicher Verlaufsplan
9. Anlagen
10. Lösungen
11. Publikationsverzeichnis
12. Didaktik-Score (ohne Begründungen)

**Verwenden bei:**
- Reguläre Unterrichtsstunden
- Neue Themeneinführungen
- Wichtige Übungsphasen
- Vorbereitung auf Leistungskontrollen

### Tier 3: Minimal (4 Abschnitte)

Nur das Wesentliche:

1. Stundenziele (Grob- und Feinziele)
2. Ausführlicher Verlaufsplan
3. Anlagen
4. Lösungen
5. Didaktik-Score (nur Tabelle)

**Verwenden bei:**
- Übungsstunden
- Wiederholung bekannter Inhalte
- Routine-Lektionen
- Vertretungsstunden mit bekanntem Material

## Verwendung

### 1. Template kopieren

```bash
cp templates/lesson-plan/langentwurf-template.tex projects/FACH/PROJEKT/LE-XX-thema.tex
```

### 2. Tier festlegen

In der Datei die Zeile anpassen:

```latex
\newcommand{\plantier}{1}  % 1, 2 oder 3
```

### 3. Variablen ausfüllen

```latex
% --- Metadaten ---
\newcommand{\fach}{Spanisch}
\newcommand{\jahrgangsstufe}{11}
\newcommand{\stundenthema}{Das Verb gustar}
% ... etc.
```

### 4. Fachfarbe setzen

```latex
\newcommand{\fachfarbe}{c41e3a}  % Hex ohne #
```

| Fach | Farbe |
|------|-------|
| Physik | `2c5aa0` |
| Chemie | `2a7a4b` |
| Informatik | `b35c00` |
| Spanisch | `c41e3a` |

### 5. Kompilieren

```bash
pdflatex LE-XX-thema.tex
pdflatex LE-XX-thema.tex  # 2x für Inhaltsverzeichnis
```

## Didaktik-Score

Der integrierte Score basiert auf 10 Dimensionen:

| # | Dimension | Gewichtung |
|---|-----------|------------|
| 1 | Differenzierung | 15% |
| 2 | Taxonomie (AFB) | 10% |
| 3 | Lernziel-Alignment | 10% |
| 4 | Aktivierung | 10% |
| 5 | Scaffolding | 10% |
| 6 | Feedback-Qualität | 10% |
| 7 | Sprachliche Klarheit | 10% |
| 8 | Motivation & Relevanz | 10% |
| 9 | Inklusion (UDL) | 10% |
| 10 | Praktikabilität | 5% |

### Score-Schwellwerte

| Score | Status | Aktion |
|-------|--------|--------|
| >= 9.0 | Premium | Freigabe, Mustermaterial |
| >= 8.0 | Gut | Freigabe |
| 6.0-7.9 | Okay | Iteration empfohlen |
| < 6.0 | Mangelhaft | Grundlegende Überarbeitung |

## Entscheidungsbaum: Welchen Tier wählen?

```
Ist es eine Prüfungsstunde / Unterrichtsbesuch?
├── Ja → Tier 1
└── Nein
    └── Ist das Thema neu oder komplex?
        ├── Ja → Tier 1 oder 2
        └── Nein
            └── Ist es eine Übungs-/Wiederholungsstunde?
                ├── Ja → Tier 3
                └── Nein → Tier 2
```

## Workflow-Empfehlung

### Vor der Materialerstellung

1. **Tier wählen** basierend auf Entscheidungsbaum
2. **Langentwurf erstellen** (oder zumindest Stundenziele + Verlaufsplan)
3. **Score prüfen** - Ziel: >= 8.0
4. **Dann erst:** LP, AB, LH erstellen

### Nach der Materialerstellung

1. **Score aktualisieren** mit finalen Werten
2. **Reflexion ausfüllen** (nach Durchführung, nur Tier 1)
3. **Template für ähnliche Stunden** wiederverwenden

## Dateibenennung

```
LE-XX-kurzname.tex     # Langentwurf
LE-XX-kurzname.pdf     # Kompiliertes PDF

# Begleitende Materialien:
LP-XX-kurzname.html    # Lernpfad
AB-XX-kurzname.tex     # Arbeitsblatt
LH-XX-kurzname.tex     # Lehrerhinweise
ML-XX-kurzname.tex     # Musterlösung
```

XX = zweistellige Stundennummer (01, 02, 03...)

## Beispiel: Gustar-Stunde

```
projects/spanisch/oberstufe-gustos/
├── LE-01-gustar-langentwurf.tex  # Tier 1, vollständig
├── LE-01-gustar-langentwurf.pdf
├── LH-01-gustar.tex              # Lehrerhinweise
├── LH-01-gustar.pdf
├── arbeitsblatt-gustos.tex       # AB
├── arbeitsblatt-gustos.pdf
├── lernpfad.html                 # Interaktiver LP
└── SCORE-MATRIX-9-10.md          # Detaillierte Score-Analyse
```

## Tipps

1. **Tier 1 für das erste Mal** - Einmal richtig planen spart später Zeit
2. **Kopieren und anpassen** - Ähnliche Themen können Struktur übernehmen
3. **Score ernst nehmen** - Unter 8.0 bedeutet echte Schwächen
4. **Reflexion nutzen** - Nur so verbessert sich die Planung langfristig
5. **Variablen konsequent** - Alle Metadaten zentral änderbar
