# Prüfplan: MINT-Lernpfad (LP)

> Allgemeiner Prüfplan zur Qualitätssicherung von Lernpfaden nach dem MINT-Template.
> Umfasst Vollständigkeit, Technik, Persistenz, Navigation, Didaktik, Inhalt und Deployment.

---

## Phase 0: Vollständigkeits-Check

> **Ziel:** Alle erforderlichen Dateien existieren und sind funktionsfähig.

| # | Prüfpunkt | Kriterium | Datei |
|---|-----------|-----------|-------|
| 0.1 | LP-HTML | Lernpfad-Datei existiert | `LP-XX-name.html` |
| 0.2 | QR-LP-TEX | QR-Code LaTeX existiert | `QR-LP-XX-name.tex` |
| 0.3 | QR-LP-PDF | Kompiliert ohne Fehler | `QR-LP-XX-name.pdf` |
| 0.4 | AB-TEX | Zugehöriges Arbeitsblatt existiert | `AB-XX-name.tex` |
| 0.5 | AB-PDF | Kompiliert ohne Fehler | `AB-XX-name.pdf` |
| 0.6 | ARBEITSPFAD | LP↔AB Mapping existiert | `ARBEITSPFAD-XX-name.md` |
| 0.7 | Abhängigkeiten | Alle Bilder/SIMs im Ordner | `img/`, `leifi/`, `SIM-XX.html` |

### Checkliste Dateien

```
projects/[fach]/[klasse]/[thema]/
├── LP-XX-name.html          ← Lernpfad
├── AB-XX-name.tex           ← Zugehöriges Arbeitsblatt
├── AB-XX-name.pdf
├── ARBEITSPFAD-XX-name.md   ← LP↔AB Mapping (QA-Dokument)
├── QR-LP-XX-name.tex        ← QR für Lernpfad
├── QR-LP-XX-name.pdf
├── SIM-XX-name.html         ← Simulation (falls vorhanden)
└── [img/leifi/...]          ← Abhängigkeiten (Bilder, etc.)
```

---

## Phase 1: Technische Prüfung (Struktur & Code)

| # | Prüfpunkt | Kriterium |
|---|-----------|-----------|
| 1.1 | HTML-Struktur | Folgt Template-Muster (`lernpfad-mint.html`) |
| 1.2 | JavaScript | ES5-konform (kein `let`/`const`/Arrow Functions) |
| 1.3 | STORAGE_KEY | Eindeutig definiert (`lp-[fach]-[klasse]-[thema]`) |
| 1.4 | TOTAL_STEPS | Korrekt gesetzt (entspricht Anzahl der Steps) |
| 1.5 | Fachfarbe | Durchgängig korrekt (body class + CSS Variables) |
| 1.6 | Bildpfade | Relative Pfade, keine absoluten URLs |
| 1.7 | SIM-Einbindung | iframes mit korrektem src-Pfad |

### Fachfarben (body class)

```html
<body class="physik">     <!-- --accent: #2c5aa0 -->
<body class="chemie">     <!-- --accent: #2a7a4b -->
<body class="informatik"> <!-- --accent: #b35c00 -->
```

---

## Phase 2: Persistenz-Prüfung

| # | Prüfpunkt | Kriterium |
|---|-----------|-----------|
| 2.1 | currentStep | Wird in localStorage gespeichert (`-step`) |
| 2.2 | visitedSteps | Array wird gespeichert (`-visited`) |
| 2.3 | Eingaben | Alle Inputs/Selects werden bei Änderung gespeichert |
| 2.4 | Reload während Bearbeitung | Alle Eingaben + Step werden wiederhergestellt |
| 2.5 | Step-Indicators | visitedSteps werden als "completed" angezeigt |

### localStorage-Keys (Beispiel)

```
lp-physik-9-09a-gleichstrommotor-step
lp-physik-9-09a-gleichstrommotor-visited
lp-physik-9-09a-gleichstrommotor-[input-id]
```

### Kritische Init-Reihenfolge

```javascript
// WICHTIG: loadProgress() VOR generateStepIndicators()!
loadProgress();
generateStepIndicators();
updateProgress();

// Falls gespeicherter Step > 1, diesen anzeigen
if (currentStep > 1) {
    // Steps wechseln ohne visitedSteps zu ändern
}
```

---

## Phase 3: Navigation & Interaktivität

| # | Prüfpunkt | Kriterium |
|---|-----------|-----------|
| 3.1 | Step-Indicators | Klickbar, zeigen aktuellen Step (current) |
| 3.2 | Completed-Status | Besuchte Steps grün markiert |
| 3.3 | Progress-Bar | Aktualisiert sich bei Step-Wechsel |
| 3.4 | Weiter-Button | Wechselt zum nächsten Step |
| 3.5 | Zurück-Button | Wechselt zum vorherigen Step |
| 3.6 | Wide-Mode | Container wird breiter bei SIM-Steps (`.has-sim`) |
| 3.7 | Scroll-to-Top | `window.scrollTo(0, 0)` bei Step-Wechsel |
| 3.8 | Übungs-Feedback | "Prüfen"-Button gibt sofortiges Feedback |

### Step-Indicator Zustände

| Zustand | CSS-Klasse | Aussehen |
|---------|------------|----------|
| Nicht besucht | (keine) | Weißer Hintergrund, grauer Rand |
| Aktuell | `.current` | Dicker blauer Rand |
| Abgeschlossen | `.completed` | Grüner Hintergrund |

---

## Phase 4: Didaktische Struktur

| # | Prüfpunkt | Kriterium |
|---|-----------|-----------|
| 4.1 | Hefter-Hinweise | Vorhanden mit konkreten AB-Verweisen |
| 4.2 | AB-Referenzen | Aufgabennummern stimmen mit AB überein |
| 4.3 | Interleaved Structure | Content → Exercise → Content → Exercise |
| 4.4 | Scaffolding | Gestufte Hilfen bei Übungen |
| 4.5 | Feedback-Qualität | Lernförderlich, nicht nur richtig/falsch |
| 4.6 | Merkkästen | Wichtige Formeln/Definitionen hervorgehoben |
| 4.7 | Beispiele | Durchgerechnete Beispiele vor Übungen |
| 4.8 | SIM-Beobachtungsaufträge | Konkrete Aufgaben zur Simulation |
| 4.9 | **Kein MT-Link** | LP darf **keinen** Link zum Minitest enthalten |

### Regel 4.9: Kein MT-Link im LP

**KRITISCH:** Lernpfade dürfen **niemals** einen direkten Link zum Minitest (MT) enthalten.

**Begründung:**
- Der Lehrer entscheidet, wann der Test gestartet wird
- Schüler sollen nicht vorzeitig auf den Test zugreifen können
- LP und MT sind getrennte Ressourcen (unterschiedliche QR-Codes)

**Prüfung:**
```bash
grep -E "MT-|minitest|Minitest|stundenleistung|Stundenleistung|Zum Test" LP-*.html
# Erwartung: Keine Treffer (oder nur Metadaten ohne Links)
```

**Verboten:**
```html
<!-- FALSCH - niemals im LP! -->
<button onclick="window.location.href='MT-XX.html'">Zum Test</button>
<a href="MT-XX.html">Zur Stundenleistung</a>
```

---

## Phase 4b: ARBEITSPFAD-Konsistenz

> **Ziel:** LP und AB sind **vollständig** aufeinander abgestimmt. **Jede Aufgabe und jeder Aufgabenteil** des AB wird explizit vom LP angesteuert.
>
> **KRITISCH:** Score muss **100/100** sein für Freigabe. Keine Ausnahmen.
>
> **Template:** `templates/mint/ARBEITSPFAD-TEMPLATE.md`

### 4b.1 ARBEITSPFAD-Dokument

| # | Prüfpunkt | Kriterium |
|---|-----------|-----------|
| 4b.1.1 | Dokument existiert | `ARBEITSPFAD-XX-name.md` vorhanden |
| 4b.1.2 | AB-Inventar **vollständig** | Alle Kästen (K), Aufgaben (A), **Aufgabenteile (a, b, c)**, Tabellen (T), Diagramme (D) erfasst |
| 4b.1.3 | Arbeitspfad-Sequenz | Didaktisch sinnvolle Reihenfolge dokumentiert |
| 4b.1.4 | Vollständigkeits-Check | **Jedes Element und Teilelement** genau 1× einem LP-Schritt zugeordnet |

### 4b.2 LP ↔ AB Mapping (KRITISCH)

| # | Prüfpunkt | Kriterium |
|---|-----------|-----------|
| 4b.2.1 | Jeder Hefter-Hinweis | zeigt auf existierendes AB-Element |
| 4b.2.2 | **Jede Aufgabe** | wird durch Hefter-Hinweis angesteuert |
| 4b.2.3 | **Jeder Aufgabenteil (a, b, c)** | wird explizit genannt (nicht nur "Aufgabe 3") |
| 4b.2.4 | Keine Lücken | Kein AB-Element wird vergessen |
| 4b.2.5 | Keine Duplikate | Kein AB-Element wird mehrfach angesteuert |
| 4b.2.6 | Reihenfolge konsistent | LP-Reihenfolge = AB-Reihenfolge (bei linearem Pfad) |

### Beispiel: Explizite Aufgabenteil-Verweise

```html
<!-- FALSCH - zu unspezifisch -->
<div class="hefter-hinweis">
    Bearbeite <strong>Aufgabe 3</strong>
</div>

<!-- RICHTIG - explizit jeden Teil -->
<div class="hefter-hinweis">
    <ul>
        <li>Bearbeite <strong>Aufgabe 3a)</strong>: Leistung berechnen</li>
        <li>Bearbeite <strong>Aufgabe 3b)</strong>: Energie umrechnen</li>
    </ul>
</div>
```

### 4b.3 Arbeitspfad-Score (10 Kriterien)

| # | Kriterium | Beschreibung | Punkte |
|---|-----------|--------------|--------|
| 1 | **Vollständigkeit** | Jedes AB-Element + Teilelement genau 1× angesteuert? | 15 |
| 2 | **Explizite Teilaufgaben** | Jedes a), b), c) einzeln genannt? | 15 |
| 3 | **Lückenlosigkeit** | Kann Schüler an jedem Punkt weitermachen? | 10 |
| 4 | **Erkenntnislogik** | Verstehen vor Anwenden? | 10 |
| 5 | **Vorwissen-Kette** | Baut jeder Schritt auf vorherigem auf? | 10 |
| 6 | **Explizite Verweise** | LP zeigt exakt auf AB-Element (Kasten X, Aufgabe Ya)? | 10 |
| 7 | **Schüler-Perspektive** | Kann Novize ohne Lehrer folgen? | 10 |
| 8 | **Zeitrealistik** | Pfad in geplanter Zeit machbar? | 5 |
| 9 | **Differenzierung** | Abzweigungen für ★/★★/★★★ eingeplant? | 10 |
| 10 | **Sicherung** | AB am Ende vollständig + prüfungsrelevant? | 5 |

**Bewertung:**

| Score | Status |
|-------|--------|
| < 80/100 | ❌ Grundlegende Überarbeitung nötig |
| 80-89 | ⚠️ Überarbeitung erforderlich |
| 90-99 | ⚠️ Nachbesserung nötig (fast, aber nicht freigabefähig) |
| **100/100** | ✅ **FREIGABE** |

> **WICHTIG:** Nur 100/100 führt zur Freigabe. Jeder fehlende Aufgabenteil = Punktabzug.

### Prüfmethode: ARBEITSPFAD-Konsistenz

```bash
# 1. ARBEITSPFAD-Dokument existiert?
ls -la ARBEITSPFAD-*.md

# 2. Alle Hefter-Hinweise im LP extrahieren
grep -A5 'hefter-hinweis' LP-XX.html

# 3. Alle AB-Elemente (Kästen, Aufgaben) im AB extrahieren
grep -E '\\(sub)?section|Aufgabe|Kasten' AB-XX.tex

# 4. Manuell abgleichen: Jedes AB-Element ↔ LP-Hinweis
```

### Checkliste ARBEITSPFAD

- [ ] ARBEITSPFAD-XX.md existiert?
- [ ] AB-Inventar vollständig (K1, K2, ..., A1, A2, ...)?
- [ ] Jedes AB-Element wird im LP genau 1× angesteuert?
- [ ] Hefter-Hinweise im LP stimmen mit ARBEITSPFAD überein?
- [ ] Arbeitspfad-Score = 100/100? (Pflicht!)

### Hefter-Hinweis Format

```html
<div class="hefter-hinweis">
    <strong>Arbeitsblatt (Kasten X):</strong>
    <ul>
        <li>Ergänze die <strong>Bauteile</strong>: ...</li>
        <li>Bearbeite <strong>AB Aufgabe Y</strong></li>
    </ul>
</div>
```

### Feedback-Stufen (aufsteigend)

| Stufe | Beispiel | Lernwirksamkeit |
|-------|----------|-----------------|
| KR | "Falsch" | ★☆☆☆☆ |
| KCR | "Richtig ist: 20 m/s" | ★★☆☆☆ |
| Elaboriert | "Du hast ÷3,6 vergessen" | ★★★★☆ |
| Prozess | "Rechenweg richtig, nur Einheitenfehler" | ★★★★★ |

---

## Phase 5: Fachliche Prüfung

| # | Prüfpunkt | Kriterium |
|---|-----------|-----------|
| 5.1 | Fachliche Korrektheit | Alle Erklärungen und Formeln richtig |
| 5.2 | Korrekte Antworten | In check-Funktionen richtig implementiert |
| 5.3 | Feedback-Texte | Fachlich korrekte Erklärungen |
| 5.4 | Fachkonventionen | Korrekt angewendet (z.B. Schaltzeichen, UVW-Regel) |
| 5.5 | Einheiten | SI-Einheiten, kopfrechenbare Werte |
| 5.6 | Bilder/Diagramme | Unterstützen Verständnis, korrekt beschriftet |
| 5.7 | SVG-Grafiken | Farben korrekt (rot/blau/grün-Konventionen) |
| 5.8 | Simulations-Quellenangabe | Autor/Lizenz angegeben |

---

## Phase 5b: ISO 80000 Typografie

> **Ziel:** Alle Formeln und Einheiten entsprechen ISO 80000 / DIN 1338.
>
> **Referenz:** `CLAUDE.md` → Abschnitt "ISO 80000 Typografie (Formeln & Einheiten)"

### 5b.1 Formelzeichen & Einheiten

| # | Prüfpunkt | Kriterium |
|---|-----------|-----------|
| 5b.1.1 | **Formelzeichen kursiv** | *F*, *m*, *a*, *U*, *I*, *R*, *P*, *E*, *t* etc. |
| 5b.1.2 | **Einheiten aufrecht** | N, kg, m, s, V, A, Ω, W, J, kWh etc. |
| 5b.1.3 | **Zahlen aufrecht** | 5, 3,14, 230 (nicht kursiv) |
| 5b.1.4 | **Leerzeichen Zahl-Einheit** | 5 N (nicht 5N) |

### 5b.2 Indizes

| # | Prüfpunkt | Kriterium |
|---|-----------|-----------|
| 5b.2.1 | **Deskriptive Indizes aufrecht** | *F*<sub>G</sub>, *F*<sub>R</sub>, *U*<sub>ges</sub>, *P*<sub>max</sub> |
| 5b.2.2 | **Zählvariablen kursiv** | *F*<sub>*n*</sub>, *x*<sub>*i*</sub>, *a*<sub>*k*</sub> |

### 5b.3 Bruchstriche

| # | Prüfpunkt | Kriterium |
|---|-----------|-----------|
| 5b.3.1 | **Horizontale Bruchstriche** | Keine Slashes in Formeln (m/V → Bruchstrich) |
| 5b.3.2 | **Einheiten-Brüche** | m/s, ct/kWh als horizontaler Bruch oder Ausnahme-Slash in Fließtext |

### HTML-Prüfung

```bash
# CSS-Klassen prüfen
grep -E 'class="fz"|class="einheit"|class="frac"' LP-XX.html

# Formelzeichen kursiv?
grep -oE '<span class="fz">[A-Za-z]</span>' LP-XX.html | head -10

# Einheiten aufrecht?
grep -oE '<span class="einheit">[^<]+</span>' LP-XX.html | head -10

# Brüche korrekt?
grep -oE 'class="frac"' LP-XX.html
```

### Checkliste ISO 80000 (LP)

- [ ] Alle Formelzeichen (*F*, *m*, *U*, *I*, etc.) kursiv (`<span class="fz">`)?
- [ ] Alle Einheiten (N, V, A, Ω, etc.) aufrecht (`<span class="einheit">`)?
- [ ] Deskriptive Indizes (G, R, ges, max) aufrecht?
- [ ] Zählvariablen-Indizes (*n*, *i*, *k*) kursiv?
- [ ] Horizontale Bruchstriche (`<span class="frac">`) in Formeln?
- [ ] Leerzeichen zwischen Zahl und Einheit?
- [ ] Mittelpunkt (·) als Multiplikationszeichen?

### Typische Fehler (HTML)

| FALSCH | RICHTIG |
|--------|---------|
| `F = 5 N` | `<span class="fz">F</span> = 5 <span class="einheit">N</span>` |
| `m/s` in Formel | `<span class="frac"><span class="frac-num">m</span><span class="frac-den">s</span></span>` |
| `<i>N</i>` | `<span class="einheit">N</span>` (aufrecht!) |
| `F<sub><i>G</i></sub>` | `<span class="fz">F</span><sub>G</sub>` (G aufrecht!) |

### Farbkonventionen (Physik)

| Element | Farbe | Hex |
|---------|-------|-----|
| Positive Ladung/Pol | ROT | `#c62828` |
| Negative Ladung/Pol | BLAU | `#1565c0` |
| Magnetfeld (B) | GRÜN | `#2e7d32` |

---

## Phase 6: UI/Layout-Prüfung

| # | Prüfpunkt | Kriterium |
|---|-----------|-----------|
| 6.1 | Header | Titel + Meta korrekt, Fachfarbe |
| 6.2 | Progress-Bar | Visuell korrekt, Prozent stimmt |
| 6.3 | Step-Indicators | Gleichmäßig, responsiv bei vielen Steps |
| 6.4 | Step-Header | Fachfarbe, Schritt-Nummer + Titel |
| 6.5 | Info-Boxen | Fachfarbe korrekt |
| 6.6 | Hefter-Hinweise | Orange Rahmen, "Arbeitsblatt"-Badge |
| 6.7 | SIM-Container | iframe-Höhe angemessen (400-650px) |
| 6.8 | Feedback-Farben | Grün (richtig), Rot (falsch) |
| 6.9 | Responsive | Keine Überlappungen, Container max-width |
| 6.10 | Bilder | Laden korrekt, max-width: 100% |
| 6.11 | Farblegenden | Bei SVGs vorhanden |

---

## Phase 7: Deployment & Abhängigkeiten

> **Ziel:** Online-Ressourcen sind erreichbar, Print-Dokumente existieren lokal mit korrekten QR-Links.

### Deployment-Übersicht

| Dokumenttyp | Deployment | Prüfung |
|-------------|------------|---------|
| `LP-XX.html` | **Online** (GitHub Pages) | HTTP 200 prüfen |
| `SIM-XX.html` | **Online** (GitHub Pages) | HTTP 200 prüfen |
| Bilder (`img/`, `leifi/`, `leifi/img/`) | **Online** (GitHub Pages) | HTTP 200 prüfen |
| `QR-LP-XX.pdf` | **Lokal** (nur Print) | Existiert, QR → Online-URL |
| `AB-XX.pdf` | **Lokal** (nur Print) | Existiert |

### 7.1 Online-Ressourcen (GitHub Pages)

| # | Prüfpunkt | Kriterium |
|---|-----------|-----------|
| 7.1.1 | LP online | `https://devbox42.github.io/sciencesim/[pfad]/LP-XX.html` → HTTP 200 |
| 7.1.2 | SIM online | Falls vorhanden: `SIM-XX.html` → HTTP 200 |
| 7.1.3 | Eingebettete SIMs | iframe-src URLs → HTTP 200 |
| 7.1.4 | Bilder online | Alle `<img src="...">` laden (DevTools → Network) |
| 7.1.5 | Konsole sauber | Keine 404-Fehler in Browser-Konsole |
| 7.1.6 | Version aktuell | Online-Version = lokale Version |

### 7.2 Print-Dokumente (nur lokal)

> **Hinweis:** Diese PDFs werden **nicht** online deployed. Sie dienen zum Ausdrucken und Austeilen im Unterricht.

| # | Prüfpunkt | Kriterium |
|---|-----------|-----------|
| 7.2.1 | QR-LP-PDF | Existiert lokal, kompiliert ohne Fehler |
| 7.2.2 | AB-PDF | Existiert lokal, kompiliert ohne Fehler |

### 7.3 QR-Code-Verknüpfung

> **Kritisch:** Die QR-Codes in den Print-Dokumenten müssen auf die **Online-URLs** zeigen!

| # | Prüfpunkt | Kriterium |
|---|-----------|-----------|
| 7.3.1 | QR-LP-URL | QR zeigt auf `devbox42.github.io/.../LP-XX.html` |
| 7.3.2 | QR scannbar | Smartphone kann QR lesen und URL öffnen |
| 7.3.3 | Link klickbar | `\href{}` in .tex → Klick auf QR im PDF öffnet Browser |
| 7.3.4 | hyperref aktiv | `\usepackage{hyperref}` in .tex vorhanden |

### Prüfmethode: Online-Ressourcen

```bash
# LP online prüfen
curl -s -o /dev/null -w "%{http_code}" "https://devbox42.github.io/sciencesim/[pfad]/LP-XX.html"
# Erwartung: 200

# Alle iframe-src Pfade im LP extrahieren
grep -oE 'src="[^"]+\.html"' LP-XX.html

# Alle Bildpfade im LP extrahieren
grep -oE 'src="[^"]+\.(png|jpg|gif|svg)"' LP-XX.html

# Bilder/SIMs online prüfen
curl -s -o /dev/null -w "%{http_code}" "https://devbox42.github.io/sciencesim/[pfad]/[datei]"
# Erwartung: 200
```

### Prüfmethode: Print-Dokumente & QR

```bash
# 1. PDFs existieren?
ls -la QR-LP-*.pdf AB-*.pdf

# 2. URL in .tex prüfen (muss devbox42.github.io enthalten)
grep "devbox42" QR-LP-*.tex

# 3. PDF öffnen, QR mit Smartphone scannen
open QR-LP-XX.pdf

# 4. Im PDF auf QR klicken → Browser öffnet korrekte URL?
```

---

## Bewertungskriterien

| Ergebnis | Bedeutung | Aktion |
|----------|-----------|--------|
| ✅ Alle Phasen bestanden | Freigabe | Kann eingesetzt werden |
| ⚠️ Kleinere Mängel | Bedingte Freigabe | Nachbesserung empfohlen |
| ❌ Kritische Fehler | Keine Freigabe | Überarbeitung erforderlich |

### Kritische Fehler (sofortige Überarbeitung)

- Persistenz funktioniert nicht (Step/Eingaben gehen verloren)
- Falsche fachliche Inhalte
- Navigation kaputt (Steps nicht erreichbar)
- **LP nicht online erreichbar** (HTTP 404)
- **Eingebettete SIMs/Bilder fehlen online** (HTTP 404)
- **QR-Codes zeigen auf falsche/alte URL**
- AB-Verweise in Hefter-Hinweisen falsch
- **ARBEITSPFAD-Score < 100** (LP und AB nicht vollständig konsistent)
- **ISO 80000 verletzt** (Einheiten kursiv, Formelzeichen aufrecht, Slashes in Formeln)

### Kleinere Mängel (Nachbesserung)

- Styling-Inkonsistenzen
- Fehlende Quellenangaben für Simulationen
- Unklare Formulierungen
- Print-PDFs nicht aktuell kompiliert (lokal)
- `\href{}` fehlt in .tex (QR nicht klickbar im PDF)
- Feedback nur richtig/falsch (nicht elaboriert)
- ARBEITSPFAD-Score < 100 (Nachbesserung nötig bis 100/100 erreicht)
- ARBEITSPFAD-Dokument fehlt (muss nacherstellt werden)

---

## Prüfprotokoll-Vorlage

```markdown
## Prüfprotokoll: [LP-Name]

**Datum:** [TT.MM.JJJJ]
**Prüfer:** [Name/Claude]
**Version:** [vX.Y]
**GitHub-URL:** https://devbox42.github.io/sciencesim/[pfad]/LP-XX-name.html

### Ergebnisse

| Phase | Status | Anmerkungen |
|-------|--------|-------------|
| 0. Vollständigkeit | ✅/⚠️/❌ | |
| 1. Technisch | ✅/⚠️/❌ | |
| 2. Persistenz | ✅/⚠️/❌ | |
| 3. Navigation | ✅/⚠️/❌ | |
| 4. Didaktik | ✅/⚠️/❌ | |
| 4b. ARBEITSPFAD | ✅/⚠️/❌ | Score: __/100 |
| 5. Fachlich | ✅/⚠️/❌ | |
| **5b. ISO 80000** | ✅/⚠️/❌ | Typografie |
| 6. UI/Layout | ✅/⚠️/❌ | |
| 7. Deployment | ✅/⚠️/❌ | |

### Online-Ressourcen (GitHub Pages)

| Datei | Lokal | Online (HTTP) | Status |
|-------|-------|---------------|--------|
| LP-XX.html | ✅ | 200 | OK |
| SIM-XX.html | ✅ | 200 | OK |
| leifi/xxx.html | ✅ | 200 | OK |
| img/bild.png | ✅ | 404 | FEHLT |

### Print-Dokumente (nur lokal)

| Dokument | PDF existiert | QR → Online-URL | Link klickbar |
|----------|---------------|-----------------|---------------|
| QR-LP | ✅/❌ | ✅/❌ | ✅/❌ |
| AB | ✅/❌ | — | — |

### Gefundene Fehler

1. [Beschreibung]
2. [Beschreibung]

### Fazit

[ ] Freigabe
[ ] Nachbesserung erforderlich
[ ] Keine Freigabe
```

---

## Schnell-Check (5 Minuten)

Für eilige Prüfungen - die wichtigsten Punkte:

```bash
# 1. Online-Ressourcen erreichbar?
curl -s -o /dev/null -w "%{http_code}" "https://devbox42.github.io/sciencesim/[pfad]/LP-XX.html"
# Erwartung: 200

# 2. Print-PDFs existieren lokal?
ls -la QR-LP-*.pdf AB-*.pdf

# 3. QR-URL korrekt? (muss devbox42.github.io enthalten)
grep "devbox42" QR-LP-*.tex

# 4. QR-Code scannen (manuell mit Smartphone) → Öffnet LP?

# 5. Im Browser: DevTools → Console → Keine 404-Fehler?

# 6. Persistenz: Step wechseln → Reload → Noch am gleichen Step?

# 7. Hefter-Hinweise: Stimmen AB-Aufgabennummern?

# 8. ARBEITSPFAD: Existiert und ist vollständig?
ls -la ARBEITSPFAD-*.md
grep -c "✓" ARBEITSPFAD-*.md  # Sollte = Anzahl AB-Elemente
```

### Zusammenfassung: Was muss wo sein?

| Was | Wo | Warum |
|-----|-----|-------|
| LP.html | **Online** (GitHub) | Schüler greifen per QR darauf zu |
| SIM.html | **Online** (GitHub) | Wird von LP per iframe geladen |
| Bilder, Abhängigkeiten | **Online** (GitHub) | Werden von LP geladen |
| QR-LP.pdf | **Lokal** (Print) | Wird ausgedruckt/projiziert |
| AB.pdf | **Lokal** (Print) | Wird ausgedruckt und ausgeteilt |

---

## LP-spezifische Checkliste

### Struktur

- [ ] STORAGE_KEY eindeutig? (`lp-[fach]-[klasse]-[thema]`)
- [ ] TOTAL_STEPS = Anzahl der Steps?
- [ ] Fachfarbe korrekt (body class)?
- [ ] ES5-konform (kein let/const/arrow)?

### Navigation

- [ ] Step-Indicators vorhanden und klickbar?
- [ ] visitedSteps werden als grün markiert?
- [ ] Progress-Bar aktualisiert sich?
- [ ] Wide-Mode bei SIM-Steps?

### Persistenz

- [ ] Step wird gespeichert bei Wechsel?
- [ ] visitedSteps werden gespeichert?
- [ ] Eingaben werden bei Änderung gespeichert?
- [ ] Reload stellt alles wieder her?

### Didaktik

- [ ] Hefter-Hinweise vorhanden?
- [ ] AB-Verweise korrekt (Aufgabennummern)?
- [ ] Feedback elaboriert (nicht nur richtig/falsch)?
- [ ] Interleaved: Content ↔ Exercise?
- [ ] SIM-Beobachtungsaufträge klar?

### ARBEITSPFAD-Konsistenz

- [ ] ARBEITSPFAD-XX.md existiert?
- [ ] AB-Inventar vollständig (K1, K2, ..., A1, A2, ...)?
- [ ] Jedes AB-Element genau 1× im LP angesteuert?
- [ ] Hefter-Hinweise = ARBEITSPFAD-Sequenz?
- [ ] Arbeitspfad-Score = 100/100? (Pflicht für Freigabe!)

### ISO 80000 Typografie

- [ ] Formelzeichen kursiv (`<span class="fz">`)?
- [ ] Einheiten aufrecht (`<span class="einheit">`)?
- [ ] Deskriptive Indizes aufrecht (G, R, ges, max)?
- [ ] Horizontale Bruchstriche (`<span class="frac">`)?
- [ ] Leerzeichen zwischen Zahl und Einheit?

### Deployment

- [ ] LP online erreichbar (HTTP 200)?
- [ ] Alle SIMs online erreichbar?
- [ ] Alle Bilder online erreichbar?
- [ ] QR-LP zeigt auf Online-URL?
- [ ] AB-PDF existiert lokal?

---

## Vergleich: LP vs. MT

| Aspekt | LP (Lernpfad) | MT (Minitest) |
|--------|---------------|---------------|
| **Zweck** | Lernen & Üben | Bewerten |
| **Persistenz** | Step + visitedSteps + Inputs | Seat + Niveau + Answers + Submitted |
| **Navigation** | Step-Indicators (frei klickbar) | Linear (nicht zurück nach Submit) |
| **Niveau** | Optional (Differenzierung) | Pflicht (Niveau-Lock) |
| **Feedback** | Sofort (pro Übung) | Am Ende (nach Submit) |
| **Anti-Betrug** | Nein | Ja (Tab-Wechsel, Zeiten) |
| **AB-Bezug** | Hefter-Hinweise → AB | Keine |
| **SIM-Einbindung** | Häufig (inline) | Selten (Referenz) |

---

## Referenzen

- Template: `templates/mint/lernpfad-mint.html`
- Dokumentation: `templates/mint/README-LERNPFAD-MINT.md`
- Workflow: `templates/mint/WORKFLOW-MINT.md`
- Design-System: `CLAUDE.md` (Abschnitt "Design-System")
- MT-Prüfplan: `templates/mint/pruefplan_MT.md`
