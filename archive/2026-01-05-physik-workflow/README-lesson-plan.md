# Langentwurf-Template v2.0

Standardisiertes Template für Unterrichtsentwürfe nach den Vorgaben der Fächerübergreifenden Handreichung M-V.

## Konfigurationsdimensionen

Das Template hat **drei Konfigurationsachsen**:

| Achse | Optionen | Beschreibung |
|-------|----------|--------------|
| **Tier** | 1, 2, 3 | Detailtiefe des Entwurfs |
| **Profil** | A, B, C, D, E | Lerngruppen-Typ |
| **Fach** | physik, chemie, informatik, spanisch | Bestimmt Testdifferenzierung |

## Tier-System

| Tier | Name | Seiten | Anwendung |
|------|------|--------|-----------|
| **1** | Vollständig | ~12 | Prüfungsstunden, Unterrichtsbesuche, komplexe Themen |
| **2** | Standard | ~8 | Normale Unterrichtsstunden, neue Themen |
| **3** | Minimal | ~3 | Übungsstunden, Wiederholung, Routine |

### Tier 1: Vollständig

1. Deckblatt + Inhaltsverzeichnis
2. Bedingungsanalyse (6 Unterabschnitte)
3. Sachanalyse (vollständig mit Kontrastierung)
4. Didaktische Analyse
5. Stundenziele (Grob- und Feinziele)
6. Methodische Analyse (8 Unterabschnitte)
7. Verlaufsplanung
8. Reflexion (nach Durchführung)
9. Anlagen
10. Lösungen
11. Literatur
12. Didaktik-Score (mit Begründungen)

### Tier 2: Standard

- Ohne Reflexion
- Verkürzte Sachanalyse
- Score ohne Detailbegründungen

### Tier 3: Minimal

- Nur Stundenziele
- Verlaufsplanung
- Lösungen
- Score (nur Tabelle)

## Lerngruppen-Profile

Fiktive Referenzklassen für konsistente Materialentwicklung:

| Profil | Bezeichnung | Klassenstufe | Zusammensetzung |
|--------|-------------|--------------|-----------------|
| **A** | Gesamtschule heterogen | 7-9 | BR 20%, MR 50%, GY 30% + Inklusion |
| **B** | E-Kurs Gesamtschule | 9-10 | MR 30%, GY 70% |
| **C** | G-Kurs Gesamtschule | 9-10 | BR 40%, MR 60% + Inklusion |
| **D** | Gymnasium Sek I | 7-10 | 100% GY |
| **E** | Gymnasium Sek II | 11-12 | 100% Abiturniveau |

### Profil A: Gesamtschule heterogen

```
Klassenstufe:        7-9
Zusammensetzung:     BR (20%), MR (50%), GY (30%)
Inklusion:           2-3 SuS mit LRS, 1 SuS mit Förderbedarf
Testdifferenzierung: 3 Niveaus (*/**/​***)
Besonderheiten:      Hohe Heterogenität, intensive Differenzierung nötig
```

### Profil B: E-Kurs Gesamtschule

```
Klassenstufe:        9-10
Zusammensetzung:     MR (30%), GY (70%)
Inklusion:           Ggf. 1 SuS mit LRS (Nachteilsausgleich)
Testdifferenzierung: 1-2 Niveaus (Standard + Zusatz)
Besonderheiten:      Leistungsorientiert, GY-Vorbereitung
```

### Profil C: G-Kurs Gesamtschule

```
Klassenstufe:        9-10
Zusammensetzung:     BR (40%), MR (60%)
Inklusion:           2-4 SuS mit LRS, teils Förderbedarf
Testdifferenzierung: 2 Niveaus (Basis + Standard)
Besonderheiten:      Praxisorientiert, MR-Vorbereitung
```

### Profil D: Gymnasium Sek I

```
Klassenstufe:        7-10
Zusammensetzung:     100% GY-Niveau
Inklusion:           Ggf. einzelne SuS mit LRS (Nachteilsausgleich)
Testdifferenzierung: 1 Niveau (mit BE-Differenzierung)
Besonderheiten:      Homogen, Abitur-Vorbereitung
```

### Profil E: Gymnasium Sek II / Oberstufe

```
Klassenstufe:        11-12
Zusammensetzung:     100% Abiturniveau
Kursart:             Grundkurs / Leistungskurs
Testdifferenzierung: 1 Niveau (15-NP-Skala)
Besonderheiten:      Wissenschaftspropädeutisch, EPA-konform
```

## Testdifferenzierung nach Fach

| Fach | Differenzierte Tests | Begründung |
|------|---------------------|------------|
| **Physik** | Ja (3 Niveaus) | Unterschiedliche Abschlüsse in einer Klasse |
| **Chemie** | Ja (3 Niveaus) | Unterschiedliche Abschlüsse in einer Klasse |
| **Informatik** | Nein (1 Niveau) | Wahlfach, homogenere Gruppe |
| **Spanisch** | Nein (1 Niveau) | Wahlfach, homogenere Gruppe |

## Verwendung

### 1. Template kopieren

```bash
cp templates/lesson-plan/langentwurf-template.tex \
   projects/FACH/PROJEKT/LE-XX-thema.tex
```

### 2. Konfiguration anpassen

```latex
% --- TIER (1, 2 oder 3) ---
\newcommand{\plantier}{1}

% --- LERNGRUPPEN-PROFIL (A, B, C, D oder E) ---
\newcommand{\lerngruppenprofil}{A}

% --- FACH (physik, chemie, informatik, spanisch) ---
\newcommand{\fachid}{physik}
```

### 3. Variablen ausfüllen

```latex
\newcommand{\fach}{Physik}
\newcommand{\jahrgangsstufe}{8}
\newcommand{\stundenthema}{Ohmsches Gesetz}
\newcommand{\fachfarbe}{2c5aa0}  % Physik-Blau
```

### 4. Kompilieren

```bash
pdflatex LE-XX-thema.tex
pdflatex LE-XX-thema.tex  # 2x für Inhaltsverzeichnis
```

## Didaktik-Score

**Ziel-Score: >= 9.0 (Premium-Qualität)**

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

### Score-Schwellen

| Score | Status | Aktion |
|-------|--------|--------|
| >= 9.0 | FREIGABE | Premium-Qualität, einsatzbereit |
| 8.0-8.9 | Iteration | Empfohlene Überarbeitung |
| 6.0-7.9 | Überarbeitung | Erforderliche Verbesserungen |
| < 6.0 | Neukonzeption | Grundlegende Überarbeitung |

## Abschnitts-Terminologie

Korrekte didaktische Fachbegriffe:

| Abschnitt | Bezeichnung |
|-----------|-------------|
| 1 | Bedingungsanalyse |
| 2 | Sachanalyse |
| 3 | Didaktische Analyse |
| 4 | Stundenziele |
| 5 | Methodische Analyse |
| 6 | Verlaufsplanung |
| 7 | Reflexion |
| 8 | Anlagen |
| 9 | Lösungen |
| 10 | Literatur |
| 11 | Didaktik-Score |

## Entscheidungsmatrix

```
                          ┌─────────────────────────────────────┐
                          │      Welches Profil wählen?         │
                          └─────────────────────────────────────┘
                                          │
                    ┌─────────────────────┼─────────────────────┐
                    │                     │                     │
              Gesamtschule           Gymnasium            Gymnasium
                 Kl. 7-9             Sek I                Sek II
                    │                     │                     │
         ┌──────────┴──────────┐          │                     │
         │                     │          │                     │
      heterogen            Kl. 9-10       │                     │
      (Profil A)               │          │                     │
                        ┌──────┴──────┐   │                     │
                        │             │   │                     │
                     E-Kurs        G-Kurs │                     │
                   (Profil B)   (Profil C)│                     │
                                          │                     │
                                     (Profil D)            (Profil E)
```

## Workflow: Langentwurf -> Materialien

```
1. Profil + Tier wählen
         │
         ▼
2. Langentwurf erstellen
   (LE-XX-thema.tex)
         │
         ▼
3. Score prüfen (>= 9.0?)
         │
    ┌────┴────┐
    │ Nein    │ Ja
    ▼         ▼
 Iteration  4. Materialien erstellen:
    │          - LP-XX (Lernpfad)
    │          - AB-XX (Arbeitsblatt)
    │          - LH-XX (Lehrerhinweise)
    │          - ML-XX (Musterlösung)
    │
    └──────────────────────────────────────►
                                     Fertig
```

## Dateibenennung

```
LE-XX-kurzname.tex     # Langentwurf
LE-XX-kurzname.pdf

LP-XX-kurzname.html    # Lernpfad
AB-XX-kurzname.tex     # Arbeitsblatt
LH-XX-kurzname.tex     # Lehrerhinweise
ML-XX-kurzname.tex     # Musterlösung
```

## Tipps

1. **Tier 1 beim ersten Mal** - Einmal richtig planen spart später Zeit
2. **Profil konsequent nutzen** - Ermöglicht Wiederverwendung
3. **Score >= 9.0 anstreben** - Unter 9.0 bedeutet echte Lücken
4. **Reflexion nutzen** (Tier 1) - Verbessert zukünftige Planung
5. **Fachfarbe korrekt setzen** - Visuelle Konsistenz

## Fachfarben

| Fach | Hex-Code |
|------|----------|
| Physik | `2c5aa0` |
| Chemie | `2a7a4b` |
| Informatik | `b35c00` |
| Spanisch | `c41e3a` |
