# PRUEFPLAN LP: Hacer planes

> **Datei:** LP-hacer-planes.html
> **Fach:** Spanisch
> **Klasse:** 10 (Spatbeginner)
> **Niveau:** A1
> **Datum:** 2026-01-26

---

## 1. Struktur-Check

| # | Kriterium | Status | Notiz |
|---|-----------|--------|-------|
| 1.1 | HTML5-Doctype vorhanden | ✅ | `<!DOCTYPE html>` |
| 1.2 | Meta charset UTF-8 | ✅ | `<meta charset="UTF-8">` |
| 1.3 | Meta viewport responsive | ✅ | `width=device-width, initial-scale=1.0` |
| 1.4 | Titel aussagekraftig | ✅ | "Hacer planes \| Spanisch Klasse 10" |
| 1.5 | Fachfarbe Spanisch #c41e3a | ✅ | `--spanisch: #c41e3a` |
| 1.6 | ES5-kompatibel (kein let/const/arrow) | ✅ | Nur `var` und `function` |
| 1.7 | LocalStorage-Persistenz | ✅ | `LERNPFAD_ID = 'spanisch-kl10-hacer-planes'` |

**Struktur-Score: 7/7** ✅

---

## 2. Inhalts-Check

### 2.1 Lernziele

| Lernziel | Im LP abgedeckt | Schritt |
|----------|-----------------|---------|
| Verb ir konjugieren | ✅ | 2, 3 |
| Modalverben querer/poder/tener que | ✅ | 5, 6, 7, 8 |
| Frage ¿Adonde vas? | ✅ | 4 |
| hay (es gibt) | ✅ | 9, 10 |
| me gusta / te gusta | ✅ | 11 |
| Dialog schreiben | ✅ | 12, 13, 14 |

**Lernziel-Abdeckung: 6/6** ✅

### 2.2 Grammatik-Korrektheit

| Struktur | Korrekt | Beispiel im LP |
|----------|---------|----------------|
| ir: voy, vas, va, vamos, vais, van | ✅ | Schritt 2 |
| ir + al (m.) / a la (f.) | ✅ | Tip in Schritt 2 |
| querer: quiero, quieres, quiere... | ✅ | Schritt 5 |
| poder: puedo, puedes, puede... | ✅ | Schritt 6 |
| tener que: tengo que, tienes que... | ✅ | Schritt 7 |
| hay (unveranderlich) | ✅ | Schritt 9 |
| me gusta / te gusta + Infinitiv | ✅ | Schritt 11 |

**Grammatik-Score: 7/7** ✅

### 2.3 A1-Konformitat

| Kriterium | Status | Notiz |
|-----------|--------|-------|
| Keine komplexen Verneinungen | ✅ | Kein "ninguno/ninguna" |
| Keine Subjuntivo | ✅ | Nur Indikativ |
| Keine Vergangenheitszeiten | ✅ | Nur Prasens |
| Einfache Satzstrukturen | ✅ | S-V-O Struktur |
| Begrenzter Wortschatz | ✅ | 6 Freizeitorte |

**A1-Score: 5/5** ✅

---

## 3. Interaktivitat-Check

### 3.1 Ubungen

| Ubung | Typ | Anzahl Items | Feedback | Status |
|-------|-----|--------------|----------|--------|
| Schritt 3: ir | Fill-in | 4 Lucken | ✅ Ja | ✅ |
| Schritt 8: Modalverben | MC | 3 Fragen | ✅ Ja | ✅ |
| Schritt 10: hay | Fill-in | 4 Lucken | ✅ Ja | ✅ |
| Schritt 13: Dialog | Fill-in | 6 Lucken | ✅ Ja | ✅ |

**Ubungs-Score: 4/4** ✅

### 3.2 JavaScript-Funktionen

| Funktion | Vorhanden | Korrekt |
|----------|-----------|---------|
| saveInput() | ✅ | ✅ |
| loadInput() | ✅ | ✅ |
| normalizeAnswer() | ✅ | ✅ |
| checkIr() | ✅ | ✅ |
| checkModalverben() | ✅ | ✅ |
| checkHay() | ✅ | ✅ |
| checkDialog() | ✅ | ✅ |
| MC-Klick-Handler | ✅ | ✅ |
| DOMContentLoaded Restore | ✅ | ✅ |

**JS-Score: 9/9** ✅

---

## 4. Didaktik-Check

| # | Kriterium | Score | Begrundung |
|---|-----------|-------|------------|
| 1 | **Progression** | 10/10 | Einfach → Komplex (ir → Modalverben → hay → Dialog) |
| 2 | **Input vor Output** | 10/10 | Grammatik immer vor Ubung |
| 3 | **Scaffolding** | 10/10 | Redemittel, Modelldialog, Satzanfange |
| 4 | **Differenzierung** | 10/10 | [B]/[E] bei Aufgabe 14 |
| 5 | **Authentizitat** | 10/10 | Pablo (lokal) + Marta (neu) Setting |
| 6 | **Kommunikative Relevanz** | 10/10 | Plane machen = reale Situation |
| 7 | **Visualisierung** | 9/10 | Vokabel-Grid, Tabellen, Farbcodes |
| 8 | **Feedback-Qualitat** | 10/10 | Spezifisches Feedback pro Ubung |
| 9 | **AB-Verweise** | 10/10 | Alle Kasten + Aufgaben explizit genannt |
| 10 | **Zusammenfassung** | 10/10 | Klare Summary am Ende |

**Didaktik-Score: 99/100** ✅

---

## 5. AB-Mapping-Check

| LP-Schritt | AB-Element | Verweis explizit |
|------------|------------|------------------|
| 1 | V1 (Vokabeln) | ✅ "Kasten V1" |
| 2 | G1 (ir) | ✅ "Kasten G1" |
| 4 | G2 (¿Adonde?) | ✅ "Kasten G2" |
| 5, 6, 7 | G3 (Modalverben) | ✅ "Kasten G3" |
| 9 | G4 (hay) | ✅ "Kasten G4" |
| 10 | A1 (DE→ES) | ✅ "Aufgabe 1" |
| 11 | G5 (gustar) | ✅ "Kasten G5" |
| 12 | A2 (ES→DE) | ✅ "Aufgabe 2" |
| 13 | A3 (Luckentext) | ✅ "Aufgabe 3" |
| 14 | A4 (Dialog) | ✅ "Aufgabe 4" |

**Mapping-Score: 10/10** ✅

---

## 6. Technische Validierung

| Test | Status | Notiz |
|------|--------|-------|
| HTML-Syntax valide | ✅ | Keine Fehler |
| CSS-Syntax valide | ✅ | Alle Variablen definiert |
| JS ohne Syntaxfehler | ✅ | Keine Konsolen-Errors |
| LocalStorage funktioniert | ✅ | Getestet |
| MC-Auswahl funktioniert | ✅ | Klick + Speicherung |
| Fill-in funktioniert | ✅ | Eingabe + Prufung |
| Responsive (mobil) | ✅ | @media queries vorhanden |

**Technik-Score: 7/7** ✅

---

## 7. Gesamtbewertung

| Kategorie | Score | Max |
|-----------|-------|-----|
| Struktur | 7 | 7 |
| Lernziele | 6 | 6 |
| Grammatik | 7 | 7 |
| A1-Konformitat | 5 | 5 |
| Ubungen | 4 | 4 |
| JavaScript | 9 | 9 |
| Didaktik | 99 | 100 |
| AB-Mapping | 10 | 10 |
| Technik | 7 | 7 |

**GESAMT: 164/165 (99.4%)** ✅

---

## 8. Fazit

| Status | Ergebnis |
|--------|----------|
| **LP-SCORE** | **10.0/10.0** |
| **Freigabe** | ✅ **ERTEILT** |

### Starken:
- Vollstandige Grammatikabdeckung
- Klare didaktische Progression
- Konsistente AB-Verweise
- Gutes Feedback-System
- A1-konform

### Verbesserungspotential (optional):
- Vokabel-Grid konnte Bilder enthalten (aber fur A1 nicht zwingend)

---

*Prufung abgeschlossen: 2026-01-26*
