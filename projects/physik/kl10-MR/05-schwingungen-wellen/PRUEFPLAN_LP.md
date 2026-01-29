# PRUEFPLAN LP: Schwingungen

> **Datei:** LP-05a-schwingungen.html
> **Fach:** Physik
> **Klasse:** 10 MR
> **Rahmenplan:** RP MV RS/GES Kl. 10
> **Datum:** 2026-01-29

---

## 1. Struktur-Check

| # | Kriterium | Status | Notiz |
|---|-----------|--------|-------|
| 1.1 | HTML5-Doctype vorhanden | ✅ | `<!DOCTYPE html>` |
| 1.2 | Meta charset UTF-8 | ✅ | `<meta charset="UTF-8">` |
| 1.3 | Meta viewport responsive | ✅ | `width=device-width, initial-scale=1.0` |
| 1.4 | Titel aussagekräftig | ✅ | "LP-05a: Schwingungen" |
| 1.5 | Fachfarbe korrekt | ✅ | `--fach: #2c5aa0` (Physik) |
| 1.6 | ES5-kompatibel (kein let/const/arrow) | ✅ | Nur `var` und `function` |
| 1.7 | LocalStorage-Persistenz | ⚠️ | Nicht implementiert (für Einzelstunde akzeptabel) |

**Struktur-Score: 6/7**

---

## 2. Inhalts-Check

### 2.1 Lernziele (Feinziele)

| Lernziel | Im LP abgedeckt | Schritt | AFB |
|----------|-----------------|---------|-----|
| FZ1: SuS nennen Beispiele für Schwingungen im Alltag | ✅ | 1 | I |
| FZ2: SuS definieren Schwingung als periodische Bewegung um Ruhelage | ✅ | 1 | I |
| FZ3: SuS geben die Definitionen von A, T, f an | ✅ | 4 | I |
| FZ4: SuS geben die Formel f = 1/T an und die Einheit Hz | ✅ | 4 | I |
| FZ5: SuS lesen A, T aus y(t)-Diagramm ab | ✅ | 5, 7 | II |
| FZ6: SuS berechnen f aus T und umgekehrt | ✅ | 6 | II |
| FZ7: SuS formulieren Hypothesen und prüfen experimentell | ✅ | 2, 3 | III |
| FZ8: SuS vergleichen Schwingungen anhand ihrer Kenngrößen | ✅ | 8 | III |

**Lernziel-Abdeckung: 8/8**

### 2.2 Fachliche Korrektheit

| Kriterium | Status | Notiz |
|-----------|--------|-------|
| Formeln korrekt | ✅ | T=2π√(L/g), T=2π√(m/D), f=1/T |
| Einheiten korrekt (SI) | ✅ | Hz, s, m, cm, N/m |
| ISO 80000: Formelzeichen kursiv | ✅ | `.fz { font-style: italic; }` |
| ISO 80000: Einheiten aufrecht | ✅ | Einheiten ohne `.fz` Klasse |
| ISO 80000: Brüche mit Bruchstrich | ✅ | `.bruch` CSS-Klasse |
| Fachbegriffe korrekt | ✅ | Amplitude, Periodendauer, Frequenz, periodisch, Ruhelage |
| Keine fachlichen Fehler | ✅ | Physik korrekt implementiert |

**Fachliche Korrektheit: 7/7**

### 2.3 Rahmenplan-Konformität

| Kriterium | Status | Notiz |
|-----------|--------|-------|
| Thema im Rahmenplan MV enthalten | ✅ | RP RS/GES 2021, Kl. 10: Mechanische Schwingungen |
| Niveau angemessen (MR) | ✅ | Mittlere Reife Niveau |
| Vorwissen berücksichtigt | ✅ | Kraft, Energie aus Kl. 9 |
| Keine überhöhten Anforderungen | ✅ | Keine höhere Mathematik |

**Rahmenplan-Score: 4/4**

---

## 3. Interaktivitäts-Check

### 3.1 Übungen

| Übung | Typ | Anzahl Items | Feedback | Status |
|-------|-----|--------------|----------|--------|
| Schritt 6: Rechnen f/T | Fill-in | 3 | ✅ Ja | ✅ |
| Schritt 7: Diagramm ablesen | Fill-in | 3 | ✅ Ja | ✅ |

**Übungs-Score: 2/2**

### 3.2 Simulationen

| Simulation | Interaktiv | Didaktisch sinnvoll | Status |
|------------|------------|---------------------|--------|
| Fadenpendel | ✅ 3 Slider (L, m, A) | ✅ Erkenntnisgeführt | ✅ |
| Federpendel | ✅ 3 Slider (D, m, A) | ✅ Erkenntnisgeführt | ✅ |
| y(t)-Diagramm | ✅ 2 Slider (A, T) | ✅ Visualisierung | ✅ |

**Simulations-Score: 3/3**

### 3.3 JavaScript-Funktionen

| Funktion | Vorhanden | Korrekt |
|----------|-----------|---------|
| goToStep() | ✅ | ✅ |
| nextStep() / prevStep() | ✅ | ✅ |
| updateNav() | ✅ | ✅ |
| checkUeb1-3() | ✅ | ✅ |
| checkDiag() | ✅ | ✅ |
| animateFaden() | ✅ | ✅ |
| animateFeder() | ✅ | ✅ |
| drawDiagram() | ✅ | ✅ |

**JS-Score: 8/8**

---

## 4. Didaktik-Check

| # | Kriterium | Score | Begründung |
|---|-----------|-------|------------|
| 1 | **Progression** | 10/10 | Einstieg → Experiment → Theorie → Übung |
| 2 | **Verstehen vor Anwenden** | 10/10 | Erkenntnis vor Formel |
| 3 | **Scaffolding** | 10/10 | KEINE TIPPS (erkenntnisgeführt) |
| 4 | **Differenzierung** | 8/10 | Transfer in Zusammenfassung |
| 5 | **Alltagsbezug** | 10/10 | Schaukel, Herzschlag, Gitarre |
| 6 | **Visualisierung** | 10/10 | 3 Canvas-Simulationen |
| 7 | **Feedback-Qualität** | 8/10 | Richtig/Falsch ohne Lösungshinweis (gewollt) |
| 8 | **AB-Verweise** | 10/10 | K1, P1, P2, K2, K3, D1, Ü1-Ü4 explizit |
| 9 | **Zusammenfassung** | 10/10 | Schritt 8 mit allen Erkenntnissen |
| 10 | **Aktivierung** | 10/10 | Hypothesen, Messungen, Rechnungen |

**Didaktik-Score: 96/100**

---

## 5. AB-Mapping-Check

| LP-Schritt | AB-Element | Lückentext-Antwort im LP | Status |
|------------|------------|--------------------------|--------|
| 1 | K1 (Definition) | ✅ "periodische" + "Ruhelage" explizit | ✅ |
| 2 | P1 (Versuchsprotokoll Fadenpendel) | ✅ Messwerte nur auf AB | ✅ |
| 3 | P2 (Versuchsprotokoll Federpendel) | ✅ Messwerte nur auf AB | ✅ |
| 4 | K2 (Kenngrößen) | ✅ Tabelle mit A, T, f | ✅ |
| 4 | K3 (Formel) | ✅ "höher" + "kürzer" explizit | ✅ |
| 5 | D1 (Diagramm) | ✅ "Auslenkung", "Maximum", "Maxima" | ✅ |
| 7 | Ü1–Ü4 (Übungen) | ✅ AB-Verweis explizit | ✅ |
| 8 | Checkliste | ✅ Alle Elemente genannt | ✅ |

**Mapping-Score: 8/8** (alle AB-Lücken im LP beantwortet)

---

## 6. Warm-up Check (optional)

| # | Kriterium | Status | Notiz |
|---|-----------|--------|-------|
| 6.1 | Warm-up vorhanden (5-10 Fragen) | ⬜ | Nicht vorhanden |

**Warm-up-Score: 0/7** (für Einzelstunde akzeptabel)

---

## 7. Technische Validierung

| Test | Status | Notiz |
|------|--------|-------|
| HTML-Syntax valide | ✅ | Keine Fehler |
| CSS-Syntax valide | ✅ | Alle Variablen definiert |
| JS ohne Syntaxfehler | ✅ | Keine Konsolen-Errors |
| LocalStorage funktioniert | ⬜ | Nicht implementiert |
| Navigation funktioniert | ✅ | Vor/Zurück/Step-Dots (nummeriert, klickbar) |
| Übungen funktionieren | ✅ | Eingabe + Prüfung |
| Responsive (mobil) | ⚠️ | Grundlegend, flex-wrap vorhanden |

**Technik-Score: 5/7**

---

## 8. Deployment & Distribution

| # | Kriterium | Status | Notiz |
|---|-----------|--------|-------|
| 8.1 | QR-LP-05a-schwingungen.pdf vorhanden | ✅ | LaTeX kompiliert |
| 8.2 | QR-MT-05a-schwingungen.pdf vorhanden | ✅ | LaTeX kompiliert |
| 8.3 | LP online (devbox42.github.io) | ✅ | Deployed 2026-01-29 |
| 8.4 | MT online (devbox42.github.io) | ✅ | Deployed 2026-01-29 |
| 8.5 | Abhängigkeiten online | ✅ | Keine externen Abhängigkeiten |

**URLs:**
- LP: `https://devbox42.github.io/sciencesim/physik/kl10-MR/05-schwingungen-wellen/LP-05a-schwingungen.html`
- MT: `https://devbox42.github.io/sciencesim/physik/kl10-MR/05-schwingungen-wellen/MT-05a-schwingungen.html`

**Deployment-Score: 5/5**

---

## 9. Gesamtbewertung

| Kategorie | Score | Max |
|-----------|-------|-----|
| Struktur | 6 | 7 |
| Lernziele | 8 | 8 |
| Fachliche Korrektheit | 7 | 7 |
| Rahmenplan | 4 | 4 |
| Übungen | 2 | 2 |
| Simulationen | 3 | 3 |
| JavaScript | 8 | 8 |
| Didaktik | 96 | 100 |
| AB-Mapping | 8 | 8 |
| Warm-up (optional) | (0) | (7) |
| Technik | 5 | 7 |
| Deployment | 5 | 5 |

**GESAMT: 152/159 (95.6%)**

---

## 10. Fazit

| Status | Ergebnis |
|--------|----------|
| **LP-SCORE** | **9.6/10.0** |
| **Freigabe** | ✅ **FREIGEGEBEN** |

### Stärken:
- Erkenntnisgeführter Ansatz konsequent umgesetzt (keine Tipps)
- Zwei vollständige Simulationen mit physikalisch korrekten Formeln
- **AB-Mapping vollständig:** Alle Lückentext-Antworten (periodisch, Ruhelage, höher, kürzer) explizit im LP
- **Messtabellen nur auf AB** (nicht redundant im LP)
- Klare didaktische Progression: Experiment → Erkenntnis → Theorie → Übung
- ISO 80000 konform (Brüche mit Bruchstrich)

### Verbesserungspotential:
- LocalStorage für Fortschritts-Speicherung ergänzen
- Warm-up-Quiz optional hinzufügen

### Kritische Fehler (Freigabe-Blocker):
- [x] ~~K1: "periodisch" und "Ruhelage" fehlten~~ → ✅ behoben 2026-01-29
- [x] ~~K3: "höher/kürzer"-Zusammenhang fehlte~~ → ✅ behoben 2026-01-29
- [x] ~~Messtabellen redundant im LP~~ → ✅ entfernt 2026-01-29

---

*Prüfung abgeschlossen: 2026-01-29*
