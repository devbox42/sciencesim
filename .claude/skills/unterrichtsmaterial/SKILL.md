# Skill: Unterrichtsmaterial

Erstellt qualitätsgesicherte Materialsets für Einzel- oder Doppelstunden.

**Aufruf:** `/unterrichtsmaterial` oder automatisch bei Anfragen wie:
- "Erstelle Material für..."
- "Mach ein Arbeitsblatt zu..."
- "Bereite die Doppelstunde vor..."

---

## Fach-Routing

| Fachgruppe | Fächer | Workflow | Templates |
|------------|--------|----------|-----------|
| **MINT** | Physik, Chemie, Informatik | `/templates/mint/WORKFLOW-MINT.md` | `/templates/mint/` |
| **Spanisch** | Kl. 7-9 | `/templates/spanisch/WORKFLOW-SPANISCH.md` | `/templates/spanisch/` |
| **Spanisch** | Spätbeginner | `/projects/spanisch/spaetbeginner/ANLEITUNG-SPANISCH-SPAETBEGINNER.md` | `/templates/spanisch/` |

**WICHTIG:** Immer zuerst den fachspezifischen WORKFLOW lesen!

---

## Referenzen nach Fach

### MINT (Rahmenpläne)

| Fach | Referenz |
|------|----------|
| Physik Sek I | `knowledge/curriculum/physik-mv-sek1.md` |
| Physik Sek II | `knowledge/curriculum/physik-mv-sek2.md` |
| Chemie | `knowledge/curriculum/chemie-mv.md` |
| Informatik | `knowledge/curriculum/informatik-mv.md` |

### Spanisch (Lehrwerke)

| Kurs | Lehrwerk | Referenz |
|------|----------|----------|
| Kl. 7-8 | Qué pasa 1 | `knowledge/Spanisch-Que-Pasa-1/que-pasa-1-referenz.md` |
| Kl. 9 | Qué pasa 2 | `knowledge/Spanish-Que-Pasa-2/que-pasa-2-referenz.md` ⚠️ |
| Spätbeginner | A_tope.com | `knowledge/Spanisch-A_tope_Spaetbeginner/a-tope-spaetbeginner-referenz.md` |

⚠️ = Platzhalter (unvollständig)

---

## Materialtypen

### MINT

| Kürzel | Name | Format | Erstellung | Nutzung |
|--------|------|--------|------------|---------|
| **AB** | Arbeitsblatt | LaTeX→PDF | Pflicht | Pflicht |
| **ML** | Musterlösung | LaTeX→PDF | Pflicht | Pflicht |
| **LH** | Lehrerhinweise | LaTeX→PDF | Pflicht | Pflicht |
| **LS** | Lehrbuchseite | LaTeX→PDF | Pflicht | Optional* |
| **LP** | Lernpfad | HTML | Pflicht | Optional* |
| **SL** | Stundenleistung | HTML+PDF | Pflicht | Optional |
| **SIM** | Simulation | HTML | Optional+ | Optional |
| **PPT** | Präsentation | Beamer/PPTX | Optional | Optional |
| **QR-*** | QR-Codes | LaTeX→PDF | Bei LP/SL/SIM | Optional |
| **PLATZKARTEN** | Platzkarten | LaTeX→PDF | Bei SL | Optional |

*LS und LP sind funktional redundant (analog vs. digital)
+SIM: Optional mit Tendenz zu Pflicht. Bei Zweifeln nachfragen.

### Spanisch

| Kürzel | Name | Format | Beschreibung |
|--------|------|--------|--------------|
| **AB** | Arbeitsblatt | PDF | Für SuS, zum Abheften |
| **LB** | Lernblatt | PDF | Vokabeln, Grammatik, Redemittel |
| **ML** | Musterlösung | PDF | AB mit roten Lösungen |
| **LH** | Lehrerhinweise | PDF | Kurzplan + Differenzierung |
| **LP** | Lernpfad | HTML | Interaktiv, digital |
| **PPT** | PowerPoint | PPTX | 10-15 Folien |
| **MT** | Minitest | HTML+PDF | 25 BE pro Stunde |
| **PLATZKARTEN** | Platzkarten | PDF | 24 Karten mit QR für Tests |

**Dateinamenskonvention:** `[TYP]-[XX][y]-kurzname.[ext]`
- XX = Stundennummer (01, 02, ...)
- y = Block (a, b, c, d)

---

## Planungs-Modi

| Modus | Format | Score | Default für |
|-------|--------|-------|-------------|
| **KOMPAKT** | Planungsnotiz (.md) | 10/10 | Alle Fächer |
| Tier 1 | Langentwurf (.tex) | 10/10 | Bei Anfrage |
| Tier 2 | Langentwurf (.tex) | — | Bei Anfrage |
| Tier 3 | Langentwurf (.tex) | — | Bei Anfrage |

**KOMPAKT ist Default.** Tier 1-3 nur bei expliziter Anfrage ("erstelle einen Langentwurf").

---

## Phase 0: Kontextaufnahme (WICHTIG!)

**Vor der Materialerstellung:** User-Input in 4 Kategorien erfassen:

| Kategorie | User sagt... | Wird zu... |
|-----------|--------------|------------|
| **A) Vorwissen** | "Ich habe ... unterrichtet" | Voraussetzungen |
| **B) Lernziele** | "Ich möchte ... einführen" | Feinziele FZ1-FZ4 |
| **C) Aktivitäten** | "Ich stelle mir vor ..." | Verlaufsphasen |
| **D) Kontext** | "Nur 45 Min / Klasse unruhig" | Didaktische Hinweise |

**Fallback:**
- MINT: Rahmenplan prüfen, bei Lücken nachfragen
- Spanisch: Lehrwerksreferenz nutzen

---

## Workflow mit Checkpoints

```
Phase 0: KONTEXTAUFNAHME (A/B/C/D)
        │
Phase 1: ANFRAGE + MODUS (KOMPAKT vs Tier)
        │
Phase 2: PLANUNG (Didaktik-Score 10/10)
        │
        ▼
┌───────────────────────────────────────────┐
│ 🔲 CHECKPOINT 1: Planung OK? Weiter?      │
└───────────────────────────────────────────┘
        │
Phase 2b: ARBEITSPFAD (PFLICHT!)
        │   ├─ AB-Inventar erstellen
        │   ├─ Sequenz planen (Spracherwerbslogik)
        │   ├─ Rücksprünge dokumentieren
        │   └─ Arbeitspfad-Score 100/100
        │
        ▼
┌───────────────────────────────────────────┐
│ 🔲 CHECKPOINT 2: Arbeitspfad OK? Weiter?  │
└───────────────────────────────────────────┘
        │
Phase 3: CONTENT-MATERIALIEN (folgen Arbeitspfad!)
        │
Phase 4: KOMPILIERUNG & QA
        │
        ▼
┌───────────────────────────────────────────┐
│ 🔲 CHECKPOINT 3: Materialien prüfen?      │
└───────────────────────────────────────────┘
        │
        ▼
    ✅ FREIGABE
```

---

## Phase 2b: Arbeitspfad (KRITISCH!)

> **Definition:** Der Arbeitspfad ist die explizite, didaktisch optimierte Sequenz, in der Schüler durch LP/LB geführt werden und dabei das AB bearbeiten.

### Warum Pflicht?

- Ohne Arbeitspfad: Schüler springt unkontrolliert, Lücken bleiben leer
- Mit Arbeitspfad: Explizite Sequenz, jedes Element wird angesteuert

### Spracherwerbslogik (Spanisch)

```
INPUT → VERSTEHEN → ÜBEN → PRODUZIEREN
```

### AB-Element-Typen

| Kürzel | Typ | Beispiel |
|--------|-----|----------|
| **V** | Vokabelkasten | V1: "La ropa" |
| **G** | Grammatikkasten | G1: llevar-Konjugation |
| **R** | Redemittel | R1: Einkaufsdialog |
| **A** | Aufgabe | A1: Zuordnung (4 BE) |
| **T** | Textproduktion | T1: Freier Dialog |
| **W** | Warm-up (MINT) | W1: Funfact/Alltagsbezug |

### Warm-up-Quiz (MINT, optional)

**Zweck:** Aktivierung, Motivation, Alltagsbezug vor dem eigentlichen Lernpfad.

| Eigenschaft | Beschreibung |
|-------------|--------------|
| Position | Schritt 0 (vor Einstieg) |
| Umfang | 5-10 MC-Fragen |
| Verhalten | Nicht-blockierend |
| Feedback | Infobox mit Auflösung |
| AB-Übernahme | Optional 1-3 Fragen |

**Fragetypen:**
- Funfacts / Historie
- Alltagsbezug ("Was hat das mit mir zu tun?")
- Schätzfragen
- Vorwissen-Aktivierung

**Siehe:** `templates/mint/ARBEITSPFAD-TEMPLATE.md`

### Aktionstypen

| Aktion | Verweis im LP/LB |
|--------|------------------|
| **LESEN** | "→ Lies AB Kasten V1" |
| **AUSFÜLLEN** | "→ Ergänze AB Kasten G1" |
| **BEARBEITEN** | "→ Bearbeite AB Aufgabe A2" |
| **SCHREIBEN** | "→ Schreibe AB Aufgabe T1" |

### Score-Schwellen

| Phase | Score | Freigabe |
|-------|-------|----------|
| Phase 2: Didaktik | 10/10 | Weiter zu Arbeitspfad |
| **Phase 2b: Arbeitspfad** | **100/100** | **Weiter zu Materialien** |

### Arbeitspfad-Kriterien (10×10 Punkte)

1. Vollständigkeit – Jedes AB-Element genau 1× angesteuert
2. Lückenlosigkeit – Keine Sackgassen
3. Spracherwerbslogik – Input→Verstehen→Üben→Produzieren
4. Vorwissen-Kette – Jeder Schritt baut auf
5. Explizite Verweise – "→ AB Kasten X", nicht "→ AB"
6. Rücksprung-Begründung – Didaktisch erklärt
7. Schüler-Perspektive – Novize kann folgen
8. Zeitrealistik – 90 Min machbar
9. Differenzierung – [B]/[S]/[E] eingeplant
10. Kommunikative Kompetenz – Sprachhandlung am Ende

**Vollständige Dokumentation:** `templates/spanisch/WORKFLOW-SPANISCH.md` §1b

---

## Parameter

```
/unterrichtsmaterial [FACH] [KLASSE] [THEMA]
```

Beispiele:
- `/unterrichtsmaterial physik 10 "Ohmsches Gesetz"`
- `/unterrichtsmaterial chemie 8 "Oxidation"`
- `/unterrichtsmaterial informatik 11 "Rekursion"`
- `/unterrichtsmaterial spanisch 7 "Mi instituto"`

---

## Fachfarben

| Fach | Farbe | Hex |
|------|-------|-----|
| **Physik** | Blau | `#2c5aa0` |
| **Chemie** | Grün | `#2a7a4b` |
| **Informatik** | Orange | `#b35c00` |
| **Spanisch** | Karminrot | `#c41e3a` |

---

## Differenzierung

### MINT (Kl. 6-9)

| Niveau | Symbol | Zielgruppe |
|--------|--------|------------|
| Basis | ★ | Berufsreife (BR) |
| Standard | ★★ | Mittlere Reife (MR) |
| Erweiterung | ★★★ | Gymnasium (GY) |

### MINT (Kl. 9 mit Kursen)

- **G-Kurs:** MR-Niveau (keine Sternchen)
- **E-Kurs:** GY-Niveau (keine Sternchen)

### MINT (Kl. 10+)

- **10 MR:** 6-Noten-Skala
- **10 E / 11 / 12:** 15-NP-Skala

### Spanisch

- **[B]/[S]/[E]** nur in Lehrermaterialien
- Schülermaterial: A/B-Gruppen (A2/B1)

---

*Für Details: Fachspezifische Workflow-Dateien lesen!*
