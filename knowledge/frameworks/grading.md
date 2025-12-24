# Bewertung - Notenskalen und Punktesysteme

## Übersicht der Skalen

| Klassenstufe | Skala | Verwendung |
|--------------|-------|------------|
| 6-9 | 14-NP | Sek I Gymnasium |
| 10 MR | 6-Noten | Mittlere Reife |
| 10 GY - 12 | 15-NP | Sek II / Abitur |

---

## 15-NP-Skala (Sek II)

### Für Klasse 10E, 11, 12 (Gymnasium)

| NP | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
|----|----|----|----|----|----|----|---|---|---|---|---|---|---|---|---|---|
| % | ≥98,67 | ≥97,33 | ≥96 | ≥90,67 | ≥85,33 | ≥80 | ≥73,33 | ≥66,67 | ≥60 | ≥53,33 | ≥46,67 | ≥40 | ≥33,33 | ≥26,67 | ≥20 | <20 |
| Note | 1+ | 1 | 1- | 2+ | 2 | 2- | 3+ | 3 | 3- | 4+ | 4 | 4- | 5+ | 5 | 5- | 6 |

### JavaScript-Implementierung

```javascript
function calculate15NP(percent) {
    const thresholds = [
        { np: 15, min: 98.67 },
        { np: 14, min: 97.33 },
        { np: 13, min: 96 },
        { np: 12, min: 90.67 },
        { np: 11, min: 85.33 },
        { np: 10, min: 80 },
        { np: 9, min: 73.33 },
        { np: 8, min: 66.67 },
        { np: 7, min: 60 },
        { np: 6, min: 53.33 },
        { np: 5, min: 46.67 },
        { np: 4, min: 40 },
        { np: 3, min: 33.33 },
        { np: 2, min: 26.67 },
        { np: 1, min: 20 }
    ];
    
    for (const t of thresholds) {
        if (percent >= t.min) return `${t.np} NP`;
    }
    return "0 NP";
}
```

---

## 14-NP-Skala (Sek I)

### Für Klasse 6-9 (Gymnasium)

| NP | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
|----|----|----|----|----|----|---|---|---|---|---|---|---|---|---|---|
| % | 100 | ≥96 | ≥90,67 | ≥86 | ≥80 | ≥73,33 | ≥66,67 | ≥60 | ≥53,33 | ≥46,67 | ≥40 | ≥33,33 | ≥26,67 | ≥20 | <20 |
| Note | 1+ | 1 | 1- | 2+ | 2 | 2- | 3+ | 3 | 3- | 4+ | 4 | 4- | 5+ | 5 | 6 |

### JavaScript-Implementierung

```javascript
function calculate14NP(percent) {
    const thresholds = [
        { np: 14, min: 100 },
        { np: 13, min: 96 },
        { np: 12, min: 90.67 },
        { np: 11, min: 86 },
        { np: 10, min: 80 },
        { np: 9, min: 73.33 },
        { np: 8, min: 66.67 },
        { np: 7, min: 60 },
        { np: 6, min: 53.33 },
        { np: 5, min: 46.67 },
        { np: 4, min: 40 },
        { np: 3, min: 33.33 },
        { np: 2, min: 26.67 },
        { np: 1, min: 20 }
    ];
    
    for (const t of thresholds) {
        if (percent >= t.min) return `${t.np} NP`;
    }
    return "0 NP";
}
```

---

## 6-Noten-Skala (MR)

### Für Klasse 10 Mittlere Reife

| Note | 1 | 2 | 3 | 4 | 5 | 6 |
|------|---|---|---|---|---|---|
| % | ≥96 | ≥80 | ≥60 | ≥40 | ≥20 | <20 |
| Beschreibung | sehr gut | gut | befriedigend | ausreichend | mangelhaft | ungenügend |

### JavaScript-Implementierung

```javascript
function calculate6Note(percent) {
    if (percent >= 96) return "1";
    if (percent >= 80) return "2";
    if (percent >= 60) return "3";
    if (percent >= 40) return "4";
    if (percent >= 20) return "5";
    return "6";
}
```

---

## Quiz-Template Konfiguration

```javascript
const CONFIG = {
    // ...
    GRADING_SCALE: "15-NP",  // "15-NP" | "14-NP" | "6-Note"
    // ...
};
```

### Automatische Skalenauswahl

```javascript
function getGradingScale(grade, schulart) {
    if (schulart === "MR" && grade === 10) {
        return "6-Note";
    }
    if (grade >= 10) {
        return "15-NP";
    }
    return "14-NP";
}
```

---

## Bewertungseinheiten (BE)

### Punkteverteilung pro Zeiteinheit

| Dauer | Empfohlene BE |
|-------|---------------|
| 20 min | 20-25 BE |
| 45 min | 40-50 BE |
| 60 min | 50-60 BE |
| 90 min | 80-100 BE |

### Faustregeln

- **1 BE** ≈ 1-2 Minuten Bearbeitungszeit
- **MC-Frage**: 1-2 BE
- **Kurzrechnung**: 2-3 BE
- **Mehrstufige Aufgabe**: 4-6 BE
- **Transferaufgabe**: 5-8 BE

---

## Teilpunktevergabe

### Mehrstufige Aufgaben

```javascript
{
    type: "multi-calc",
    points: 6,
    fields: [
        { id: "a", points: 1 },  // Teilaufgabe a
        { id: "b", points: 2 },  // Teilaufgabe b
        { id: "c", points: 3 }   // Teilaufgabe c
    ]
}
```

### Numerische Aufgaben

```javascript
{
    type: "numeric-unit",
    points: 3,
    scoring: {
        value: 2,   // Für korrekten Zahlenwert
        unit: 1     // Für korrekte Einheit
    }
}
```

### Zuordnungsaufgaben

```javascript
{
    type: "matching",
    points: 4,
    pairs: 4,
    scoring: {
        perPair: 1  // 1 Punkt pro korrekter Zuordnung
    }
}
```

---

## Notenspiegel (Kopfbereich AB)

### Vorlage für Arbeitsblätter

```
╔════════════════════════════════════════════════════════════════╗
║ Stundenleistung: [Thema]                    Datum: ________    ║
║ Name: ____________________  Klasse: ____  Sitzplatz: P____    ║
╠════════════════════════════════════════════════════════════════╣
║ Note:  1   │  2   │  3   │  4   │  5   │  6                   ║
║ ab:   48  │ 40  │ 30  │ 20  │ 10  │  0   BE                  ║
╠════════════════════════════════════════════════════════════════╣
║ Erreichte BE: ______ / 50        Note: ______                 ║
╚════════════════════════════════════════════════════════════════╝
```

---

## Grenzfälle und Rundung

### Prozentberechnung

```javascript
const percent = (earned / total) * 100;
// Keine Rundung bei der Berechnung
// Nur bei der Anzeige auf 1 Dezimalstelle
```

### Grenzwerte

- Exakte Schwellenwerte verwenden (96, nicht 95.5)
- Bei exaktem Schwellenwert: höhere Note
- Beispiel: 96.00% = Note 1, 95.99% = Note 2

---

## Bonuspunkte

### Konfiguration

```javascript
const CONFIG = {
    TOTAL_POINTS: 50,
    BONUS_POINTS: 5
};
```

### Berechnung

```javascript
// Bonuspunkte werden addiert, aber max ist TOTAL_POINTS
const earned = Math.min(regularPoints + bonusPoints, CONFIG.TOTAL_POINTS);
const percent = (earned / CONFIG.TOTAL_POINTS) * 100;
```

### Im Quiz markieren

```javascript
{
    id: "BONUS",
    type: "mc",
    bonus: true,
    points: 2,
    // ...
}
```

---

## Leistungsarten

| Typ | Kürzel | Gewichtung |
|-----|--------|------------|
| Stundenleistung | SL | niedrig |
| Leistungskontrolle | LK | mittel |
| Klassenarbeit | KA | hoch |
| mündlich | mdl | variabel |

### Im Template

```javascript
const CONFIG = {
    TYPE: "SL",  // SL | LK | KA
    // ...
};
```

---

## Checkliste Bewertung

- [ ] Richtige Skala gewählt (14-NP, 15-NP, 6-Note)?
- [ ] TOTAL_POINTS = Summe aller Einzelpunkte?
- [ ] Teilpunkte korrekt konfiguriert?
- [ ] Bonuspunkte separat markiert?
- [ ] Notenspiegel im Kopfbereich (Print)?
- [ ] Prozentgrenzen exakt implementiert?
