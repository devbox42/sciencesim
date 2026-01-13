# Skill: Publish MINT

Kopiert finale MINT-Materialien (Physik, Chemie, Informatik) nach iCloud und prüft GitHub-Sync.

**Aufruf:** `/publish-mint`

---

## Funktionen

| Befehl | Aktion |
|--------|--------|
| `/publish-mint` | Alle MINT-Fächer nach iCloud + GitHub/QR-Check |
| `/publish-mint physik` | Nur Physik |
| `/publish-mint chemie` | Nur Chemie |
| `/publish-mint informatik` | Nur Informatik |
| `/publish-mint --check` | Nur GitHub-Sync prüfen |
| `/publish-mint --check-qr` | Nur QR-Code-URLs validieren |
| `/publish-mint -o` | Nach Kopieren Finder öffnen |

---

## Was wird kopiert?

**Finale Outputs + Quellen:**
- `*.pdf` – Alle PDFs (AB, ML, LH, LB, LP, MT, QR, LE, etc.)
- `*.html` – Alle HTMLs (LP, MT, SIM, STUNDENPLAN, etc.)
- `*.tex` – Alle TEX-Quelldateien
- `*.md` – Alle Markdown-Dateien (PLANUNG, README, etc.)
- Subfolders: `img/`, `images/`, `assets/`, `css/`, `js/`

**NICHT kopiert (LaTeX-Residuals):**
`.aux`, `.log`, `.out`, `.synctex.gz`, `.fls`, `.fdb_latexmk`, `.toc`, `.lof`, `.lot`, `.bbl`, `.blg`, `.nav`, `.snm`, `.vrb`

---

## Zusätzliche Prüfungen

1. **GitHub-Sync:** Prüft ob LP-*.html, MT-*.html, SIM-*.html auf GitHub liegen
2. **QR-Validierung:** Prüft ob QR-Code-URLs mit GitHub-Dateien übereinstimmen

---

## Zielstruktur (iCloud)

```
~/Library/Mobile Documents/com~apple~CloudDocs/
└── MINT-Materialien/
    ├── Physik/
    │   ├── Klasse-06/
    │   │   └── 02-bewegungen/
    │   │       ├── 01-bewegungsarten/
    │   │       ├── 02-wiederholung/
    │   │       └── 03-st-diagramme/
    │   ├── Klasse-07/
    │   ├── Klasse-08/
    │   └── ...
    ├── Chemie/
    └── Informatik/
```

---

## Ausführung

Das Skill führt das Script aus:
```bash
/Users/jpc/claudecode/sciencesim-lernpfade/projects/publish-mint.sh [args]
```

### Parameter-Handling

| User sagt | Aktion |
|-----------|--------|
| `/publish-mint` | Alle MINT-Fächer |
| `/publish-mint physik` | Nur Physik |
| `/publish-mint --check` | Nur GitHub prüfen |
| `/publish-mint --check-qr` | Nur QR-URLs prüfen |
| `/publish-mint physik -o` | Physik + Finder öffnen |

---

## Proaktive Nutzung

**Nach Erstellung von MINT-Materialien automatisch fragen:**

> "Die Materialien sind fertig. Soll ich sie nach iCloud publishen? (`/publish-mint physik`)"

**Trigger-Situationen:**
- Nach erfolgreicher PDF-Kompilierung (pdflatex)
- Nach Erstellung eines kompletten Materialsets (AB + ML + LH + LP)
- Nach Upload auf GitHub
- Wenn User "fertig" oder "abgeschlossen" sagt

---

## Technische Details

**Script-Pfad:** `projects/publish-mint.sh`

**iCloud-Basis:** `~/Library/Mobile Documents/com~apple~CloudDocs/MINT-Materialien/`

**Verhalten:**
- Erstellt Zielordner automatisch
- Überspringt unveränderte Dateien (Zeitstempel-Vergleich)
- Wandelt Ordnernamen um: `kl06` → `Klasse-06`, `kl9E` → `Klasse-09-E`
- Nutzt rsync für Subfolders (effizient)

---

## Beispiel-Workflow

```
User: Kompiliere AB-03-st-diagramme.tex

[Claude führt pdflatex aus]

Claude: Die Materialien für 03-st-diagramme sind fertig:
- AB-03-st-diagramme.pdf ✓
- ML-03-st-diagramme.pdf ✓
- LH-03-st-diagramme.pdf ✓

Soll ich nach iCloud publishen? (`/publish-mint physik`)

User: ja

[Claude führt /publish-mint physik aus]

Claude: ✓ Physik-Materialien nach iCloud kopiert.
✓ GitHub-Sync geprüft: LP-03, MT-03 online
✓ QR-Codes validiert: URLs korrekt
```
