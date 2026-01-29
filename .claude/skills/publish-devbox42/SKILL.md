# Skill: Publish DevBox42

Veröffentlicht HTML-Dateien auf GitHub Pages (`devbox42/sciencesim`) via GitHub API.

**Aufruf:** `/publish-devbox42` oder "push auf github devbox42"

---

## Workflow (IMMER mit Rückfrage!)

### Schritt 1: Dateien ermitteln

Claude analysiert das aktuelle Verzeichnis und zeigt Vorschlag:

```
📤 GitHub Push (devbox42/sciencesim)

Aktuelles Verzeichnis: projects/physik/kl08/elektrik/

Folgende Dateien werden veröffentlicht:
┌─────────────────────────────────────────┬────────────────────────────────────────────────────────────┐
│ Lokale Datei                            │ GitHub-Ziel                                                │
├─────────────────────────────────────────┼────────────────────────────────────────────────────────────┤
│ MT-01-stromstaerke-spannung.html        │ physik/kl08/elektrik/MT-01-stromstaerke-spannung.html      │
│ LP-01-stromstaerke-spannung.html        │ physik/kl08/elektrik/LP-01-stromstaerke-spannung.html      │
└─────────────────────────────────────────┴────────────────────────────────────────────────────────────┘

URL nach Push: https://devbox42.github.io/sciencesim/physik/kl08/elektrik/

Soll ich diese Dateien veröffentlichen? (j/n)
```

### Schritt 2: Nach Bestätigung ausführen

```bash
cd projects/FACH && ./publish.sh PFAD/
```

### Schritt 3: Verifizierung zeigen

```
✅ Veröffentlicht:
  • MT-01-stromstaerke-spannung.html (79 KB) – neu erstellt
  • LP-01-stromstaerke-spannung.html (45 KB) – aktualisiert

URLs:
  https://devbox42.github.io/sciencesim/physik/kl08/elektrik/MT-01-stromstaerke-spannung.html
  https://devbox42.github.io/sciencesim/physik/kl08/elektrik/LP-01-stromstaerke-spannung.html
```

---

## Fach-Erkennung

| cwd enthält | Fach | Script |
|-------------|------|--------|
| `projects/physik/` | Physik | `projects/physik/publish.sh` |
| `projects/chemie/` | Chemie | `projects/chemie/publish.sh` |
| `projects/spanisch/` | Spanisch | `projects/spanisch/publish.sh` |

---

## Technische Details

**Repository:** `devbox42/sciencesim`
**Methode:** GitHub API via `gh api` (kein git push!)
**Dateitypen:** Nur `*.html` (LP, MT, SIM)

### API-Aufrufe (intern)

```bash
# Prüfen ob existiert
gh api "repos/devbox42/sciencesim/contents/PFAD"

# Neu erstellen
gh api "repos/devbox42/sciencesim/contents/PFAD" \
    --method PUT \
    --field message="add: PFAD" \
    --field content="$(base64 -i DATEI)"

# Aktualisieren (mit SHA)
gh api "repos/devbox42/sciencesim/contents/PFAD" \
    --method PUT \
    --field message="update: PFAD" \
    --field content="$(base64 -i DATEI)" \
    --field sha="$SHA"
```

---

## Vorteile

- ✅ Kein Merge-Konflikt (direkte API)
- ✅ Kein git stash nötig
- ✅ Einzelne Dateien möglich
- ✅ Immer Vorschau vor Ausführung

---

## Beispiel-Aufruf

```
User: /publish-devbox42

Claude:
📤 GitHub Push (devbox42/sciencesim)

Aktuelles Verzeichnis: projects/physik/kl08/elektrik/

Folgende Dateien werden veröffentlicht:
│ MT-01-stromstaerke-spannung.html │ → physik/kl08/elektrik/MT-01-stromstaerke-spannung.html │

Soll ich diese Dateien veröffentlichen?

User: ja

Claude: [führt publish.sh aus]

✅ MT-01-stromstaerke-spannung.html veröffentlicht
URL: https://devbox42.github.io/sciencesim/physik/kl08/elektrik/MT-01-stromstaerke-spannung.html
```

---

## Abgrenzung

| Skill | Ziel | Methode |
|-------|------|---------|
| `/publish-devbox42` | GitHub Pages (devbox42/sciencesim) | GitHub API |
| `/publish-mint` | iCloud + GitHub-Check | Dateikopie + Check |

Andere Repositories (nicht devbox42) benötigen ggf. eigene Skills mit anderem Workflow.
