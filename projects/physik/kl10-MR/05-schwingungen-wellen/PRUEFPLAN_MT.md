# PRUEFPLAN MT: Schwingungen

> **Datei:** MT-05a-schwingungen.html
> **Fach:** Physik
> **Klasse:** 10 MR
> **BE:** 25
> **Zeit:** 25 Minuten
> **Bewertung:** Notenskala MR (96/80/60/40/20%)
> **Datum:** 2026-01-29

---

## 1. Struktur-Check

| # | Kriterium | Status | Notiz |
|---|-----------|--------|-------|
| 1.1 | HTML5-Doctype | ✅ | `<!DOCTYPE html>` |
| 1.2 | Meta charset UTF-8 | ✅ | vorhanden |
| 1.3 | Meta viewport responsive | ✅ | vorhanden |
| 1.4 | Titel aussagekräftig | ✅ | "Stundenleistung: Schwingungen" |
| 1.5 | Fachfarbe Physik #2c5aa0 | ✅ | korrekt |
| 1.6 | ES5-kompatibel | ✅ | Nur `var` und `function` |
| 1.7 | QUIZ_ID eindeutig | ✅ | `mt05a-schwingungen-v2` |

**Struktur-Score: 7/7** ✅

---

## 2. Fragetypen-Check

| Aufgabe | Typ | BE | Korrekte Antwort | Kopfrechenbar | Status |
|---------|-----|-----|------------------|---------------|--------|
| A1 | Single-Choice (Experimentdaten) | 3 | Option 1 (T~L, nicht m) | ✅ | ✅ |
| A2 | Zuordnung (3 Dropdowns) | 3 | nein/ja/nein | ✅ | ✅ |
| A3 | Fill-in (Diagramm) | 3 | A=8, n=4, T=1,5 | ✅ 6/4=1,5 | ✅ |
| A4 | Fill-in (Umkehr Fadenpendel) | 3 | L≈1,0-1,1 m | ⚠️ √ benötigt | ✅ |
| A5 | Fill-in (Metronom) | 2 | f=2, T=0,5 | ✅ 120/60=2 | ✅ |
| A6 | Single-Choice (Proportionalität) | 2 | Option 1 (T verdoppelt) | ✅ √4=2 | ✅ |
| A7 | Fill-in (Federpendel) | 3 | 0,0025; 0,05; 0,3 | ⚠️ √ benötigt | ✅ |
| A8 | Multi-Select (Vergleich) | 2 | a, b, d | ✅ | ✅ |
| A9 | Fill-in (Seismograph) | 2 | T=2, f=0,5 | ✅ 30/15=2 | ✅ |
| A10 | Single-Choice (Mond-Knobel) | 2 | Option 0 (nur Fadenpendel) | ✅ Formeln vergleichen | ✅ |

**Gesamt-BE: 3+3+3+3+2+2+3+2+2+2 = 25 BE** ✅

---

## 3. Inhalts-Abdeckung (Lernziele)

| Lernziel (aus LP) | Abgedeckt in Aufgabe(n) | AFB | Status |
|-------------------|------------------------|-----|--------|
| FZ1: Beispiele für Schwingungen | — | — | (im LP, nicht MT) |
| FZ2: Definition Schwingung | — | — | (im LP, nicht MT) |
| FZ3: Definitionen A, T, f | A3, A8 | I | ✅ |
| FZ4: Formel f = 1/T | A5, A9 | I | ✅ |
| FZ5: A, T aus Diagramm ablesen | A3 | II | ✅ |
| FZ6: f aus T berechnen | A3, A5, A9 | II | ✅ |
| FZ7: Hypothesen + Experiment | A1 | II | ✅ |
| FZ8: Schwingungen vergleichen | A2, A6, A8, A10 | II/III | ✅ |

**Inhalts-Score: 6/6** ✅ (alle prüfbaren Lernziele abgedeckt)

---

## 4. Anforderungsbereiche

| AFB | Aufgaben | BE | Anteil |
|-----|----------|-----|--------|
| I (Reproduktion) | — | 0 | 0% |
| II (Anwendung) | A1, A2, A3, A5, A6, A8, A9 | 17 | 68% |
| III (Transfer) | A4, A7, A10 | 8 | 32% |

**AFB-Verteilung:** ✅ angemessen für MR (Schwerpunkt II)

---

## 5. Kopfrechenbarkeit

| Kriterium | Status | Notiz |
|-----------|--------|-------|
| Rechenhilfen angezeigt | ✅ | π≈3, √10≈3, √2≈1,4, g=10 m/s² |
| Keine komplizierten Zahlen | ✅ | Ganzzahlen oder einfache Brüche |
| Wurzeln vermeidbar/gegeben | ✅ | √4=2, √(1/400)=1/20 |
| Division einfach | ✅ | 6/4, 30/15, 120/60 |

**Kopfrechenbar-Score: 4/4** ✅

---

## 6. Anti-Betrug-Funktionen

| Feature | Implementiert | Status |
|---------|--------------|--------|
| Platznummer-Sperrung | ✅ | confirmSeat() + localStorage |
| Startzeit erfasst | ✅ | In DOMContentLoaded |
| Abgabezeit erfasst | ✅ | In submitTest() |
| Tab-Wechsel-Tracking | ✅ | visibilitychange Event |
| Tab-Wechsel-Dauer | ✅ | Sekunden aufsummiert |
| Zeitstempel-Anzeige | ✅ | In Ergebnis-Box |
| Lehrer-Reset | ✅ | Code: 2026 |

**Anti-Betrug-Score: 7/7** ✅

---

## 7. JavaScript-Funktionen

| Funktion | Vorhanden | Korrekt |
|----------|-----------|---------|
| parseNumber() mit Komma-Support | ✅ | ✅ |
| getRadio() | ✅ | ✅ |
| getCheckboxes() | ✅ | ✅ |
| markMcCorrect() | ✅ | ✅ |
| markCheckboxCorrect() | ✅ | ✅ |
| markInputCorrect() | ✅ | ✅ |
| showSolutionBox() | ✅ | ✅ |
| submitTest() | ✅ | ✅ |
| saveProgress() | ✅ | ✅ |
| loadProgress() | ✅ | ✅ |
| resetTest() | ✅ | ✅ |
| restoreSubmittedState() | ✅ | ✅ |
| getNote() | ✅ | ✅ (MR-Skala) |
| initTabSwitchTracking() | ✅ | ✅ |
| confirmSeat() / checkSeatLocked() | ✅ | ✅ |
| teacherReset() | ✅ | ✅ |
| formatTimestamp() / formatDuration() | ✅ | ✅ |

**JS-Score: 17/17** ✅

---

## 8. Fachliche Korrektheit

| Kriterium | Status | Notiz |
|-----------|--------|-------|
| Formeln korrekt | ✅ | T=2π√(L/g), T=2π√(m/D), f=1/T |
| Einheiten korrekt | ✅ | Hz, s, m, N/m |
| ISO 80000: Brüche mit Bruchstrich | ✅ | `.bruch` CSS-Klasse |
| ISO 80000: Formelzeichen kursiv | ✅ | `.fz` CSS-Klasse |
| Antworten fachlich korrekt | ✅ | Alle verifiziert |
| Toleranzen angemessen | ✅ | ±0.1 für Dezimalwerte |
| Keine Sternchen-Niveaus | ✅ | Einheitlicher Test |

**Fachliche Korrektheit: 7/7** ✅

---

## 9. UI/UX-Check

| Kriterium | Status | Notiz |
|-----------|--------|-------|
| Platznummer-Auswahl | ✅ | P1-P24 |
| Feedback pro Aufgabe | ✅ | correct/partial/incorrect |
| Lösungsbox angezeigt | ✅ | Nach Abgabe sichtbar |
| Ergebnis-Anzeige | ✅ | BE + % + Note |
| Responsive Design | ✅ | Flexbox |
| Print-CSS | ✅ | @media print vorhanden |
| Diagramm mit Grid | ✅ | A3: SVG mit Hilfslinien |

**UX-Score: 7/7** ✅

---

## 10. Feedback-Qualität

| Aufgabe | Feedback korrekt | Lösungsweg gezeigt |
|---------|-----------------|-------------------|
| A1 | ✅ | ✅ T~L erklärt |
| A2 | ✅ | ✅ Alle 3 Zuordnungen |
| A3 | ✅ | ✅ A=8, n=4, T=6/4=1,5 |
| A4 | ✅ | ✅ Umstellung + Einsetzen |
| A5 | ✅ | ✅ 120/60=2, 1/2=0,5 |
| A6 | ✅ | ✅ T~√L erklärt |
| A7 | ✅ | ✅ Schrittweise |
| A8 | ✅ | ✅ Alle Optionen bewertet |
| A9 | ✅ | ✅ 30/15=2, 1/2=0,5 |
| A10 | ✅ | ✅ Formeln verglichen |

**Feedback-Score: 10/10** ✅

---

## 11. Gesamtbewertung

| Kategorie | Score | Max |
|-----------|-------|-----|
| Struktur | 7 | 7 |
| Fragetypen | 10 | 10 |
| Inhalts-Abdeckung | 6 | 6 |
| AFB-Verteilung | ✅ | ✅ |
| Kopfrechenbarkeit | 4 | 4 |
| Anti-Betrug | 7 | 7 |
| JavaScript | 17 | 17 |
| Fachliche Korrektheit | 7 | 7 |
| UI/UX | 7 | 7 |
| Feedback | 10 | 10 |

**GESAMT: 75/75 (100%)**

---

## 12. Fazit

| Status | Ergebnis |
|--------|----------|
| **MT-SCORE** | **10.0/10.0** |
| **Freigabe** | ✅ **FREIGEGEBEN** |

### Stärken:
- **Anspruchsvoll und kreativ:** Umkehraufgaben, Proportionalitäts-Reasoning, Mond-Transfer
- **Kopfrechenbar:** Alle Werte ohne Taschenrechner lösbar (Hinweise gegeben)
- **ISO 80000 konform:** Brüche mit Bruchstrich, keine Sternchen-Niveaus
- **Diagramm mit Grid:** A3 SVG hat Hilfslinien für klares Ablesen
- **Vollständige Lösungswege:** Jede Aufgabe mit erklärendem Feedback
- **Gute AFB-Verteilung:** 68% II, 32% III (für MR angemessen)
- **Anti-Betrug vollständig:** Platznummer-Sperre, Tab-Wechsel-Tracking, Zeitstempel, Lehrer-Reset (Code: 2026)

### Kritische Fehler (Freigabe-Blocker):
- [x] Keine kritischen Fehler

### Änderungen 2026-01-29:
- [x] Sternchen-Niveaus (★★, ★★★) entfernt
- [x] Grid zu A3-Diagramm hinzugefügt
- [x] ISO 80000 Brüche implementiert
- [x] Test anspruchsvoller gestaltet

---

*Prüfung abgeschlossen: 2026-01-29*
