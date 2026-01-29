# PRUEFPLAN LP: Impuls & Impulserhaltung

> **Datei:** LP-02-impuls.html
> **Fach:** Physik
> **Klasse:** 10E (Gymnasium)
> **Rahmenplan:** RP MV Gym Kl. 10
> **Datum:** 2026-01-28

---

## 1. Struktur-Check

| # | Kriterium | Status | Notiz |
|---|-----------|--------|-------|
| 1.1 | HTML5-Doctype vorhanden | ✅ | `<!DOCTYPE html>` |
| 1.2 | Meta charset UTF-8 | ✅ | `<meta charset="UTF-8">` |
| 1.3 | Meta viewport responsive | ✅ | `width=device-width, initial-scale=1.0` |
| 1.4 | Titel aussagekräftig | ✅ | "Lernpfad: Impuls & Impulserhaltung \| Physik Klasse 10E" |
| 1.5 | Fachfarbe korrekt | ✅ | `--physik: #2c5aa0` |
| 1.6 | ES5-kompatibel (kein let/const/arrow) | ✅ | Nur `var` und `function` |
| 1.7 | LocalStorage-Persistenz | ✅ | `LP_ID = 'lp-physik-10e-02-impuls-v2'` |

**Struktur-Score: 7/7**

---

## 2. Inhalts-Check

### 2.1 Lernziele (Feinziele)

| Lernziel | Im LP abgedeckt | Schritt | AFB |
|----------|-----------------|---------|-----|
| FZ1: Impuls definieren und berechnen (p = m·v) | ✅ | 3, 4, 5 | I/II |
| FZ2: Abgeschlossenes System erklären | ✅ | 8 | I |
| FZ3: Impulserhaltungssatz anwenden | ✅ | 9, 11 | II |
| FZ4: Elastischen/unelastischen Stoß unterscheiden | ✅ | 10 | I/II |

**Lernziel-Abdeckung: 4/4**

### 2.2 Fachliche Korrektheit

| Kriterium | Status | Notiz |
|-----------|--------|-------|
| Formeln korrekt | ✅ | p = m·v, Σp_vor = Σp_nach |
| Einheiten korrekt (SI) | ✅ | kg·m/s |
| ISO 80000: Formelzeichen kursiv | ✅ | `.fz { font-style: italic; }` |
| ISO 80000: Einheiten aufrecht | ✅ | `.einheit { font-style: normal; }` |
| ISO 80000: Multiplikationspunkt | ✅ | · (nicht ×) durchgehend |
| Fachbegriffe korrekt | ✅ | Impuls, abgeschlossenes System, elastisch/unelastisch |
| Keine fachlichen Fehler | ✅ | — |

**Fachliche Korrektheit: 7/7**

### 2.3 Rahmenplan-Konformität

| Kriterium | Status | Notiz |
|-----------|--------|-------|
| Thema im Rahmenplan MV enthalten | ✅ | RP Gym Kl. 10, Mechanik |
| Niveau angemessen (Gym/MR) | ✅ | E-Kurs Niveau |
| Vorwissen berücksichtigt | ✅ | Newton 1 als Voraussetzung genannt |
| Keine überhöhten Anforderungen | ✅ | — |

**Rahmenplan-Score: 4/4**

---

## 3. Interaktivitäts-Check

### 3.1 Übungen

| Übung | Typ | Anzahl Items | Feedback | Status |
|-------|-----|--------------|----------|--------|
| Schritt 1: Vorhersage | MC | 3 | ✅ spezifisch | ✅ |
| Schritt 5: Impuls berechnen | Fill-in | 4 (a-d sequentiell) | ✅ spezifisch | ✅ |
| Schritt 6: Challenge Duelle + Airbag | MC | 4 | ✅ spezifisch | ✅ |
| Schritt 11: Ü3, Ü4, Ü5 | Fill-in + MC | 5 | ✅ spezifisch | ✅ |

**Übungs-Score: 4/4** (übertrifft Minimum)

### 3.2 Simulationen

| Simulation | Interaktiv | Didaktisch sinnvoll | Status |
|------------|------------|---------------------|--------|
| Wucht-O-Meter (Schritt 2) | ✅ 2 Slider + Presets | ✅ Impuls-Visualisierung | ✅ |
| Stoß-Simulator (Schritt 9) | ✅ 4 Slider + flüssige Animation | ✅ Impulserhaltung zeigen | ✅ |

**Simulations-Score: 2/2**

### 3.3 JavaScript-Funktionen

| Funktion | Vorhanden | Korrekt |
|----------|-----------|---------|
| saveInput() | ✅ | ✅ |
| loadInputs() | ✅ | ✅ |
| checkVorhersage(), checkEx1-3(), checkU3-5() | ✅ | ✅ |
| goToStep(), nextStep(), prevStep() | ✅ | ✅ |
| window.onload → init() | ✅ | ✅ |

**JS-Score: 5/5**

---

## 4. Didaktik-Check

| # | Kriterium | Score | Begründung |
|---|-----------|-------|------------|
| 1 | **Progression** | 10/10 | Einstieg → Definition → Übung → Transfer → Zusammenfassung |
| 2 | **Verstehen vor Anwenden** | 10/10 | Simulation vor Formel, Formel vor Übungen |
| 3 | **Scaffolding** | 10/10 | Hilfe-Buttons (3 Stufen), Presets, gestaffelte Hinweise |
| 4 | **Differenzierung** | 10/10 | Sequentielle Aufgaben a-d mit steigender Komplexität, Transfer optional |
| 5 | **Alltagsbezug** | 10/10 | Tennisball vs Medizinball, Airbag, Bolt vs Sumo, Schnecke |
| 6 | **Visualisierung** | 10/10 | 2 Simulationen, Compare-Cards, Farbcodes, Icons |
| 7 | **Feedback-Qualität** | 10/10 | Spezifisch, erklärt Fehler, gibt Hinweise |
| 8 | **AB-Verweise** | 10/10 | K1-K7, Ü1-Ü5 alle explizit mit "Kasten/Übung" genannt |
| 9 | **Zusammenfassung** | 10/10 | Schritt 12 mit klarer Summary + Checkliste |
| 10 | **Aktivierung** | 10/10 | Vorhersagen, Berechnungen, Challenges, MC-Auswahl |

**Didaktik-Score: 100/100**

---

## 5. AB-Mapping-Check

| LP-Schritt | AB-Element | Verweis explizit |
|------------|------------|------------------|
| 3 | K1 (Definition Impuls) | ✅ "Kasten K1" + Lückentexte |
| 4 | K2 (Formel p = m·v) | ✅ "Kasten K2" |
| 5 | Ü1 (Impuls berechnen) | ✅ "Übung Ü1" |
| 6 | Ü2 (Vergleiche + Airbag) | ✅ "Übung Ü2" |
| 7 | K3 (Zwischensicherung) | ✅ "Kasten K3" |
| 8 | K4 (Abgeschl. System) | ✅ "Kasten K4" |
| 8 | K5 (Impulserhaltungssatz) | ✅ "Kasten K5" |
| 10 | K6 (Vergleichstabelle elast./unelast.) | ✅ "Kasten K6" |
| 11 | Ü3 (Elastischer Stoß) | ✅ "Übungen Ü3, Ü4, Ü5" |
| 11 | Ü4 (Unelastischer Stoß) | ✅ |
| 11 | Ü5 (Transfer Knautschzone) | ✅ |
| 12 | K7 (Zusammenfassung) | ✅ "Kasten K7" |

**Mapping-Score: 12/12** (alle AB-Elemente explizit verwiesen)

---

## 6. Warm-up Check (optional)

| # | Kriterium | Status | Notiz |
|---|-----------|--------|-------|
| 6.1 | Warm-up vorhanden (5-10 Fragen) | ❌ | Nicht vorhanden |
| 6.2 | Themenbezug gegeben | — | — |
| 6.3 | Funfacts/Historie/Alltagsbezug | — | — |
| 6.4 | Nicht-blockierend | — | — |
| 6.5 | Feedback pro Frage vorhanden | — | — |
| 6.6 | Auflösung zeigt richtige Antwort | — | — |
| 6.7 | Optional: AB-Übernahme | — | — |

**Warm-up-Score: 0/7** (nicht vorhanden → Empfehlung: nachrüsten)

---

## 7. Technische Validierung

| Test | Status | Notiz |
|------|--------|-------|
| HTML-Syntax valide | ✅ | Keine Fehler |
| CSS-Syntax valide | ✅ | Alle CSS-Variablen definiert |
| JS ohne Syntaxfehler | ✅ | ES5-konform, keine Konsolen-Errors |
| LocalStorage funktioniert | ✅ | Fortschritt + Eingaben persistent |
| Navigation funktioniert | ✅ | Vor/Zurück/Dots |
| Übungen funktionieren | ✅ | Eingabe + Prüfung + Feedback |
| Responsive (mobil) | ✅ | @media queries für max-width: 600px |

**Technik-Score: 7/7**

---

## 8. Deployment & Distribution

| # | Kriterium | Status | Notiz |
|---|-----------|--------|-------|
| 8.1 | QR-LP-02-impuls.pdf vorhanden | ✅ | LaTeX kompiliert |
| 8.2 | QR-MT-02-impuls.pdf vorhanden | ✅ | Generiert 2026-01-28 |
| 8.3 | LP online (devbox42.github.io) | ✅ | Deployed 2026-01-27 |
| 8.4 | MT online (devbox42.github.io) | ✅ | Deployed 2026-01-28 |
| 8.5 | Abhängigkeiten online | ✅ | LP + MT sind self-contained |

**URLs:**
- LP: `https://devbox42.github.io/sciencesim/physik/kl10/06-bewegungslehre-v2/LP-02-impuls.html`
- MT: `https://devbox42.github.io/sciencesim/physik/kl10/06-bewegungslehre-v2/MT-02-impuls.html`

**Deployment-Score: 5/5**

---

## 9. Gesamtbewertung

| Kategorie | Score | Max |
|-----------|-------|-----|
| Struktur | 7 | 7 |
| Lernziele | 4 | 4 |
| Fachliche Korrektheit | 7 | 7 |
| Rahmenplan | 4 | 4 |
| Übungen | 4 | 4 |
| Simulationen | 2 | 2 |
| JavaScript | 5 | 5 |
| Didaktik | 100 | 100 |
| AB-Mapping | 12 | 12 |
| Warm-up (optional) | (0) | (7) |
| Technik | 7 | 7 |
| Deployment | 5 | 5 |

**GESAMT: 157/157 (100%)**

---

## 10. Fazit

| Status | Ergebnis |
|--------|----------|
| **LP-SCORE** | **10.0/10.0** |
| **Freigabe** | ✅ **FREIGEGEBEN** |

### Stärken:
- Exzellente Didaktik mit klarer Progression
- Zwei interaktive Simulationen (Stoß-Simulator mit flüssiger Animation)
- Sequentielle Aufgaben a-d mit steigender Komplexität
- Starker Alltagsbezug (Airbag, Bolt vs Sumo)
- Vollständiges AB-Mapping mit expliziten Verweisen
- Hochwertiges, spezifisches Feedback (MC statt Freitext)
- ISO 80000 konform (Multiplikationspunkt ·)
- MT-02-impuls mit 7 Aufgaben (25 BE, 15-NP-Skala)

### Verbesserungspotential:
- Warm-up-Quiz nachrüsten (Funfacts, Historie)

### Kritische Fehler (Freigabe-Blocker):
- [x] ~~LP nicht online deployed~~ → ✅ erledigt 2026-01-27
- [x] ~~MT-02-impuls fehlt~~ → ✅ erstellt 2026-01-28
- [x] ~~QR-MT-02-impuls.pdf fehlt~~ → ✅ generiert 2026-01-28

### Nächste Schritte für 100%:
1. ~~LP deployen~~ ✅
2. ~~MT-02-impuls.html erstellen~~ ✅
3. ~~QR-MT-02-impuls.pdf generieren~~ ✅
4. ~~MT-02 deployen~~ ✅

**ALLE SCHRITTE ABGESCHLOSSEN**

---

## Score-Schwellen

| Score | Status |
|-------|--------|
| < 100% | ❌ Nachbesserung erforderlich |
| **100%** | ✅ **FREIGABE** |

---

*Prüfung aktualisiert: 2026-01-28*
