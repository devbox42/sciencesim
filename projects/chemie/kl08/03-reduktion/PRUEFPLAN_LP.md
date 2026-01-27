# PRUEFPLAN LP: Reduktion von Silberoxid

> **Datei:** LP-03-reduktion.html
> **Fach:** Chemie
> **Klasse:** 8 (Gesamtschule)
> **Thema:** 2.5 Redoxreaktionen
> **Datum:** 2026-01-27

---

## 1. Struktur-Check

| # | Kriterium | Status | Notiz |
|---|-----------|--------|-------|
| 1.1 | HTML5-Doctype vorhanden | ✅ | `<!DOCTYPE html>` |
| 1.2 | Meta charset UTF-8 | ✅ | `<meta charset="UTF-8">` |
| 1.3 | Meta viewport responsive | ✅ | `width=device-width, initial-scale=1.0` |
| 1.4 | Titel aussagekräftig | ✅ | "Reduktion \| Chemie Klasse 8" |
| 1.5 | Fachfarbe Chemie #2a7a4b | ✅ | `--accent: #2a7a4b` |
| 1.6 | ES5-kompatibel (kein let/const/arrow) | ✅ | Nur `var` und `function` |
| 1.7 | LocalStorage-Persistenz | ✅ | `LERNPFAD_ID = 'lp-03-reduktion'` |

**Struktur-Score: 7/7** ✅

---

## 2. Inhalts-Check

### 2.1 Lernziele

| Lernziel | Im LP abgedeckt | Schritt |
|----------|-----------------|---------|
| FZ1: Reduktion als Sauerstoff-Entzug definieren (AFB I) | ✅ | 9 |
| FZ2: Sicherheitsregeln nennen (AFB I) | ✅ | 3 |
| FZ3: Beobachtungen beschreiben (AFB II) | ✅ | 5 |
| FZ4: Teilchenebene deuten (AFB II) | ✅ | 6 |
| FZ5: Reaktionsgleichung aufstellen (AFB II) | ✅ | 7 |
| FZ6: Oxidation/Reduktion vergleichen (AFB I) | ✅ | 8 |

**Lernziel-Abdeckung: 6/6** ✅

### 2.2 Fachliche Korrektheit

| Struktur | Korrekt | Beispiel im LP |
|----------|---------|----------------|
| Reduktion = Sauerstoff-Entzug | ✅ | Schritt 9: Definition |
| Oxidation = Sauerstoff-Aufnahme | ✅ | Schritt 1, 8: Vergleich |
| Reaktionsgleichung Reduktion | ✅ | 2 Ag₂O → 4 Ag + O₂ (Schritt 7) |
| Reaktionsgleichung Oxidation | ✅ | 4 Ag + O₂ → 2 Ag₂O (Schritt 1) |
| Glimmspanprobe = O₂-Nachweis | ✅ | Schritt 5: Merke-Box |
| Etymologie reducere | ✅ | Schritt 2: re- + ducere = zurückführen |

**Fachliche Korrektheit: 6/6** ✅

### 2.3 Rahmenplan-Konformität

| Kriterium | Status | Notiz |
|-----------|--------|-------|
| Thema 2.5 Redoxreaktionen | ✅ | Reduktion als Teilthema |
| Experiment mit Silberoxid | ✅ | Video + Beobachtung |
| Reaktionsgleichung aufstellen | ✅ | Step-by-Step in SIM-03b |
| Vergleich Oxidation/Reduktion | ✅ | Tabelle in Schritt 8 |

**RP-Score: 4/4** ✅

---

## 3. Interaktivitäts-Check

### 3.1 Übungen

| Übung | Typ | Anzahl Items | Feedback | Status |
|-------|-----|--------------|----------|--------|
| Schritt 5: Beobachtung | Dropdown | 3 Lücken | ✅ Ja | ✅ |
| Schritt 9: Quiz Q1 | MC | 3 Optionen | ✅ Ja | ✅ |
| Schritt 9: Quiz Q2 | MC | 3 Optionen | ✅ Ja | ✅ |
| Schritt 9: Quiz Q3 | MC | 3 Optionen | ✅ Ja | ✅ |

**Übungs-Score: 4/4** ✅

### 3.2 JavaScript-Funktionen

| Funktion | Vorhanden | Korrekt |
|----------|-----------|---------|
| createStepIndicators() | ✅ | ✅ |
| getMaxCompletedStep() | ✅ | ✅ |
| updateUI() | ✅ | ✅ |
| goToStep() | ✅ | ✅ |
| nextStep() | ✅ | ✅ |
| prevStep() | ✅ | ✅ |
| checkObservation() | ✅ | ✅ |
| selectQuiz() | ✅ | ✅ |
| IIFE-Init | ✅ | ✅ |

**JS-Score: 9/9** ✅

---

## 4. Didaktik-Check

| # | Kriterium | Score | Begründung |
|---|-----------|-------|------------|
| 1 | **Progression** | 10/10 | Einstieg → Etymologie → Sicherheit → Video → Beobachtung → Deutung → Gleichung → Vergleich → Definition → Abschluss |
| 2 | **Input vor Output** | 10/10 | Theorie/Simulation immer vor Übung |
| 3 | **Scaffolding** | 10/10 | Simulationen, Merkkästen, Etymologie-Box, Vergleichstabelle |
| 4 | **Differenzierung** | 9/10 | Im AB umgesetzt (★/★★/★★★), LP selbst ohne explizite Niveaus |
| 5 | **Authentizität** | 10/10 | Echtes Experiment (Video), Bezug zu Silberschmuck |
| 6 | **Kommunikative Relevanz** | 10/10 | Metallgewinnung, Hochofen, Alltagsbezug |
| 7 | **Visualisierung** | 10/10 | Farbcodierte Gleichungen (Ag grau, O rot), 3 Simulationen, Video |
| 8 | **Feedback-Qualität** | 10/10 | Spezifisches Feedback bei allen Übungen |
| 9 | **AB-Verweise** | 10/10 | Alle 7 Kästen explizit verwiesen |
| 10 | **Zusammenfassung** | 10/10 | Schritt 10 mit Checkliste und Ausblick |

**Didaktik-Score: 99/100** ✅

---

## 5. AB-Mapping-Check

| LP-Schritt | AB-Element | Verweis explizit |
|------------|------------|------------------|
| 2 | Kasten 1: Begriff (Etymologie) | ✅ "→ AB Kasten 1" |
| 3 | Kasten 2: Sicherheit | ✅ "→ AB Kasten 2" |
| 5 | Kasten 3: Beobachtung | ✅ "→ AB Kasten 3" |
| 6 | Kasten 4: Deutung + Skizze | ✅ "→ AB Kasten 4" |
| 7 | Kasten 5: Reaktionsgleichung | ✅ "→ AB Kasten 5" |
| 8 | Kasten 6: Vergleichstabelle | ✅ "→ AB Kasten 6" |
| 9 | Kasten 7: Definition | ✅ "→ AB Kasten 7" |
| 10 | Checkliste | ✅ Alle 7 Kästen aufgelistet |

**Mapping-Score: 8/8** ✅

---

## 6. Technische Validierung

| Test | Status | Notiz |
|------|--------|-------|
| HTML-Syntax valide | ✅ | Keine Fehler |
| CSS-Syntax valide | ✅ | Alle Variablen definiert |
| JS ohne Syntaxfehler | ✅ | ES5-konform |
| LocalStorage funktioniert | ✅ | Getestet |
| MC-Auswahl funktioniert | ✅ | selectQuiz() |
| Dropdown funktioniert | ✅ | checkObservation() |
| Responsive (mobil) | ✅ | @media 768px, 480px |
| Simulationen vorhanden | ✅ | SIM-03a/b/c.html existieren |
| Video eingebettet | ✅ | YouTube iframe |

**Technik-Score: 9/9** ✅

---

## 7. Gesamtbewertung

| Kategorie | Score | Max |
|-----------|-------|-----|
| Struktur | 7 | 7 |
| Lernziele | 6 | 6 |
| Fachliche Korrektheit | 6 | 6 |
| RP-Konformität | 4 | 4 |
| Übungen | 4 | 4 |
| JavaScript | 9 | 9 |
| Didaktik | 99 | 100 |
| AB-Mapping | 8 | 8 |
| Technik | 9 | 9 |

**GESAMT: 152/153 (99.3%)** ✅

---

## 8. Fazit

| Status | Ergebnis |
|--------|----------|
| **LP-SCORE** | **9.9/10.0** |
| **Freigabe** | ✅ **ERTEILT** |

### Stärken:
- Vollständige Lernzielabdeckung (6/6)
- Klare didaktische Progression (10 Schritte)
- Konsistente AB-Verweise (7 Kästen)
- Gutes Feedback-System (Dropdown + MC)
- Farbcodierte Reaktionsgleichungen
- 3 eingebettete Simulationen
- Responsive Design (@media queries)
- ES5-kompatibel

### Verbesserungspotential (optional):
- Explizite Niveaudifferenzierung im LP (★/★★/★★★) - derzeit nur im AB

---

## 9. Änderungsprotokoll

| Datum | Änderung | Status |
|-------|----------|--------|
| 2026-01-27 | Titel korrigiert: "Reduktion \| Chemie Klasse 8" | ✅ |
| 2026-01-27 | @media queries hinzugefügt (768px, 480px) | ✅ |

---

*Prüfung abgeschlossen: 2026-01-27*
