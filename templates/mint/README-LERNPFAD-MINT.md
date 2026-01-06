# Step-Navigation für MINT-Lernpfade

**Template:** `templates/mint/lernpfad-mint.html`

## Konzept
Klickbare Step-Indikatoren im Header, die:
- Fortschritt visualisieren (grün = abgeschlossen)
- Direktnavigation ermöglichen
- Unterschiedliche Step-Typen kennzeichnen

---

## CSS-Komponenten

### 1. Step-Indicators Container
```css
.step-indicators {
    display: flex;
    gap: 4px;
    margin-top: 10px;
    flex-wrap: wrap;
}
```

### 2. Step-Dot Basis
```css
.step-dot {
    width: 24px;
    height: 24px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 0.7em;
    font-weight: 600;
    border: 2px solid var(--border);
    background: var(--white);
    cursor: pointer;
    transition: all 0.15s;
}

.step-dot:hover {
    border-color: var(--accent);
}
```

### 3. Step-Dot Zustände
```css
/* Abgeschlossen = GRÜN */
.step-dot.completed {
    background: var(--success);
    border-color: var(--success);
    color: var(--white);
}

/* Aktueller Schritt = Blauer dicker Rand */
.step-dot.current {
    border-color: var(--accent);
    border-width: 3px;
    color: var(--accent);
}
```

### 4. Step-Typen (optional)
```css
.step-dot.content { border-style: solid; }
.step-dot.exercise { border-style: dashed; }
.step-dot.simulation { background: var(--accent-light); }
.step-dot.test { background: var(--warning-bg); border-color: var(--warning); }
```

---

## HTML-Struktur

### Progress-Container mit Step-Indicators
```html
<div class="progress-container">
    <div class="progress-header">
        <span class="progress-label">Fortschritt:</span>
        <span class="progress-count">
            <span id="completedSteps">0</span> /
            <span id="totalSteps">7</span> Schritte
        </span>
    </div>
    <div class="progress-bar">
        <div class="progress-fill" id="progressFill"></div>
    </div>
    <!-- Step-Indicators hier -->
    <div class="step-indicators" id="stepIndicators"></div>
</div>
```

---

## JavaScript-Funktionen (ES5!)

### 1. Step-Indicators generieren
```javascript
function generateStepIndicators() {
    var container = document.getElementById('stepIndicators');
    container.innerHTML = '';

    for (var i = 0; i < TOTAL_STEPS; i++) {
        var dot = document.createElement('div');
        dot.className = 'step-dot';
        // Optional: Step-Typ hinzufügen
        // dot.classList.add(steps[i].type);

        if (i === currentStep) dot.classList.add('current');
        if (visitedSteps.indexOf(i) !== -1) dot.classList.add('completed');

        dot.textContent = i + 1;
        dot.setAttribute('data-step', i);
        dot.onclick = function() {
            var stepIndex = parseInt(this.getAttribute('data-step'));
            goToStep(stepIndex);
        };

        container.appendChild(dot);
    }
}
```

### 2. Step-Indicators aktualisieren
```javascript
function updateStepIndicators() {
    var dots = document.querySelectorAll('.step-dot');
    for (var i = 0; i < dots.length; i++) {
        dots[i].classList.remove('current');
        if (i === currentStep) {
            dots[i].classList.add('current');
        }
        if (visitedSteps.indexOf(i) !== -1) {
            dots[i].classList.add('completed');
        }
    }
}
```

### 3. In goToStep() einbinden
```javascript
function goToStep(index) {
    // Aktuellen Step als besucht markieren
    if (visitedSteps.indexOf(currentStep) === -1) {
        visitedSteps.push(currentStep);
    }

    // Alle Steps ausblenden, neuen einblenden
    // ...

    currentStep = index;
    updateStepIndicators();
    updateProgress();
    saveState();
}
```

### 4. State in localStorage
```javascript
var STORAGE_KEY = 'lp-physik-7-kraft-02';

function saveState() {
    var state = {
        currentStep: currentStep,
        visitedSteps: visitedSteps,
        answers: answers
    };
    localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
}

function loadState() {
    var saved = localStorage.getItem(STORAGE_KEY);
    if (saved) {
        try {
            var state = JSON.parse(saved);
            currentStep = state.currentStep || 0;
            visitedSteps = state.visitedSteps || [];
            answers = state.answers || {};
            goToStep(currentStep);
        } catch(e) {
            console.error('State load error:', e);
        }
    }
}
```

---

## Farb-Variablen (CSS :root)

```css
:root {
    --accent: #2c5aa0;      /* Physik-Blau */
    --accent-light: #e8f0fa;
    --success: #2a7a4b;     /* Grün für completed */
    --success-bg: #e8f5e9;
    --warning: #b35c00;     /* Orange für Test-Steps */
    --warning-bg: #fff3e0;
    --border: #dddddd;
    --white: #ffffff;
}

/* Fachfarben */
body.physik { --accent: #2c5aa0; }
body.chemie { --accent: #2a7a4b; }
body.informatik { --accent: #b35c00; }
```

---

## Integration in bestehendes LP

1. CSS oben einfügen (Step-Indicators Styles)
2. HTML: `<div class="step-indicators" id="stepIndicators"></div>` nach progress-bar
3. JS: `generateStepIndicators()` in init()
4. JS: `updateStepIndicators()` in goToStep()
5. JS: visitedSteps Array für State-Tracking

---

## Checkliste für Template-Update

- [x] CSS Variables (:root) hinzufügen
- [x] .step-indicators Container-Styles
- [x] .step-dot Basis + Zustände (.completed, .current)
- [x] Optional: .step-dot Typ-Varianten (.exercise, .simulation)
- [x] HTML: Step-Indicators div im Progress-Bereich
- [x] JS: generateStepIndicators() Funktion
- [x] JS: updateStepIndicators() Funktion
- [x] JS: visitedSteps Array + localStorage Integration
- [x] JS: Klick-Handler für Direktnavigation

---

## Template-Nutzung

### Neuen Lernpfad erstellen

1. `lernpfad-mint.html` kopieren nach `projects/[fach]/[klasse]/[thema]/LP-XX-[name].html`
2. Platzhalter ersetzen:
   - `[THEMA]` → Thema des Lernpfads
   - `[FACH]` → Physik/Chemie/Informatik
   - `body class="physik"` → Fachfarbe setzen
3. `TOTAL_STEPS` anpassen (Anzahl der Schritte)
4. `STORAGE_KEY` eindeutig setzen (z.B. `lp-physik-7-dichte`)
5. Steps hinzufügen/entfernen nach Bedarf
6. `checkStepX()` Funktionen implementieren

### Fachfarben

```html
<body class="physik">     <!-- Blau #2c5aa0 -->
<body class="chemie">     <!-- Grün #2a7a4b -->
<body class="informatik"> <!-- Orange #b35c00 -->
```
