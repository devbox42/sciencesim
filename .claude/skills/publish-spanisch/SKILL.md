# Skill: Publish Spanisch

Kopiert finale Spanisch-Materialien (PDFs, HTMLs) nach iCloud zur Freigabe.

**Aufruf:** `/publish-spanisch` oder `/publish`

---

## Funktionen

| Befehl | Aktion |
|--------|--------|
| `/publish-spanisch` | Alle Spanisch-Materialien nach iCloud |
| `/publish-spanisch kl07` | Nur Klasse 7 |
| `/publish-spanisch kl08` | Nur Klasse 8 |
| `/publish-spanisch --open` | Nach Kopieren Finder öffnen |

---

## Was wird kopiert?

**Nur finale Outputs:**
- `AB-*.pdf` – Arbeitsblätter
- `ML-*.pdf` – Musterlösungen
- `LH-*.pdf` – Lehrerhinweise
- `SLIDES-*.pdf` – Präsentationen
- `LP-*.html` – Lernpfade
- `LB-*.pdf` – Lernblätter
- `PLANUNG-*.md` – Planungsnotizen

**NICHT kopiert:** .tex, .aux, .log, .out, Quelldateien

---

## Zielstruktur (iCloud)

```
~/Library/Mobile Documents/com~apple~CloudDocs/
└── Spanisch-Materialien/
    ├── Klasse-07/
    │   └── Unidad-2-mi-instituto/
    │       ├── DS-01/
    │       │   ├── AB-01.pdf
    │       │   ├── ML-01.pdf
    │       │   ├── LH-01.pdf
    │       │   └── SLIDES-01.pdf
    │       └── DS-02/
    ├── Klasse-08/
    ├── Klasse-09/
    └── spaetbeginner/
```

---

## Ausführung

Das Skill führt das Script aus:
```bash
/Users/jpc/claudecode/sciencesim-lernpfade/projects/spanisch/publish-spanisch.sh
```

### Parameter-Handling

| User sagt | Aktion |
|-----------|--------|
| `/publish-spanisch` | Script ohne Parameter |
| `/publish-spanisch kl07` | Nur `kl07/` verarbeiten |
| `/publish-spanisch --open` | Script mit `--open` Flag |

---

## Proaktive Nutzung

**Nach Erstellung von Spanisch-Materialien automatisch fragen:**

> "Die Materialien sind fertig. Soll ich sie nach iCloud publishen? (`/publish-spanisch`)"

**Trigger-Situationen:**
- Nach erfolgreicher PDF-Kompilierung
- Nach Erstellung eines kompletten Materialsets (AB + ML + LH)
- Wenn User "fertig" oder "abgeschlossen" sagt

---

## Technische Details

**Script-Pfad:** `projects/spanisch/publish-spanisch.sh`

**iCloud-Basis:** `~/Library/Mobile Documents/com~apple~CloudDocs/Spanisch-Materialien/`

**Verhalten:**
- Erstellt Zielordner automatisch
- Überspringt unveränderte Dateien (Zeitstempel-Vergleich)
- Wandelt Ordnernamen um: `kl07` → `Klasse-07`

---

## Beispiel-Workflow

```
User: Erstelle Material für DS-05 Mi instituto

[Claude erstellt AB-05.pdf, ML-05.pdf, LH-05.pdf, SLIDES-05.pdf]

Claude: Die Materialien für DS-05 sind fertig:
- AB-05.pdf ✓
- ML-05.pdf ✓
- LH-05.pdf ✓
- SLIDES-05.pdf ✓

Soll ich nach iCloud publishen?

User: ja

[Claude führt /publish-spanisch aus]

Claude: ✓ 4 Dateien nach iCloud kopiert.
Ordner: Spanisch-Materialien/Klasse-07/Unidad-2-mi-instituto/DS-05/
```
