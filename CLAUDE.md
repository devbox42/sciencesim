# CLAUDE.md - Greenhouse Lernpfade

## Projektübersicht

Dieses Projekt erstellt digitale Lernpfade, Quizze und Arbeitsblätter für Greenhouse Schools Rostock.

- **Fächer:** Physik, Chemie, Informatik, Spanisch
- **Klassenstufen:** 5-12 (Gesamtschule MV)
- **Outputs:** HTML (digital), LaTeX/docx (Print)

---

## Wichtige Regeln

### 1. Vor dem Arbeiten

```bash
# IMMER zuerst prüfen:
pwd                    # Muss diesen Ordner zeigen!
git status             # Muss clean sein!
```

### 2. Workflow

1. **Lese zuerst** die relevanten Dateien in `knowledge/`
2. **Plane** bevor du Code schreibst
3. **Zeige** den Plan zur Bestätigung
4. **Implementiere** schrittweise
5. **Teste** nach jeder Änderung
6. **Committe** wenn es funktioniert

### 3. Git-Commits

```bash
# Nach jeder funktionierenden Änderung:
git add .
git commit -m "feat: Beschreibung"

# Bei Fehlern:
git checkout .         # Alle Änderungen verwerfen
```

---

## Fachspezifische Workflows

### Spanisch-Unterricht (PFLICHT)

> **KRITISCH:** Bei JEDER Spanisch-Material-Anfrage diese Schritte befolgen!

**1. Workflow lesen (IMMER zuerst):**
```bash
# Pflichtlektüre vor jeder Spanisch-Materialerstellung:
templates/spanisch/WORKFLOW-SPANISCH.md
```

**2. Phasen strikt einhalten:**
```
Phase 0: Kontextaufnahme (User-Input → A/B/C/D kategorisieren)
Phase 1: Anfrage + Modus (KOMPAKT oder Tier 1-3?)
Phase 2: Planung (PLANUNG-xxx.md oder LE-xxx.tex erstellen)
Phase 3: Materialien (AB → LB/LP/SLIDES → ML/LH)
Phase 4: Kompilierung & Prüfung
```

**3. Keine Materialien ohne Planung:**
- DEFAULT: KOMPAKT-Planungsnotiz (`PLANUNG-xxx.md`, ~250 Tokens)
- Bei Anfrage: Langentwurf (`LE-xxx.tex`, Tier 1/2/3)
- **VERBOTEN:** Materialien direkt erstellen ohne Phase 2!

**4. Lehrwerk-Referenz nutzen:**
| Klassenstufe | Lehrwerk | Referenz |
|--------------|----------|----------|
| 7-8 | Qué pasa 1 | `knowledge/Spanisch-Que-Pasa-1/` |
| 9 | Qué pasa 2 | `knowledge/Spanish-Que-Pasa-2/` |
| 10-12 | A_tope.com | `knowledge/Spanisch-A_tope_Spaetbeginner/` |

**5. Qualitäts-Checkliste (vor Freigabe):**
- [ ] Spanisch-Korrektheit (Akzente, Grammatik, Genus)
- [ ] AB max. 2 Seiten, mind. 25 BE
- [ ] ES5-JavaScript (kein let/const/Arrow)
- [ ] Fachfarbe `#c41e3a` (Karminrot)

---

## Sprachliche Konventionen

### Deutsche Umlaute und Sonderzeichen

**IMMER echte Umlaute und Sonderzeichen verwenden:**

| Richtig | Falsch |
|---------|--------|
| ä, ö, ü | ae, oe, ue |
| Ä, Ö, Ü | Ae, Oe, Ue |
| ß | ss |

**Gilt für alle Ausgabeformate:** HTML, LaTeX, Markdown, etc.

**Ausnahme:** Dateinamen dürfen `ae`, `oe`, `ue` verwenden (Kompatibilität).

---

## Design-System (sciencesim-konsistent)

### Farben

```css
/* Hintergrund */
--bg: #f5f5f5;
--white: #ffffff;
--border: #dddddd;

/* Text */
--text-primary: #222222;
--text-secondary: #555555;
--text-muted: #888888;

/* Fach-Akzente */
--physik: #2c5aa0;      /* Blau */
--chemie: #2a7a4b;      /* Grün */
--informatik: #b35c00;  /* Orange */
--spanisch: #c41e3a;    /* Karminrot */

/* Feedback */
--success: #2a7a4b;
--warning: #b35c00;
--error: #c62828;

/* Ladungen & Pole (Physik) */
--positive: #c62828;    /* ROT: +, techn. Stromrichtung */
--negative: #1565c0;    /* BLAU: -, Elektronen */

/* Magnetfeld (Physik) */
--magnetic: #2e7d32;    /* GRÜN: B-Feld, Feldlinien */
```

### Farbkonventionen Ladungen, Pole & Magnetfeld (Physik)

| Element | Farbe | CSS-Variable |
|---------|-------|--------------|
| Positive Ladung (+) | ROT | `--positive` |
| Positive Pole | ROT | `--positive` |
| Techn. Stromrichtung | ROT | `--positive` |
| Protonen | ROT | `--positive` |
| Negative Ladung (-) | BLAU | `--negative` |
| Negative Pole | BLAU | `--negative` |
| Elektronen | BLAU | `--negative` |
| **Magnetfeld (B)** | **GRÜN** | `--magnetic` |
| **Feldlinien** | **GRÜN** | `--magnetic` |
| **B-Feld-Pfeile** | **GRÜN** | `--magnetic` |

**Gilt für:** Simulationen, Schaltbilder, Atom-Darstellungen, alle Visualisierungen mit Ladungen und Magnetfeldern.

### Schaltzeichen (DIN-Norm) – IMMER deutsche Symbole!

**KRITISCH:** In allen Schaltplänen, Simulationen und Arbeitsblättern **ausschließlich deutsche DIN-Schaltzeichen** verwenden – KEINE IEC/amerikanischen Symbole!

| Bauteil | DIN-Symbol | Beschreibung |
|---------|------------|--------------|
| **Spannungsquelle (DC)** | Zwei parallele Linien | Lange Linie = + (rot), kurze dicke Linie = − (blau) |
| **Widerstand** | Rechteck | Leeres Rechteck mit R-Beschriftung |
| **Amperemeter** | Kreis mit A | Messgerät für Stromstärke |
| **Voltmeter** | Kreis mit V | Messgerät für Spannung (parallel geschaltet) |
| **Lampe** | Kreis mit X | Glühlampe |
| **Schalter** | Unterbrochene Linie | Offener/geschlossener Schalter |
| **Leitung** | Durchgezogene Linie | Verbindung, Kreuzung ohne Punkt = keine Verbindung |

**SVG-Beispiel Spannungsquelle:**
```svg
<!-- Lange Linie = + (oben, rot) -->
<line x1="35" y1="80" x2="65" y2="80" stroke="#c62828" stroke-width="2"/>
<!-- Kurze dicke Linie = − (unten, blau) -->
<line x1="40" y1="100" x2="60" y2="100" stroke="#1565c0" stroke-width="4"/>
```

**VERBOTEN:**
- ❌ IEC-Kreis für Spannungsquellen
- ❌ Amerikanische Zickzack-Widerstände
- ❌ Symbole ohne + / − Beschriftung bei Quellen

### Schaltplan-Score (10/10)

Nach jedem erstellten Schaltplan diese Checkliste prüfen:

| # | Kriterium | Prüfpunkt |
|---|-----------|-----------|
| 1 | **Spannungsquelle** | Zwei parallele Linien (lang = +, kurz/dick = −) |
| 2 | **Pole farbig** | + in rot (#c62828), − in blau (#1565c0) |
| 3 | **Widerstand** | Rechteck (nicht Zickzack), mit R beschriftet |
| 4 | **Messgeräte** | Kreis mit A/V, weiß gefüllt |
| 5 | **Leitungen bündig** | Alle Verbindungen schließen exakt an, keine Lücken |
| 6 | **Bauteile zentriert** | R, A, V exakt auf der Leitung, nicht daneben |
| 7 | **Rechte Winkel** | Nur 90°-Ecken, keine Diagonalen |
| 8 | **Stromrichtung** | Pfeil mit I beschriftet (rot = technisch) |
| 9 | **Werte lesbar** | U, R mit Einheiten (V, Ω, A) beschriftet |
| 10 | **Sauber** | Keine Überlappungen, weißer Fill bei Bauteilen |

**Bewertung:** 10/10 = Freigabe | < 10 = Nachbessern

**PFLICHT:** Bei technischen Zeichnungen (Schaltpläne, Diagramme) MUSS 10/10 erreicht werden. Keine Freigabe unter 10/10!

### Layout

- Container: `max-width: 900px`, zentriert
- Boxen: `border: 1px solid #ddd`, KEINE Schatten
- Radius: **max 3px** (besser: gar keiner)
- Grid: Hauptbereich + 280px Sidebar (für Simulationen)

### Typografie

- Font: System-Fonts (`-apple-system, BlinkMacSystemFont, ...`)
- h1: `1.4em`, weight 600
- Body: `0.9em`
- Labels: `0.85em`
- Mono: Für Werte und Code

### VERBOTEN (AI-typisch)

- ❌ Gradients
- ❌ Box-shadows
- ❌ border-radius > 3px
- ❌ Bunte Buttons
- ❌ Hover-Animationen
- ❌ Glassmorphism
- ❌ "Hero Sections"

---

## Differenzierung (★-System)

| Niveau | Marker | Zielgruppe | Charakteristik |
|--------|--------|------------|----------------|
| ★ | `niveau: 1` | Berufsreife (BR) | Qualitativ, Lückentext, Kopfrechnen |
| ★★ | `niveau: 2` | Mittlere Reife (MR) | Formelumstellung, mehrstufig |
| ★★★ | `niveau: 3` | Gymnasium (GY) | Transfer, Analyse, komplex |

### Klasse 6-8
- Sternchen sichtbar auf AB/Test: `(*)`, `(**)`, `(***)`
- BR-Aufgaben müssen mind. 25 BE ergeben

### Klasse 9
- G-Kurs → MR-Niveau (keine Sternchen drucken)
- E-Kurs → GY-Niveau (keine Sternchen drucken)

### Klasse 10+
- MR → Schulnote 1-6
- GY/Sek II → 15-NP-Skala

---

## Kopfrechenbar-Regeln (KRITISCH!)

### IMMER verwenden

| Größe | Erlaubte Werte |
|-------|----------------|
| **g** | **10 m/s²** (NICHT 9,81!) |
| Geschwindigkeiten | 36, 72, 90, 108 km/h |
| Zeiten | 2, 3, 4, 5, 6, 8, 10 s |
| Beschleunigungen | 2, 4, 5, 10 m/s² |
| Strecken | 20, 25, 40, 50, 80, 100 m |

### Erlaubte Wurzeln

√4=2, √9=3, √16=4, √25=5, √36=6, √49=7, √64=8, √81=9, √100=10

### Umrechnungen

36→10, 72→20, 90→25, 108→30 (km/h → m/s, ÷3,6)

---

## Bewertungsskalen

### Sek II (15-NP)

| NP | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 |
|----|----|----|----|----|----|----|---|---|---|---|---|---|---|---|---|
| % | 98,67 | 97,33 | 96 | 90,67 | 85,33 | 80 | 73,33 | 66,67 | 60 | 53,33 | 46,67 | 40 | 33,33 | 26,67 | 20 |

### Sek I (14-NP)

| NP | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 |
|----|----|----|----|----|----|----|---|---|---|---|---|---|---|---|
| % | 100 | 96 | 90,67 | 86 | 80 | 73,33 | 66,67 | 60 | 53,33 | 46,67 | 40 | 33,33 | 26,67 | 20 |

### MR Klasse 10 (6-Noten)

| Note | 1 | 2 | 3 | 4 | 5 | 6 |
|------|---|---|---|---|---|---|
| % | ≥96 | ≥80 | ≥60 | ≥40 | ≥20 | <20 |

---

## Lernpfad-Struktur (Interleaved)

```
Content → Exercise → Content → Exercise → Test
   ↑         ↑          ↑         ↑         ↑
   │         │          │         │         │
Optional  Auto-check  Optional  Auto-check  Graded
```

### Modul-Typen

| Type | Zweck | Auto-check |
|------|-------|------------|
| `content` | Erklärung, Text, Bilder | — |
| `simulation` | Eingebettete sciencesim | — |
| `exercise` | Übung mit Feedback | ✅ |
| `test` | Bewertete Stundenleistung | ✅ |

### Arbeitsblatt-Hinweise (Hefter-Hinweis)

Bei Lernpfaden mit begleitendem Arbeitsblatt: Nach jedem Content-Schritt einen **Hefter-Hinweis** einfügen, der zeigt, was ins Arbeitsblatt übernommen werden soll.

**CSS-Styling:**

```css
.hefter-hinweis {
    background: var(--warning-bg);      /* #fff3e0 */
    border: 2px solid var(--warning);   /* #b35c00 */
    padding: 12px 15px;
    margin: 20px 0;
    font-size: 0.9em;
}
.hefter-hinweis::before {
    content: "Arbeitsblatt";
    display: inline-block;
    background: var(--warning);
    color: white;
    font-size: 0.75em;
    font-weight: 600;
    padding: 2px 8px;
    margin-bottom: 8px;
}
```

**HTML-Verwendung:**

```html
<div class="hefter-hinweis">
    <strong>Arbeitsblatt (Abschnitt X):</strong>
    <ul>
        <li>Ergänze die <strong>Definition</strong> im Lückentext</li>
        <li>Übernimm die <strong>Formel</strong></li>
    </ul>
</div>
```

**Regeln:**
- Orange Rahmen hebt sich von blauen Info-Boxen ab
- Label "Arbeitsblatt" als Badge oben
- Konkrete Anweisungen (welcher Abschnitt, was eintragen)
- Nach Content-Schritten, nicht nach Übungen

### Persistenz (localStorage)

**Pflicht:** Alle Eingaben in Lernpfaden und Tests müssen mit `localStorage` gespeichert werden.

```javascript
// Speichern bei Eingabe
document.querySelectorAll('input, select').forEach(el => {
    const key = 'lp-' + LERNPFAD_ID + '-' + el.id;

    // Beim Laden wiederherstellen
    if (localStorage.getItem(key)) {
        el.value = localStorage.getItem(key);
    }

    // Bei Änderung speichern
    el.addEventListener('change', () => {
        localStorage.setItem(key, el.value);
    });
});
```

**Regeln:**
- Eindeutiger Präfix pro Lernpfad/Test (z.B. `lp-ohm-01-`)
- Alle `input`, `select`, `textarea` Elemente einbinden
- Fortschritt (aktuelle Sektion) ebenfalls speichern
- Reset-Button nur mit Bestätigung

### Keine Sequenz-Kommunikation für Schüler

**WICHTIG:** Schülermaterialien (LP, AB) kommunizieren KEINE Stundensequenz.

| Erlaubt | Verboten |
|---------|----------|
| "Das Ohmsche Gesetz" | "Stunde 1 von 4" |
| "Elektrischer Widerstand" | "In der nächsten Stunde..." |
| Thema ohne Nummer | "Ausblick: Folgestunden" |

**Nur für Lehrer (LH):**
- Stundennummern
- Sequenz-Übersicht
- Ausblick auf Folgestunden

**Grund:** Flexibilität für Lehrkräfte bei Reihenfolge und Zeiteinteilung.

---

## Materialstruktur pro Unterrichtseinheit

### MINT-Unterricht (Physik, Chemie, Informatik)

> **Workflow-Referenz:** `templates/mint/WORKFLOW-MINT.md`

**Phasen:**
```
Phase 0: Kontextaufnahme (User-Input → A/B/C/D kategorisieren)
Phase 1: Anfrage + Modus (KOMPAKT oder Tier 1-3?)
Phase 2: Planung (PLANUNG-xxx.md oder LE-xxx.tex erstellen)
Phase 3: Materialien (AB → LS/LP/SIM → ML/LH/SL)
Phase 4: Kompilierung & Prüfung
```

**Planungs-Modi:**
| Modus | Format | Wann verwenden |
|-------|--------|----------------|
| **KOMPAKT** | `PLANUNG-xxx.md` | **DEFAULT** – Regulärer Unterricht |
| Tier 1-3 | `LE-xxx.tex` | Nur bei expliziter Anfrage |

**KOMPAKT ist Default.** Langentwurf (Tier 1-3) nur bei Unterrichtsbesuchen oder expliziter Anfrage.

### Pflicht-Dokumente pro Stunde

| Nr | Typ | Dateiname-Muster | Beschreibung |
|----|-----|------------------|--------------|
| 0 | Langentwurf | `LE-XX-kurzname.tex` | Unterrichtsentwurf (Tier 1/2/3) |
| 1 | Lernpfad | `LP-XX-kurzname.html` | Interaktiver Lernpfad |
| 2 | Arbeitsblatt | `AB-XX-kurzname.tex` | Wissensbasis + Aufgaben (Hefter) |
| 3 | Lehrerhinweise | `LH-XX-kurzname.tex` | Kurz-Lessonplan + Lösungen |
| 4 | Musterlösung | `ML-XX-kurzname.tex` | AB mit Lösungen (rot) |
| 5 | Simulation | `SIM-XX-kurzname.html` | Interaktive Simulation (wo sinnvoll) |

**XX** = zweistellige Stundennummer (01, 02, 03...)

### Dateinamen-Konventionen

```
LP-01-atommodelle.html      # Lernpfad Stunde 1
AB-01-atommodelle.tex       # Arbeitsblatt Stunde 1
LH-01-atommodelle.tex       # Lehrerhinweise Stunde 1
SIM-01-rutherford.html      # Simulation zu Stunde 1

LP-02-radioaktivitaet.html
AB-02-radioaktivitaet.tex
LH-02-radioaktivitaet.tex
...
```

**Regeln:**
- Max. 20 Zeichen nach der Nummer
- **Keine Umlaute in Dateinamen** (hier: ae, oe, ue erlaubt)
- Kleinschreibung, Bindestriche statt Leerzeichen

### Verknüpfung Lernpfad ↔ Arbeitsblatt

- Lernpfad verweist auf explizite AB-Aufgaben: `→ Bearbeite AB Aufgabe 3`
- AB enthält konsolidiertes Wissen nach Bearbeitung des Lernpfads
- AB dient als **Lernbasis für Prüfungsvorbereitung** (zum Abheften)

### Lehrerhinweise (Kurz-Lessonplan)

Jedes LH-Dokument enthält:

| Abschnitt | Inhalt |
|-----------|--------|
| **Stundenverlauf** | Tabellarisch, 5-Minuten-Raster |
| **Differenzierung** | Hinweise für ★/★★/★★★ |
| **Häufige Fehler** | Typische Schülerfehler + Reaktionen |
| **Material** | Benötigte Materialien/Geräte |
| **Lösungen** | Vollständige AB-Lösungen |

### Arbeitsblätter (AB) – Konzept

**Grundprinzip:** ABs sind **begleitende Dokumente zum Lernpfad**, keine eigenständigen Wissenssammlungen.

| Regel | Beschreibung |
|-------|--------------|
| **Keine Dopplung** | Was im Lernpfad erklärt wird, wird NICHT nochmal aufs AB kopiert |
| **Kästen zum Übertragen** | Schüler übertragen Merksätze/Formeln selbst aus dem Lernpfad |
| **Vollständig nach Bearbeitung** | AB enthält am Ende alles Prüfungsrelevante (rahmenplankonform) |
| **Keine Lösungen auf AB** | Lösungen kommen in separate Musterlösung |

**Musterlösung (ML):**
- Identisches Layout wie AB
- Lösungen in **roter Farbe** eingesetzt
- Dateiname: `ML-XX-kurzname.tex` (bzw. `.pdf`)
- Wird immer zusammen mit AB erstellt

**AB-Struktur:**

| Element | Inhalt |
|---------|--------|
| **Kästen** | Leer mit Beschriftung – Schüler übertragen aus Lernpfad |
| **Übungen AFB I** | Einsetzen, Zuordnen, Beschriften, Lückentext |
| **Übungen AFB II** | Berechnen, Erklären, Anwenden, Vergleichen |
| **Übungen AFB III** | Fehler begründen, Bewerten, Transfer, Freies Schreiben |

**Format:**
- LaTeX → PDF (druckbar, A4)
- Kompakt: 1-2 Seiten, evtl. zweispaltig
- Serifenlos (Helvetica)
- Kopfzeile: Fach, Klasse, Thema, Name-Feld

**Verzahnung mit Lernpfad:**
Der Lernpfad enthält `hefter-hinweis`-Boxen, die auf konkrete AB-Abschnitte verweisen:
```html
<div class="hefter-hinweis">
    <ul>
        <li><strong>Kasten 1:</strong> Übertrage die Definition</li>
        <li><strong>Übung 2:</strong> Berechne die Halbwertszeit</li>
    </ul>
</div>
```

---

### Simulationen

Erstelle interaktive HTML5/Canvas/JS-Simulationen wo didaktisch sinnvoll:

| Thema | Simulationsidee |
|-------|-----------------|
| Atommodelle | Rutherford-Streuversuch |
| Radioaktivität | Würfel-Zerfall, Abschirmung |
| Halbwertszeit | Exponentieller Zerfall visualisiert |
| Kernreaktionen | Kettenreaktion |
| Strahlenschutz | Abstandsgesetz (1/r²) |
| Elektrik | Stromkreis-Simulator |
| Optik | Strahlengang, Linsen |
| Mechanik | Kräfte, Bewegung |

---

## Visualisierungen & Grafiken

### Grundsatz: Visuell arbeiten

**Wo immer möglich:**
- Illustrationen statt langer Texte
- Skizzen und Schemazeichnungen
- Diagramme (auch interaktiv)
- Animationen bei Prozessen
- Infografiken für Zusammenhänge

### Umsetzung in HTML

**Statische Grafiken:**
```html
<!-- SVG inline für Schemata -->
<svg viewBox="0 0 400 200" style="max-width: 100%;">
  <circle cx="100" cy="100" r="30" fill="var(--positive)"/> <!-- Proton -->
  <circle cx="150" cy="80" r="8" fill="var(--negative)"/>   <!-- Elektron -->
</svg>
```

**Interaktive Diagramme:**
```html
<!-- Canvas für Simulationen -->
<canvas id="simulation" width="600" height="400"></canvas>
<script>
  // Interaktive Visualisierung
</script>
```

### Diagramm-Typen nach Inhalt

| Inhalt | Diagramm-Typ |
|--------|--------------|
| Vergleiche | Balkendiagramm |
| Zeitverläufe | Liniendiagramm |
| Anteile | Kreisdiagramm (sparsam!) |
| Prozesse | Flussdiagramm |
| Strukturen | Schemazeichnung |
| Atome/Moleküle | SVG-Darstellung |
| Experimente | Aufbau-Skizze |

### Interaktive Elemente

- **Hover-Tooltips:** Zusatzinfos bei Mouseover
- **Klickbare Bereiche:** Erklärungen einblenden
- **Slider:** Parameter verändern (z.B. Zeit bei HWZ)
- **Drag & Drop:** Zuordnungsaufgaben
- **Zoom:** Details vergrößern

---

## Interaktive Elemente (Lückentexte, Dropdowns)

### Grundregel: Inline-Platzierung

Lücken, Inputs und Dropdowns **IMMER inline an der korrekten Textstelle** platzieren – nicht darunter oder daneben.

**FALSCH:**
```html
<p>Ergänze das fehlende Wort:</p>
<p>Die Masse beträgt:</p>
<input type="text">
```

**RICHTIG:**
```html
<p>Die Masse beträgt <input type="number" style="width:60px"> kg.</p>
<p>Das Elektron hat die Ladung <select><option>+1</option><option>-1</option></select>.</p>
```

### Styling für Inline-Inputs

```css
.fill-blank {
    border: none;
    border-bottom: 2px solid var(--physik);
    padding: 2px 5px;
    width: 80px;
    font-size: inherit;
    background: transparent;
    text-align: center;
}

.inline-select {
    padding: 2px 5px;
    font-size: inherit;
    border: 1px solid var(--border);
}
```

### Beispiele

```html
<!-- Numerische Lücke im Fließtext -->
<p>Ein Körper mit m = 5 kg und a = <input type="number" class="fill-blank" style="width:50px"> m/s²
   erfährt die Kraft F = <input type="number" class="fill-blank" style="width:50px"> N.</p>

<!-- Dropdown im Fließtext -->
<p>Beim α-Zerfall sinkt die Massenzahl um
   <select class="inline-select">
     <option>2</option>
     <option>4</option>
     <option>6</option>
   </select>
   und die Ordnungszahl um
   <select class="inline-select">
     <option>1</option>
     <option>2</option>
     <option>3</option>
   </select>.</p>
```

---

## Fragetypen (Quiz)

### Multiple Choice (`mc`)

```javascript
{
    id: "F1", type: "mc", niveau: 1, points: 2, afb: 1,
    text: "<span class='operator'>Nenne</span> ...",
    options: ["A", "B", "C", "D"],
    correct: 1,
    solution: "Erklärung"
}
```

### Numerisch mit Einheit (`numeric-unit`)

```javascript
{
    id: "F2", type: "numeric-unit", niveau: 2, points: 3, afb: 2,
    text: "<span class='operator'>Berechne</span> ...",
    correct: 20, tolerance: 0.5, correctUnit: "m/s",
    unitOptions: ["m/s", "km/h", "m/s²", "m", "s"],
    scoring: { value: 2, unit: 1 },
    solution: "72 ÷ 3,6 = 20 m/s"
}
```

### Zuordnung (`matching`)

```javascript
{
    id: "F3", type: "matching", niveau: 1, points: 4, afb: 1,
    pairs: 4,
    labels: ["v", "a", "s₁", "s₂"],
    options: ["v=s/t", "a=Δv/Δt", "s=v·t", "s=½at²"],
    correct: [0, 1, 2, 3],
    scoring: { perPair: 1 }
}
```

### Mehrstufig (`multi-calc`)

```javascript
{
    id: "F4", type: "multi-calc", niveau: 3, points: 6, afb: 3,
    fields: [
        { id: "a", label: "Teilaufgabe a", points: 2, accepted: [...] },
        { id: "b", label: "Teilaufgabe b", points: 4, accepted: [...] }
    ]
}
```

---

## KMK-Operatoren

### AFB I (~20-30%)
`nenne`, `gib an`, `beschreibe`, `ordne zu`

### AFB II (~40-50%)
`berechne`, `ermittle`, `bestimme`, `erkläre`, `vergleiche`

### AFB III (~20-30%)
`analysiere`, `begründe`, `beurteile`, `entwickle`

**Formatierung:** `<span class='operator'>Berechne</span> die ...`

---

## Dateistruktur

```
greenhouse-lernpfade/
├── CLAUDE.md                 ← Diese Datei
├── README.md
│
├── knowledge/                ← Referenzmaterial (read-only)
│   ├── curriculum/
│   │   ├── physik-mv-sek1.md
│   │   ├── physik-mv-sek2.md
│   │   ├── chemie-mv-sek1.md
│   │   ├── chemie-mv-sek2.md
│   │   └── informatik-mv.md
│   ├── frameworks/
│   │   ├── differentiation.md
│   │   ├── grading.md
│   │   └── quiz-format.md
│   └── design/
│       └── sciencesim-css.md
│
├── templates/                ← Vorlagen
│   ├── lesson-plan/
│   │   ├── langentwurf-template.tex  ← Langentwurf (Tier 1/2/3)
│   │   └── README.md
│   ├── quiz/
│   │   ├── quiz-template.html
│   │   └── decoder.html
│   ├── learning-path/
│   │   └── lernpfad-template.html
│   └── worksheet-tex/
│       └── arbeitsblatt.tex
│
└── projects/                 ← Echte Inhalte
    ├── physik/
    │   └── kl7-dichte/
    │       ├── spec.md
    │       ├── lernpfad.html
    │       └── stundenleistung.html
    ├── chemie/
    └── informatik/
```

---

## Checklisten

### Vor Ausgabe eines Quiz

- [ ] QUIZ_ID eindeutig?
- [ ] SUBJECT korrekt (physik/chemie/informatik)?
- [ ] g = 10 m/s² (nicht 9,81)?
- [ ] Alle Zahlen kopfrechenbar?
- [ ] Jede Frage hat `solution`?
- [ ] Operatoren mit `<span class='operator'>`?
- [ ] 5 Einheiten-Optionen pro Dropdown?
- [ ] AFB-Verteilung ~20/45/35%?
- [ ] UNLOCK_CODE geändert?
- [ ] TOTAL_POINTS = Summe aller Punkte?
- [ ] Mind. 25 BE für BR-Niveau?

### Vor Ausgabe eines Lernpfads

- [ ] Interleaved: Content ↔ Exercise?
- [ ] Jede Übung hat Feedback?
- [ ] Simulation-Links funktionieren?
- [ ] Fortschritt wird gespeichert?

### Vor Ausgabe eines LaTeX-AB

- [ ] Notenspiegel im Kopfbereich?
- [ ] Sternchen-Differenzierung (Kl. 6-8)?
- [ ] Punkteplatzhalter hinter jeder Teilaufgabe?
- [ ] Serifenlose Grundschrift?
- [ ] Mind. 25 BE gesamt?
- [ ] **Keine Einsetzstriche in Brüchen** (nur Bruchstrich!)

### LaTeX-Formeln in Arbeitsblättern

**Einsetzstriche und Brüche:**

```latex
% FALSCH - Doppellinien-Problem:
$\rho = \dfrac{\luecke{1.2cm}}{\luecke{1.2cm}}$

% RICHTIG - Lücken außerhalb des Bruchs:
$\rho = \dfrac{m}{V} = \dfrac{\text{\luecke{1.2cm}}}{\text{\luecke{1.2cm}}} = $ \luecke{1.5cm}

% BESSER - Nur Ergebnis-Lücke:
$\rho = \dfrac{m}{V} = $ \luecke{2cm}
```

**Regel:** Einsetzstriche (`\luecke{}`) erzeugen horizontale Linien. Diese kollidieren mit anderen horizontalen Linien → unlesbar. Daher:
- Formeln mit Brüchen: **Werte vorgeben** oder **Ergebnis als Lücke**
- Einsetzstriche nur in einzeiligen Gleichungen
- **Keine Einsetzstriche in Tabellenzellen** → leere Zellen mit `\\[0.8em]` für Höhe

---

## ISO 80000 Typografie (Formeln & Einheiten)

> **PFLICHT:** Alle Materialien (LP, AB, ML, LH, MT, SIM) müssen ISO 80000 / DIN 1338 konform sein!

### Grundregeln

| Element | Schreibweise | Beispiel |
|---------|--------------|----------|
| **Formelzeichen (Variablen)** | *kursiv* | *F*, *m*, *a*, *U*, *I*, *R* |
| **Einheiten** | aufrecht (nicht kursiv) | N, kg, m/s², V, A, Ω |
| **Zahlen** | aufrecht | 5, 3,14, 230 |
| **Bruchstriche** | horizontal (nicht Slash) | $$\frac{m}{V}$$ statt m/V |

### Indizes

| Index-Typ | Schreibweise | Beispiel | Erklärung |
|-----------|--------------|----------|-----------|
| **Deskriptiv** (beschreibend) | aufrecht | *F*<sub>G</sub>, *F*<sub>R</sub>, *U*<sub>ges</sub> | G = Gewicht, R = Reibung, ges = gesamt |
| **Zählvariable** | *kursiv* | *F*<sub>*n*</sub>, *x*<sub>*i*</sub>, *a*<sub>*k*</sub> | n, i, k sind Laufvariablen |

### Bruchstriche – KEINE Slashes!

**FALSCH:**
- m/s, kg/m³, ct/kWh, N/m²
- P = U·I, E = P·t (Punkt als Mal-Zeichen in Text)

**RICHTIG:**

In LaTeX:
```latex
$\dfrac{\text{m}}{\text{s}}$, $\dfrac{\text{kg}}{\text{m}^3}$, $\dfrac{\text{ct}}{\text{kWh}}$
```

In HTML:
```html
<span class="frac"><span class="frac-num">m</span><span class="frac-den">s</span></span>
```

**Ausnahme Slash:** Nur in Fließtext bei sehr einfachen Einheiten erlaubt (z.B. "30 ct/kWh"), aber in Formeln und Aufgabenstellungen IMMER horizontaler Bruchstrich.

### LaTeX-Umsetzung

```latex
% Formelzeichen kursiv (Standard in $...$)
$F = m \cdot a$

% Einheiten aufrecht mit \text{} oder \mathrm{}
$F = 5\,\text{N}$
$v = 20\,\dfrac{\text{m}}{\text{s}}$

% Deskriptive Indizes aufrecht
$F_{\text{G}} = m \cdot g$
$U_{\text{ges}} = U_1 + U_2$

% Zählvariablen-Indizes kursiv (automatisch)
$F_n$, $x_i$
```

### HTML-Umsetzung (Lernpfade, Minitests)

```html
<!-- Formelzeichen kursiv -->
<span class="fz">F</span> = <span class="fz">m</span> · <span class="fz">a</span>

<!-- Einheiten aufrecht -->
<span class="einheit">N</span>, <span class="einheit">kg</span>

<!-- Bruch in HTML -->
<span class="frac">
    <span class="frac-num">m</span>
    <span class="frac-den">s</span>
</span>
```

**CSS-Klassen:**
```css
.fz { font-family: "Times New Roman", Times, serif; font-style: italic; }
.einheit { font-family: -apple-system, BlinkMacSystemFont, sans-serif; font-style: normal; }
.frac { display: inline-block; vertical-align: middle; text-align: center; }
.frac-num { display: block; border-bottom: 1px solid currentColor; padding: 0 3px 2px; }
.frac-den { display: block; padding: 2px 3px 0; }
```

### Typische Fehler

| FALSCH | RICHTIG | Erklärung |
|--------|---------|-----------|
| F = 5 N | *F* = 5 N | Formelzeichen kursiv |
| *N*, *kg*, *m/s* | N, kg, m/s | Einheiten aufrecht |
| F<sub>*G*</sub> | *F*<sub>G</sub> | Deskriptiver Index aufrecht |
| m/s, kg/m³ | m⁄s mit Bruchstrich | Horizontaler Bruchstrich |
| 5m/s | 5 m/s oder 5 m·s⁻¹ | Leerzeichen zwischen Zahl und Einheit |

### Checkliste ISO 80000

- [ ] Alle Formelzeichen (*F*, *m*, *U*, *I*, etc.) kursiv?
- [ ] Alle Einheiten (N, V, A, Ω, etc.) aufrecht?
- [ ] Deskriptive Indizes (G, R, ges, max) aufrecht?
- [ ] Zählvariablen-Indizes (*n*, *i*, *k*) kursiv?
- [ ] Horizontale Bruchstriche (keine Slashes in Formeln)?
- [ ] Leerzeichen zwischen Zahl und Einheit?
- [ ] Mittelpunkt (·) als Multiplikationszeichen?

---

## Didaktisches QA-Framework

> **Pflicht-Workflow:** Nach jedem erstellten Unterrichtsmaterial Score ausgeben!

### Workflow

```
DRAFT erstellen
      ↓
DIDAKTIK-SCORE ausgeben (10 Dimensionen)
      ↓
  Score ≥ 9.0? ───Ja───→ ✅ FREIGABE
      │
     Nein
      ↓
Top-3 Schwächen verbessern
      ↓
  (zurück zu SCORE)
```

### Die 10 Dimensionen

| # | Dimension | Kernfrage | Gewicht |
|---|-----------|-----------|---------|
| 1 | **Differenzierung** | Qualitativ verschieden (★/★★/★★★), nicht nur mehr/weniger? | 15% |
| 2 | **Taxonomie (AFB)** | Operatoren korrekt? Mix ~25/50/25? | 10% |
| 3 | **Lernziel-Alignment** | Passt zum Rahmenplan? Kompetenzen adressiert? | 10% |
| 4 | **Aktivierung** | Müssen SuS wirklich denken – nicht nur ankreuzen? | 10% |
| 5 | **Scaffolding** | Hilfen gestuft? Nicht Lösung verraten? | 10% |
| 6 | **Feedback-Qualität** | Lernförderlich – nicht nur richtig/falsch? | 10% |
| 7 | **Sprachliche Klarheit** | Sofort verständlich? Altersgerecht? | 10% |
| 8 | **Motivation & Relevanz** | Alltagsbezug? Warum sollte ich das lernen? | 10% |
| 9 | **Inklusion (UDL)** | Verschiedene Zugänge? Keine Barrieren? | 10% |
| 10 | **Praktikabilität** | Zeitrahmen realistisch? Material vorhanden? | 5% |

### Score-Ausgabe (IMMER nach Draft)

```
DIDAKTIK-SCORE: [Produktname]
═══════════════════════════════════════════════════
 #  Dimension              Score   Notiz
───────────────────────────────────────────────────
 1  Differenzierung        [ ]/10
 2  Taxonomie (AFB)        [ ]/10
 3  Lernziel-Alignment     [ ]/10
 4  Aktivierung            [ ]/10
 5  Scaffolding            [ ]/10
 6  Feedback-Qualität      [ ]/10
 7  Sprachliche Klarheit   [ ]/10
 8  Motivation             [ ]/10
 9  Inklusion (UDL)        [ ]/10
10  Praktikabilität        [ ]/10
═══════════════════════════════════════════════════
GESAMT: [X.X]/10  →  [✅ Freigabe / ⚠️ Iteration nötig]

[Falls < 9.0:]
TOP-3 VERBESSERUNGEN:
1. [Schwächste Dimension]: [Konkrete Maßnahme]
2. [Zweitschlechteste]:    [Konkrete Maßnahme]
3. [Drittschlechteste]:    [Konkrete Maßnahme]
```

### Scoring-Kurzreferenz

**Pro Dimension (1-10):**

| Score | Bedeutung |
|-------|-----------|
| 1-2 | Nicht vorhanden / grundlegend falsch |
| 3-4 | Ansätze erkennbar, aber unzureichend |
| 5-6 | Akzeptabel, Verbesserungspotential |
| 7-8 | Gut, kleinere Optimierungen möglich |
| 9-10 | Exzellent, professionelle Qualität |

**Gesamt-Score → Aktion:**

| Score | Status | Aktion |
|-------|--------|--------|
| < 6.0 | ❌ | Grundlegende Überarbeitung |
| 6.0-7.9 | ⚠️ | Überarbeitung erforderlich |
| 8.0-8.9 | ⚠️ | Iteration empfohlen |
| **≥ 9.0** | ✅ | **FREIGABE (Premium-Qualität)** |

### Schnell-Check (5 Killer-Fragen)

Vor vollständigem Score – wenn EINE Frage "Nein" → Score nötig:

1. ❓ Würde ich das als Lehrkraft kaufen/nutzen?
2. ❓ Lernen SuS wirklich etwas – oder nur "abarbeiten"?
3. ❓ Echte Differenzierung (nicht nur leicht/schwer)?
4. ❓ Können SuS ihre Fehler verstehen und korrigieren?
5. ❓ Passt es in den Zeitrahmen?

### Dimensions-Details

#### 1. Differenzierung (15%)

- **Gut:** ★ beschreibt qualitativ, ★★ wendet Formel an, ★★★ modelliert eigene Situation
- **Schlecht:** ★ hat 3 Aufgaben, ★★ hat 5 Aufgaben, ★★★ hat 7 Aufgaben

#### 2. Taxonomie/AFB (10%)

| Format | AFB I | AFB II | AFB III |
|--------|-------|--------|---------|
| Kurztest | 40% | 50% | 10% |
| Stundenleistung | 25% | 50% | 25% |
| Klassenarbeit | 20% | 45% | 35% |

#### 3. Lernziel-Alignment (10%)

- Rahmenplan-Kompetenzen explizit adressiert?
- Fachbegriffe aktuell (nicht veraltet)?
- Jahrgangsstufe angemessen?

#### 4. Aktivierung (10%)

**Aktivierungsgrade (aufsteigend):**
Passiv → Reaktiv (ankreuzen) → Konstruktiv (berechnen) → Interaktiv → Generativ

**Ziel:** Mind. 50% auf "konstruktiv" oder höher

#### 5. Scaffolding (10%)

1. Strategischer Impuls ("Welche Formel?")
2. Denkanstoß ("Schau auf die Einheiten")
3. Teillösung ("Erster Schritt: F = m·a")
4. Musterbeispiel (andere Werte)

#### 6. Feedback-Qualität (10%)

| Typ | Beispiel | Lernwirksamkeit |
|-----|----------|-----------------|
| KR | "Falsch" | ★☆☆☆☆ |
| KCR | "Richtig ist: 20 m/s" | ★★☆☆☆ |
| Elaboriert | "Du hast ÷3,6 vergessen" | ★★★★☆ |
| Prozess | "Rechenweg richtig, nur Einheitenfehler" | ★★★★★ |

#### 7. Sprachliche Klarheit (10%)

| Klassenstufe | Max. Satzlänge | Fachbegriffe |
|--------------|----------------|--------------|
| 5-6 | 12-15 Wörter | Mit Erklärung |
| 7-8 | 15-18 Wörter | Einige bekannt |
| 9-10 | 18-22 Wörter | Erwartet |
| 11-12 | 20-25 Wörter | Wissenschaftlich |

#### 8. Motivation & Relevanz (10%)

**ARCS-Modell:**
- **A**ttention: Überraschende Fakten, Rätsel
- **R**elevance: Alltagsbezug, "Warum lerne ich das?"
- **C**onfidence: Erste Aufgabe schaffbar
- **S**atisfaction: Feedback, Punkte, Erfolg

#### 9. Inklusion/UDL (10%)

- Text + Bild + Diagramm (multiple Repräsentation)
- Schriftgröße ≥ 11pt
- S/W-Version funktioniert (keine Farbabhängigkeit)
- Genug Platz für Antworten

#### 10. Praktikabilität (5%)

| Format | Zeit |
|--------|------|
| Warm-up | 5-10 Min |
| Arbeitsblatt | 15-25 Min |
| Quiz | 20-30 Min |
| Stundenleistung | 45 Min |
| Klassenarbeit | 45-90 Min |

---

## Material-QA (nach Didaktik-Score)

Nach der didaktischen Freigabe (Score ≥ 9.0) folgen drei weitere QA-Schritte:

```
Didaktik-Score ≥ 9.0
        ↓
┌───────────────────────────────────────────────────────────────┐
│  1. TRACEABILITY    2. KONSISTENZ    3. LAYOUT-QA            │
│  (LE → Material)    (Material ↔ Material)    (PDF visuell)   │
└───────────────────────────────────────────────────────────────┘
        ↓
   ✅ FREIGABE
```

### 1. Traceability: LE → Materialien

**Prinzip:** Jedes Feinziel im Langentwurf wird zu einer konkreten Aufgabe.

| LE-Element | Wird zu | In Material |
|------------|---------|-------------|
| Feinziel FZ1 (AFB I) | Aufgabe 1 | AB, LP |
| Feinziel FZ2 (AFB II) | Aufgabe 2 | AB, LP |
| Feinziel FZ3 (AFB II) | Aufgabe 3 | AB, LP |
| Feinziel FZ4 (AFB III) | Aufgabe 4 | AB, LP |
| Verlaufsphase "Einstieg" | Schritt 1-2 | LP |
| Verlaufsphase "Erarbeitung" | Schritt 3-6 | LP |
| Verlaufsphase "Übung" | Übungen | LP |
| Verlaufsphase "Sicherung" | Zusammenfassung | LP |
| Differenzierung [B]/[S]/[E] | Hinweise | LH |
| Erwartete Fehler | Feedback-Texte | LP, LH |
| Lösungen | Rote Einträge | ML |

**Prüfung:**
```
Für jedes FZ im LE:
  → Gibt es eine Aufgabe im AB? (gleiche AFB-Stufe?)
  → Gibt es einen LP-Schritt dazu?
  → Ist die Differenzierung in LH dokumentiert?
```

### 2. Konsistenz-Check: Material ↔ Material

**Prinzip:** Alle Materialien müssen dasselbe sagen.

| Prüfpunkt | Vergleich | Fehler wenn |
|-----------|-----------|-------------|
| AB-Aufgabe hat FZ? | AB ↔ LE | Aufgabe ohne Lernziel |
| LP-Schritte = LE-Phasen? | LP ↔ LE | LP deckt nicht alle Phasen ab |
| LH-Diff = LE-Diff? | LH ↔ LE | Widersprüchliche Differenzierung |
| ML-Lösungen = LE-Lösungen? | ML ↔ LE | Falsche Musterlösung |
| Fachfarbe durchgängig? | Alle | Verschiedene Farben |
| AB-Verweise korrekt? | LP/LB/SLIDES ↔ AB | "→ AB Aufgabe 3" zeigt auf falsche Aufgabe |

**Prüfung:**
```
Für jede AB-Aufgabe X:
  → LB sagt "→ AB Aufgabe X"?
  → LP sagt "→ Hefter: AB Aufgabe X"?
  → SLIDES sagt "→ Jetzt: AB Aufgabe X"?
  → Alle drei meinen dieselbe Aktivität?
```

### 3. Layout-QA: PDF visuell prüfen

**Prinzip:** Nach `pdflatex` jedes PDF öffnen und visuell prüfen.

**Prüfmethode:**
```bash
# PDFs kompilieren
pdflatex AB-01.tex && pdflatex AB-01.tex

# PDFs öffnen und HINSCHAUEN
open AB-01.pdf ML-01.pdf LH-01.pdf
```

**Prüfpunkte:**

| Problem | Symptom | Lösung |
|---------|---------|--------|
| Aufgabe am Seitenende | Titel S.1, Inhalt S.2 | `\newpage` vor Aufgabe |
| Box-Titel abgeschnitten | Text ragt über Rand | `yshift` anpassen |
| Tabelle zerrissen | Zeilen auf 2 Seiten | `\needspace{10em}` vor Tabelle |
| Zu wenig Antwortplatz | Zeilen zu eng | `\antwortzeilen{8}` statt 6 |
| SW-Druck unleserlich | Grau druckt schlecht | Nur Linien, keine Flächen |

**Korrektur-Workflow:**
```
1. PDF öffnen
2. Seite für Seite durchgehen
3. Problem identifizieren
4. .tex anpassen:
   - \newpage (harter Umbruch)
   - \needspace{Xem} (weicher Umbruch)
   - \vspace{Xpt} (Abstände)
5. Neu kompilieren (2x pdflatex)
6. Erneut prüfen
7. Wiederholen bis sauber
```

### QA-Checkliste (nach Materialgenerierung)

**Traceability:**
- [ ] Jedes FZ hat eine AB-Aufgabe (gleiche AFB-Stufe)
- [ ] LP-Schritte decken alle LE-Phasen ab
- [ ] Differenzierung LE = LH

**Konsistenz:**
- [ ] AB-Verweise in LP/LB/SLIDES korrekt
- [ ] ML-Lösungen = LE-Lösungen
- [ ] Fachfarbe durchgängig

**Layout:**
- [ ] Keine Seitenumbrüche mitten in Aufgaben
- [ ] Boxen-Titel vollständig sichtbar
- [ ] Tabellen nicht über Seiten gebrochen
- [ ] Genug Platz für Schüler-Antworten
- [ ] SW-Version druckerfreundlich

---

## Ressourcen

### Rahmenpläne MV

- Physik Sek I: `RP_PHYS_Gym_Ges_7_10.pdf`
- Physik Sek II: `RP_PHYS_SEK2_Erprobungsfassung.pdf`
- Chemie Sek I GY: `Anlage_9_RP_CHE_AHR-7-10_final1.pdf`
- Chemie Sek I MR: `Anlage_3_RP_CHE_MR_8-10_final1.pdf`
- Informatik Sek II: `RP_INFO_SEK2.pdf`

### Simulationen

- sciencesim: `https://sciencesim.github.io/`
- PhET: `https://phet.colorado.edu/`
- LEIFI: `https://www.leifiphysik.de/`

### Videos

- SimpleClub
- musstewissen Physik/Chemie
- Terra X Lesch & Co
