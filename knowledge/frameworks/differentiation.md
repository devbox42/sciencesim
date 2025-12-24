# Differenzierung - Lehrpfadfinder System

## Übersicht

Das Dreistufige Differenzierungssystem ermöglicht Materialien für alle Leistungsniveaus in einer Gesamtschule.

---

## Die drei Niveaustufen

| Niveau | Symbol | Code | Zielgruppe | Abschluss |
|--------|--------|------|------------|-----------|
| **Basis** | ★ | `niveau: 1` | Berufsreife (BR) | Berufsreife nach Kl. 9 |
| **Erweiterung** | ★★ | `niveau: 2` | Mittlere Reife (MR) | Mittlere Reife nach Kl. 10 |
| **Gymnasium** | ★★★ | `niveau: 3` | Gymnasium (GY) | Abitur nach Kl. 12 |

---

## Charakteristik der Niveaus

### ★ Basis (BR)

**Aufgabentypen:**
- Lückentexte mit Wortliste
- Multiple Choice (max. 4 Optionen)
- Zuordnungsaufgaben mit Bildern
- Ja/Nein-Entscheidungen
- Einfache Kopfrechenaufgaben

**Sprache:**
- Kurze, einfache Sätze
- Alltagsnahe Begriffe
- Wenig Fachbegriffe (wenn, dann erklärt)
- Keine verschachtelten Sätze

**Mathematik:**
- Nur Grundrechenarten
- Ganze Zahlen bevorzugt
- Maximal ein Rechenschritt
- Ergebnis immer "schön" (z.B. 20, 50, 100)

**Beispiel:**
```
★ Berechne: Ein Auto fährt 100 km in 2 Stunden.
   Wie schnell ist das Auto?
   
   Formel: v = s ÷ t = ___ km ÷ ___ h = ___ km/h
```

---

### ★★ Erweiterung (MR)

**Aufgabentypen:**
- Formelumstellung erforderlich
- Mehrstufige Berechnungen (max. 3 Schritte)
- Vergleichsaufgaben
- Diagramme interpretieren
- Kurzantworten (1-2 Sätze)

**Sprache:**
- Fachbegriffe werden verwendet
- Zusammengesetzte Sätze möglich
- Operatoren wie "erkläre", "vergleiche"

**Mathematik:**
- Formelumstellung nötig
- Dezimalzahlen erlaubt
- Einheitenumrechnung
- Bis zu 3 Rechenschritte

**Beispiel:**
```
★★ Ein Radfahrer fährt 15 km mit einer Durchschnitts-
   geschwindigkeit von 20 km/h. Danach legt er noch 
   10 km mit 25 km/h zurück.
   
   a) Berechne die Gesamtzeit.
   b) Berechne die Durchschnittsgeschwindigkeit 
      für die gesamte Strecke.
```

---

### ★★★ Gymnasium (GY)

**Aufgabentypen:**
- Transferaufgaben (neuer Kontext)
- Analyse und Begründung
- Mehrere Lösungswege möglich
- Offene Fragestellungen
- Fehleranalyse
- Modellkritik

**Sprache:**
- Volle Fachsprache
- Komplexe Satzstrukturen
- Operatoren wie "analysiere", "beurteile"

**Mathematik:**
- Komplexe Rechnungen
- Terme und Gleichungen
- Graphische Lösungen
- Fehlerbetrachtung

**Beispiel:**
```
★★★ Ein Fallschirmspringer springt aus 4000 m Höhe.
   Die ersten 50 s fällt er im freien Fall, dann 
   öffnet er den Fallschirm und sinkt mit konstanter
   Geschwindigkeit von 5 m/s.
   
   a) Analysiere die Bewegung in beiden Phasen.
   b) Berechne die Gesamtfallzeit.
   c) Begründe, warum das Modell "freier Fall" 
      in der Realität nicht exakt zutrifft.
```

---

## Anzeige der Sternchen

### Klasse 5-8: Sternchen sichtbar

Auf Arbeitsblättern und Tests werden die Sternchen gedruckt:

```
3. (*) Nenne die drei Aggregatzustände.           [2 BE]

4. (**) Erkläre, warum Eis auf Wasser schwimmt.   [3 BE]

5. (***) Analysiere das Diagramm und berechne    [5 BE]
         die mittlere Dichte des Gemischs.
```

### Klasse 9: Kursabhängig

| Kurs | Niveau | Sternchen |
|------|--------|-----------|
| G-Kurs | ★★ (MR) | Nicht drucken |
| E-Kurs | ★★★ (GY) | Nicht drucken |

### Klasse 10+: Keine Sternchen

Ab Klasse 10 werden keine Sternchen mehr gedruckt. Das Niveau ergibt sich aus dem Kurs/Abschluss.

---

## Punkteverteilung

### Mindestpunkte pro Niveau

| Niveau | Min. BE | Anteil |
|--------|---------|--------|
| ★ | 25 | ~40% |
| ★★ | 20 | ~35% |
| ★★★ | 15 | ~25% |
| **Gesamt** | 60 | 100% |

### Beispielverteilung (45 min Test)

| Aufgabe | Niveau | BE |
|---------|--------|-----|
| 1 | ★ | 4 |
| 2 | ★ | 5 |
| 3 | ★ | 6 |
| 4 | ★ | 5 |
| 5 | ★ | 5 |
| 6 | ★★ | 6 |
| 7 | ★★ | 7 |
| 8 | ★★ | 7 |
| 9 | ★★★ | 5 |
| 10 | ★★★ | 5 |
| 11 | ★★★ | 5 |
| **Summe** | | **60** |

---

## Differenzierung in Quiz-Templates

### JSON-Struktur

```javascript
{
    id: "F1",
    type: "mc",
    niveau: 1,        // 1 = ★, 2 = ★★, 3 = ★★★
    points: 2,
    afb: 1,           // Anforderungsbereich
    text: "...",
    // ...
}
```

### Niveau-Auswahl im Quiz

Wenn `SHOW_NIVEAU_SELECTION: true`:

```
┌─────────────────────────────────────────────┐
│  Wähle dein Niveau:                         │
│                                             │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐       │
│  │   ★     │ │   ★★    │ │  ★★★   │       │
│  │  Basis  │ │Erweiter.│ │Gymnasium│       │
│  └─────────┘ └─────────┘ └─────────┘       │
└─────────────────────────────────────────────┘
```

### Adaptives Filtern

Optional können Fragen nach Niveau gefiltert werden:

```javascript
const filteredQuestions = QUESTIONS.filter(q => 
    q.niveau <= state.niveau
);
```

---

## Anforderungsbereiche (AFB)

Die AFB-Verteilung gilt für alle Niveaus:

| AFB | Anteil | Operatoren |
|-----|--------|------------|
| I | 20-30% | nenne, gib an, beschreibe |
| II | 40-50% | berechne, erkläre, vergleiche |
| III | 20-30% | analysiere, beurteile, entwickle |

### Niveau × AFB Matrix

|  | AFB I | AFB II | AFB III |
|--|-------|--------|---------|
| ★ | Nenne Fakten | Einfache Berechnung | Einfache Begründung |
| ★★ | Beschreibe | Umstellung + Rechnung | Vergleiche |
| ★★★ | Ordne zu | Analyse | Transfer/Beurteilung |

---

## Praxisbeispiel: Dichte (Klasse 7)

### ★ Basis

```
1. Welche Formel gehört zur Dichte?
   □ ρ = m · V
   □ ρ = m / V
   □ ρ = V / m
   □ ρ = m + V
```

### ★★ Erweiterung

```
2. Ein Metallblock hat eine Masse von 500 g und 
   ein Volumen von 200 cm³.
   
   a) Berechne die Dichte.
   b) Vergleiche mit der Tabelle: Um welches 
      Metall könnte es sich handeln?
```

### ★★★ Gymnasium

```
3. Ein Gefäß enthält 100 mL Wasser (ρ = 1 g/cm³) 
   und 50 mL Öl (ρ = 0,8 g/cm³).
   
   a) Berechne die Gesamtmasse.
   b) Berechne die mittlere Dichte des Gemischs.
   c) Erkläre, warum sich die Flüssigkeiten 
      schichten und nicht vermischen.
```

---

## Checkliste Differenzierung

- [ ] Jedes Niveau vertreten?
- [ ] ★-Aufgaben wirklich einfach?
- [ ] ★★★-Aufgaben mit Transfer?
- [ ] Mindestens 25 BE für ★-Niveau?
- [ ] AFB-Verteilung eingehalten?
- [ ] Sternchen korrekt angezeigt (Kl. 5-8)?
- [ ] Kein Niveau benachteiligt?
- [ ] Sprache niveau-angepasst?
