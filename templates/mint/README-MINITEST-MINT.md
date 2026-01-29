# MINT-Minitest Template

## Übersicht

Dieses Template definiert Regeln und Code-Snippets für digitale Minitests/Stundenleistungen in MINT-Fächern (Physik, Chemie, Informatik, Mathematik).

---

## 1. Grundstruktur

### 1.1 Dateikonvention

```
MT-[DS]-[kurzname].html
```

- **MT** = Minitest/Stundenleistung
- **DS** = Doppelstunde (z.B. 08b)
- **kurzname** = Thema (max. 20 Zeichen, keine Umlaute)

### 1.2 HTML-Grundgerüst

```html
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Stundenleistung: [THEMA]</title>
    <style>
        /* CSS hier (siehe Abschnitt 2) */
    </style>
</head>
<body>
    <header>
        <h1>Stundenleistung: [THEMA]</h1>
        <div class="header-info">
            <div class="meta">[FACH] Klasse [X] | Differenziert (★/★★/★★★)</div>
        </div>
    </header>

    <!-- Platz + Niveau Auswahl -->
    <!-- Progress Bar -->
    <!-- Container mit Fragen -->
    <!-- Submit + Results Section -->

    <script>
        /* JavaScript hier (siehe Abschnitt 4) */
    </script>
</body>
</html>
```

---

## 2. Farbsystem (CSS-Variablen)

```css
/* Fachfarben */
--physik: #2c5aa0;      /* Blau */
--chemie: #2a7a4b;      /* Grün */
--informatik: #b35c00;  /* Orange */
--mathematik: #7b1fa2;  /* Violett */

/* Feedback */
--success: #2a7a4b;
--warning: #b35c00;
--error: #c62828;

/* Ladungen/Pole (Physik) */
--positive: #c62828;    /* ROT: +, Nordpol */
--negative: #1565c0;    /* BLAU: -, Südpol */

/* Niveau-Farben */
.niveau-1 { background: #e8f5e9; color: #2a7a4b; }  /* ★ Grün */
.niveau-2 { background: #e3f2fd; color: #2c5aa0; }  /* ★★ Blau */
.niveau-3 { background: #f3e5f5; color: #7b1fa2; }  /* ★★★ Violett */

/* Unbeantwortete Fragen/Dropdowns */
.question.unanswered { background: #fff3e0 !important; }
select.unanswered { border: 2px solid var(--warning) !important; }
```

---

## 3. Fragetypen

### 3.1 Single-Choice (Radio)

**BE-Wert:** 1 BE

```html
<div class="question" id="q1" data-niveau="1" data-points="1">
    <div class="question-header">
        <div class="question-title">Frage 1: [TITEL]</div>
        <div class="question-meta">
            <span class="question-niveau niveau-1">★</span>
            <span class="question-points">1 BE</span>
        </div>
    </div>
    <div class="question-text">
        [FRAGETEXT]
    </div>
    <div class="options" id="q1-options">
        <label class="option" data-value="a">
            <input type="radio" name="q1" value="a">
            [Option A]
        </label>
        <label class="option" data-value="b">
            <input type="radio" name="q1" value="b">
            [Option B]
        </label>
        <!-- Weitere Optionen (c, d, e, f) -->
    </div>
    <div class="feedback-box correct" id="q1-fb-correct">[Feedback richtig]</div>
    <div class="feedback-box incorrect" id="q1-fb-incorrect">[Feedback falsch]</div>
</div>
```

**JavaScript-Auswertung:**
```javascript
var q1Correct = userAnswers.q1 === answers.q1;
var q1Pts = q1Correct ? 1 : 0;
score += q1Pts;
markRadioQuestion('q1', answers.q1, userAnswers.q1);
showFeedback('q1', q1Correct);
showQuestionResult('q1', q1Pts, 1);
```

---

### 3.2 Multi-Select (Checkboxen)

**BE-Wert:** 0,5 BE pro richtige Antwort, -0,5 BE pro falsche

```html
<div class="question" id="q4" data-niveau="1" data-points="1">
    <div class="question-header">
        <div class="question-title">Frage 4: [TITEL]</div>
        <div class="question-meta">
            <span class="question-niveau niveau-1">★</span>
            <span class="question-points">1 BE</span>
        </div>
    </div>
    <div class="question-text">
        [FRAGETEXT] <strong>(Mehrfachauswahl, 0,5 BE pro richtige Antwort, -0,5 BE pro falsche)</strong>
    </div>
    <div class="options multi-select" id="q4-options">
        <label class="option" data-value="a">
            <input type="checkbox" name="q4" value="a">
            [Option A]
        </label>
        <label class="option" data-value="b">
            <input type="checkbox" name="q4" value="b">
            [Option B]
        </label>
        <!-- Weitere Optionen -->
    </div>
    <div class="feedback-box correct" id="q4-fb-correct">[Feedback]</div>
    <div class="feedback-box incorrect" id="q4-fb-incorrect">[Feedback]</div>
</div>
```

**JavaScript-Auswertung:**
```javascript
// answers.q4 = ['c', 'e'] (Array der richtigen Optionen)
var q4Score = scoreMultiSelect('q4', answers.q4, userAnswers.q4, 1);
score += q4Score;
showFeedback('q4', q4Score === 1);
showQuestionResult('q4', q4Score, 1);

// Hilfsfunktion
function scoreMultiSelect(qId, correctAnswers, userAnswers, maxPoints) {
    var qOptions = document.querySelectorAll('#' + qId + '-options .option');
    var score = 0;

    for (var i = 0; i < qOptions.length; i++) {
        var val = qOptions[i].dataset.value;
        var isCorrectAnswer = correctAnswers.indexOf(val) !== -1;
        var wasSelected = userAnswers.indexOf(val) !== -1;

        if (isCorrectAnswer && wasSelected) {
            score += 0.5;
            qOptions[i].classList.add('correct');
        } else if (isCorrectAnswer && !wasSelected) {
            qOptions[i].classList.add('missed');
        } else if (!isCorrectAnswer && wasSelected) {
            score -= 0.5;
            qOptions[i].classList.add('incorrect');
        }
    }
    return Math.max(0, Math.min(score, maxPoints));
}
```

---

### 3.3 Dropdown-Zuordnung

**BE-Wert:** 1 BE pro Dropdown

```html
<div class="question" id="q6" data-niveau="1" data-points="2">
    <div class="question-header">
        <div class="question-title">Frage 6: [TITEL]</div>
        <div class="question-meta">
            <span class="question-niveau niveau-1">★</span>
            <span class="question-points">2 BE</span>
        </div>
    </div>
    <div class="question-text">
        Ordne die Symbole der korrekten Bedeutung zu:
    </div>
    <div style="margin: 15px 0;">
        <div style="display:flex;align-items:center;gap:10px;margin:10px 0;">
            <span>[Symbol/Label]</span>
            <select id="q6-a" style="padding:8px;flex:1;max-width:300px;">
                <option value="">-- Auswählen --</option>
                <option value="option1">[Option 1]</option>
                <option value="option2">[Option 2]</option>
            </select>
        </div>
        <div style="display:flex;align-items:center;gap:10px;margin:10px 0;">
            <span>[Symbol/Label]</span>
            <select id="q6-b" style="padding:8px;flex:1;max-width:300px;">
                <option value="">-- Auswählen --</option>
                <option value="option1">[Option 1]</option>
                <option value="option2">[Option 2]</option>
            </select>
        </div>
    </div>
    <div class="feedback-box correct" id="q6-fb-correct">[Feedback]</div>
    <div class="feedback-box incorrect" id="q6-fb-incorrect">[Feedback]</div>
</div>
```

**JavaScript-Auswertung:**
```javascript
// answers.q6a = 'option1', answers.q6b = 'option2'
var q6Score = 0;
var q6aEl = document.getElementById('q6-a');
var q6bEl = document.getElementById('q6-b');
if (userAnswers.q6a === answers.q6a) { q6Score++; q6aEl.classList.add('correct'); }
else { q6aEl.classList.add('incorrect'); }
if (userAnswers.q6b === answers.q6b) { q6Score++; q6bEl.classList.add('correct'); }
else { q6bEl.classList.add('incorrect'); }
score += q6Score;
showFeedback('q6', q6Score === 2);
showQuestionResult('q6', q6Score, 2);
```

---

### 3.4 Szenario-Grid mit SVG + Dropdown

**BE-Wert:** 1 BE pro Szenario

```html
<div class="question" id="q22" data-niveau="1" data-points="2">
    <div class="question-header">
        <div class="question-title">Frage 22: Lorentzkraft bestimmen</div>
        <div class="question-meta">
            <span class="question-niveau niveau-1">★</span>
            <span class="question-points">2 BE</span>
        </div>
    </div>
    <div class="question-text">
        Bestimme die Richtung der Lorentzkraft. Das Magnetfeld zeigt von N nach S = ↑
    </div>
    <div class="scenario-grid">
        <div class="scenario" id="scenario-a">
            <div class="scenario-label">a) Strom nach rechts (→)</div>
            <svg viewBox="0 0 120 100" width="120">
                <!-- SVG-Inhalt -->
            </svg>
            <select id="q22-a">
                <option value="">-- Richtung --</option>
                <option value="oben">Nach oben ↑</option>
                <option value="unten">Nach unten ↓</option>
                <option value="heraus">Heraus ⊙</option>
                <option value="hinein">Hinein ⊗</option>
            </select>
        </div>
        <div class="scenario" id="scenario-b">
            <div class="scenario-label">b) Strom nach links (←)</div>
            <svg viewBox="0 0 120 100" width="120">
                <!-- SVG-Inhalt -->
            </svg>
            <select id="q22-b">
                <option value="">-- Richtung --</option>
                <option value="oben">Nach oben ↑</option>
                <option value="unten">Nach unten ↓</option>
                <option value="heraus">Heraus ⊙</option>
                <option value="hinein">Hinein ⊗</option>
            </select>
        </div>
    </div>
    <div class="feedback-box correct" id="q22-fb-correct">Richtig! a) heraus, b) hinein.</div>
    <div class="feedback-box incorrect" id="q22-fb-incorrect">Rechte-Hand-Regel anwenden!</div>
</div>
```

---

### 3.5 Bild-Auswahl (SVG-Optionen)

**BE-Wert:** 1 BE

```html
<div class="question" id="q24" data-niveau="2" data-points="1">
    <div class="question-header">
        <div class="question-title">Frage 24: Magnetische Polung einer Spule</div>
        <div class="question-meta">
            <span class="question-niveau niveau-2">★★</span>
            <span class="question-points">1 BE</span>
        </div>
    </div>
    <div class="question-text">
        Die Spule ist an eine Spannungsquelle angeschlossen. Welche magnetische Polung entsteht?
    </div>
    <div class="diagram" style="text-align:center; margin: 15px 0;">
        <!-- Haupt-SVG mit Aufgabenstellung -->
        <svg viewBox="0 0 280 140" width="320">
            <!-- Spulen-Darstellung -->
        </svg>
    </div>
    <div class="options-grid" style="display:grid; grid-template-columns: 1fr 1fr; gap:10px;">
        <label class="option" data-value="a" style="padding:10px; text-align:center;">
            <input type="radio" name="q24" value="a">
            <svg viewBox="0 0 160 50" width="140" style="display:block; margin:5px auto;">
                <!-- Option A SVG -->
            </svg>
        </label>
        <label class="option" data-value="b" style="padding:10px; text-align:center;">
            <input type="radio" name="q24" value="b">
            <svg viewBox="0 0 160 50" width="140" style="display:block; margin:5px auto;">
                <!-- Option B SVG -->
            </svg>
        </label>
        <!-- Weitere Optionen -->
    </div>
    <div class="feedback-box correct" id="q24-fb-correct">[Feedback]</div>
    <div class="feedback-box incorrect" id="q24-fb-incorrect">[Feedback]</div>
</div>
```

---

## 4. JavaScript-Kernfunktionen

### 4.1 Konfiguration

```javascript
// Eindeutige ID für localStorage
var STORAGE_KEY = 'mt-[FACH]-[KLASSE]-[DS]-[THEMA]';

// Niveau-Variablen
var selectedNiveau = 0;
var testSubmitted = false;

// BE pro Niveau
var niveauPoints = {
    1: 25.5,  // ★ (Basis)
    2: 30.5,  // ★★ (Standard)
    3: 32.5   // ★★★ (Erweitert)
};

// Korrekte Antworten
var answers = {
    // ★ Niveau
    q1: 'b',
    q2: 'b',
    q3: 'a',
    q4: ['c', 'e'],  // Multi-Select: Array
    q5: 'd',
    q6a: 'heraus',   // Dropdown
    q6b: 'hinein',
    // ★★ Niveau
    q20: 'b',
    q21: 'c',
    // ★★★ Niveau
    q25: 'd',
    q26: 'c'
};
```

### 4.2 Platz-/Niveau-Sperrung

```javascript
function confirmSeat() {
    var select = document.getElementById('seatSelect');
    var num = select.value;
    if (!num) { alert('Bitte wähle zuerst eine Platznummer!'); return; }

    var ok = confirm('Platznummer P' + num + ' bestätigen?\n\nDiese Auswahl kann NICHT mehr geändert werden!');
    if (!ok) return;

    localStorage.setItem(STORAGE_KEY + '-seat', num);
    localStorage.setItem(STORAGE_KEY + '-seat-locked', 'true');
    document.getElementById('seatNumber').value = num;
    showLockedSeat(num);
}

function confirmNiveau() {
    var select = document.getElementById('niveauSelect');
    var val = select.value;
    if (!val) { alert('Bitte wähle zuerst ein Niveau!'); return; }

    var niveauStars = ['', '★ Basis', '★★ Standard', '★★★ Erweitert'][parseInt(val)];
    var ok = confirm('Niveau "' + niveauStars + '" bestätigen?\n\nDiese Auswahl kann NICHT mehr geändert werden!');
    if (!ok) return;

    localStorage.setItem(STORAGE_KEY + '-niveau', val);
    localStorage.setItem(STORAGE_KEY + '-niveau-locked', 'true');
    selectedNiveau = parseInt(val);
    showLockedNiveau(val);
    selectNiveau(selectedNiveau);
}
```

### 4.3 Fortschrittsanzeige

```javascript
function isQuestionAnswered(qId) {
    switch(qId) {
        case 'q1': return !!document.querySelector('input[name="q1"]:checked');
        case 'q4': return !!document.querySelector('input[name="q4"]:checked');
        case 'q6': return document.getElementById('q6-a').value && document.getElementById('q6-b').value;
        // Weitere Fragen...
        default: return false;
    }
}

function countAnsweredQuestions() {
    if (selectedNiveau === 0) return { answered: 0, total: 0 };
    var answered = 0, total = 0;
    var questions = document.querySelectorAll('.question');

    for (var i = 0; i < questions.length; i++) {
        var qNiveau = parseInt(questions[i].dataset.niveau);
        if (qNiveau <= selectedNiveau) {
            total++;
            if (isQuestionAnswered(questions[i].id)) answered++;
        }
    }
    return { answered: answered, total: total };
}

function updateProgress() {
    var status = countAnsweredQuestions();
    var percent = status.total > 0 ? (status.answered / status.total) * 100 : 0;
    document.getElementById('progressFill').style.width = percent + '%';
    document.getElementById('progressText').textContent =
        status.answered + ' / ' + status.total + ' beantwortet (' + niveauPoints[selectedNiveau] + ' BE)';
}
```

### 4.4 Niveau-abhängige Bewertung

```javascript
function submitTest() {
    if (testSubmitted) return;

    // Prüfungen...
    testSubmitted = true;
    var userAnswers = collectAllAnswers();
    var score = 0;
    var maxPoints = niveauPoints[selectedNiveau];

    // ===== NIVEAU 1 (★) =====
    if (selectedNiveau >= 1) {
        // Q1 bewerten
        var q1Correct = userAnswers.q1 === answers.q1;
        var q1Pts = q1Correct ? 1 : 0;
        score += q1Pts;
        markRadioQuestion('q1', answers.q1, userAnswers.q1);
        showFeedback('q1', q1Correct);
        showQuestionResult('q1', q1Pts, 1);
    }

    // ===== NIVEAU 2 (★★) =====
    // Fragen mit notGraded-Flag für niedrigere Niveaus
    var q20NotGraded = selectedNiveau < 2;
    var q20Correct = userAnswers.q20 === answers.q20;
    var q20Pts = q20Correct ? 1 : 0;
    if (!q20NotGraded) score += q20Pts;
    markRadioQuestion('q20', answers.q20, userAnswers.q20);
    showFeedback('q20', q20Correct);
    showQuestionResult('q20', q20Pts, 1, q20NotGraded);

    // ===== NIVEAU 3 (★★★) =====
    var q25NotGraded = selectedNiveau < 3;
    // ... (analog)

    displayResults(score, maxPoints);
}
```

### 4.5 Hilfsfunktionen

```javascript
function markRadioQuestion(name, correct, selected) {
    var options = document.querySelectorAll('#' + name + '-options .option');
    for (var i = 0; i < options.length; i++) {
        var val = options[i].dataset.value;
        if (val === correct) options[i].classList.add('correct');
        else if (val === selected && val !== correct) options[i].classList.add('incorrect');
    }
}

function showFeedback(qId, isCorrect) {
    var fbCorrect = document.getElementById(qId + '-fb-correct');
    var fbIncorrect = document.getElementById(qId + '-fb-incorrect');
    if (isCorrect && fbCorrect) fbCorrect.classList.add('show');
    else if (!isCorrect && fbIncorrect) fbIncorrect.classList.add('show');
}

function showQuestionResult(qId, achieved, maxPts, notGraded) {
    var question = document.getElementById(qId);
    var meta = question.querySelector('.question-meta');

    var result = document.createElement('span');
    result.className = 'question-result';

    if (notGraded) {
        result.style.background = '#f0f0f0';
        result.style.color = '#888';
        result.textContent = '(' + achieved + ')/' + maxPts + ' BE';
    } else {
        if (achieved === maxPts) result.classList.add('full');
        else if (achieved > 0) result.classList.add('partial');
        else result.classList.add('zero');
        result.textContent = achieved + '/' + maxPts + ' BE';
    }
    meta.appendChild(result);
}
```

### 4.6 setupOptions() mit IIFE-Closure (WICHTIG!)

**Problem:** In einer `for`-Schleife referenzieren Event-Listener dieselbe Variable. Beim Klick zeigen alle Handler auf das letzte Element.

**Lösung:** IIFE (Immediately Invoked Function Expression) erstellt eigenen Scope pro Iteration:

```javascript
function setupOptions(containerId) {
    var container = document.getElementById(containerId);
    if (!container) {
        console.error('Container not found: ' + containerId);
        return;  // Null-Check verhindert Fehler
    }
    var options = container.querySelectorAll('.option');
    for (var i = 0; i < options.length; i++) {
        (function(opt) {  // IIFE für korrektes Scoping
            var input = opt.querySelector('input');
            var isCheckbox = input && input.type === 'checkbox';

            opt.addEventListener('click', function(e) {
                e.preventDefault();

                if (isCheckbox) {
                    // Multi-Select: Toggle
                    opt.classList.toggle('selected');
                    if (input) input.checked = opt.classList.contains('selected');
                } else {
                    // Single-Select: Siblings deselektieren
                    var siblings = opt.parentNode.querySelectorAll('.option');
                    for (var j = 0; j < siblings.length; j++) {
                        siblings[j].classList.remove('selected');
                        var sib = siblings[j].querySelector('input');
                        if (sib) sib.checked = false;
                    }
                    opt.classList.add('selected');
                    if (input) input.checked = true;
                }
            });
        })(options[i]);  // options[i] wird als 'opt' übergeben
    }
}
```

### 4.7 markDropdown() - Dropdown-Auswertung

Einheitliche visuelle Markierung von Dropdown-Antworten:

| Zustand | Darstellung |
|---------|-------------|
| Richtig | Grüner Rand |
| Falsch | Roter Rand + richtige Option grün hinterlegt |
| Nicht beantwortet | Oranger Rand |

```javascript
function markDropdown(selectEl, correctVal, userVal) {
    if (!selectEl) return;
    if (userVal === correctVal) {
        selectEl.classList.add('correct');
    } else if (userVal && userVal !== correctVal) {
        selectEl.classList.add('incorrect');
        // Richtige Option grün markieren
        var opts = selectEl.options;
        for (var i = 0; i < opts.length; i++) {
            if (opts[i].value === correctVal) {
                opts[i].style.background = '#e8f5e9';
                opts[i].style.fontWeight = 'bold';
            }
        }
    } else if (!userVal) {
        selectEl.classList.add('unanswered');
    }
}
```

**Verwendung:**
```javascript
// Statt manuell:
if (userAnswers.q6a === answers.q6a) { q6aEl.classList.add('correct'); }
else { q6aEl.classList.add('incorrect'); }

// Besser:
markDropdown(q6aEl, answers.q6a, userAnswers.q6a);

// Unbeantwortete Frage markieren:
if (!userAnswers.q6a || !userAnswers.q6b) {
    document.getElementById('q6').classList.add('unanswered');
}
```

---

## 5. SVG-Vorlagen

### 5.1 Magnetfeld (Punkt/Kreuz)

```html
<!-- Strom heraus (Punkt) -->
<circle cx="40" cy="50" r="12" fill="#666" stroke="#333"/>
<circle cx="40" cy="50" r="4" fill="#c62828"/>

<!-- Strom hinein (Kreuz) -->
<circle cx="40" cy="50" r="12" fill="#666" stroke="#333"/>
<line x1="31" y1="41" x2="49" y2="59" stroke="#c62828" stroke-width="2"/>
<line x1="49" y1="41" x2="31" y2="59" stroke="#c62828" stroke-width="2"/>
```

### 5.2 Magnetpole

```html
<!-- Nordpol (rot) -->
<rect x="10" y="15" width="60" height="20" fill="#c62828"/>
<text x="40" y="29" text-anchor="middle" fill="white" font-size="11" font-weight="bold">N</text>

<!-- Südpol (blau) -->
<rect x="70" y="15" width="60" height="20" fill="#1565c0"/>
<text x="100" y="29" text-anchor="middle" fill="white" font-size="11" font-weight="bold">S</text>
```

### 5.3 Spannungsquelle (DIN)

```html
<!-- Zwei parallele Linien: lang=+, kurz/dick=- -->
<line x1="35" y1="80" x2="65" y2="80" stroke="#c62828" stroke-width="2"/>  <!-- + oben -->
<line x1="40" y1="100" x2="60" y2="100" stroke="#1565c0" stroke-width="4"/>  <!-- - unten -->
<text x="25" y="82" fill="#c62828" font-weight="bold">+</text>
<text x="25" y="102" fill="#1565c0" font-weight="bold">−</text>
```

### 5.4 Ladung in Bewegung

```html
<!-- Elektron (blau, negativ) -->
<circle cx="70" cy="60" r="8" fill="#1565c0"/>
<text x="70" y="64" text-anchor="middle" fill="white" font-size="9" font-weight="bold">−</text>
<line x1="82" y1="60" x2="120" y2="60" stroke="#333" stroke-width="2"/>
<polygon points="120,60 110,55 110,65" fill="#333"/>
<text x="100" y="52" font-size="9">v</text>

<!-- Proton (rot, positiv) -->
<circle cx="70" cy="60" r="8" fill="#c62828"/>
<text x="70" y="64" text-anchor="middle" fill="white" font-size="9" font-weight="bold">+</text>
```

---

## 6. BE-Kalkulation

### 6.1 Fragetypen und BE

| Fragetyp | BE-Wert | Scoring |
|----------|---------|---------|
| Single-Choice | 1 BE | Richtig = 1, Falsch = 0 |
| Multi-Select | 0,5 BE/Option | +0,5 richtig, -0,5 falsch, min 0 |
| Dropdown (1) | 1 BE | Pro Dropdown |
| Dropdown (2) | 2 BE | 2 Dropdowns à 1 BE |
| SVG-Auswahl | 1 BE | Wie Single-Choice |

### 6.2 Niveau-Struktur

```
★ (Basis):     Q1-Q19 + Q22 → ~25 BE
★★ (Standard): + Q20, Q21, Q23, Q24 → ~30 BE
★★★ (Erweitert): + Q25, Q26 → ~32 BE
```

**Regel:** Jedes höhere Niveau enthält ALLE Fragen der niedrigeren Niveaus.

### 6.3 Notenspiegel (14-NP, Sek I)

```javascript
var thresholds = [100, 96, 90.67, 86, 80, 73.33, 66.67, 60, 53.33, 46.67, 40, 33.33, 26.67, 20];
// NP:           14   13    12    11   10    9      8     7     6      5     4     3      2     1
```

---

## 7. Wichtige Regeln

### 7.1 JavaScript: Nur ES5!

```javascript
// RICHTIG (ES5)
var x = 5;
function foo() { return x; }
for (var i = 0; i < arr.length; i++) { }

// FALSCH (ES6+)
let x = 5;           // ❌
const y = 10;        // ❌
arr.forEach(item => { });  // ❌
```

### 7.2 Antworten mischen

Korrekte Antworten NICHT immer an Position 'a' oder 'b'. Mischen, um Muster zu vermeiden.

### 7.3 Feedback

Jede Frage braucht BEIDE Feedback-Boxen:
- `id="qX-fb-correct"` — Lob + kurze Erklärung
- `id="qX-fb-incorrect"` — Richtige Antwort + Hinweis

### 7.4 localStorage-Persistenz

Alle Eingaben speichern für Reload-Schutz:
```javascript
function saveProgress() {
    var data = { answers: collectAllAnswers(), timestamp: new Date().toISOString() };
    localStorage.setItem(STORAGE_KEY, JSON.stringify(data));
}
```

### 7.5 Drucken

CSS für @media print:
```css
@media print {
    button, .progress-container, .niveau-selection, .selection-row { display: none; }
    .question { page-break-inside: avoid; }
}
```

### 7.6 Lehrer-Reset

Jeder Minitest enthält einen Lehrer-Bereich zum Zurücksetzen eines Platzes:

```javascript
function teacherReset() {
    var code = prompt('Lehrer-Code eingeben:');
    if (code === '2024') {  // Standard-Code
        localStorage.removeItem(STORAGE_KEY);
        alert('Platz wurde zurückgesetzt. Seite wird neu geladen.');
        location.reload();
    } else if (code !== null) {
        alert('Falscher Code!');
    }
}
```

**Standard-Rücksetzcode:** `2024`

**Wichtig:** Den Code im QR-MT-Dokument für Lehrkräfte dokumentieren!

---

## 8. Checkliste vor Freigabe

### 8.1 Grundlegend

- [ ] STORAGE_KEY eindeutig?
- [ ] Alle Fragetypen korrekt implementiert?
- [ ] answers-Objekt vollständig?
- [ ] isQuestionAnswered für alle Fragen?
- [ ] collectAllAnswers vollständig?
- [ ] restoreAnswers vollständig?
- [ ] Scoring pro Niveau korrekt?
- [ ] niveauPoints aktualisiert?
- [ ] BE-Summen korrekt?
- [ ] Feedback für alle Fragen?
- [ ] Fachliche Korrektheit geprüft?
- [ ] Im Browser getestet?

### 8.2 Interaktivität (NEU)

- [ ] setupOptions() verwendet IIFE-Closure? (nicht `options[i]` im Handler!)
- [ ] markDropdown() für alle Dropdowns verwendet?
- [ ] Unbeantwortete Fragen/Dropdowns mit `.unanswered` markiert?
- [ ] options-grid funktioniert? (SVG-Optionen klickbar)

---

## 9. Anti-Betrug: Zeitstempel-System

### 9.1 Übersicht

Jeder Minitest speichert automatisch zwei Zeitstempel zur Betrugsverhinderung:

| Zeitstempel | localStorage-Key | Wird gespeichert... |
|-------------|------------------|---------------------|
| **Aufruf** | `STORAGE_KEY + '-start'` | Beim ersten Öffnen der Seite |
| **Abgabe** | `STORAGE_KEY + '-submit-time'` | Beim Klick auf "Test abgeben" |

### 9.2 Implementierung

**1. Startzeit speichern (in `window.onload`):**
```javascript
// Startzeit beim ersten Aufruf speichern (Anti-Betrug)
var startTime = localStorage.getItem(STORAGE_KEY + '-start');
if (!startTime) {
    localStorage.setItem(STORAGE_KEY + '-start', Date.now());
}
```

**2. Abgabezeit speichern (in `submitTest()`):**
```javascript
testSubmitted = true;
localStorage.setItem(STORAGE_KEY + '-submit-time', Date.now());
```

**3. Zeitstempel formatieren (Hilfsfunktion):**
```javascript
function formatTimestamp(ts) {
    if (!ts) return '—';
    var d = new Date(parseInt(ts));
    var day = d.getDate();
    var month = d.getMonth() + 1;
    var year = d.getFullYear();
    var hours = d.getHours();
    var minutes = d.getMinutes();
    return (day < 10 ? '0' : '') + day + '.' +
           (month < 10 ? '0' : '') + month + '.' + year + ' ' +
           (hours < 10 ? '0' : '') + hours + ':' +
           (minutes < 10 ? '0' : '') + minutes + ' Uhr';
}
```

**4. Zeitstempel anzeigen (am Ende von `displayResults()`):**
```javascript
// Zeitstempel anzeigen (Anti-Betrug)
var startTS = localStorage.getItem(STORAGE_KEY + '-start');
var submitTS = localStorage.getItem(STORAGE_KEY + '-submit-time');
var timestampHtml = '<div style="margin-top:20px; padding:12px; background:#f5f5f5; border:1px solid #ddd; text-align:left; font-size:0.85em;">' +
    '<div><strong>Aufruf:</strong> ' + formatTimestamp(startTS) + '</div>' +
    '<div><strong>Abgabe:</strong> ' + formatTimestamp(submitTS) + '</div>' +
    '</div>';
document.getElementById('resultsSection').insertAdjacentHTML('beforeend', timestampHtml);
```

### 9.3 Anzeige im Ergebnis

Nach Testabgabe erscheint im Ergebnisbereich:

```
┌─────────────────────────────────────────┐
│  Aufruf: 19.01.2026 09:15 Uhr          │
│  Abgabe: 19.01.2026 09:28 Uhr          │
└─────────────────────────────────────────┘
```

### 9.4 Nutzen für Lehrkräfte

- **Bearbeitungszeit prüfbar:** Differenz Abgabe - Aufruf
- **Auffälligkeiten erkennen:** Sehr kurze oder sehr lange Zeiten
- **PDF-Export:** Zeitstempel werden mit ausgedruckt
- **Persistent:** Auch nach Reload sichtbar

### 9.5 Checkliste Zeitstempel

- [ ] `formatTimestamp()` Funktion vorhanden?
- [ ] Startzeit wird in `window.onload` gespeichert?
- [ ] Abgabezeit wird in `submitTest()` gespeichert?
- [ ] Zeitstempel werden in `displayResults()` angezeigt?
- [ ] Zeitstempel erscheinen im PDF-Druck?

---

## 10. Fragen-Ausblendung bis Identifikation

### 10.1 Übersicht

Fragen werden erst angezeigt, **nachdem** der Schüler:
1. Seine **Platznummer** mit OK bestätigt hat
2. Sein **Niveau** mit OK bestätigt hat

Beide Bestätigungen sind persistent (localStorage) und können nicht mehr geändert werden.

### 10.2 HTML-Struktur

**Unlock-Hinweis (sichtbar bis Freigabe):**
```html
<div class="unlock-hint" id="unlockHint">
    <strong>Bitte bestätige zuerst:</strong><br>
    1. Deine Platznummer (mit OK)<br>
    2. Dein Niveau (mit OK)<br><br>
    Danach werden die Aufgaben angezeigt.
</div>
```

**Fragen-Container (ausgeblendet bis Freigabe):**
```html
<div id="questionsContainer">
    <!-- Alle .question Elemente + submitSection + resultsSection -->
</div><!-- END questionsContainer -->
```

### 10.3 CSS

```css
/* Fragen standardmäßig ausgeblendet */
#questionsContainer { display: none; }
#questionsContainer.unlocked { display: block; }

/* Hinweis-Box */
.unlock-hint {
    background: #fff3e0;
    border: 2px solid #b35c00;
    padding: 20px;
    margin: 20px 0;
    text-align: center;
    color: #b35c00;
}
```

### 10.4 JavaScript

**checkUnlocked() Funktion:**
```javascript
function checkUnlocked() {
    var seatLocked = localStorage.getItem(STORAGE_KEY + '-seat-locked') === 'true';
    var niveauLocked = localStorage.getItem(STORAGE_KEY + '-niveau-locked') === 'true';
    var container = document.getElementById('questionsContainer');
    var hint = document.getElementById('unlockHint');

    if (seatLocked && niveauLocked) {
        container.classList.add('unlocked');
        hint.style.display = 'none';
    } else {
        container.classList.remove('unlocked');
        hint.style.display = 'block';
    }
}
```

**Aufrufe von checkUnlocked():**
- Am Ende von `confirmSeat()`
- Am Ende von `confirmNiveau()`
- In `window.onload` (nach `updateProgress()`)

### 10.5 Checkliste Fragen-Ausblendung

- [ ] CSS für `#questionsContainer` und `.unlock-hint` vorhanden?
- [ ] `<div id="unlockHint">` vor dem questionsContainer?
- [ ] Alle Fragen + submitSection + resultsSection in `<div id="questionsContainer">`?
- [ ] `</div><!-- END questionsContainer -->` am richtigen Ort?
- [ ] `checkUnlocked()` Funktion vorhanden?
- [ ] `checkUnlocked()` wird in `confirmSeat()` aufgerufen?
- [ ] `checkUnlocked()` wird in `confirmNiveau()` aufgerufen?
- [ ] `checkUnlocked()` wird in `window.onload` aufgerufen?

---

## 11. Tab-/App-Wechsel-Protokoll

### 11.1 Übersicht

Das System protokolliert, wenn Schüler während des Tests den Tab/die App wechseln (z.B. um zu googeln). Erfasst wird:

| Information | Beispiel | Erfasst |
|-------------|----------|---------|
| Anzahl Wechsel | `3×` | ✅ |
| Gesamtdauer außerhalb | `2:15 Min.` | ✅ |
| Welche Seite besucht | — | ❌ (technisch unmöglich) |

### 11.2 Was wird erkannt?

| Aktion | Erkannt? |
|--------|----------|
| Anderer Browser-Tab | ✅ Ja |
| Andere App öffnen | ✅ Ja |
| Browser minimieren | ✅ Ja |
| Bildschirm sperren | ✅ Ja |
| Split-Screen (beide sichtbar) | ⚠️ Teilweise |
| Zweites Gerät | ❌ Nein |

### 11.3 Implementierung

**Variablen (im Konfigurationsbereich):**
```javascript
// Tab-Wechsel-Protokoll (Anti-Betrug)
var tabSwitchCount = 0;
var tabSwitchStart = 0;
var tabSwitchSeconds = 0;
```

**Tracking-Funktion:**
```javascript
function initTabSwitchTracking() {
    // Gespeicherte Werte laden
    var savedCount = localStorage.getItem(STORAGE_KEY + '-tabswitches');
    var savedSeconds = localStorage.getItem(STORAGE_KEY + '-tabseconds');
    if (savedCount) tabSwitchCount = parseInt(savedCount);
    if (savedSeconds) tabSwitchSeconds = parseInt(savedSeconds);

    document.addEventListener('visibilitychange', function() {
        if (testSubmitted) return;

        if (document.hidden) {
            // Tab verlassen - Startzeit merken
            tabSwitchStart = Date.now();
            tabSwitchCount++;
            localStorage.setItem(STORAGE_KEY + '-tabswitches', tabSwitchCount);
        } else {
            // Tab wieder aktiv - Dauer berechnen
            if (tabSwitchStart > 0) {
                var duration = Math.round((Date.now() - tabSwitchStart) / 1000);
                tabSwitchSeconds += duration;
                localStorage.setItem(STORAGE_KEY + '-tabseconds', tabSwitchSeconds);
                tabSwitchStart = 0;
            }
        }
    });
}

function formatDuration(seconds) {
    if (seconds < 60) return seconds + ' Sek.';
    var min = Math.floor(seconds / 60);
    var sec = seconds % 60;
    return min + ':' + (sec < 10 ? '0' : '') + sec + ' Min.';
}
```

**Aufruf in `window.onload`:**
```javascript
initTabSwitchTracking();
```

**Anzeige in `displayResults()`:**
```javascript
var switches = localStorage.getItem(STORAGE_KEY + '-tabswitches') || '0';
var switchSec = localStorage.getItem(STORAGE_KEY + '-tabseconds') || '0';
// In timestampHtml einfügen:
'<div><strong>Tab-Wechsel:</strong> ' + switches + '× (' + formatDuration(parseInt(switchSec)) + ')</div>'
```

### 11.4 Anzeige im Ergebnis

```
┌─────────────────────────────────────────┐
│  Aufruf:       19.01.2026 09:15 Uhr     │
│  Abgabe:       19.01.2026 09:28 Uhr     │
│  Tab-Wechsel:  3× (2:15 Min.)           │
└─────────────────────────────────────────┘
```

### 11.5 DSGVO-Konformität

- ✅ Nur lokale Speicherung (localStorage)
- ✅ Keine personenbezogenen Daten (nur Platznummer)
- ✅ Keine Übertragung an Server
- ✅ Schüler kann Daten selbst löschen
- ✅ Keine Erfassung besuchter Seiten

### 11.6 Checkliste Tab-Wechsel

- [ ] Variablen `tabSwitchCount`, `tabSwitchStart`, `tabSwitchSeconds` vorhanden?
- [ ] `initTabSwitchTracking()` Funktion vorhanden?
- [ ] `formatDuration()` Funktion vorhanden?
- [ ] `initTabSwitchTracking()` wird in `window.onload` aufgerufen?
- [ ] Tab-Wechsel werden in `displayResults()` angezeigt?
