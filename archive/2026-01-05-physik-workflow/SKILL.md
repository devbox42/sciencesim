# Skill: Unterrichtsmaterial

Erstellt qualitätsgesicherte Materialsets für Einzel- oder Doppelstunden.

**Aufruf:** `/unterrichtsmaterial` oder automatisch bei Anfragen wie:
- "Erstelle Material für..."
- "Mach ein Arbeitsblatt zu..."
- "Bereite die Doppelstunde vor..."

---

## Fach-Routing

| Fach | Workflow | Templates |
|------|----------|-----------|
| **Spanisch Kl. 7-8** | `/templates/spanisch/WORKFLOW-SPANISCH.md` | `/templates/spanisch/` |
| **Spanisch Kl. 9** | `/templates/spanisch/WORKFLOW-SPANISCH.md` | `/templates/spanisch/` |
| **Spanisch Spätbeg.** | `/projects/spanisch/spaetbeginner/ANLEITUNG-SPANISCH-SPAETBEGINNER.md` | `/templates/spanisch/` |
| Physik | `/CLAUDE.md` | `/templates/` |
| Chemie | `/CLAUDE.md` | `/templates/` |
| Informatik | `/CLAUDE.md` | `/templates/` |

**WICHTIG:** Bei Spanisch immer zuerst den WORKFLOW lesen!

---

## Lehrwerksreferenzen

| Kurs | Lehrwerk | Referenz |
|------|----------|----------|
| Spanisch Kl. 7-8 | Qué pasa 1 | `knowledge/Spanisch-Que-Pasa-1/que-pasa-1-referenz.md` |
| Spanisch Kl. 9 | Qué pasa 2 | `knowledge/Spanish-Que-Pasa-2/que-pasa-2-referenz.md` ⚠️ |
| Spanisch Spätbeg. | A_tope.com | `knowledge/Spanisch-A_tope_Spaetbeginner/a-tope-spaetbeginner-referenz.md` |

⚠️ = Platzhalter (unvollständig)

---

## Materialtypen pro Doppelstunde

| Kürzel | Name | Format | Beschreibung |
|--------|------|--------|--------------|
| **LE** | Langentwurf | PDF | Tier 1/2/3 Unterrichtsentwurf |
| **AB** | Arbeitsblatt | PDF | Für SuS, zum Abheften |
| **ML** | Musterlösung | PDF | AB mit roten Lösungen |
| **LH** | Lehrerhinweise | PDF | Kurzplan + Differenzierung |
| **LP** | Lernpfad | HTML | Interaktiv, digital |
| **PPT** | PowerPoint | PPTX | 10-15 Folien |
| **MT** | Minitest | HTML+PDF | 25 BE pro Stunde |
| **SL** | Sequenztest | HTML+PDF | 25-50 BE am Sequenzende |
| **PLATZKARTEN** | Platzkarten | PDF | 24 Karten mit QR für Tests |

**Dateinamenskonvention:** `[TYP]-[XX][y]-kurzname.[ext]`
- XX = Stundennummer (01, 02, ...)
- y = Block (a, b, c, d)

---

## Phase 0: Kontextaufnahme (WICHTIG!)

**Vor der Materialerstellung:** User-Input in 4 Kategorien erfassen:

| Kategorie | User sagt... | Wird im LE zu... |
|-----------|--------------|------------------|
| **A) Vorwissen** | "Ich habe ... unterrichtet" | Voraussetzungen |
| **B) Lernziele** | "Ich möchte ... einführen" | Feinziele FZ1-FZ4 |
| **C) Aktivitäten** | "Ich stelle mir vor ..." | Verlaufsphasen |
| **D) Kontext** | "Nur 45 Min / Klasse unruhig" | Didaktische Hinweise |

**Fallback:** Wenn kein Kontext → Lehrwerksreferenz oder Standard-Aktivitäten.

**Details:** Siehe `/templates/spanisch/WORKFLOW-SPANISCH.md` → §1a Phase 0

---

## Qualitäts-Gate

**REGEL:** Kein Material ohne LE-Score ≥ 9.0

```
LE erstellen → Score ≥ 9.0? → Materialien → Material-QA → ✅ FREIGABE
                   │                              │
                  Nein                    (Traceability,
                   ↓                      Konsistenz,
              Iteration                   Layout-QA)
```

**Vollständige QA-Dokumentation:** Siehe `/CLAUDE.md`:
- **Didaktik-Score:** Abschnitt "Didaktisches QA-Framework" (10 Dimensionen)
- **Material-QA:** Abschnitt "Material-QA" (Traceability, Konsistenz, Layout)

---

## Parameter

```
/unterrichtsmaterial [FACH] [KLASSE] [THEMA]
```

Beispiele:
- `/unterrichtsmaterial spanisch 7 "Mi instituto"`
- `/unterrichtsmaterial physik 10 "Ohmsches Gesetz"`

---

## Fachfarben

| Fach | Farbe |
|------|-------|
| Physik | `#2c5aa0` |
| Chemie | `#2a7a4b` |
| Informatik | `#b35c00` |
| **Spanisch** | `#c41e3a` |

---

*Für Details: Fachspezifische Workflow-Dateien lesen!*
