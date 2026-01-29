# Anleitung: Spanisch-Materialerstellung Spätbeginner (Kl. 10-12)

## Projektübersicht

- **Fach:** Spanisch (neu begonnene Fremdsprache)
- **Klassenstufe:** 10, 11, 12 (Spätbeginner, Gesamtschule MV)
- **Lehrwerk:** A_tope.com (Cornelsen, Ausgabe 2017)
- **Zielniveau:** A1→B1 (GER, über 3 Jahre)
- **Fachfarbe:** #c41e3a (Karminrot)
- **Wochenstunden:** 4 WStd (gemäß APVO M-V)

### Besonderheit: Jahrgangsübergreifender Kurs

**Dieser Kurs wird SYNCHRON unterrichtet:**
- Klasse 10, 11 und 12 gemeinsam im Raum
- Wenige Schüler pro Jahrgang
- Binnendifferenzierung nach Lernjahr
- Klausuren differenziert nach Jahrgang

### Prüfungsregelungen MV

Siehe: `knowledge/curriculum/spanisch/SEQUENZPLAN-SPAETBEGINNER-MV.tex`

| Jahrgang | Klausurlänge | Niveau | Sprechprüfung |
|----------|--------------|--------|---------------|
| Kl. 10 | 90 Min. | A2 | Optional |
| Kl. 11 | 135 Min. | A2+ | Empfohlen (2. HJ) |
| Kl. 12 | 135 Min. | B1 | Pflicht für Abitur |

### Lehrwerksreferenz

**Detaillierte Seitenangaben:** `knowledge/Spanisch-A_tope_Spaetbeginner/a-tope-spaetbeginner-referenz.md`

Diese Referenz enthält:
- Komplettes Inhaltsverzeichnis mit Seitenzahlen
- Mapping Lehrwerk-Unidades → Sequenzen pro Lernjahr
- Grammatik-Schnellreferenz (welche Grammatik auf welcher Seite)
- Detailinfos pro Unidad (Kommunikation, Grammatik, Wortfeld, Interkulturelles)
- Besonderheiten für jahrgangsübergreifenden Unterricht

**Verwendung in Materialien:**
```latex
\newcommand{\lehrwerkseite}{S. 40-42}  % für gustar (Unidad 3)
```

---

## Kurszuordnung nach Lernjahr

### 1. Lernjahr (typisch: Kl. 10)

| Sequenz | Thema | A_tope-Bezug | Seiten |
|---------|-------|--------------|--------|
| Seq 01 | Empezamos | Hablamos español + Unidad 1 | 8-21 |
| Seq 02 | Mi gente y mi barrio | Unidad 2 | 22-39 |
| Seq 03 | ¡Me gusta! | Unidad 3 | 40-51 |
| Seq 04 | El día a día | Unidad 4 | 52-69 |
| Seq 05 | En Madrid | Unidad 5 | 70-81 |

**Zielniveau Ende Kl. 10:** A2

### 2. Lernjahr (typisch: Kl. 11)

| Sequenz | Thema | A_tope-Bezug | Seiten |
|---------|-------|--------------|--------|
| Seq 06 | Perú - un país andino | Unidad 6 | 82-99 |
| Seq 07 | ¿A qué te quieres dedicar? | Unidad 7 | 100-109 |
| Seq 08 | Andalucía | Unidad 8 | 110-125 |
| Seq 09 | Módulos | Module 1-4 | 126-133 |

**Zielniveau Ende Kl. 11:** A2+/B1

### 3. Lernjahr (typisch: Kl. 12)

| Sequenz | Thema | Material |
|---------|-------|----------|
| Seq 10 | Wiederholung / Vertiefung | Evaluaciones + Panoramas |
| Seq 11+ | Abitur-Themen | Ergänzungsmaterial |

**Zielniveau Ende Kl. 12:** B1

---

## Materialstruktur pro Doppelstunde

### Pflicht-Dokumente

| Typ | Dateiname | Beschreibung | Pflicht |
|-----|-----------|--------------|---------|
| **LE** | `LE-XXy.tex` | Langentwurf (Tier 1, vollständig) | ✅ |
| **AB** | `AB-XXy.tex` | Arbeitsblatt (Schüler) | ✅ |
| **ML** | `ML-XXy.tex` | Musterlösung (Lösungen in rot) | ✅ |
| **LH** | `LH-XXy.tex` | Lehrerhinweise + Kurzplan | ✅ |
| **LP** | `LP-XXy.html` | Interaktiver Lernpfad | ✅ |

**XX** = Sequenznummer (01, 02, ...)
**y** = Doppelstunden-Buchstabe (a, b, c, d)

### Differenzierung im jahrgangsübergreifenden Kurs

| Marker (nur LH/LE) | Zielgruppe | Beschreibung |
|--------------------|------------|--------------|
| [LJ1] grün | 1. Lernjahr (Kl. 10) | Basis, A2-Niveau |
| [LJ2] blau | 2. Lernjahr (Kl. 11) | Standard, A2+-Niveau |
| [LJ3] lila | 3. Lernjahr (Kl. 12) | Erweiterung, B1-Niveau |

**WICHTIG:**
- Auf Schülermaterialien (AB, LP) **KEINE** Lernjahrmarkierungen!
- Differenzierung nur in Lehrermaterialien (LH, LE) sichtbar
- Klausuren: Nach Jahrgang differenziert (siehe Prüfungsregelungen)

---

## Klausuren und Tests

### Klausurregelungen Spätbeginner

**Wichtig:** Spätbeginner = 4 WStd = eigene Kategorie (nicht GK, nicht LK!)

| Jahrgang | Klausuren/Jahr | Dauer | Niveau |
|----------|----------------|-------|--------|
| Kl. 10 | 2 | 90 Min. | A2 |
| Kl. 11 | 2 | 135 Min. | A2+ |
| Kl. 12 | 2 | 135 Min. | B1 |

### Klausur-Formate (alle Jahrgänge)

| Teil | Anteil | Zeit (135 Min.) | Zeit (90 Min.) |
|------|--------|-----------------|----------------|
| Hörverstehen | 20% | 20-25 Min. | 15-20 Min. |
| Leseverstehen | 25% | 25-30 Min. | 20-25 Min. |
| Schreiben | 30% | 40-45 Min. | 25-30 Min. |
| Sprachmittlung | 25% | 35-40 Min. | 20-25 Min. |

### Sprechprüfung

| Jahrgang | Empfehlung |
|----------|------------|
| Kl. 10 | Optional (Erfahrung sammeln) |
| Kl. 11 | Empfohlen (2. Schulhalbjahr) |
| Kl. 12 | Pflicht für Abitur |

**Durchführung:** Paarprüfung (15 Min.), Bewertungsbögen A2/B1

---

## Technische Spezifikation

### Lernpfade (LP)

Identisch zu Klasse 7:
- ES5-kompatibles JavaScript
- Fachfarbe `#c41e3a`
- localStorage-Persistenz
- Eingabetoleranz für deutsche Tastatur

### Eingabetoleranz

Akzeptiere Eingaben **auch ohne**:
- Akzente (á, é, í, ó, ú → a, e, i, o, u)
- Tilde (ñ → n)
- Umgekehrte Satzzeichen (¿, ¡)
- Groß-/Kleinschreibung

**Beide Sprachen akzeptieren:**
- ✅ `hola` (Spanisch)
- ✅ `Hallo` (Deutsch)

---

## Ordnerstruktur

```
projects/spanisch/spaetbeginner/
├── ANLEITUNG-SPANISCH-SPAETBEGINNER.md  ← Diese Datei
├── JAHRESSEQUENZ-LJ1.md                 ← Übersicht 1. Lernjahr
├── JAHRESSEQUENZ-LJ2.md                 ← Übersicht 2. Lernjahr
├── JAHRESSEQUENZ-LJ3.md                 ← Übersicht 3. Lernjahr
│
├── lj1-sequenz-01-empezamos/            ← 1. Lernjahr, Sequenz 1
│   ├── 01a-hola/
│   │   ├── LE-01a.tex
│   │   ├── AB-01a.tex
│   │   ├── ML-01a.tex
│   │   ├── LH-01a.tex
│   │   └── LP-01a.html
│   ├── 01b-.../
│   ├── 01c-.../
│   └── 01d-.../
│
├── lj1-sequenz-02-mi-gente/
│   └── ...
│
├── lj2-sequenz-06-peru/                 ← 2. Lernjahr
│   └── ...
│
└── klausuren/
    ├── KL-10-01.tex                     ← Klausur Kl. 10, Nr. 1
    ├── KL-11-01.tex                     ← Klausur Kl. 11, Nr. 1
    └── KL-12-01.tex                     ← Klausur Kl. 12, Nr. 1
```

---

## Checkliste pro Doppelstunde

**Pflichtmaterialien:**
- [ ] LE erstellt (Tier 1, vollständig)
- [ ] AB erstellt (Punkteformat `_/X`)
- [ ] ML erstellt (Lösungen in rot)
- [ ] LH erstellt (Differenzierung [LJ1]/[LJ2]/[LJ3] sichtbar)
- [ ] LP erstellt (Navigation, Persistenz, Eingabetoleranz)
- [ ] Alle PDFs kompiliert

**Differenzierung geprüft:**
- [ ] Aufgaben für alle 3 Lernjahre geeignet ODER
- [ ] Differenzierte Aufgaben markiert ([LJ1], [LJ2], [LJ3])
- [ ] LH enthält Hinweise zur Binnendifferenzierung

---

## Vergleich: Klasse 7 vs. Spätbeginner

| Aspekt | Klasse 7 | Spätbeginner |
|--------|----------|--------------|
| Lehrwerk | Qué pasa 1 | A_tope.com |
| Niveau | A1 | A1→B1 |
| Dauer | 1 Jahr | 3 Jahre |
| Differenzierung | [B]/[S]/[E] | [LJ1]/[LJ2]/[LJ3] |
| Kurszusammensetzung | Homogen | Jahrgangsübergreifend |
| Klausuren | Klassenarbeiten | Klausuren (90-135 Min.) |
| Sprechprüfung | Keine | Ab Kl. 11 empfohlen |

---

## Versionshistorie

| Datum | Änderung |
|-------|----------|
| 2026-01-04 | Initiale Version erstellt |
