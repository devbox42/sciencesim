# BLP-Referenz: Bewerteter Lernpfad

> **Version:** 1.1
> **Stand:** 05.02.2026
> **Referenz-Implementierung:** `physik/kl10-MR/05-schwingungen-wellen/BLP-05b-wellen.html`
> **Template:** `knowledge/didaktik/templates/BLP-TEMPLATE.html`

---

## 1. Abgrenzung LP vs. MT vs. BLP

| Typ | Dateiname | Zweck | Bewertung | Lehrinhalt |
|-----|-----------|-------|-----------|------------|
| **LP** | `LP-XX-thema.html` | Formativer Lernpfad | Nein | Ja |
| **MT** | `MT-XX-thema.html` | Minitest (summativ) | Ja | Nein |
| **BLP** | `BLP-XX-thema.html` | Bewerteter Lernpfad | Ja | Ja |

**BLP = INPUT + TEST in einer Datei.** Jede Phase hat:
1. Lehrmaterial (Info-Box, Animation, Simulation, Formel)
2. Übungszone (unbewertet, mit Feedback)
3. Bewertungszone (1 Versuch, BE-Punkte)

---

## 2. Technische Architektur

### 2.1 Dateistruktur

Einzige HTML-Datei, ca. 2500-3000 Zeilen. Keine externen Abhängigkeiten.

```
<html>
  <head>
    <style>  /* ~500 Zeilen CSS */  </style>
  </head>
  <body>
    <!-- ~570 Zeilen HTML (8 Phasen) -->
    <script> /* ~1500 Zeilen ES5 JS */ </script>
  </body>
</html>
```

### 2.2 ES5-Pflicht

**Kein ES6+.** iPad-Safari-Kompatibilität.

```javascript
// RICHTIG
var x = 5;
function foo() { return x; }
for (var i = 0; i < arr.length; i++) {}

// FALSCH
let x = 5;        // ← verboten
const y = 10;     // ← verboten
arr.forEach(x => {});  // ← verboten
```

### 2.3 ID-Konvention

```
BLP_ID = 'blp-XX-thema';   // localStorage-Prefix
LP_VERSION = '2.0';         // Version-Check
```

---

## 3. Anti-Cheating-System

### 3.1 Seed-basierte Personalisierung

```javascript
// Name → Seed → deterministische Zufallszahlen
function seedFromName(name) {
    var hash = 0;
    var str = name.trim().toLowerCase();
    for (var i = 0; i < str.length; i++) {
        hash = ((hash << 5) - hash) + str.charCodeAt(i);
        hash = hash & hash;
    }
    return Math.abs(hash);
}

function createRNG(seed) {
    var s = seed;
    return {
        next: function() {
            s = (s * 9301 + 49297) % 233280;
            return s / 233280;
        },
        nextInt: function(max) {
            return Math.floor(this.next() * max);
        }
    };
}

function shuffleWithRNG(arr, rng) {
    var result = arr.slice();
    for (var i = result.length - 1; i > 0; i--) {
        var j = rng.nextInt(i + 1);
        var temp = result[i];
        result[i] = result[j];
        result[j] = temp;
    }
    return result;
}
```

**Prinzip:** Verschiedene RNG-Seeds für verschiedene Phasen (seed+100, seed+300, etc.)
→ Jeder Schüler bekommt andere Fragen und andere Optionsreihenfolge.

### 3.2 Tab-Alarm-System

**Auslöser:** `document.visibilitychange` Event

| Aktion | Was passiert |
|--------|-------------|
| Tab verlassen (hidden) | Counter erhöht, Außenzeit läuft |
| Tab zurückkehren (visible) | **Puls-Alarm:** 5× Beep (0,5s an, 0,5s aus = 5s) + Overlay |
| Overlay während Alarm | "Zurück"-Button **deaktiviert** bis alle Beeps fertig |
| Overlay nach Alarm | Schüler klickt "Zurück zum Test" |

**Puls-Alarm statt Dauer-Ton:** Beim Zurückkehren ertönen 5 Beeps à 0,5 Sekunden (800Hz square, 0,5s an + 0,5s Pause = 5s gesamt).
Der Dismiss-Button wird erst nach dem letzten Beep klickbar. Das Overlay zeigt die
kumulierte Außenzeit und die Anzahl der Tab-Wechsel.

**sessionReady-Flag:** Tab-Alarm wird erst aktiviert, nachdem `startLP()` oder `restoreSession()` abgeschlossen ist. Verhindert Fehl-Alarm bei Reload (Browser feuert `visibilitychange` beim Laden).

**Audio-Fallback:** Falls `AudioContext.resume()` nach Reload fehlschlägt (iOS, keine User-Geste), wird der Dismiss-Button nach 2s automatisch freigegeben.

**goToPhase-Override Reihenfolge:** In `window.onload` muss der `goToPhase`-Override (Timer-Starts) **vor** `loadState()`/`restoreSession()` stehen, damit bei Reload die Timer (Hypo-Timer, Experiment-Timer) korrekt neu starten. Andernfalls ruft `restoreSession()` → `goToPhase(2)` den alten `goToPhase` ohne Timer-Start auf → Button bleibt disabled.

```javascript
// Web Audio API (funktioniert auch bei stummgeschaltetem Media-Volume!)
function initAudioContext() {
    audioCtx = new (window.AudioContext || window.webkitAudioContext)();
    // iOS-Unlock: stummer Ton nach User-Geste
    var buf = audioCtx.createBuffer(1, 1, 22050);
    var src = audioCtx.createBufferSource();
    src.buffer = buf;
    src.connect(audioCtx.destination);
    src.start(0);
}

function startAlarm() {
    if (!audioCtx || alarmActive) return;
    alarmOsc = audioCtx.createOscillator();
    alarmGain = audioCtx.createGain();
    alarmOsc.connect(alarmGain);
    alarmGain.connect(audioCtx.destination);
    alarmOsc.frequency.value = 800;   // 800 Hz Piepton
    alarmOsc.type = 'square';         // Durchdringend
    alarmGain.gain.value = 0.15;      // Moderate Lautstärke
    alarmOsc.start();
    alarmActive = true;
}
```

**Wichtig zu Web Audio API vs. Lautstärke:**
- Web Audio API wird NICHT durch den Media-Volume-Slider beeinflusst
- ABER: Der Schalter "Stumm" (Hardware-Switch am iPad) schaltet auch Web Audio stumm
- ABER: `<audio>`-Elemente und Web Audio können NICHT die System-Lautstärke überschreiben
- Es gibt KEINE Web-API, die Geräte-Stummschaltung umgeht — das ist ein iOS-Sicherheitsfeature

**Vibration:**
- `navigator.vibrate()` existiert als Web-API
- iPad/iPhone unterstützen es NICHT (Safari ignoriert die API komplett)
- Nur Android-Chrome unterstützt `navigator.vibrate()`

### 3.3 Tab-Tracking Persistenz

```javascript
// 5 localStorage-Keys pro BLP:
BLP_ID + '-state'       // Gesamtzustand (JSON)
BLP_ID + '-inputs'      // Alle Formularwerte (JSON)
BLP_ID + '-result'      // Ergebnis-Lock nach Abschluss (JSON)
BLP_ID + '-tabswitches' // Tab-Wechsel Anzahl (Integer)
BLP_ID + '-tabseconds'  // Tab-Wechsel Gesamtdauer (Integer)
```

### 3.4 Forward-Only Navigation

```javascript
function goToPhase(n) {
    if (n < state.currentPhase && n !== 0) return; // Kein Zurück!
    // ...
}
```

### 3.5 Prüfcode (Verifizierung)

```javascript
function generateVerification(name, score, date) {
    var str = name.toLowerCase().trim() + '-' + score + '-' + date;
    var hash = 0;
    for (var i = 0; i < str.length; i++) {
        hash = ((hash << 5) - hash) + str.charCodeAt(i);
        hash = hash & hash;
    }
    return Math.abs(hash).toString(36).toUpperCase().substr(0, 6);
}
// → z.B. "A3F72K" — reproduzierbar mit gleichem Name+Score+Datum
```

---

## 4. Timer-System

### 4.1 Hypothesen-Timer (60s)

- Simulation läuft 60s, dann einfrieren
- Submit-Button wird erst nach 60s aktiv
- Frozen-Overlay über der Simulation

### 4.2 Experiment-Timer (180s = 3 min)

```javascript
function startExperimentTimer() {
    experimentTimer = state.experimentTimeLeft || 180;
    experimentInterval = setInterval(function() {
        experimentTimer--;
        state.experimentTimeLeft = experimentTimer;
        // Display aktualisieren
        if (experimentTimer <= 30) { /* rot färben */ }
        if (experimentTimer <= 0) { freezeExperiment(); }
        saveState();  // Timer-Stand wird gespeichert!
    }, 1000);
}
```

**Anti-Reload-Trick:** Timer-Stand in `state.experimentTimeLeft` gespeichert.
Bei Reload setzt der Timer bei der gespeicherten Zeit fort.

---

## 5. Persistenz-System (Dreifach-Speicherung)

### 5.1 State-Objekt

```javascript
var state = {
    name: '', seed: 0, version: LP_VERSION,
    currentPhase: 0,
    scores: { p1:0, p2:0, p3:0, p4:0, p5:0, p6:0 },
    submitted: { p1:false, p2:false, p3:false, p4:false, p5:false, p6:false },
    hypotheses: { lambda:'', lambdaReason:'', freq:'', freqReason:'' },
    measurements: [null, null, null, null],
    completed: false,
    startTime: null, phaseTimestamps: {},
    experimentTimeLeft: 180
};
```

### 5.2 Input-Snapshot

Alle Formularwerte und MC-Selektionen werden bei jedem Input-Event gespeichert:

```javascript
document.addEventListener('input', function(e) {
    if (e.target.matches('input, select')) {
        saveInputSnapshot();
        saveState();
    }
});
// + In jedem MC-onclick-Handler: saveInputSnapshot()
```

### 5.3 Version-Check

```javascript
if (data.version !== LP_VERSION) {
    localStorage.removeItem(BLP_ID + '-state');
    localStorage.removeItem(BLP_ID + '-inputs');
    return false;  // Alte Daten verwerfen
}
```

---

## 6. Bewertungsschema

### 6.1 Notenskala (25 BE, MR)

| Note | 1 | 2 | 3 | 4 | 5 | 6 |
|------|---|---|---|---|---|---|
| ab BE | 23 | 20 | 15 | 12 | 7 | 0 |
| ab % | 92 | 80 | 60 | 48 | 28 | <28 |

```javascript
function getGrade(be) {
    if (be >= 23) return 1;
    if (be >= 20) return 2;
    if (be >= 15) return 3;
    if (be >= 12) return 4;
    if (be >= 7) return 5;
    return 6;
}
```

### 6.2 BE pro Phase (Skalierbar)

Die Phasenstruktur folgt dem NaWi-Erkenntnisweg:

```
Phänomen → Hypothese → Experiment → Auswertung → Anwendung → Verallgemeinerung
```

Jede Phase hat 2-6 BE. Summe = TOTAL_BE.

### 6.3 Scoring-Muster

**MC-Fragen:** `data-correct="1"` auf richtiger Option
**Rechnungen:** `parseNum(input) < tolerance`
**Zuordnungen:** Exakter String-Match
**Gestaffelt:** z.B. 4/4=3 BE, 3/4=2 BE, 2/4=1 BE, ≤1/4=0 BE

---

## 7. CSS-Design-System

### 7.1 Farben

```css
--fach: #2c5aa0;          /* Physik-Blau */
--success: #2a7a4b;       /* Grün (richtig) */
--warning: #b35c00;       /* Orange */
--error: #c62828;          /* Rot (bewertet, falsch) */
--hypo: #6a1b9a;           /* Lila (Hypothese) */
```

### 7.2 Zonen

```css
.practice-zone  → Grüne gestrichelte Umrandung, Label "ÜBUNG"
.assess-zone    → Rote gestrichelte Umrandung, Label "BEWERTET – X BE"
.hypo-zone      → Lila Umrandung, Label "HYPOTHESE"
```

### 7.3 Neue BLP-spezifische Styles

```css
.tab-warning-overlay    → Fullscreen-Overlay (z-index: 9999)
.locked-notice          → Gelber Banner oben
.frozen-overlay         → Grauer Overlay über Simulation
.timer-display          → Großer zentrierter Timer
.hefter-hint            → Grüner Hinweis-Balken
```

---

## 8. Fragen-Pool-Design

### 8.1 Prinzipien

1. **Pool > Anzahl:** z.B. 10 Items im Pool, 4 werden ausgewählt
2. **Ganzzahlig:** Alle Berechnungen müssen kopfrechenbar sein
3. **Seed-basiert:** `shuffleWithRNG(pool, rng).slice(0, n)`
4. **Optionen shufflen:** Richtige Antwort nicht immer an Position 0

### 8.2 Pool-Formate

```javascript
// MC mit correct-Index
{ text: 'Frage', options: ['A','B','C','D'], correct: 1 }

// Berechnung
{ l: 3, f: 4, v: 12 }  // v = λ·f

// Zuordnung
{ name: 'Gitarrensaite', answer: 'trans' }

// 2-Schritt-Erklärung
{ text: 'Phänomen', step1: ['opt1','opt2','opt3'], step1correct: 0,
  step2: ['grund1','grund2','grund3'], step2correct: 0 }
```

---

## 9. Lehrer-Reset

```javascript
function teacherReset() {
    var code = prompt('Lehrer-Code eingeben:');
    if (code === '2026') {
        if (confirm('Wirklich alle Daten löschen?')) {
            localStorage.removeItem(BLP_ID + '-state');
            localStorage.removeItem(BLP_ID + '-inputs');
            localStorage.removeItem(BLP_ID + '-result');
            localStorage.removeItem(BLP_ID + '-tabswitches');
            localStorage.removeItem(BLP_ID + '-tabseconds');
            location.reload();
        }
    }
}
```

Position: Fixed, unten rechts, 50% Opacity. Code: `2026`.

---

## 10. Hefter-Hinweise & AB-Integration

### 10.1 Hefter-Hints im BLP

An definierten Stellen im BLP erscheint ein grüner Hinweis, der Schüler auffordert,
Ergebnisse auf dem begleitenden AB (Arbeitsblatt) zu sichern:

```html
<div class="hefter-hint">Text hier.</div>
```

**Position:** Immer **nach** der Bewertungszone einer Phase, **vor** dem „Weiter"-Button.

### 10.2 Grundprinzip: AB-Eintrag nach Assessment

> **Regel:** Der AB-Eintrag für Phase N erfolgt **nach** dem Assessment von Phase N.
> Er darf **keine** Antworten für das Assessment von Phase N+1 vorwegnehmen.

**Warum?**
- Das AB dient als **dauerhafte Dokumentation** der Feinziele im Hefter.
- Würde der AB-Eintrag *vor* dem Assessment kommen, hätten Schüler einen Spickzettel.
- Innerhalb einer Phase ist alles auf einer scrollbaren Seite sichtbar — Lerninhalte
  **über** der Bewertungszone sind also einsehbar. Das ist gewollt (Lernphase → Test
  auf gleicher Seite). Aber das AB muss nach der Abgabe ausgefüllt werden.

**Ablauf pro Phase:**

```
┌─ Phase N (eine scrollbare Seite) ──────────┐
│  1. Lerninhalt (Text, Animation, Tabelle)   │  ← Schüler liest/lernt
│  2. Übungszone (unbewertet, beliebig oft)   │  ← Schüler übt
│  3. Bewertungszone (1 Versuch, X BE)        │  ← Schüler wird bewertet
│  4. Hefter-Hint: "Übertrage ins AB"         │  ← JETZT erst aufs AB
│  5. [Weiter →]                              │
└─────────────────────────────────────────────┘
```

### 10.3 Spoiler-Check (Pflicht bei BLP-Erstellung)

Bei jeder BLP-Erstellung muss geprüft werden, ob der AB-Eintrag von Phase N
die Antworten für Phase N+1 verrät.

**Checkliste:**

| Prüfung | Frage | Ergebnis |
|---------|-------|----------|
| Phase 1 → Phase 2 | Enthält der AB-Eintrag (Wellentypen) Antworten für die Hypothese? | ✅/❌ |
| Phase 2 → Phase 3 | Enthält der AB-Eintrag (Hypothese) Messwerte für das Experiment? | ✅/❌ |
| Phase 3 → Phase 4 | Enthält der AB-Eintrag (Messwerte) Berechnungsergebnisse? | ✅/❌ |
| Phase 4 → Phase 5 | Enthält der AB-Eintrag (Formel) Antworten auf Anwendungsfragen? | ✅/❌ |
| Phase 5 → Phase 6 | Enthält der AB-Eintrag (Anwendung) Antworten auf Transfer-Fragen? | ✅/❌ |

**Bewertungskriterium:** Jede Zeile muss ✅ (= kein Spoiler) sein.
Wenn ❌: AB-Eintrag umformulieren, sodass er Wissen sichert, aber nicht die
spezifischen Assessment-Antworten der Folgephase enthält.

**Typische sichere Muster:**

| Phase N sichert... | Phase N+1 testet... | Spoiler? |
|---------------------|---------------------|----------|
| Definitionen & Beispiele | Hypothesen formulieren | Nein |
| Hypothesen (qualitativ) | Messungen durchführen | Nein |
| Messwerte (Rohdaten) | Berechnungen mit Formel | Nein |
| Formel v = λ·f | Anwendung auf Schall (s = v·t) | Nein (andere Formel) |
| Schall-Fakten (Hörbereich etc.) | Logisches Schlussfolgern (Claims) | Nein |

### 10.4 AB-Design-Richtlinien

1. **Lückentext statt fertiger Text:** Schüler füllen Schlüsselbegriffe selbst ein
2. **Leere Tabellen:** Strukturvorgabe ja, Antworten nein
3. **Formelrahmen:** Formel-Platzhalter mit Einheiten, nicht ausgefüllt
4. **Keine Pool-Antworten:** Die Beispiel-Tabelle aus dem LP steht NICHT fertig auf dem AB
5. **Feinziel-Vollständigkeit:** Jedes Feinziel muss auf dem AB einen Eintrag haben
6. **Reihenfolge = Phasenfolge:** AB-Aufgaben 1–6 entsprechen Phase 1–6

---

## 11. Workflow-Optimierung

### 11.1 Problem: Token-Limit

Eine BLP-Datei (~2500 Zeilen) überschreitet das Output-Token-Limit.
**Lösung: Modularer Aufbau.**

### 11.2 Empfohlener Erstellungs-Workflow

#### Schritt 1: Planung (Plan Mode)

- Phasenstruktur mit BE-Verteilung
- Fragen-Pools definieren
- Scoring-Logik festlegen

#### Schritt 2: HTML/CSS schreiben

- Header, EW-Nav, Phasen-Container
- Alle IDs korrekt setzen
- Leerer `<script>` Tag am Ende

#### Schritt 3: JavaScript injizieren (Edit-Tool)

- Pools + State + Seed-Funktionen
- buildPhase-Funktionen
- Submit-Funktionen + Scoring
- Simulation (Canvas)
- Persistenz + Timer + Tab-Tracking
- Init/Restore

#### Schritt 4: Validierung

```bash
node -e "var html=require('fs').readFileSync('file.html','utf8'); \
  var js=html.match(/<script>([\s\S]*?)<\/script>/); \
  try{new Function(js[1]);console.log('OK')}catch(e){console.log(e.message)}"
```

### 11.3 Besserer Ansatz: LP→BLP Transformation

**Statt BLP from scratch:** Bestehenden LP als Basis nehmen und erweitern.

```
LP-05b-wellen.html (unbewerteter Lernpfad, ~800 Zeilen)
    ↓ Transformation
BLP-05b-wellen.html (bewerteter Lernpfad, ~2500 Zeilen)
```

**Was sich ändert:**
1. `LP_ID` → `BLP_ID`, `LP_VERSION` hinzufügen
2. `TOTAL_BE` setzen
3. Übungszone → Bewertungszone (1 Versuch)
4. Forward-only Navigation
5. Tab-Tracking + Alarm
6. Persistenz-System erweitern
7. Ergebnis-Seite mit Notenspiegel
8. Neue Pools hinzufügen

### 11.4 Template-Ansatz (verfügbar!)

```
knowledge/didaktik/templates/BLP-TEMPLATE.html (~1680 Zeilen)
```

**Workflow mit Template:**

1. Template kopieren → `fach/klXX/thema/BLP-XX-thema.html`
2. CONTENT-Blöcke ausfüllen (markiert mit `══ CONTENT`):
   - Config: `BLP_ID`, `LP_VERSION`, `TOTAL_BE`, `PHASE_CONFIG`, `GRADE_SCALE`
   - Fragen-Pools + `buildPersonalTasks()`
   - HTML Phasen 1–6 (Lerninhalt, Übung, Bewertungszonen)
   - `buildPhase1–6()`, `submitPhase1–6()`, `checkPractice*()`
   - Canvas/Simulation (optional)
3. TEMPLATE-Blöcke **nicht ändern** (markiert mit `── TEMPLATE`)

**Config-Objekte** (statt Hardcoding):
- `PHASE_CONFIG[]` — Phasen-Namen + maxBE → Ergebnis-Tabelle wird generiert
- `GRADE_SCALE[]` — Notenskala → Notenspiegel wird generiert
- `HYPO_TIMER`, `EXP_TIMER` — Timer konfigurierbar (0 = aus)
- `TAB_WARN_BEEPS` — Anzahl Puls-Beeps bei Tab-Rückkehr

**Vorteil:** Statt ~2500 Zeilen schreiben, nur ~800 Zeilen Fach-Content einfügen.

---

## 12. Bekannte Limitierungen

### Audio/Vibration auf iPad

| Feature | iPad-Support | Workaround |
|---------|-------------|------------|
| Web Audio API | Ja (nach User-Geste) | `initAudioContext()` bei Button-Klick |
| navigator.vibrate() | **Nein** | Keiner — iOS unterstützt es nicht |
| Lautstärke erzwingen | **Nein** | iOS erlaubt keine Lautstärke-Kontrolle per Web |
| Stumm-Schalter umgehen | **Nein** | iOS-Sicherheitsfeature |

### Anti-Cheating Grenzen

| Maßnahme | Schutz gegen | Nicht gegen |
|----------|-------------|-------------|
| Tab-Alarm | Schnelles Nachschauen | Zweites Gerät |
| Tab-Counter | Dokumentation der Wechsel | Zweites Gerät |
| Forward-only | Zurückgehen + Ändern | Reload + Name ändern |
| Seed-Personalisierung | Abschreiben | Gleicher Name eingeben |
| Timer-Persistenz | Reload-Trick | localStorage löschen (DevTools) |
| Version-Check | Alte Antworten wiederverwenden | — |
