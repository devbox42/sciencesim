# Stundenplan-Template

**Version:** 1.0 (2026-01-05)
**Datei:** `templates/stundenplan-template.html`

---

## Zweck

Visueller Halbjahres-/Jahresplan für alle Fächer mit:
- Kalenderübersicht (Monate, Ferien, Tests, Klausuren)
- Stundendetails pro Themenblock
- Feinziele + AFB-Stufen
- Material-Zuordnung

---

## Fachfarben

| Fach | Farbe | CSS-Variable |
|------|-------|--------------|
| Physik | `#2c5aa0` | `--fach-color` |
| Chemie | `#2a7a4b` | `--fach-color` |
| Informatik | `#b35c00` | `--fach-color` |
| Spanisch | `#c41e3a` | `--fach-color` |

---

## Platzhalter

### Header

| Platzhalter | Beispiel |
|-------------|----------|
| `{{FACH}}` | Physik |
| `{{KLASSE}}` | 12 GK |
| `{{HALBJAHR}}` | Q4 |
| `{{SCHULJAHR}}` | 2025/26 |
| `{{NOTENSTOPP}}` | 17.04.2026 |
| `{{LETZTER_TAG}}` | 24.04.2026 |

### Kalender

| Platzhalter | Beispiel |
|-------------|----------|
| `{{TAG1_NAME}}` | Mi |
| `{{TAG1_TYP}}` | ES |
| `{{TAG2_NAME}}` | Fr |
| `{{TAG2_TYP}}` | DS |
| `{{MONAT1_NAME}}` | Januar 2026 |
| `{{KW}}` | 2 |
| `{{MO}}, {{DI}}, ...` | 5, 6, 7, 8, 9 |

### Stunden

| Platzhalter | Beispiel |
|-------------|----------|
| `{{NR}}` | 1 |
| `{{WOCHENTAG}}` | Mi |
| `{{DATUM}}` | 07.01. |
| `{{TYP}}` | ES / DS |
| `{{THEMA}}` | Photoeffekt 1: Hallwachs |
| `{{FEINZIEL}}` | SuS beschreiben Versuch |
| `{{AFB}}` | 1 / 2 / 3 |
| `{{KERNINHALT}}` | Zinkplatte, UV-Licht |
| `{{MATERIAL}}` | AB, SIM |

### Tests/Klausuren

| Platzhalter | Beispiel |
|-------------|----------|
| `{{TEST_NR}}` | 1 |
| `{{TEST_THEMEN}}` | Photoeffekt, De-Broglie |
| `{{DAUER}}` | 45 / 90 |
| `{{BE}}` | 30 / 60 |

---

## Verwendung

### 1. Template kopieren

```bash
cp templates/stundenplan-template.html projects/FACH/KLASSE/STUNDENPLAN-XXX.html
```

### 2. Fachfarbe anpassen

```css
:root {
    --fach-color: #c41e3a;  /* Spanisch */
}
```

### 3. Platzhalter ersetzen

Alle `{{...}}` durch konkrete Werte ersetzen.

### 4. Kalender-Wochen einfügen

Pro Woche eine `week-row` mit den Tagen:

```html
<div class="week-row">
    <span class="kw">2</span>
    <span class="day">5</span>
    <span class="day">6</span>
    <span class="day tag1" title="Thema">7</span>
    <span class="day">8</span>
    <span class="day tag2" title="Thema">9</span>
</div>
```

### 5. Stunden einfügen

Pro Stunde eine `stunde`-Karte:

```html
<div class="stunde theme-1 bg-1">
    <div class="stunde-header">
        <span class="stunde-nr">1</span>
        <span class="stunde-datum">Mi 07.01.</span>
        <span class="stunde-typ es">ES</span>
    </div>
    <div class="stunde-thema">Thema</div>
    <div class="stunde-fz">Feinziel <span class="afb afb-2">II</span></div>
    <div class="stunde-inhalt">Kerninhalt</div>
    <div class="stunde-material">→ AB, SIM</div>
</div>
```

---

## CSS-Klassen

### Tage

| Klasse | Bedeutung |
|--------|-----------|
| `.tag1` | Unterrichtstag 1 (hellblau) |
| `.tag2` | Unterrichtstag 2 (blau) |
| `.ferien` | Ferien (grau) |
| `.test` | Test (orange) |
| `.klausur` | Klausur (rot) |
| `.notenstopp` | Notenstopp-Markierung |
| `.letzter` | Letzter Schultag (schwarz) |

### Themen

| Klasse | Farbe |
|--------|-------|
| `.theme-1`, `.bg-1` | Lila |
| `.theme-2`, `.bg-2` | Blau |
| `.theme-3`, `.bg-3` | Grün |
| `.theme-4`, `.bg-4` | Orange |
| `.theme-5`, `.bg-5` | Rot |
| `.theme-6`, `.bg-6` | Grau |

### Stunden-Typen

| Klasse | Bedeutung |
|--------|-----------|
| `.es` | Einzelstunde |
| `.ds` | Doppelstunde |
| `.test` | Test |
| `.klausur` | Klausur |

### AFB-Badges

| Klasse | Farbe |
|--------|-------|
| `.afb-1` | Grün (AFB I) |
| `.afb-2` | Gelb (AFB II) |
| `.afb-3` | Rot (AFB III) |

---

## Beispiele

- `projects/physik/kl12-GK/STUNDENPLAN-Q4-2526.html`
