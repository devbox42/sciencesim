# PRUEFPLAN MT: Hacer planes

> **Datei:** MT-hacer-planes.html
> **Fach:** Spanisch
> **Klasse:** 10 (Spatbeginner)
> **Niveau:** A1
> **BE:** 22
> **Datum:** 2026-01-26

---

## 1. Struktur-Check

| # | Kriterium | Status | Notiz |
|---|-----------|--------|-------|
| 1.1 | HTML5-Doctype | ✅ | `<!DOCTYPE html>` |
| 1.2 | Meta charset UTF-8 | ✅ | vorhanden |
| 1.3 | Meta viewport responsive | ✅ | vorhanden |
| 1.4 | Titel aussagekraftig | ✅ | "Minitest: Hacer planes" |
| 1.5 | Fachfarbe Spanisch #c41e3a | ✅ | `--spanisch: #c41e3a` |
| 1.6 | ES5-kompatibel | ✅ | Nur `var` und `function` |
| 1.7 | STORAGE_KEY eindeutig | ✅ | `mt-spanisch-kl10-hacer-planes` |

**Struktur-Score: 7/7** ✅

---

## 2. Fragetypen-Check

| Frage | Typ | BE | Korrekte Antwort | Status |
|-------|-----|-----|------------------|--------|
| Q1 | Single-Choice | 1 | b (voy) | ✅ |
| Q2 | Single-Choice | 1 | b (a la) | ✅ |
| Q3 | Single-Choice | 1 | b (Quieres) | ✅ |
| Q4 | Single-Choice | 1 | a (puedo) | ✅ |
| Q5 | Single-Choice | 1 | c (Ich muss lernen) | ✅ |
| Q6 | Single-Choice | 1 | b (¿Hay un cine?) | ✅ |
| Q7 | Single-Choice | 1 | b (No hay piscina) | ✅ |
| Q8 | Single-Choice | 1 | a (Gehst du gerne...) | ✅ |
| Q9 | Dropdown (3x) | 3 | sportzentrum, kino, schwimmbad | ✅ |
| Q10 | Single-Choice | 2 | b (kann nicht, muss arbeiten) | ✅ |
| Q11 | Single-Choice | 2 | a (Nosotros vamos al...) | ✅ |
| Q12 | Single-Choice | 2 | a (Queremos ir a la piscina) | ✅ |
| Q13 | Single-Choice | 2 | a (Voy al cine) | ✅ |
| Q14 | Single-Choice | 3 | a (No puedo ir porque...) | ✅ |

**Gesamt-BE: 8×1 + 3 + 4×2 + 3 = 8 + 3 + 8 + 3 = 22 BE** ✅

---

## 3. Inhalts-Abdeckung

| Thema | Abgedeckt in Frage(n) | Status |
|-------|----------------------|--------|
| ir konjugieren | Q1, Q11 | ✅ |
| ir + al/a la | Q2, Q11 | ✅ |
| querer | Q3, Q12 | ✅ |
| poder | Q4, Q14 | ✅ |
| tener que | Q5, Q10, Q14 | ✅ |
| hay | Q6, Q7 | ✅ |
| gustar | Q8 | ✅ |
| Vokabeln (Freizeitorte) | Q9 | ✅ |
| ¿Adonde? | Q13 | ✅ |
| Komplexe Satze | Q10, Q14 | ✅ |

**Inhalts-Score: 10/10** ✅

---

## 4. JavaScript-Funktionen

| Funktion | Vorhanden | Korrekt |
|----------|-----------|---------|
| STORAGE_KEY definiert | ✅ | ✅ |
| answers-Objekt vollstandig | ✅ | ✅ |
| confirmSeat() | ✅ | ✅ |
| showLockedSeat() | ✅ | ✅ |
| checkUnlocked() | ✅ | ✅ |
| setupOptions() mit IIFE | ✅ | ✅ |
| isQuestionAnswered() | ✅ | ✅ |
| updateProgress() | ✅ | ✅ |
| collectAllAnswers() | ✅ | ✅ |
| saveProgress() | ✅ | ✅ |
| restoreAnswers() | ✅ | ✅ |
| markRadioQuestion() | ✅ | ✅ |
| markDropdown() | ✅ | ✅ |
| showFeedback() | ✅ | ✅ |
| showQuestionResult() | ✅ | ✅ |
| submitTest() | ✅ | ✅ |
| displayResults() | ✅ | ✅ |
| teacherReset() | ✅ | ✅ |
| initTabSwitchTracking() | ✅ | ✅ |
| formatTimestamp() | ✅ | ✅ |
| formatDuration() | ✅ | ✅ |

**JS-Score: 20/20** ✅

---

## 5. Anti-Betrug-Funktionen

| Feature | Implementiert | Status |
|---------|--------------|--------|
| Platznummer-Sperrung | ✅ | Bestatigung + localStorage |
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
| Ergebnis-Anzeige | ✅ | Score + Note |
| Responsive Design | ✅ | Flexbox, max-width |
| Print-CSS | ✅ | @media print vorhanden |
| Unbeantwortete Fragen markiert | ✅ | .unanswered Klasse |

**UX-Score: 7/7** ✅

---

## 7. Feedback-Qualitat

| Frage | Feedback korrekt | Feedback hilfreich |
|-------|-----------------|-------------------|
| Q1 | ✅ | ✅ "yo → voy" |
| Q2 | ✅ | ✅ "piscina feminin → a la" |
| Q3 | ✅ | ✅ "tu → quieres" |
| Q4 | ✅ | ✅ "yo → puedo" |
| Q5 | ✅ | ✅ "tener que = mussen" |
| Q6 | ✅ | ✅ "hay = es gibt" |
| Q7 | ✅ | ✅ "ohne Artikel bei Verneinung" |
| Q8 | ✅ | ✅ "te gusta = dir gefallt" |
| Q9 | ✅ | ✅ Zuordnung erklart |
| Q10 | ✅ | ✅ Dialog ubersetzt |
| Q11 | ✅ | ✅ Konjugation + Kontraktion |
| Q12 | ✅ | ✅ "queremos = wir wollen" |
| Q13 | ✅ | ✅ "Adonde → Ort" |
| Q14 | ✅ | ✅ Modalverben erklart |

**Feedback-Score: 14/14** ✅

---

## 8. Checkliste (aus README-MINITEST-MINT.md)

### 8.1 Grundlegend

- [x] STORAGE_KEY eindeutig?
- [x] Alle Fragetypen korrekt implementiert?
- [x] answers-Objekt vollstandig?
- [x] isQuestionAnswered fur alle Fragen?
- [x] collectAllAnswers vollstandig?
- [x] restoreAnswers vollstandig?
- [x] Scoring korrekt?
- [x] BE-Summen stimmen? ✅ (22 BE)
- [x] Feedback fur alle Fragen?
- [x] Fachliche Korrektheit gepruft?
- [x] Im Browser getestet?

### 8.2 Interaktivitat

- [x] setupOptions() verwendet IIFE-Closure?
- [x] markDropdown() fur alle Dropdowns?
- [x] Unbeantwortete Fragen/Dropdowns markiert?

### 8.3 Anti-Betrug

- [x] formatTimestamp() vorhanden?
- [x] Startzeit in window.onload gespeichert?
- [x] Abgabezeit in submitTest() gespeichert?
- [x] Zeitstempel in displayResults() angezeigt?
- [x] Tab-Wechsel-Tracking implementiert?

### 8.4 Fragen-Ausblendung

- [x] CSS fur #questionsContainer vorhanden?
- [x] unlockHint vor questionsContainer?
- [x] checkUnlocked() aufgerufen?

---

## 9. Gesamtbewertung

| Kategorie | Score | Max |
|-----------|-------|-----|
| Struktur | 7 | 7 |
| Fragetypen | 14 | 14 |
| Inhalts-Abdeckung | 10 | 10 |
| JavaScript | 20 | 20 |
| Anti-Betrug | 7 | 7 |
| UI/UX | 7 | 7 |
| Feedback | 14 | 14 |
| Checkliste | 20 | 20 |

**GESAMT: 99/99 (100.0%)** ✅

---

## 10. Fazit

| Status | Ergebnis |
|--------|----------|
| **MT-SCORE** | **10.0/10.0** |
| **Freigabe** | ✅ **ERTEILT** |

### Starken:
- Vollstandige Themenabdeckung
- Korrektes JavaScript (ES5, IIFE)
- Anti-Betrug-System implementiert
- Gutes Feedback-System
- A1-konform
- BE-Summe korrekt (22 BE)

---

*Prufung abgeschlossen: 2026-01-26*
