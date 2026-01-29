# WORKFLOW: MINT-Materialerstellung

> **Fächer:** Physik, Chemie, Informatik
> **Version:** 1.0
> **Siehe auch:** `/.claude/skills/unterrichtsmaterial/SKILL.md`

---

## Kurzübersicht

```
Phase 0: KONTEXTAUFNAHME
    │   └─ Vorwissen, Lernziele, Aktivitäten, Kontext
    ▼
Phase 1: ANFRAGE + MODUS
    │   └─ KOMPAKT (Default) oder Tier 1-3
    ▼
Phase 2: PLANUNG (Didaktik-Score 10/10)
    │
    ▼
Phase 2b: ARBEITSPFAD (Score 100/100)  ← PFLICHT!
    │   └─ Warm-up (optional) + AB-Inventar + Sequenz
    ▼
Phase 3: CONTENT-MATERIALIEN
    │   └─ AB, ML, LH, LP (mit Warm-up), SL, SIM
    ▼
Phase 4: QA + FREIGABE
    │   └─ PRUEFPLAN-LP-MINT.md anwenden
    ▼
    ✅ FERTIG
```

---

## Materialtypen MINT

| Kürzel | Name | Format | Pflicht |
|--------|------|--------|---------|
| **AB** | Arbeitsblatt | LaTeX→PDF | ✅ |
| **ML** | Musterlösung | LaTeX→PDF | ✅ |
| **LH** | Lehrerhinweise | LaTeX→PDF | ✅ |
| **LP** | Lernpfad | HTML | ✅ |
| **SL** | Stundenleistung/Minitest | HTML | ✅ |
| SIM | Simulation | HTML | Optional |
| PPT | Präsentation | Beamer/PPTX | Optional |
| QR-* | QR-Codes | LaTeX→PDF | Bei LP/SL |

---

## Fachfarben

| Fach | Hex | CSS-Variable |
|------|-----|--------------|
| **Physik** | `#2c5aa0` | `--physik` |
| **Chemie** | `#2a7a4b` | `--chemie` |
| **Informatik** | `#b35c00` | `--informatik` |

---

## Differenzierung

| Klassenstufe | System |
|--------------|--------|
| Kl. 6-9 | ★ (Basis) / ★★ (Standard) / ★★★ (Erweiterung) |
| Kl. 9 Kurse | G-Kurs (MR) / E-Kurs (GY) |
| Kl. 10+ | MR: 6-Noten / GY: 15-NP |

---

## Warm-up-Quiz (NEU)

**Position:** Schritt 0 im Lernpfad (vor dem Einstieg)

| Eigenschaft | Wert |
|-------------|------|
| Umfang | 5-10 MC-Fragen |
| Verhalten | Nicht-blockierend |
| Inhalt | Funfacts, Historie, Alltagsbezug |
| Feedback | Infobox mit Auflösung |
| AB-Übernahme | Optional (1-3 Fragen) |

**Fragetypen:**
1. Funfacts ("Wusstest du...?")
2. Historie ("Wer hat X entdeckt?")
3. Alltagsbezug ("Wo begegnet dir X?")
4. Schätzfragen ("Wie groß ist X?")
5. Vorwissen-Aktivierung

**Siehe:** `ARBEITSPFAD-TEMPLATE.md` §Warm-up

---

## AB-Element-Typen (MINT)

| Kürzel | Typ | Beispiel |
|--------|-----|----------|
| **K** | Kasten/Definition | K1: Formel F = m·a |
| **T** | Tabelle | T1: Messwerte |
| **D** | Diagramm | D1: Kennlinie |
| **Ü** | Übung | Ü1: Berechnung (6 BE) |
| **W** | Warm-up | W1: Funfact (nur LP) |

---

## Qualitätssicherung

### Prüfpläne

| Material | Prüfplan |
|----------|----------|
| Lernpfad (LP) | `PRUEFPLAN-LP-MINT.md` |
| Minitest (MT/SL) | `README-MINITEST-MINT.md` §8 |
| Arbeitspfad | `ARBEITSPFAD-TEMPLATE.md` §5 |

### Score-Schwellen

| Phase | Score | Freigabe |
|-------|-------|----------|
| Didaktik | 10/10 | Weiter zu Arbeitspfad |
| Arbeitspfad | 100/100 | Weiter zu Materialien |
| LP-Prüfplan | 100% | ✅ FREIGABE |

---

## Technische Standards

- **JavaScript:** Nur ES5 (kein let/const/arrow)
- **Formeln:** ISO 80000 (Formelzeichen kursiv, Einheiten aufrecht)
- **Persistenz:** localStorage für alle interaktiven Materialien
- **Responsive:** @media queries für mobile Geräte

---

## Referenzen

| Dokument | Pfad |
|----------|------|
| Haupt-Skill | `/.claude/skills/unterrichtsmaterial/SKILL.md` |
| Arbeitspfad-Template | `./ARBEITSPFAD-TEMPLATE.md` |
| LP-Prüfplan | `./PRUEFPLAN-LP-MINT.md` |
| MT-Template | `./MT-TEMPLATE-minitest.html` |
| MT-Dokumentation | `./README-MINITEST-MINT.md` |

---

*Version 1.0 | 2026-01-27*
