# Prüfplan: MINT-Minitest (MT)

> Allgemeiner Prüfplan zur Qualitätssicherung von Minitests nach dem MINT-Template.
> Umfasst Vollständigkeit, Technik, Funktion, Inhalt und Deployment.

---

## Phase 0: Vollständigkeits-Check

> **Ziel:** Alle erforderlichen Dateien existieren und sind kompilierbar.

| # | Prüfpunkt | Kriterium | Datei |
|---|-----------|-----------|-------|
| 0.1 | MT-HTML | Minitest-Datei existiert | `MT-XX-name.html` |
| 0.2 | Platzkarten-TEX | LaTeX-Quelle existiert | `PLATZKARTEN-XX-name.tex` |
| 0.3 | Platzkarten-PDF | Kompiliert ohne Fehler | `PLATZKARTEN-XX-name.pdf` |
| 0.4 | QR-LP-TEX | Lernpfad-QR existiert | `QR-LP-XX-name.tex` |
| 0.5 | QR-LP-PDF | Kompiliert ohne Fehler | `QR-LP-XX-name.pdf` |
| 0.6 | QR-MT-TEX | Minitest-QR existiert | `QR-MT-XX-name.tex` |
| 0.7 | QR-MT-PDF | Kompiliert ohne Fehler | `QR-MT-XX-name.pdf` |
| 0.8 | Abhängigkeiten | Alle Bilder/SIMs im Ordner | `img/`, `leifi/`, etc. |

### Checkliste Dateien

```
projekts/[fach]/[klasse]/[thema]/
├── MT-XX-name.html          ← Minitest
├── PLATZKARTEN-XX-name.tex  ← Platzkarten LaTeX
├── PLATZKARTEN-XX-name.pdf  ← Platzkarten PDF
├── QR-LP-XX-name.tex        ← QR für Lernpfad
├── QR-LP-XX-name.pdf
├── QR-MT-XX-name.tex        ← QR für Minitest
├── QR-MT-XX-name.pdf
└── [img/leifi/...]          ← Abhängigkeiten (Bilder, etc.)
```

---

## Phase 1: Technische Prüfung (Struktur & Code)

| # | Prüfpunkt | Kriterium |
|---|-----------|-----------|
| 1.1 | HTML-Struktur | Folgt Template-Muster (`MT-TEMPLATE-minitest.html`) |
| 1.2 | JavaScript | ES5-konform (kein `let`/`const`/Arrow Functions) |
| 1.3 | STORAGE_KEY | Eindeutig definiert (`mt-[fach]-[klasse]-[thema]`) |
| 1.4 | Element-IDs | Konsistent mit Bindestrichen (`q1-a`, `q1-b`, etc.) |
| 1.5 | Fachfarbe | Durchgängig korrekt (Physik: `#2c5aa0`, Chemie: `#2a7a4b`, etc.) |
| 1.6 | Bildpfade | Relative Pfade, keine absoluten URLs |

---

## Phase 2: Persistenz-Prüfung

| # | Prüfpunkt | Kriterium |
|---|-----------|-----------|
| 2.1 | Platznummer | Wird in localStorage gespeichert (`-seat`) |
| 2.2 | Niveau | Wird in localStorage gespeichert (`-niveau`) |
| 2.3 | Antworten | Alle Inputs (Dropdowns, Radio, Text) werden bei Änderung gespeichert |
| 2.4 | Reload während Test | Alle Eingaben werden wiederhergestellt |
| 2.5 | Submitted-Status | Bleibt nach Abgabe erhalten (`-submitted`) |
| 2.6 | Reload nach Abgabe | Bewertung und Feedback bleiben sichtbar |

### Kritische Init-Reihenfolge

```javascript
window.onload = function() {
    generateSeatDropdown();
    setupOptions();
    setupDropdowns();

    // WICHTIG: loadProgress() VOR restoreNiveauDropdown()!
    // Sonst überschreibt selectNiveau() → saveProgress() die Daten
    loadProgress();

    restoreNiveauDropdown();
    updateProgress();
    checkUnlocked();
    // ...
};
```

---

## Phase 3: Funktionale Prüfung

| # | Prüfpunkt | Kriterium |
|---|-----------|-----------|
| 3.1 | Platznummer-Lock | OK-Button sperrt Auswahl dauerhaft |
| 3.2 | Niveau-Lock | OK-Button sperrt Auswahl und zeigt Aufgaben |
| 3.3 | Fortschrittsbalken | Aktualisiert sich bei jeder Eingabe |
| 3.4 | Niveau-Filter | Höhere Niveau-Aufgaben als "nicht gewertet" markiert |
| 3.5 | Submit-Button | Löst Bewertung aus, deaktiviert Inputs |
| 3.6 | **Submit-Button Sichtbarkeit** | **Vor Platz/Niveau-Unlock versteckt (hidden class)** |
| 3.7 | Punkteberechnung | Korrekt pro Aufgabe und gesamt |
| 3.8 | Feedback | Richtig (grün) / Falsch (rot) wird angezeigt |
| 3.9 | Lösungsanzeige | Korrekte Antworten werden nach Abgabe gezeigt |
| 3.10 | Notenspiegel | Tabelle mit NP/%-Schwellen wird angezeigt |
| 3.11 | Notenpunkte | Werden korrekt aus Prozent berechnet |
| 3.12 | **Reset-Button (Lehrer)** | **Button mit Code "2024" zum Zurücksetzen des Tests** |
| 3.13 | **Drucken-Button** | **Button zum Drucken/PDF-Export vorhanden** |
| 3.14 | **Platznummer in Ergebnis** | **Nach Abgabe: Platznummer groß und ROT angezeigt** |

---

## Phase 4: Anti-Betrug-Prüfung

| # | Prüfpunkt | Kriterium |
|---|-----------|-----------|
| 4.1 | Startzeit | Wird erfasst (`-start`) |
| 4.2 | Tab-Wechsel | Werden gezählt (`-tabswitches`) |
| 4.3 | Abgabezeit | Wird erfasst (`-submit-time`) |
| 4.4 | Platznummer-Sperre | Nach OK nicht mehr änderbar |
| 4.5 | Niveau-Sperre | Nach OK nicht mehr änderbar |
| 4.6 | Input-Sperre | Nach Abgabe alle Inputs deaktiviert |

### localStorage-Keys (Beispiel)

```
mt-physik-9-09a-gleichstrommotor-start
mt-physik-9-09a-gleichstrommotor-seat
mt-physik-9-09a-gleichstrommotor-seat-locked
mt-physik-9-09a-gleichstrommotor-niveau
mt-physik-9-09a-gleichstrommotor-niveau-locked
mt-physik-9-09a-gleichstrommotor-progress
mt-physik-9-09a-gleichstrommotor-tabswitches
mt-physik-9-09a-gleichstrommotor-submitted
mt-physik-9-09a-gleichstrommotor-submit-time
```

---

## Phase 5: Fachliche Prüfung

| # | Prüfpunkt | Kriterium |
|---|-----------|-----------|
| 5.1 | Fragestellungen | Fachlich korrekt formuliert |
| 5.2 | Korrekte Antworten | Im `answers`-Objekt fachlich richtig |
| 5.3 | Feedback-Texte | Fachlich korrekte Erklärungen |
| 5.4 | Fachkonventionen | Korrekt angewendet (z.B. Rechte-Hand-Regel, Schaltzeichen) |
| 5.5 | Einheiten | SI-Einheiten, kopfrechenbare Werte |
| 5.6 | Bilder/Diagramme | Unterstützen Verständnis, korrekt beschriftet |
| 5.7 | Niveau-Zuordnung | Angemessen (★ AFB I, ★★ AFB II, ★★★ AFB III) |
| 5.8 | BE-Verteilung | Mindestens 25 BE für BR-Niveau |

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

### HTML-Prüfung (MT)

```bash
# CSS-Klassen prüfen
grep -E 'class="fz"|class="einheit"|class="frac"' MT-XX.html

# Formelzeichen kursiv?
grep -oE '<span class="fz">[A-Za-z]</span>' MT-XX.html | head -10

# Einheiten aufrecht?
grep -oE '<span class="einheit">[^<]+</span>' MT-XX.html | head -10

# Brüche korrekt?
grep -oE 'class="frac"' MT-XX.html
```

### Checkliste ISO 80000 (MT)

- [ ] Alle Formelzeichen (*F*, *m*, *U*, *I*, etc.) kursiv (`<span class="fz">`)?
- [ ] Alle Einheiten (N, V, A, Ω, etc.) aufrecht (`<span class="einheit">`)?
- [ ] Deskriptive Indizes (G, R, ges, max) aufrecht?
- [ ] Zählvariablen-Indizes (*n*, *i*, *k*) kursiv?
- [ ] Horizontale Bruchstriche (`<span class="frac">`) in Formeln?
- [ ] Leerzeichen zwischen Zahl und Einheit?
- [ ] Mittelpunkt (·) als Multiplikationszeichen?

---

## Phase 6: UI/Layout-Prüfung

| # | Prüfpunkt | Kriterium |
|---|-----------|-----------|
| 6.1 | Header | Fachfarbe korrekt |
| 6.2 | Niveau-Badges | ★ grün, ★★ blau, ★★★ lila |
| 6.3 | Fragenkarten | Weißer Hintergrund, saubere Abstände |
| 6.4 | Bilder | Laden korrekt, Attribution vorhanden |
| 6.5 | Fortschrittsbalken | Visuell korrekt, Prozent stimmt |
| 6.6 | Feedback-Farben | Grün (richtig), Rot (falsch), Orange (Hinweis) |
| 6.7 | Deaktivierte Inputs | Visuell erkennbar nach Abgabe |
| 6.8 | Ergebnis-Box | Notenspiegel lesbar, Punkte prominent |
| 6.9 | **Platznummer in Ergebnis** | **Platznummer groß und ROT (#c62828) angezeigt** |
| 6.10 | Responsive | Keine Überlappungen bei verschiedenen Breiten |
| 6.11 | Druckansicht | Buttons ausgeblendet, sauberes Layout |
| 6.12 | **Drucken-Button** | **Button "Drucken / PDF" vorhanden und funktional** |
| 6.13 | **Reset-Button** | **Lehrer-Reset mit Code "2024" vorhanden** |

---

## Phase 7: Deployment & Abhängigkeiten

> **Ziel:** Online-Ressourcen sind erreichbar, Print-Dokumente existieren lokal mit korrekten QR-Links.

### Deployment-Übersicht

| Dokumenttyp | Deployment | Prüfung |
|-------------|------------|---------|
| `MT-XX.html` | **Online** (GitHub Pages) | HTTP 200 prüfen |
| `LP-XX.html` | **Online** (GitHub Pages) | HTTP 200 prüfen |
| `SIM-XX.html` | **Online** (GitHub Pages) | HTTP 200 prüfen |
| Bilder (`img/`, `leifi/img/`) | **Online** (GitHub Pages) | HTTP 200 prüfen |
| `PLATZKARTEN-XX.pdf` | **Lokal** (nur Print) | Existiert, QR → Online-URL |
| `QR-LP-XX.pdf` | **Lokal** (nur Print) | Existiert, QR → Online-URL |
| `QR-MT-XX.pdf` | **Lokal** (nur Print) | Existiert, QR → Online-URL |

### 7.1 Online-Ressourcen (GitHub Pages)

| # | Prüfpunkt | Kriterium |
|---|-----------|-----------|
| 7.1.1 | MT online | `https://devbox42.github.io/sciencesim/[pfad]/MT-XX.html` → HTTP 200 |
| 7.1.2 | LP online | `https://devbox42.github.io/sciencesim/[pfad]/LP-XX.html` → HTTP 200 |
| 7.1.3 | SIM online | Falls vorhanden: `SIM-XX.html` → HTTP 200 |
| 7.1.4 | Bilder online | Alle `<img src="...">` laden (DevTools → Network) |
| 7.1.5 | Konsole sauber | Keine 404-Fehler in Browser-Konsole |
| 7.1.6 | Version aktuell | Online-Version = lokale Version |

### 7.2 Print-Dokumente (nur lokal)

> **Hinweis:** Diese PDFs werden **nicht** online deployed. Sie dienen zum Ausdrucken und Austeilen im Unterricht.

| # | Prüfpunkt | Kriterium |
|---|-----------|-----------|
| 7.2.1 | PLATZKARTEN-PDF | Existiert lokal, kompiliert ohne Fehler |
| 7.2.2 | QR-LP-PDF | Existiert lokal, kompiliert ohne Fehler |
| 7.2.3 | QR-MT-PDF | Existiert lokal, kompiliert ohne Fehler |

### 7.3 QR-Code-Verknüpfung

> **Kritisch:** Die QR-Codes in den Print-Dokumenten müssen auf die **Online-URLs** zeigen!

| # | Prüfpunkt | Kriterium |
|---|-----------|-----------|
| 7.3.1 | PLATZKARTEN-URL | QR zeigt auf `devbox42.github.io/.../MT-XX.html` |
| 7.3.2 | QR-LP-URL | QR zeigt auf `devbox42.github.io/.../LP-XX.html` |
| 7.3.3 | QR-MT-URL | QR zeigt auf `devbox42.github.io/.../MT-XX.html` |
| 7.3.4 | QR scannbar | Smartphone kann QR lesen und URL öffnen |
| 7.3.5 | Link klickbar | `\href{}` in .tex → Klick auf QR im PDF öffnet Browser |
| 7.3.6 | hyperref aktiv | `\usepackage{hyperref}` in allen .tex vorhanden |

### Prüfmethode: Online-Ressourcen

```bash
# MT online prüfen
curl -s -o /dev/null -w "%{http_code}" "https://devbox42.github.io/sciencesim/[pfad]/MT-XX.html"
# Erwartung: 200

# Alle Bildpfade im MT extrahieren
grep -oE 'src="[^"]+\.(png|jpg|gif|svg)"' MT-XX.html

# Bilder online prüfen
curl -s -o /dev/null -w "%{http_code}" "https://devbox42.github.io/sciencesim/[pfad]/[bild]"
# Erwartung: 200
```

### Prüfmethode: Print-Dokumente & QR

```bash
# 1. PDFs existieren?
ls -la PLATZKARTEN-*.pdf QR-LP-*.pdf QR-MT-*.pdf

# 2. URL in .tex prüfen (muss devbox42.github.io enthalten)
grep "devbox42" PLATZKARTEN-*.tex QR-*.tex

# 3. PDF öffnen, QR mit Smartphone scannen
open PLATZKARTEN-XX.pdf

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

- Persistenz funktioniert nicht
- Falsche fachliche Inhalte
- Bewertung berechnet falsch
- Anti-Betrug-Mechanismen fehlen
- **MT/LP nicht online erreichbar** (HTTP 404)
- **Bilder/Abhängigkeiten fehlen online** (HTTP 404)
- **QR-Codes zeigen auf falsche/alte URL**
- **Submit-Button vor Unlock sichtbar** (ermöglicht leere Abgabe)
- **Reset-Button für Lehrer fehlt** (Lehrer kann nicht bei Schüler-Problemen helfen)
- **Platznummer nicht in Ergebnissen** (Zuordnung bei Ausdruck unklar)
- **ISO 80000 verletzt** (Einheiten kursiv, Formelzeichen aufrecht, Slashes in Formeln)

### Kleinere Mängel (Nachbesserung)

- Styling-Inkonsistenzen
- Fehlende Attributionen
- Unklare Formulierungen
- Print-PDFs nicht aktuell kompiliert (lokal)
- `\href{}` fehlt in .tex (QR nicht klickbar im PDF)

---

## Prüfprotokoll-Vorlage

```markdown
## Prüfprotokoll: [MT-Name]

**Datum:** [TT.MM.JJJJ]
**Prüfer:** [Name/Claude]
**Version:** [vX.Y]
**GitHub-URL:** https://devbox42.github.io/sciencesim/[pfad]/MT-XX-name.html

### Ergebnisse

| Phase | Status | Anmerkungen |
|-------|--------|-------------|
| 0. Vollständigkeit | ✅/⚠️/❌ | |
| 1. Technisch | ✅/⚠️/❌ | |
| 2. Persistenz | ✅/⚠️/❌ | |
| 3. Funktional | ✅/⚠️/❌ | |
| 4. Anti-Betrug | ✅/⚠️/❌ | |
| 5. Fachlich | ✅/⚠️/❌ | |
| **5b. ISO 80000** | ✅/⚠️/❌ | Typografie |
| 6. UI/Layout | ✅/⚠️/❌ | |
| 7. Deployment | ✅/⚠️/❌ | |

### Online-Ressourcen (GitHub Pages)

| Datei | Lokal | Online (HTTP) | Status |
|-------|-------|---------------|--------|
| MT-XX.html | ✅ | 200 | OK |
| LP-XX.html | ✅ | 200 | OK |
| img/bild1.png | ✅ | 200 | OK |
| img/bild2.png | ✅ | 404 | FEHLT |

### Print-Dokumente (nur lokal)

| Dokument | PDF existiert | QR → Online-URL | Link klickbar |
|----------|---------------|-----------------|---------------|
| PLATZKARTEN | ✅/❌ | ✅/❌ | ✅/❌ |
| QR-LP | ✅/❌ | ✅/❌ | ✅/❌ |
| QR-MT | ✅/❌ | ✅/❌ | ✅/❌ |

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
curl -s -o /dev/null -w "%{http_code}" "https://devbox42.github.io/sciencesim/[pfad]/MT-XX.html"
# Erwartung: 200

# 2. Print-PDFs existieren lokal?
ls -la PLATZKARTEN-*.pdf QR-*.pdf

# 3. QR-URL korrekt? (muss devbox42.github.io enthalten)
grep "devbox42" PLATZKARTEN-*.tex

# 4. QR-Code scannen (manuell mit Smartphone) → Öffnet MT?

# 5. Im Browser: DevTools → Console → Keine 404-Fehler?

# 6. Persistenz: Eingabe machen → Reload → Eingabe noch da?
```

### Funktions-Check (nach jeder MT-Erstellung)

| # | Prüfung | Aktion |
|---|---------|--------|
| 1 | Submit vor Unlock? | Seite laden → Submit-Button MUSS hidden sein |
| 2 | Reset-Button? | Nach Abgabe → "Reset"-Button mit Code "2024" MUSS erscheinen |
| 3 | Drucken-Button? | Nach Abgabe → "Drucken / PDF"-Button MUSS vorhanden sein |
| 4 | Platznummer rot? | Nach Abgabe → Platznummer MUSS groß & ROT angezeigt werden |

### Zusammenfassung: Was muss wo sein?

| Was | Wo | Warum |
|-----|-----|-------|
| MT/LP/SIM.html | **Online** (GitHub) | Schüler greifen per QR darauf zu |
| Bilder, Abhängigkeiten | **Online** (GitHub) | Werden von MT/LP geladen |
| PLATZKARTEN.pdf | **Lokal** (Print) | Wird ausgedruckt und ausgeteilt |
| QR-LP/QR-MT.pdf | **Lokal** (Print) | Wird ausgedruckt/projiziert |

---

## Referenzen

- Template: `templates/mint/MT-TEMPLATE-minitest.html`
- Dokumentation: `templates/mint/README-MINITEST-MINT.md`
- Design-System: `CLAUDE.md` (Abschnitt "Design-System")
- Publish-Script: `projects/physik/publish.sh` (falls vorhanden)
