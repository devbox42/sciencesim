# Anleitung: Spanisch-Materialerstellung Klasse 7

## Projektübersicht

- **Fach:** Spanisch (2. Fremdsprache)
- **Klassenstufe:** 7 (Gesamtschule MV)
- **Lehrwerk:** Qué pasa 1 (Diesterweg, Ausgabe 2016)
- **Zielniveau:** A1 (GER)
- **Fachfarbe:** #c41e3a (Karminrot)

### Anonymität

**PFLICHT:** Alle Materialien sind **schulneutral** zu erstellen.

- ❌ Keine Schulnamen (z.B. "Greenhouse Schools")
- ❌ Keine schulspezifischen Logos
- ❌ Keine Ortsangaben (außer für Unterrichtskontext)
- ✅ Nur generische Bezeichnungen: "Spanisch Klasse 7", "Sequenz X"

**Grund:** Materialien sollen universell einsetzbar sein.

### Lehrwerksreferenz

**Detaillierte Seitenangaben:** `knowledge/Spanisch-Que-Pasa-1/que-pasa-1-referenz.md`

Diese Referenz enthält:
- Komplettes Inhaltsverzeichnis mit Seitenzahlen
- Mapping Lehrwerk-Unidades → Unsere Sequenzen
- Grammatik-Schnellreferenz (welche Grammatik auf welcher Seite)
- Detailinfos pro Unidad (Kommunikation, Grammatik, Wortfeld, Interkulturelles)

**Verwendung in Materialien:**
```latex
\newcommand{\lehrwerkseite}{S. 73-74}  % für gustar
```

---

## Materialstruktur pro Doppelstunde

Jede Doppelstunde erhält ein **vollständiges Materialset**:

| Typ | Dateiname | Beschreibung | Pflicht |
|-----|-----------|--------------|---------|
| **LE** | `LE-XXy.tex` | Langentwurf (Tier 1, vollständig) | ✅ |
| **AB** | `AB-XXy.tex` | Arbeitsblatt (Schüler) | ✅ |
| **ML** | `ML-XXy.tex` | Musterlösung (Lösungen in rot) | ✅ |
| **LH** | `LH-XXy.tex` | Lehrerhinweise + Kurzplan | ✅ |
| **LP** | `LP-XXy.html` | Interaktiver Lernpfad (optional für Schüler) | ✅ |
| **MT** | `MT-XXy.html` | Minitest digital (25 BE, kein Reset) | ✅ |
| **MT** | `MT-XXy.tex` | Minitest Papierversion | ✅ |
| **MT-ML** | `MT-XXy-ML.tex` | Minitest Musterlösung | ✅ |
| **PPT** | `PPT-XXy.pptx` | PowerPoint-Präsentation (Unterrichtsbegleitung) | ✅ |

**Bei d-Lektionen (Sequenzende) zusätzlich:**

| Typ | Dateiname | Beschreibung |
|-----|-----------|--------------|
| **SL** | `SL-XXd.html` | Sequenztest digital (25-50 BE) |
| **SL** | `SL-XXd.tex` | Sequenztest Papierversion |
| **SL-ML** | `SL-XXd-ML.tex` | Sequenztest Musterlösung |

**XX** = Sequenznummer (01, 02, ...)
**y** = Doppelstunden-Buchstabe (a, b, c, d, ...)

---

## Langentwurf-Standard: Tier 1

**PFLICHT für alle Doppelstunden!**

Tier 1 = Vollständiger Langentwurf mit:
- Kopfbereich (Fach, Klasse, Thema, Zeit, Lehrwerk)
- Kompetenzziele (kommunikativ, sprachlich, interkulturell)
- Verlaufsplanung (beide Stunden, 5-Min-Raster)
- Differenzierung (Basis/Standard/Erweiterung)
- Erwartete Schwierigkeiten + Reaktionen
- Tafelanschrieb
- Materialcheckliste
- Hausaufgabe
- Reflexionsfragen (für Lehrkraft)
- Lernstandserhebung

**Grund:** Absicherung der praktischen Umsetzbarkeit.

---

## Differenzierung

### Intern (nicht sichtbar für Schüler)

| Niveau | Marker (nur LH/LE) | Zielgruppe |
|--------|-------------------|------------|
| Basis | [B] grün | Berufsreife |
| Standard | [S] blau | Mittlere Reife |
| Erweiterung | [E] lila | Gymnasium |

**WICHTIG:**
- Auf Schülermaterialien (AB, LP) **KEINE** Sternchen oder Niveaumarkierungen!
- Differenzierung nur in Lehrermaterialien (LH, LE) sichtbar
- Tests: Einheitliches MR-Niveau für alle

---

## Lernpfad-Konzept

### Verzahnung LP ↔ AB ↔ Lehrbuch

| Komponente | Rolle | Pflicht? |
|------------|-------|----------|
| **Lehrbuch** (Qué pasa 1) | Basis-Input, Texte, Grammatik | ✅ |
| **Arbeitsblatt (AB)** | Schriftliche Übung, Hefter-Dokumentation | ✅ |
| **Lernpfad (LP)** | Digitale Führung, interaktive Übung, Feedback | Optional |

**Grundprinzip:**
- **Offline-Variante (AB + Buch) reicht IMMER aus!**
- Lernpfad führt und übt **zusätzlich** – ist aber nicht zwingend erforderlich
- LP verweist auf konkrete AB-Aufgaben und Lehrbuch-Seiten
- Schüler ohne Gerät arbeiten gleichwertig mit AB + Buch

---

## Tests / Assessments

### Grundregeln für ALLE Tests

| Kriterium | Vorgabe |
|-----------|---------|
| Mindestpunkte | **25 BE** (auch Minitests!) |
| Bewertungsskala | **14-NP-Skala** (Sek I, sonstige Leistungen) |
| Varianten | **Immer beides:** Digital (HTML) + Papier (PDF) |
| Niveau | Einheitlich MR für alle |

### Testtypen

| Testtyp | Wann | Umfang | Dateien |
|---------|------|--------|---------|
| **Minitest** | Jede Doppelstunde | 25-30 BE | `MT-XXy.html` + `MT-XXy.tex` |
| **Sequenztest** | Ende jeder Sequenz (d-Lektion) | 25-50 BE | `SL-XXd.html` + `SL-XXd.tex` |
| Klassenarbeit | Nach Repaso-Block | 40-60 BE | `KA-XX.html` + `KA-XX.tex` |

### Digitale Tests (HTML) – Spezifikation

**Technisch wie Lernpfad, ABER:**

| Eigenschaft | Lernpfad (LP) | Test (MT/SL) |
|-------------|---------------|--------------|
| Reset durch Schüler | ✅ Mit Bestätigung | ❌ **Gesperrt** |
| Auto-Reset | — | ✅ Nach **24 Stunden** |
| Lehrer-Reset | — | ✅ Via **Knopf mit PIN** |
| Retention | Normale Persistenz | **Strenge Retention** |
| Feedback | Sofort nach Aufgabe | Erst am Ende (Gesamtscore) |

**Retention-Mechanismus:**
```javascript
// Test-Sperre: Kein Reset durch Schüler
function reset() {
    alert('Reset nicht möglich. Wende dich an die Lehrkraft.');
    return;
}

// Auto-Reset nach 24h
var TEST_ID = 'mt01a';
var startTime = localStorage.getItem(TEST_ID + '-start');
if (startTime && (Date.now() - parseInt(startTime)) > 86400000) {
    clearTestData();
}

// Lehrer-Reset via Knopf (am Seitenende, klein/unauffällig)
function lehrerReset() {
    var pin = prompt('Lehrer-PIN eingeben:');
    if (pin === '2024') {
        clearTestData();
        alert('Test wurde zurückgesetzt.');
        location.reload();
    } else if (pin !== null) {
        alert('Falsche PIN.');
    }
}
```

**Lehrer-Reset-Button (am Seitenende):**
```html
<div style="text-align:center; margin-top:40px; opacity:0.3;">
    <button onclick="lehrerReset()" style="font-size:0.7em; padding:5px 10px;
        background:#eee; border:1px solid #ccc; cursor:pointer;">
        Lehrkraft: Reset
    </button>
</div>
```

### Papiervarianten

**Für jeden digitalen Test eine Papierversion:**

| Digital | Papier | Inhalt |
|---------|--------|--------|
| `MT-01a.html` | `MT-01a.tex` / `.pdf` | Ähnliche Aufgaben, nicht identisch |
| `SL-01d.html` | `SL-01d.tex` / `.pdf` | + Erwartungshorizont (EWH) |

**Papier-Besonderheiten:**
- Platz für handschriftliche Antworten
- Punkteboxen (`_/X`) hinter jeder Aufgabe
- Notentabelle am Ende
- Erwartungshorizont als separate Datei (`SL-XXd-EWH.tex`)

### 14-NP-Skala (Sek I)

| NP | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 |
|----|----|----|----|----|----|----|---|---|---|---|---|---|---|---|
| % | 100 | 96 | 90,67 | 86 | 80 | 73,33 | 66,67 | 60 | 53,33 | 46,67 | 40 | 33,33 | 26,67 | 20 |

---

## Lernpfade (LP) – Technische Spezifikation

### Mindestumfang pro Lernpfad

**WICHTIG: Lernpfade dürfen NICHT mager sein!**

| Kriterium | Minimum |
|-----------|---------|
| **Schritte (Karten)** | Mind. 8-12 Schritte |
| **Interaktive Übungen** | Mind. 4-6 pro LP |
| **Vokabel-Input** | Vollständige Einführung mit Bildern/Kontext |
| **Grammatik** | Erklärung + Merkkasten + Übung |
| **Hefter-Hinweise** | Nach jedem Content-Schritt |
| **Dialog/Anwendung** | Mind. 1 Dialogübung |
| **Abschluss-Zusammenfassung** | Immer |

**Typischer LP-Aufbau (10-12 Schritte):**

| Schritt | Inhalt | Typ |
|---------|--------|-----|
| 1 | Begrüßung + Lernziele | Content |
| 2 | Vokabel-Input (mit Bildern) | Content |
| 3 | Vokabel-Übung 1 (Zuordnung) | Übung |
| 4 | Vokabel-Übung 2 (Lückentext) | Übung |
| 5 | Grammatik-Erklärung | Content |
| 6 | Grammatik-Übung 1 | Übung |
| 7 | Grammatik-Übung 2 | Übung |
| 8 | Anwendung (Dialog/Kontext) | Content |
| 9 | Dialog-Übung | Übung |
| 10 | Zusammenfassung + Hefter | Content |
| 11 | Abschluss (Punkte, Lob) | Abschluss |

### Verbindliche Design-Grundlage

**Referenz:** `/CLAUDE.md` → Abschnitt "Design-System (sciencesim-konsistent)"

### HTML-Layout (VERBINDLICH)

| Eigenschaft | Wert |
|-------------|------|
| **Fachfarbe** | `#c41e3a` (Karminrot) |
| **Container** | `max-width: 900px`, zentriert |
| **Hintergrund** | `#f5f5f5` (Seite), `#fff` (Karten) |
| **Borders** | `1px solid #ddd` |
| **Border-Radius** | max. `3px` (oder `0`) |
| **Schrift** | System-Fonts, 16px Basis |
| **Tabellen-Header** | Fachfarbe als Hintergrund, weiße Schrift |

**VERBOTEN (AI-typisch):**
- ❌ Gradients
- ❌ Box-shadows
- ❌ Border-radius > 3px
- ❌ Bunte Buttons (nur Fachfarbe)
- ❌ Hover-Animationen
- ❌ Glassmorphism

### HTML-Struktur eines Lernpfads

```html
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <title>LP-XXy: [Thema]</title>
    <style>
        /* CSS inline, keine externen Dateien */
    </style>
</head>
<body>

<!-- 1. NAVIGATION (sticky) -->
<nav class="nav-bar">
    <div class="nav-content">
        <div class="nav-title">LP-XXy: [Kurzthema]</div>
        <div class="nav-steps" id="stepDots"></div>
        <div class="progress-info"><span id="pct">0</span>%</div>
    </div>
</nav>

<!-- 2. CONTAINER -->
<div class="container">

    <!-- 3. KARTEN (eine pro Schritt) -->
    <div class="card visible" id="step1">
        <div class="card-header">
            <div class="card-step">Schritt 1 von N</div>
            <h1 class="card-title">[Titel]</h1>
        </div>
        <!-- Inhalt -->
        <div class="nav-buttons">
            <div></div>
            <button class="btn btn-main" onclick="goTo(2)">Weiter →</button>
        </div>
    </div>

    <div class="card" id="step2">...</div>
    <!-- ... weitere Schritte ... -->

    <!-- N+1. ABSCHLUSS-KARTE -->
    <div class="card" id="stepN+1">
        <div class="complete-screen">
            <h2>Muy bien!</h2>
            <div class="score"><span id="finalScore">0</span> / X Punkte</div>
        </div>
    </div>

</div>

<!-- 4. JAVASCRIPT (am Ende, ES5-kompatibel) -->
<script>
    // Kein DOMContentLoaded nötig
    init();
</script>

</body>
</html>
```

### Komponenten im Detail

#### Navigation (sticky)

```css
.nav-bar {
    background: #fff;
    border-bottom: 1px solid #ddd;
    padding: 12px 20px;
    position: sticky;
    top: 0;
    z-index: 100;
}

.step-dot {
    width: 28px;
    height: 28px;
    border-radius: 50%;
    border: 2px solid #ddd;
    /* ... */
}

.step-dot.active {
    border-color: #c41e3a;
    background: #c41e3a;
    color: #fff;
}

.step-dot.done {
    border-color: #2a7a4b;
    background: #2a7a4b;
    color: #fff;
}
```

#### Karten (Schritte)

```css
.card {
    background: #fff;
    border: 1px solid #ddd;
    padding: 30px;
    display: none;
}

.card.visible {
    display: block;
}

.card-header {
    margin-bottom: 25px;
    padding-bottom: 15px;
    border-bottom: 2px solid #c41e3a;
}
```

#### Info-Box

```css
.info {
    background: #fdf2f4;          /* Fachfarbe aufgehellt */
    border: 1px solid #c41e3a;    /* Fachfarbe */
    padding: 15px;
    margin: 20px 0;
}
```

#### Hefter-Hinweis (AB-Verweis)

```css
.hefter {
    background: #fff3e0;          /* Orange aufgehellt */
    border: 2px solid #b35c00;    /* Warning-Orange */
    padding: 15px;
    margin: 20px 0;
}

.hefter-label {
    display: inline-block;
    background: #b35c00;
    color: #fff;
    font-size: 0.75em;
    font-weight: 600;
    padding: 2px 8px;
    margin-bottom: 8px;
}
```

#### Feedback

```css
.feedback {
    padding: 12px 15px;
    margin-top: 15px;
    display: none;
}

.feedback.show { display: block; }

.feedback.ok {
    background: #e8f5e9;
    border: 1px solid #2a7a4b;
    color: #2a7a4b;
}

.feedback.partial {
    background: #fff3e0;
    border: 1px solid #b35c00;
    color: #b35c00;
}

.feedback.wrong {
    background: #ffebee;
    border: 1px solid #c62828;
    color: #c62828;
}
```

#### Buttons

```css
.btn {
    padding: 10px 20px;
    font-size: 1em;
    font-weight: 600;
    border: none;
    cursor: pointer;
}

.btn-main {
    background: #c41e3a;
    color: #fff;
}

.btn-back {
    background: #fff;
    border: 1px solid #ddd;
    color: #555;
}
```

---

### Persistenz (localStorage) – Schema

**Präfix:** `lpXXy-` (z.B. `lp01a-`)

| Key | Wert | Beschreibung |
|-----|------|--------------|
| `lp01a-step` | `1`–`N` | Aktueller Schritt |
| `lp01a-[inputId]` | String | Gespeicherte Eingabe |
| `lp01a-match` | `0`–`4` | Punkte Zuordnungsaufgabe |
| `lp01a-time` | `0`–`4` | Punkte Tageszeitenaufgabe |
| `lp01a-done` | `true` | Abgeschlossen-Flag |

**JavaScript-Implementierung:**

```javascript
var LP_ID = 'lp01a';

// Schritt speichern
function saveStep(n) {
    localStorage.setItem(LP_ID + '-step', n);
}

// Schritt laden
function loadStep() {
    var saved = localStorage.getItem(LP_ID + '-step');
    return saved ? parseInt(saved) : 1;
}

// Eingabe speichern
function saveInput(id) {
    var el = document.getElementById(id);
    if (el) localStorage.setItem(LP_ID + '-' + id, el.value);
}

// Eingaben laden
function loadInputs() {
    var ids = ['m1', 'm2', 'm3', 'm4', 't1', 't2', 't3', 't4'];
    for (var i = 0; i < ids.length; i++) {
        var el = document.getElementById(ids[i]);
        var v = localStorage.getItem(LP_ID + '-' + ids[i]);
        if (el && v) el.value = v;
    }
}

// Reset (nur mit Bestätigung!)
function reset() {
    if (!confirm('Wirklich neu starten?')) return;

    var keys = [];
    for (var i = 0; i < localStorage.length; i++) {
        var k = localStorage.key(i);
        if (k && k.indexOf(LP_ID) === 0) keys.push(k);
    }
    for (var j = 0; j < keys.length; j++) {
        localStorage.removeItem(keys[j]);
    }
}
```

**WICHTIG:**
- Reset NUR mit `confirm()`-Dialog
- Eingaben bei JEDER Änderung speichern (`onchange`)
- Beim Laden: Schritt + alle Eingaben wiederherstellen

---

### Eingabetoleranz (Spanisch) – KRITISCH!

**PFLICHT: Beide Sprachen akzeptieren!**

Bei ALLEN interaktiven Übungen (LP, MT, SL) müssen **IMMER BEIDE** als korrekt akzeptiert werden:
1. **Spanisch** (korrekte Antwort)
2. **Deutsch** (ohne spanische Sonderzeichen)

**Beispiel Vokabel-Abfrage "Hallo":**
- ✅ `hola` (Spanisch)
- ✅ `Hallo` (Deutsch)
- ✅ `hallo` (Deutsch, klein)

**Beispiel Satz-Vervollständigung:**
- ✅ `¿Cómo te llamas?` (Spanisch korrekt)
- ✅ `Como te llamas` (ohne Akzente/Satzzeichen)
- ✅ `como te llamas` (kleingeschrieben)

**Deutsche Tastatur-Kompatibilität:**

Akzeptiere Eingaben **auch ohne**:
- Akzente (á, é, í, ó, ú → a, e, i, o, u)
- Tilde (ñ → n)
- Umgekehrte Satzzeichen (¿, ¡)
- Groß-/Kleinschreibung

**Implementierung (ES5-kompatibel):**

```javascript
function norm(s) {
    return s.toLowerCase()
        .normalize('NFD')
        .replace(/[\u0300-\u036f]/g, '')  // Akzente entfernen
        .replace(/[¿¡?!.,]/g, '')         // Satzzeichen entfernen
        .replace(/\s+/g, ' ')             // Mehrfache Leerzeichen
        .trim();
}

// WICHTIG: correctOptions muss BEIDE Sprachen enthalten!
// Beispiel: ['hola', 'Hallo'] oder ['Buenos días', 'Guten Morgen']
function checkAnswer(input, correctOptions) {
    var normalized = norm(input);
    for (var i = 0; i < correctOptions.length; i++) {
        if (normalized === norm(correctOptions[i])) return true;
    }
    return false;
}
```

**Begründung:** Schüler lernen Spanisch – bei der Eingabe sollen sie nicht durch fehlende Sonderzeichen auf der Tastatur bestraft werden. Gleichzeitig zeigt die Akzeptanz der deutschen Übersetzung, dass das Verständnis vorhanden ist.

---

### JavaScript-Anforderungen

**PFLICHT: ES5-kompatibel!**

| Erlaubt | Verboten |
|---------|----------|
| `var` | `let`, `const` |
| `function(){}` | `() => {}` |
| `for`-Schleifen | `forEach`, `map`, `filter` |
| String-Konkatenation | Template-Literals `` ` ` `` |
| `document.getElementById()` | `document.querySelector()` mit komplexen Selektoren |

**Grund:** Maximale Browser-Kompatibilität (auch ältere Geräte).

---

### Checkliste Lernpfad (LP)

- [ ] Fachfarbe `#c41e3a` durchgängig verwendet
- [ ] Container max. 900px, zentriert
- [ ] Keine Gradients, Box-shadows, border-radius > 3px
- [ ] Navigation sticky mit Step-Dots
- [ ] Fortschrittsanzeige (%)
- [ ] Erste Karte hat `class="card visible"`
- [ ] localStorage-Persistenz implementiert
- [ ] Reset nur mit Bestätigungsdialog
- [ ] Eingabetoleranz für deutsche Tastatur
- [ ] ES5-kompatibles JavaScript
- [ ] Hefter-Hinweise nach Content-Schritten
- [ ] Feedback-Boxen (ok/partial/wrong)

---

## PowerPoint-Präsentationen (PPT)

### Generierung

**Generator-Skript:** `templates/spanisch/generate_all_pptx.py`

**Verwendung:**
```bash
cd /path/to/sciencesim-lernpfade
python3 templates/spanisch/generate_all_pptx.py
```

**Ausgabe:** Alle 32 Präsentationen (PPT-XXy.pptx) in den jeweiligen Lektionsordnern.

### Generator-Architektur

| Datei | Beschreibung |
|-------|--------------|
| `spanisch_pptx_generator.py` | Klasse `SpanischPPTX` mit Slide-Methoden |
| `generate_all_pptx.py` | LESSONS-Dictionary + Batch-Generierung |

**Technische Details:**
- Basiert auf ChalkSheet-Template (keine echten Tabellen → keine Repair-Warnungen)
- 16:9 Format (13.333" × 7.5")
- Shape-basierte "Tabellen" statt python-pptx Tables
- Fachfarbe Karminrot (#c41e3a)

### Slide-Typen

| Methode | Beschreibung |
|---------|--------------|
| `add_title_slide()` | Titelfolie mit Flagge |
| `add_vocab_slide()` | Vokabelliste (Spanisch/Deutsch) |
| `add_grammar_slide()` | Grammatik-Erklärung |
| `add_exercise_slide()` | Übung mit Lücken |
| `add_solution_slide()` | Lösungsfolie (grün) |
| `add_summary_slide()` | Zusammenfassung |
| `add_homework_slide()` | Hausaufgaben |
| `add_map_slide()` | Karte (mit Bild-Support) |
| `add_content_slide()` | Generischer Inhalt |

### AB-Referenzen in Präsentationen

Jede Übungs- und Vokabelfolie kann auf das Arbeitsblatt verweisen:

```python
pptx.add_vocab_slide(
    title="Begrüßungen",
    vocab=[("Hola", "Hallo"), ...],
    ab_ref="AB-01a: Kasten 1"  # Referenz auf Arbeitsblatt
)
```

**PFLICHT:** Alle AB-Referenzen müssen mit tatsächlichen AB-Aufgaben übereinstimmen!

### Checkliste PPT

- [ ] Alle 32 Präsentationen generiert
- [ ] Keine PowerPoint-Repair-Warnungen
- [ ] AB-Referenzen korrekt (Aufgabennummern prüfen!)
- [ ] Konsistente Sequenz- und Lektionsbezeichnungen
- [ ] Keine Schulnamen (Anonymität)

---

## Arbeitsblätter (AB)

### Punkteformat

**RICHTIG:** `_/3` (Unterstrich als Platzhalter)
**FALSCH:** `/3`

```latex
\newcommand{\punktebox}[1]{\hfill\fbox{\small \_/#1}}
```

### Gesamtpunkte

Am Ende des AB:
```latex
\begin{flushright}
\textbf{Punkte:} \luecke{1cm} / [GESAMT]
\end{flushright}
```

---

## Ordnerstruktur

```
projects/spanisch/kl07/
├── ANLEITUNG-SPANISCH.md          ← Diese Datei
├── JAHRESSEQUENZ.md               ← Jahresübersicht
│
├── sequenz-01-empezamos/
│   ├── 01a-rally-begruessung/
│   │   ├── LE-01a.tex
│   │   ├── AB-01a.tex
│   │   ├── ML-01a.tex
│   │   ├── LH-01a.tex
│   │   ├── LP-01a.html
│   │   └── MT-01a.html (optional)
│   ├── 01b-vorstellen-ser/
│   ├── 01c-artikel-alphabet/
│   ├── 01d-quetal-test/
│   │   └── TEST-01.html          ← Sequenztest
│   └── TEST-01-papier.tex        ← Papierversion
│
├── sequenz-02-mi-vida/
│   ├── 02a-.../
│   └── ...
│
└── repaso-01/
    ├── KA-01.tex                  ← Klassenarbeit
    └── KA-01-digital.html
```

---

## Checkliste pro Doppelstunde

**Pflichtmaterialien:**
- [ ] LE erstellt (Tier 1, vollständig)
- [ ] AB erstellt (Punkteformat `_/X`)
- [ ] ML erstellt (Lösungen in rot)
- [ ] LH erstellt (Differenzierung sichtbar)
- [ ] LP erstellt (Navigation, Persistenz, Eingabetoleranz)
- [ ] Alle PDFs kompiliert

**Minitest (PFLICHT für jede Doppelstunde):**
- [ ] MT-XXy.html erstellt (digital, kein Reset, 24h Auto-Reset)
- [ ] MT-XXy.tex erstellt (Papierversion)
- [ ] MT-XXy-ML.tex erstellt (Musterlösung)
- [ ] Mind. 25 BE
- [ ] 14-NP-Skala implementiert

## Checkliste pro Sequenz

**Alle Doppelstunden (a, b, c):**
- [ ] Alle Pflichtmaterialien komplett
- [ ] Alle Minitests (digital + Papier)

**Sequenzabschluss (d-Lektion):**
- [ ] SL-XXd.html erstellt (digital, kein Reset, 24h Auto-Reset)
- [ ] SL-XXd.tex erstellt (Papierversion)
- [ ] SL-XXd-ML.tex erstellt (Musterlösung)
- [ ] 25-50 BE (umfangreicher als Minitest)
- [ ] 14-NP-Bewertung implementiert
- [ ] Alle PDFs kompiliert

---

## Versionshistorie

| Datum | Änderung |
|-------|----------|
| 2024-12-30 | Initiale Version erstellt |
| 2024-12-30 | LP-Spezifikation erweitert: HTML-Layout, Komponenten, localStorage-Schema, ES5-Pflicht |
| 2024-12-31 | Testkonzept überarbeitet: Minitest PFLICHT pro Doppelstunde (25 BE), Retention ohne Reset, 24h Auto-Reset, Lehrer-Reset via Knopf+PIN, immer digital + Papier |
| 2024-12-31 | LP-Konzept präzisiert: Offline (AB+Buch) reicht immer, LP ist optionale Ergänzung |
| 2024-12-31 | LP-Mindestumfang definiert: 8-12 Schritte, 4-6 Übungen, keine mageren LPs |
| 2024-12-31 | **PPT-Workflow hinzugefügt:** Generator-Skripte, Slide-Typen, AB-Referenzen |
| 2024-12-31 | **Anonymität:** Alle Materialien schulneutral (keine Schulnamen) |
| 2024-12-31 | **Eingabetoleranz erweitert:** Deutsch UND Spanisch als korrekte Antworten akzeptieren |
