# Showcase – Digitale Lernmaterialien

Anonyme Präsentationsseite für Bewerbungen.

## Live-URL

**https://devbox42.github.io/sciencesim/showcase/**

## Inhalt

Das Showcase präsentiert ausgewählte Lernpfade, Simulationen und Arbeitsblätter aus drei Fächern:

### Physik (Sekundarstufe I & II)

| Material | Lokal | Online |
|----------|-------|--------|
| **Photoeffekt: Gegenfeldmethode** (Kl. 12 GK) | | |
| Lernpfad | `projects/physik/kl12-GK/01-photoeffekt/02-DS-gegenfeld/LP-02-gegenfeld.html` | [LP](https://devbox42.github.io/sciencesim/physik/kl12-GK/01-photoeffekt/02-DS-gegenfeld/LP-02-gegenfeld.html) |
| Simulation | `projects/physik/kl12-GK/01-photoeffekt/02-DS-gegenfeld/SIM-02-gegenfeld.html` | [SIM](https://devbox42.github.io/sciencesim/physik/kl12-GK/01-photoeffekt/02-DS-gegenfeld/SIM-02-gegenfeld.html) |
| Arbeitsblatt | `projects/physik/kl12-GK/01-photoeffekt/02-DS-gegenfeld/AB-02-gegenfeld.pdf` | [PDF](https://devbox42.github.io/sciencesim/physik/kl12-GK/01-photoeffekt/02-DS-gegenfeld/AB-02-gegenfeld.pdf) |
| **Ohmsches Gesetz** (Kl. 8) | | |
| Lernpfad | `projects/physik/kl8-ohm/LP-02a-ohmsches-gesetz.html` | [LP](https://devbox42.github.io/sciencesim/physik/kl8-ohm/LP-02a-ohmsches-gesetz.html) |
| Arbeitsblatt | `projects/physik/kl8-ohm/AB-02a-ohmsches-gesetz.pdf` | [PDF](https://devbox42.github.io/sciencesim/physik/kl8-ohm/AB-02a-ohmsches-gesetz.pdf) |
| Simulationen | `projects/physik/kl8-ohm/SIM-02a-*.html` (4 Stück) | eingebettet im LP |

### Informatik (Sekundarstufe I)

| Material | Lokal | Online |
|----------|-------|--------|
| **Tabellenkalkulation: Formeln** (Kl. 7) | | |
| Lernpfad | `projects/informatik/kl07/tabellenkalkulation/02-praxis-formeln/LP-02-praxis-formeln.html` | [LP](https://devbox42.github.io/sciencesim/informatik/kl07/02-tabellenkalkulation/LP-02-praxis-formeln.html) |
| Spielwiese | `projects/informatik/kl07/tabellenkalkulation/02-praxis-formeln/SIM-02-excel-spielwiese.html` | [SIM](https://devbox42.github.io/sciencesim/informatik/kl07/02-tabellenkalkulation/SIM-02-excel-spielwiese.html) |
| Lernblatt | `projects/informatik/kl07/tabellenkalkulation/02-praxis-formeln/LB-02-praxis-formeln.pdf` | [PDF](https://devbox42.github.io/sciencesim/informatik/kl07/02-tabellenkalkulation/LB-02-praxis-formeln.pdf) |

### Spanisch (Sekundarstufe II)

| Material | Lokal | Online |
|----------|-------|--------|
| **Me gusta: Vorlieben ausdrücken** (Oberstufe) | | |
| Lernpfad | `projects/spanisch/oberstufe-gustos/lernpfad.html` | [LP](https://devbox42.github.io/sciencesim/spanisch/oberstufe-gustos/lernpfad.html) |
| Arbeitsblatt | `projects/spanisch/oberstufe-gustos/arbeitsblatt-gustos.pdf` | [PDF](https://devbox42.github.io/sciencesim/spanisch/oberstufe-gustos/arbeitsblatt-gustos.pdf) |

## Aktualisieren

Das Showcase wird über die GitHub API veröffentlicht (nicht via git push).

### Showcase-Seite aktualisieren

```bash
REPO="devbox42/sciencesim"
SHA=$(gh api "repos/$REPO/contents/showcase/index.html" | grep -o '"sha":"[^"]*"' | head -1 | cut -d'"' -f4)

gh api "repos/$REPO/contents/showcase/index.html" \
    --method PUT \
    --field message="update: showcase" \
    --field content="$(base64 -i showcase/index.html)" \
    --field sha="$SHA"
```

### Neue Datei hochladen

```bash
REPO="devbox42/sciencesim"
LOCAL_FILE="projects/physik/kl8-ohm/LP-02a-ohmsches-gesetz.html"
REMOTE_PATH="physik/kl8-ohm/LP-02a-ohmsches-gesetz.html"

gh api "repos/$REPO/contents/$REMOTE_PATH" \
    --method PUT \
    --field message="add: $REMOTE_PATH" \
    --field content="$(base64 -i $LOCAL_FILE)"
```

### Bestehende Datei aktualisieren

```bash
REPO="devbox42/sciencesim"
LOCAL_FILE="projects/physik/kl8-ohm/LP-02a-ohmsches-gesetz.html"
REMOTE_PATH="physik/kl8-ohm/LP-02a-ohmsches-gesetz.html"

# SHA der bestehenden Datei holen
SHA=$(gh api "repos/$REPO/contents/$REMOTE_PATH" | grep -o '"sha":"[^"]*"' | head -1 | cut -d'"' -f4)

gh api "repos/$REPO/contents/$REMOTE_PATH" \
    --method PUT \
    --field message="update: $REMOTE_PATH" \
    --field content="$(base64 -i $LOCAL_FILE)" \
    --field sha="$SHA"
```

## Pfad-Mapping

Die GitHub-Pfade unterscheiden sich von den lokalen Pfaden:

| Lokal | GitHub |
|-------|--------|
| `projects/physik/...` | `physik/...` |
| `projects/informatik/kl07/tabellenkalkulation/02-praxis-formeln/...` | `informatik/kl07/02-tabellenkalkulation/...` |
| `projects/spanisch/...` | `spanisch/...` |
| `showcase/...` | `showcase/...` |

## Regeln

1. **Keine neuen Materialien erstellen** – nur bestehende verlinken
2. **Keine Namen/Schulnamen** – Showcase bleibt anonym
3. **Originale nicht verändern** – nur hochladen
4. **Links testen** nach jedem Update:
   ```bash
   curl -s -o /dev/null -w "%{http_code}" "https://devbox42.github.io/sciencesim/showcase/"
   ```

## Dateien

```
showcase/
├── index.html   ← Showcase-Seite
└── README.md    ← Diese Dokumentation
```
