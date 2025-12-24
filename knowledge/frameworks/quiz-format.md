# Quiz-Format Referenz

## Fragetypen

### 1. Multiple Choice (`mc`)

```javascript
{
    id: "F1",
    type: "mc",
    niveau: 1,
    points: 2,
    afb: 1,
    text: "<span class='operator'>Nenne</span> die richtige Antwort.",
    options: ["Option A", "Option B", "Option C", "Option D"],
    correct: 1,  // Index (0-basiert), hier = "Option B"
    solution: "Erklärung warum B richtig ist."
}
```

---

### 2. Numerisch mit Einheit (`numeric-unit`)

```javascript
{
    id: "F2",
    type: "numeric-unit",
    niveau: 2,
    points: 3,
    afb: 2,
    text: "<span class='operator'>Berechne</span> die Geschwindigkeit.",
    correct: 20,
    tolerance: 0.5,  // ±0.5 akzeptiert
    correctUnit: "m/s",
    unitOptions: ["m/s", "km/h", "m/s²", "m", "s"],
    scoring: { value: 2, unit: 1 },
    solution: "v = s/t = 100m / 5s = 20 m/s"
}
```

---

### 3. Zuordnung (`matching`)

```javascript
{
    id: "F3",
    type: "matching",
    niveau: 1,
    points: 4,
    afb: 1,
    text: "<span class='operator'>Ordne</span> die Formeln den Größen zu.",
    pairs: 4,
    labels: ["Geschwindigkeit", "Beschleunigung", "Weg", "Kraft"],
    options: ["v = s/t", "a = Δv/Δt", "s = v·t", "F = m·a"],
    correct: [0, 1, 2, 3],  // labels[0] → options[0], etc.
    scoring: { perPair: 1 },
    solution: "..."
}
```

---

### 4. Mehrstufige Berechnung (`multi-calc`)

```javascript
{
    id: "F4",
    type: "multi-calc",
    niveau: 3,
    points: 6,
    afb: 3,
    text: "Ein Auto beschleunigt von 0 auf 72 km/h in 10 s.",
    fields: [
        {
            id: "a",
            label: "a) Geschwindigkeit in m/s",
            points: 1,
            accepted: ["20", "20.0", "20,0"],
            unit: "m/s"
        },
        {
            id: "b",
            label: "b) Beschleunigung",
            points: 2,
            accepted: ["2", "2.0", "2,0"],
            unit: "m/s²"
        },
        {
            id: "c",
            label: "c) Zurückgelegter Weg",
            points: 3,
            accepted: ["100", "100.0", "100,0"],
            unit: "m"
        }
    ],
    solution: "a) 72 ÷ 3,6 = 20 m/s\nb) a = 20/10 = 2 m/s²\nc) s = ½·2·100 = 100 m"
}
```

---

### 5. Diagramm-Dropdown (`diagram-dropdown`)

```javascript
{
    id: "F5",
    type: "diagram-dropdown",
    niveau: 2,
    points: 4,
    afb: 2,
    text: "<span class='operator'>Interpretiere</span> das Diagramm.",
    image: "diagramm.png",  // optional
    fields: [
        {
            id: "phase1",
            label: "Phase I (0-2s):",
            options: ["Ruhe", "gleichförmig", "beschleunigt", "verzögert"],
            correct: 2
        },
        {
            id: "phase2",
            label: "Phase II (2-5s):",
            options: ["Ruhe", "gleichförmig", "beschleunigt", "verzögert"],
            correct: 1
        }
    ],
    solution: "..."
}
```

---

### 6. Einfache Berechnung (`calc`)

```javascript
{
    id: "F6",
    type: "calc",
    niveau: 2,
    points: 3,
    afb: 2,
    text: "<span class='operator'>Berechne</span> die Dichte.",
    accepted: ["2.5", "2,5", "2.50"],
    unit: "g/cm³",
    solution: "ρ = m/V = 50g / 20cm³ = 2,5 g/cm³"
}
```

---

## CONFIG-Optionen

```javascript
const CONFIG = {
    QUIZ_ID: "bewegung-kl10-sl",      // Eindeutige ID
    TITLE: "Stundenleistung: ...",    // Angezeigter Titel
    SUBJECT: "physik",                // physik | chemie | informatik
    GRADE: "10",                      // Klassenstufe
    DURATION_MINUTES: 45,             // Timer-Dauer
    UNLOCK_TIME_SECONDS: 300,         // 5 min bis Musterlösung
    UNLOCK_CODE: "PHYSIK",            // Lehrer-Override
    GRADING_SCALE: "15-NP",           // 15-NP | 14-NP | 6-Note
    SHOW_NIVEAU_SELECTION: true,      // Niveau-Auswahl anzeigen?
    TOTAL_POINTS: 50,                 // Summe aller Punkte
    BONUS_POINTS: 0                   // Zusatzpunkte möglich?
};
```

---

## Checkliste vor Veröffentlichung

- [ ] `QUIZ_ID` eindeutig?
- [ ] `SUBJECT` korrekt gesetzt?
- [ ] `TOTAL_POINTS` = Summe aller `points`?
- [ ] Jede Frage hat `solution`?
- [ ] Operatoren mit `<span class='operator'>`?
- [ ] `g = 10 m/s²` verwendet (nicht 9,81)?
- [ ] Zahlen kopfrechenbar?
- [ ] 5 Einheiten pro Dropdown?
- [ ] AFB-Verteilung ~20/50/30%?
- [ ] `UNLOCK_CODE` geändert?
