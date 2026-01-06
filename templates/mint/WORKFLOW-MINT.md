# Workflow: MINT-Materialien

**Version:** 1.0 (2026-01-05)
**Für:** Physik, Chemie, Informatik – Klasse 6-12

---

## 0. Grundkonfiguration

### Fach-Zuordnung

| Fach | Fachfarbe | Rahmenplan |
|------|-----------|------------|
| **Physik** | `#2c5aa0` (Blau) | `knowledge/curriculum/physik-mv-sek1.md`, `physik-mv-sek2.md` |
| **Chemie** | `#2a7a4b` (Grün) | `knowledge/curriculum/chemie-mv.md` |
| **Informatik** | `#b35c00` (Orange) | `knowledge/curriculum/informatik-mv.md` |

### Differenzierung nach Klassenstufe

| Klassenstufe | Differenzierung | Bewertung |
|--------------|-----------------|-----------|
| **6, 7, 8** | ★/★★/★★★ | 14-NP |
| **9 (ohne Kurse)** | ★/★★/★★★ | 14-NP |
| **9 G-Kurs** | MR-Niveau | 14-NP |
| **9 E-Kurs** | GY-Niveau | 14-NP |
| **10 MR** | MR-Niveau | 6-Noten |
| **10 E** | Oberstufe | 15-NP |
| **11, 12** | Oberstufe | 15-NP |

### Planungs-Modi

| Modus | Format | Tokens | Score | Wann verwenden |
|-------|--------|--------|-------|----------------|
| **KOMPAKT** | Planungsnotiz (.md) | ~250 | **≥9.5** | **DEFAULT** – Regulärer Unterricht |
| Tier 1 | Langentwurf (.tex) | ~2500 | ≥9.5 | Unterrichtsbesuche, Dokumentation |
| Tier 2 | Langentwurf (.tex) | ~800 | — | Formale Anforderung |
| Tier 3 | Langentwurf (.tex) | ~500 | — | Minimale Dokumentation |

**KOMPAKT ist Default.** Tier 1-3 nur bei expliziter Anfrage ("erstelle einen Langentwurf").

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
- Fachbegriffe: [Liste]
- Formeln/Gesetze: [Struktur]
- Einheiten: [Liste]

## Verlauf (90 Min)
| Min | Phase | Aktivität | SF | Material |
|-----|-------|-----------|-----|----------|
| 10 | Einstieg | ... | PL | — |
| 25 | Erarbeitung | ... | EA | LS |
| 20 | Übung | ... | PA/GA | AB 1-2 |
| 25 | Anwendung | ... | PA | AB 3-4, SIM |
| 10 | Sicherung | ... | PL | AB 5 |

## Differenzierung
- ★: ...
- ★★: ...
- ★★★: ...

## Output
AB, LS, LP, SL, SIM
```

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
    ├─ Fach (Physik/Chemie/Informatik)
    ├─ Klassenstufe (6-12)
    ├─ Thema
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
    └─ FREIGABE bei Score ≥9.5

    ──────────────────────────────────────────────────────────────
    🔲 CHECKPOINT 1: "Planung OK? Weiter mit Materialien?"
    ──────────────────────────────────────────────────────────────
        │
        ↓

PHASE 3: CONTENT-MATERIALIEN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    Stufe 3.1: AB (zuerst!)
    Stufe 3.2: LS, LP, SIM (parallel)
    Stufe 3.3: ML, LH, SL, QR-* (parallel)
    Stufe 3.4: PPT (optional, falls angefragt)
        │
        ↓

PHASE 4: KOMPILIERUNG & PRÜFUNG
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    pdflatex für alle .tex
    Seitenlimits prüfen
    Checklisten durchgehen

    ──────────────────────────────────────────────────────────────
    🔲 CHECKPOINT 2: "Alle Materialien erstellt. Prüfen?"
    ──────────────────────────────────────────────────────────────
```

---

## 1a. Phase 0: Kontextaufnahme (Detail)

### Zweck

User-Input erfassen und in Planungs-Struktur überführen, bevor Materialien erstellt werden.

### Die 4 Kontext-Kategorien

```
┌─────────────────────────────────────────────────────────────────┐
│  A) VORWISSEN                                                   │
│     "Ich habe bisher ... unterrichtet"                          │
│     "Die SuS können bereits ..."                                │
│     → Wird zu: Voraussetzungen                                  │
├─────────────────────────────────────────────────────────────────┤
│  B) LERNZIELE                                                   │
│     "Ich möchte ... einführen"                                  │
│     "Die SuS sollen lernen ..."                                 │
│     "Formel: ... / Gesetz: ..."                                 │
│     → Wird zu: Feinziele FZ1-FZ4                                │
├─────────────────────────────────────────────────────────────────┤
│  C) AKTIVITÄTEN                                                 │
│     "Ich stelle mir vor ..."                                    │
│     "Ich möchte ein Experiment / eine Simulation / ..."         │
│     "Die SuS sollen ... machen"                                 │
│     → Wird zu: Verlaufsphasen                                   │
├─────────────────────────────────────────────────────────────────┤
│  D) KONTEXT                                                     │
│     "Besonderheit: ..."                                         │
│     "Ich habe nur 45 Min / Die Klasse ist unruhig / ..."        │
│     "Kein Experiment möglich / ..."                             │
│     → Wird zu: Didaktische Hinweise                             │
└─────────────────────────────────────────────────────────────────┘
```

### Mapping: User-Input → Planungs-Element

| User sagt... | Kategorie | Wird zu... |
|--------------|-----------|------------|
| "Wir haben Geschwindigkeit gemacht" | A) Vorwissen | Voraussetzungen: v = s/t bekannt |
| "Jetzt möchte ich Beschleunigung einführen" | B) Lernziel | FZ1: SuS berechnen a = Δv/Δt (AFB II) |
| "SuS sollen s-t-Diagramme interpretieren" | B) Lernziel | FZ2: SuS interpretieren Diagramme (AFB II) |
| "Ich stelle mir eine Simulation vor" | C) Aktivität | Erarbeitungsphase: SIM einbinden |
| "Gruppenarbeit bevorzugt" | C) Aktivität | Sozialform: GA in Verlaufsplan |
| "Nur 45 Minuten" | D) Kontext | Zeitplanung anpassen, Tier 3 empfehlen |
| "Kein Experiment möglich" | D) Kontext | Simulation statt Realexperiment |

### Fallback: Kein User-Kontext

Wenn User nur sagt: "Erstelle Material für Beschleunigung Klasse 10"

```
A) Vorwissen:   → Aus Rahmenplan ableiten (vorherige Themen)
B) Lernziele:   → Aus Rahmenplan übernehmen
C) Aktivitäten: → Standard-Aktivitäten (Theorie → Simulation → Berechnung)
D) Kontext:     → Defaults (90 Min, heterogene Klasse, Tablets)
```

**Genutzte Rahmenpläne:**
- `knowledge/curriculum/physik-mv-sek1.md`
- `knowledge/curriculum/physik-mv-sek2.md`
- `knowledge/curriculum/chemie-mv.md`
- `knowledge/curriculum/informatik-mv.md`

### Rückfragen bei Unklarheit

Wenn Kontext unklar oder widersprüchlich:

```
User: "Ich möchte Elektrizität machen"

Claude fragt nach:
├─ "Welcher Aspekt? (Stromkreise, Ladung, Widerstand, ...)"
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
               │   LS    │      │    LP     │     │    PPT    │
               │Lehrbuch-│      │ Lernpfad  │     │ Beamer/   │
               │ seite   │      │  (HTML)   │     │   PPTX    │
               └─────────┘      └───────────┘     └───────────┘
                    │                 │                 │
                    └─────────────────┴─────────────────┘
                                      │
                        ALLE FÜHREN DURCH AB
```

### Drei Unterrichtsszenarien

| Szenario | Führungsinstrument | Wann? |
|----------|-------------------|-------|
| **Analog** | **LS** führt durch AB | Kein Tablet, klassisch |
| **Digital** | **LP** führt durch AB | Schüler arbeiten selbstständig |
| **Frontal** | **PPT** führt durch AB | Lehrervortrag, gemeinsam |

**In allen Szenarien:** AB ist das Ergebnis, das im Hefter landet.

**LS und LP sind funktional redundant** – Lehrkraft wählt analog oder digital.

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
  │ LS  │          │ LP  │                   │ SIM │
  │→AB 1│          │→AB 1│                   │     │
  │→AB 2│          │→AB 2│                   └─────┘
  └─────┘          │+SIM │                       │
                   └─────┘                       │
     │                 │                         │
     └─────────────────┼─────────────────────────┘
                       │
     ┌─────────────────┼─────────────────┐
     ↓                 ↓                 ↓
  ┌─────┐          ┌─────┐           ┌─────┐
  │ ML  │          │ LH  │           │ SL  │
  └─────┘          └─────┘           └─────┘
                                         │
                                    ┌────┴────┐
                                    ↓         ↓
                                ┌──────┐  ┌──────┐
                                │QR-LP │  │QR-SL │
                                └──────┘  └──────┘
```

### Detaillierte Erstellungsreihenfolge

```
STUFE 3.1: AB ZUERST (definiert Struktur)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    AB erstellen:
    ├─ Aufgabe 1: [Typ] ([X] BE) – ★
    ├─ Aufgabe 2: [Typ] ([X] BE) – ★★
    ├─ Aufgabe 3: [Typ] ([X] BE) – ★★
    ├─ Aufgabe 4: [Typ] ([X] BE) – ★★★
    └─ Merkkästen (leer, zum Ausfüllen)

    → Aufgaben-Nummern stehen jetzt fest!
        │
        ↓

STUFE 3.2: FÜHRUNGSINSTRUMENTE + SIM (parallel möglich)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    LS (Lehrbuchseite):
    ├─ Einstiegsbild/-frage
    ├─ Erklärtext
    ├─ Durchgerechnetes Beispiel
    ├─ Merksatz-Box mit Formeln
    ├─ Abbildungen/Diagramme
    └─ AB-Verweise: → AB Aufgabe X

    LP (Lernpfad):
    ├─ Niveau-Auswahl ★/★★/★★★
    ├─ Schritt 1-3: Theorie          → Hefter: AB Aufgabe 1
    ├─ Schritt 4-6: Simulation       → Hefter: AB Aufgabe 2
    ├─ Schritt 7-8: Berechnung       → Hefter: AB Aufgabe 3
    └─ Schritt 9-10: Transfer        → Hefter: AB Aufgabe 4

    SIM (Simulation):
    ├─ Inline Canvas
    ├─ Vollbild-Toggle
    └─ Fallback-Link
    → Wird auch in LP eingebunden
        │
        ↓

STUFE 3.3: ABGELEITETE MATERIALIEN (parallel möglich)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    ML ─── AB + rote Lösungen
    LH ─── Kurzplan + AB-Lösungen + Differenzierung ★/★★/★★★
    SL ─── Stundenleistung (HTML + PDF), ≥25 BE
    QR-LP ─── QR-Code für Lernpfad
    QR-SL ─── QR-Code für Stundenleistung
    QR-SIM ─── QR-Code für Simulation (falls vorhanden)
    PLATZKARTEN ─── 24 Karten für SL
        │
        ↓

STUFE 3.4: OPTIONAL (falls angefragt)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    PPT ─── Beamer-Folien (LaTeX/PDF oder PPTX)
```

### Zusammenfassung: Linearer Flow

```
LE → AB → (LS | LP | SIM) → (ML | LH | SL | QR-*) → [PPT]
```

**Keine zirkulären Abhängigkeiten!**

---

## 4. Material-Übersicht pro Doppelstunde

| # | Kürzel | Name | Format | Erstellung | Nutzung |
|---|--------|------|--------|------------|---------|
| 1 | **LE** | Langentwurf | LaTeX→PDF | Bei Tier 1-3 | — |
| 2 | **AB** | Arbeitsblatt | LaTeX→PDF | **Pflicht** | **Pflicht** |
| 3 | **ML** | Musterlösung | LaTeX→PDF | **Pflicht** | **Pflicht** |
| 4 | **LH** | Lehrerhinweise | LaTeX→PDF | **Pflicht** | **Pflicht** |
| 5 | **LS** | Lehrbuchseite | LaTeX→PDF | **Pflicht** | Optional* |
| 6 | **LP** | Lernpfad | HTML | **Pflicht** | Optional* |
| 7 | **SL** | Stundenleistung | HTML+PDF | **Pflicht** | Optional |
| 8 | **SIM** | Simulation | HTML | Optional+ | Optional |
| 9 | **PPT** | Präsentation | Beamer/PPTX | Optional | Optional |
| 10 | **PLATZKARTEN** | Platzkarten | LaTeX→PDF | Bei SL | Optional |
| 11 | **QR-LP** | QR Lernpfad | LaTeX→PDF | Bei LP | Optional |
| 12 | **QR-SL** | QR Stundenleistung | LaTeX→PDF | Bei SL | Optional |
| 13 | **QR-SIM** | QR Simulation | LaTeX→PDF | Bei SIM | Optional |

*LS und LP sind **funktional redundant** – Lehrkraft wählt analog (LS) oder digital (LP).

+SIM: Optional mit Tendenz zu Pflicht. Bei Zweifeln nachfragen.

---

## 5. Lernpfad-Spezifikation (MINT)

### Niveau-Auswahl

```
┌─────────────────────────────────────────────────────────────────┐
│  Wähle dein Niveau:                                             │
│                                                                 │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐                         │
│  │    ★    │  │   ★★    │  │   ★★★   │                         │
│  │  Basis  │  │Standard │  │ Erweit. │                         │
│  └─────────┘  └─────────┘  └─────────┘                         │
└─────────────────────────────────────────────────────────────────┘
```

**Verhalten:**
- Schüler arbeitet alle Aufgaben bis einschl. gewähltem Niveau ab
- Höhere Niveaus: Sichtbar, aber **grau** dargestellt in Navigation
- Hinweis bei höheren Aufgaben: "Diese Frage geht nicht in die Bewertung ein"
- Auswertung: Gegen Musterlösung geprüft, aber **keine Punkte**
- Punktebasis: Nur gewähltes Niveau zählt

### Einheiten-Toleranz

Akzeptierte Schreibweisen:

| Eingabe | Akzeptiert als |
|---------|----------------|
| `m/s` | `m s⁻¹` |
| `m/s²` | `m s⁻²` |
| `kg*m/s²` | `kg·m·s⁻²` = N |
| `km/h` | `km h⁻¹` |

### Simulation-Einbindung

```html
<!-- Inline Canvas im Lernpfad -->
<div class="simulation-container">
    <canvas id="sim-canvas" width="600" height="400"></canvas>
    <div class="sim-controls">
        <button onclick="toggleFullscreen()">⛶ Vollbild</button>
        <a href="SIM-01-thema.html" class="fallback-link">→ Simulation separat öffnen</a>
    </div>
</div>

<script src="SIM-01-thema.js"></script>
```

**Features:**
- Inline Canvas (direkt im LP, kein iframe)
- Vollbild-Toggle Button
- Dezenter Fallback-Link

### Hefter-Hinweise

```html
<div class="hefter-hinweis">
    <strong>Arbeitsblatt:</strong>
    <ul>
        <li>Übertrage die <strong>Formel</strong> in Kasten 1</li>
        <li>Bearbeite <strong>AB Aufgabe 2</strong></li>
    </ul>
</div>
```

### localStorage

Gespeichert wird:
- Alle Eingaben (inputs, textareas, selects)
- Gewähltes Niveau
- **Simulations-Zustand** (Parameter, Position)
- Fortschritt (aktuelle Sektion)
- Zeitstempel

```javascript
var STORAGE_KEY = 'lp-physik-05a-ohm';

function saveData() {
    var data = {
        inputs: {},
        niveau: selectedNiveau,
        simState: getSimulationState(),
        currentSection: currentSection,
        timestamp: new Date().toISOString()
    };
    localStorage.setItem(STORAGE_KEY, JSON.stringify(data));
}
```

### Export für itslearning

```javascript
function exportResults() {
    var text = '=== [TITEL] ===\n';
    text += 'Name: _________________\n';
    text += 'Niveau: ' + selectedNiveau + '\n';
    text += 'Datum: ' + new Date().toLocaleDateString('de-DE') + '\n\n';

    // Ergebnisse + Berechnungswege
    text += '--- Berechnungen ---\n';
    // ... Rechenwege sammeln ...

    document.getElementById('exportArea').style.display = 'block';
    document.getElementById('exportText').value = text;
}
```

---

## 6. Kopfrechenbare Werte (MINT-spezifisch)

### IMMER verwenden

| Größe | Erlaubte Werte |
|-------|----------------|
| **g** | **10 m/s²** (NICHT 9,81!) |
| Geschwindigkeiten | 36, 72, 90, 108 km/h |
| Zeiten | 2, 3, 4, 5, 6, 8, 10 s |
| Beschleunigungen | 2, 4, 5, 10 m/s² |
| Strecken | 20, 25, 40, 50, 80, 100 m |
| Massen | 2, 5, 10, 20, 50, 100 kg |
| Widerstände | 10, 20, 50, 100, 200 Ω |
| Spannungen | 6, 12, 24, 230 V |

### Erlaubte Wurzeln

√4=2, √9=3, √16=4, √25=5, √36=6, √49=7, √64=8, √81=9, √100=10

### Umrechnungen

36→10, 72→20, 90→25, 108→30 (km/h → m/s, ÷3,6)

---

## 7. Bewertungsskalen

### 14-NP Sek I (Kl. 6-9)

| NP | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
|----|----|----|----|----|----|---|---|---|---|---|---|---|---|---|---|
| **%** | 100 | ≥96 | ≥90,67 | ≥86 | ≥80 | ≥73,33 | ≥66,67 | ≥60 | ≥53,33 | ≥46,67 | ≥40 | ≥33,33 | ≥26,67 | ≥20 | <20 |
| **Note** | 1+ | 1 | 1- | 2+ | 2 | 2- | 3+ | 3 | 3- | 4+ | 4 | 4- | 5+ | 5 | 6 |

### 15-NP Sek II (Kl. 10E-12)

| NP | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
|----|----|----|----|----|----|----|----|---|---|---|---|---|---|---|---|---|
| **%** | ≥98,67 | ≥97,33 | ≥96 | ≥90,67 | ≥85,33 | ≥80 | ≥73,33 | ≥66,67 | ≥60 | ≥53,33 | ≥46,67 | ≥40 | ≥33,33 | ≥26,67 | ≥20 | <20 |
| **Note** | 1+ | 1 | 1- | 2+ | 2 | 2- | 3+ | 3 | 3- | 4+ | 4 | 4- | 5+ | 5 | 5- | 6 |

### 6-Noten MR (Kl. 10)

| Note | 1 | 2 | 3 | 4 | 5 | 6 |
|------|---|---|---|---|---|---|
| **%** | ≥96 | ≥80 | ≥60 | ≥40 | ≥20 | <20 |

---

## 8. Dateinamens-Konvention

```
LE-05a-ohmsches-gesetz.tex      # Langentwurf
AB-05a-ohmsches-gesetz.tex      # Arbeitsblatt
LS-05a-ohmsches-gesetz.tex      # Lehrbuchseite
LP-05a-ohmsches-gesetz.html     # Lernpfad
MT-05a-ohmsches-gesetz.html     # Minitest/Stundenleistung (digital)
MT-05a-ohmsches-gesetz.tex      # Minitest/Stundenleistung (PDF)
SIM-05a-ohmsches-gesetz.html    # Simulation
ML-05a-ohmsches-gesetz.tex      # Musterlösung
LH-05a-ohmsches-gesetz.tex      # Lehrerhinweise
QR-LP-05a-ohmsches-gesetz.tex   # QR Lernpfad
QR-MT-05a-ohmsches-gesetz.tex   # QR Minitest
QR-SIM-05a-ohmsches-gesetz.tex  # QR Simulation
PLATZKARTEN-05a.tex             # Platzkarten
```

### Bezeichnung und Dateinamen

**Dateiname:** `MT-*` (Minitest) für Konsistenz mit Spanisch-Workflow.

**Schüler-Bezeichnung:** "Stundenleistung" im sichtbaren Titel.

| Element | Bezeichnung |
|---------|-------------|
| **Dateiname** | `MT-XX-thema.html` |
| **`<title>`** | `Stundenleistung: [Thema]` |
| **`<h1>`** | `Stundenleistung: [Thema]` |
| **Intern** | "MT", "Minitest", "Test" erlaubt |

**Beispiel:**
```
MT-05a-ohmsches-gesetz.html     # Dateiname
→ <title>Stundenleistung: Ohmsches Gesetz</title>
```

**Schema:** `[TYP]-[XX][y]-kurzname.[ext]`
- XX = Stundennummer (01, 02, ...)
- y = Block (a, b, c, d) bei Doppelstunden

**Regeln:**
- Keine Umlaute in Dateinamen (ae, oe, ue erlaubt)
- Kleinschreibung
- Bindestriche statt Leerzeichen

---

## 9. Seitenlimits

| Dokument | Max. Seiten | Begründung |
|----------|-------------|------------|
| **LS** (Lehrbuchseite) | **2 A4** | Doppelseiten-Format |
| **AB** (Arbeitsblatt) | **2 A4** | Kopierkosten, Bearbeitungszeit |
| **ML** (Musterlösung) | 2 A4 | Entspricht AB-Länge |
| **LH** (Lehrerhinweise) | 3 A4 | Mehr Platz für Lösungen |
| **LE** (Langentwurf) | unbegrenzt | Tier 1 erfordert Vollständigkeit |

---

## 10. Checkliste vor Freigabe

### Phase 0: Kontextaufnahme

- [ ] A) VORWISSEN erfasst?
- [ ] B) LERNZIELE erfasst?
- [ ] C) AKTIVITÄTEN erfasst?
- [ ] D) KONTEXT erfasst?
- [ ] Fallback auf Rahmenplan bei Lücken?

### Phase 2: Planung

- [ ] KOMPAKT oder Tier-Stufe korrekt?
- [ ] Didaktik-Score ≥9.5?
- [ ] Differenzierung ★/★★/★★★ oder MR/GY?

### Phase 3: Content-Materialien

**AB (Arbeitsblatt):**
- [ ] Max. 2 Seiten?
- [ ] Mind. 25 BE?
- [ ] Kopfrechenbare Werte (g=10)?
- [ ] DIN-Schaltzeichen (bei Physik)?

**LS (Lehrbuchseite):**
- [ ] Max. 2 Seiten (Doppelseite)?
- [ ] AB-Verweise korrekt?
- [ ] Durchgerechnetes Beispiel?

**LP (Lernpfad):**
- [ ] Niveau-Auswahl ★/★★/★★★?
- [ ] SIM inline eingebunden (falls vorhanden)?
- [ ] localStorage (Eingaben + Simulations-Zustand)?
- [ ] Einheiten-Toleranz?
- [ ] Hefter-Hinweise → AB?
- [ ] Export mit Berechnungswegen?

**SL (Stundenleistung):**
- [ ] HTML + PDF erstellt?
- [ ] ≥25 BE?
- [ ] Platzkarten erstellt?

**SIM (Simulation):**
- [ ] Vollbild-Toggle?
- [ ] Fallback-Link?
- [ ] Auch separat als Datei?

**QR-Codes:**
- [ ] QR-LP erstellt?
- [ ] QR-SL erstellt?
- [ ] QR-SIM erstellt (falls SIM vorhanden)?

### Phase 4: QA

- [ ] Traceability (LE → Materialien)?
- [ ] Konsistenz (Material ↔ Material)?
- [ ] Layout-QA (PDFs visuell geprüft)?
- [ ] Alle PDFs kompiliert (2× pdflatex)?

---

## 11. Automatisierung

### Checkpoints (statt ständiger Permissions)

| Checkpoint | Zeitpunkt | Frage |
|------------|-----------|-------|
| **1** | Nach Phase 2 | "Planung OK? Weiter mit Materialien?" |
| **2** | Nach Phase 4 | "Alle Materialien erstellt. Prüfen?" |

### Settings-Whitelist

In `.claude/settings.local.json` können häufige Operationen freigeschaltet werden:

```json
{
  "permissions": {
    "allow": [
      "Write(path:projects/**/*.tex)",
      "Write(path:projects/**/*.html)",
      "Bash(pdflatex:*)"
    ]
  }
}
```

---

---

## 12. Halbjahres-/Jahresplanung

### Stundenplan-Template

Für visuelle Übersichten: `templates/stundenplan-template.html`

**Dokumentation:** `templates/README-STUNDENPLAN.md`

**Workflow:**
1. Template kopieren → `projects/FACH/KLASSE/STUNDENPLAN-XXX.html`
2. Fachfarbe setzen (MINT: `#2c5aa0` / `#2a7a4b` / `#b35c00`)
3. Kalender-Monate + Ferien eintragen
4. Stunden mit Feinzielen + Material einfügen
5. Im Browser öffnen / drucken

**Beispiel:** `projects/physik/kl12-GK/STUNDENPLAN-Q4-2526.html`

---

## Versionshistorie

| Datum | Version | Änderung |
|-------|---------|----------|
| 2026-01-05 | **1.1** | Stundenplan-Template hinzugefügt |
| 2026-01-05 | **1.0** | Initiale Version basierend auf WORKFLOW-SPANISCH.md v2.8 |
