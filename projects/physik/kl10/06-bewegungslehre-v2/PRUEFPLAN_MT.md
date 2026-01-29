# PRUEFPLAN MT: Impuls & Impulserhaltung

> **Datei:** MT-02-impuls.html
> **Fach:** Physik
> **Klasse:** 10E (Gymnasium)
> **BE:** 25
> **Bewertung:** 15-NP-Skala
> **Datum:** 2026-01-28

---

## 1. Struktur-Check

| # | Kriterium | Status | Notiz |
|---|-----------|--------|-------|
| 1.1 | HTML5-Doctype | ✅ | `<!DOCTYPE html>` |
| 1.2 | Meta charset UTF-8 | ✅ | vorhanden |
| 1.3 | Meta viewport responsive | ✅ | vorhanden |
| 1.4 | Titel aussagekräftig | ✅ | "Stundenleistung: Impuls & Impulserhaltung" |
| 1.5 | Fachfarbe Physik #2c5aa0 | ✅ | korrekt |
| 1.6 | ES5-kompatibel | ✅ | Nur `var` und `function` |
| 1.7 | STORAGE_KEY eindeutig | ✅ | `mt-physik-10e-02-impuls-v1` |

**Struktur-Score: 7/7** ✅

---

## 2. Fragetypen-Check

| Frage | Typ | BE | Korrekte Antwort | Status |
|-------|-----|-----|------------------|--------|
| Q1a | Fill-in (numerisch) | 2 | 10 | ✅ |
| Q1b | Fill-in (numerisch) | 2 | 800 | ✅ |
| Q1c | Fill-in (numerisch) | 2 | 36000 | ✅ |
| Q2 | Single-Choice | 2 | b (Bolt) | ✅ |
| Q3 | Single-Choice | 2 | b (Wucht/stoppen) | ✅ |
| Q4 | Single-Choice | 2 | b (keine äußeren Kräfte) | ✅ |
| Q5a | Dropdown | 1 | elastisch | ✅ |
| Q5b | Dropdown | 1 | unelastisch | ✅ |
| Q5c | Dropdown | 1 | unelastisch | ✅ |
| Q6a | Fill-in (numerisch) | 2 | 20000 | ✅ |
| Q6b | Fill-in (numerisch) | 1 | 2500 | ✅ |
| Q6c | Fill-in (numerisch) | 2 | 8 | ✅ |
| Q7 | Multi-Select | 3 | A+C richtig, B+D falsch | ✅ |
| Q8 | Single-Choice | 2 | b (Impulserhaltung Gase/Rakete) | ✅ |

**Gesamt-BE: 6 + 2 + 2 + 2 + 3 + 5 + 3 + 2 = 25 BE** ✅

---

## 3. Inhalts-Abdeckung

| Thema | Abgedeckt in Frage(n) | Status |
|-------|----------------------|--------|
| Impuls berechnen (p = m·v) | Q1 | ✅ |
| Impuls-Vergleich | Q2 | ✅ |
| Definition Impuls | Q3 | ✅ |
| Abgeschlossenes System | Q4 | ✅ |
| Elastisch vs. Unelastisch | Q5 | ✅ |
| Impulserhaltung anwenden | Q6 | ✅ |
| Impulserhaltungssatz | Q7 | ✅ |
| Ruckstossprinzip (Anwendung) | Q8 | ✅ |

**Inhalts-Score: 8/8** ✅

---

## 4. JavaScript-Funktionen

| Funktion | Vorhanden | Korrekt |
|----------|-----------|---------|
| STORAGE_KEY definiert | ✅ | ✅ |
| answers-Objekt vollständig | ✅ | ✅ |
| confirmSeat() | ✅ | ✅ |
| showLockedSeat() | ✅ | ✅ |
| checkUnlocked() | ✅ | ✅ |
| setupOptions() | ✅ | ✅ |
| isQuestionAnswered() | ✅ | ✅ |
| updateProgress() | ✅ | ✅ |
| collectAllAnswers() | ✅ | ✅ |
| saveProgress() | ✅ | ✅ |
| restoreAnswers() | ✅ | ✅ |
| markRadioQuestion() | ✅ | ✅ |
| showFeedback() | ✅ | ✅ |
| showQuestionResult() | ✅ | ✅ |
| submitTest() | ✅ | ✅ |
| displayResults() | ✅ | ✅ |
| teacherReset() | ✅ | ✅ |
| initTabSwitchTracking() | ✅ | ✅ |
| formatTimestamp() | ✅ | ✅ |
| formatDuration() | ✅ | ✅ |
| parseNumber() | ✅ | ✅ |
| isClose() | ✅ | ✅ |

**JS-Score: 22/22** ✅

---

## 5. Anti-Betrug-Funktionen

| Feature | Implementiert | Status |
|---------|--------------|--------|
| Platznummer-Sperrung | ✅ | Bestätigung + localStorage |
| Startzeit erfasst | ✅ | In window.onload |
| Abgabezeit erfasst | ✅ | In submitTest() |
| Tab-Wechsel-Tracking | ✅ | visibilitychange Event |
| Tab-Wechsel-Dauer | ✅ | Sekunden aufsummiert |
| Zeitstempel-Anzeige | ✅ | In displayResults() |
| Lehrer-Reset | ✅ | Code: 2024 |

**Anti-Betrug-Score: 7/7** ✅

---

## 6. UI/UX-Check

| Kriterium | Status | Notiz |
|-----------|--------|-------|
| Fortschrittsanzeige | ✅ | Progress-Bar + Text |
| Fragen bis Identifikation verborgen | ✅ | unlockHint + questionsContainer |
| Feedback pro Frage | ✅ | correct/incorrect Boxen |
| Ergebnis-Anzeige | ✅ | Score + NP |
| Responsive Design | ✅ | Flexbox, max-width |
| Print-CSS | ✅ | @media print vorhanden |
| Formel-Hilfe angezeigt | ✅ | Hinweis-Box mit p = m·v |

**UX-Score: 7/7** ✅

---

## 7. Fachliche Korrektheit

| Kriterium | Status | Notiz |
|-----------|--------|-------|
| Formeln korrekt | ✅ | p = m·v |
| Einheiten korrekt | ✅ | kg·m/s |
| ISO 80000: Multiplikationspunkt | ✅ | · (nicht ×) |
| ISO 80000: Formelzeichen kursiv | ✅ | `.fz` CSS-Klasse |
| Antworten fachlich korrekt | ✅ | Alle verifiziert |
| Toleranzen angemessen | ✅ | isClose() mit Toleranz |

**Fachliche Korrektheit: 6/6** ✅

---

## 8. Feedback-Qualität

| Frage | Feedback korrekt | Feedback hilfreich |
|-------|-----------------|-------------------|
| Q1 | ✅ | ✅ Lösungsweg gezeigt |
| Q2 | ✅ | ✅ Beide Impulse berechnet |
| Q3 | ✅ | ✅ Abgrenzung zu Energie/Kraft |
| Q4 | ✅ | ✅ Beispiele genannt |
| Q5 | ✅ | ✅ Eigenschaften erklärt |
| Q6 | ✅ | ✅ Schrittweise Lösung |
| Q7 | ✅ | ✅ Richtig/Falsch erklärt |
| Q8 | ✅ | ✅ Alle Optionen erklärt |

**Feedback-Score: 8/8** ✅

---

## 9. Gesamtbewertung

| Kategorie | Score | Max |
|-----------|-------|-----|
| Struktur | 7 | 7 |
| Fragetypen | 14 | 14 |
| Inhalts-Abdeckung | 8 | 8 |
| JavaScript | 22 | 22 |
| Anti-Betrug | 7 | 7 |
| UI/UX | 7 | 7 |
| Fachliche Korrektheit | 6 | 6 |
| Feedback | 8 | 8 |

**GESAMT: 79/79 (100.0%)**

---

## 10. Fazit

| Status | Ergebnis |
|--------|----------|
| **MT-SCORE** | **10.0/10.0** |
| **Freigabe** | ✅ **JA** |

### Stärken:
- Vollständige Themenabdeckung (Impuls + Impulserhaltung + Ruckstossprinzip)
- Korrektes JavaScript (ES5-konform)
- Anti-Betrug-System vollständig
- Gutes Feedback-System mit Lösungswegen
- ISO 80000 konform (Multiplikationspunkt ·)
- 15-NP-Skala korrekt implementiert
- BE-Summe stimmt mit Header überein (25 BE)

### Kritische Fehler (Freigabe-Blocker):
- [x] ~~**BE-Summe prüfen:** Header zeigt 25 BE, Summe der Aufgaben ergibt 23 BE~~ **BEHOBEN:** Q8 (Ruckstossprinzip, 2 BE) hinzugefügt

### Nächste Schritte:
1. ~~BE-Diskrepanz klären (23 vs. 25)~~ ✅ Erledigt
2. ~~QR-MT-02-impuls.pdf generieren~~ ✅ Generiert 2026-01-28

**ALLE SCHRITTE ABGESCHLOSSEN**

---

*Prüfung abgeschlossen: 2026-01-28*
