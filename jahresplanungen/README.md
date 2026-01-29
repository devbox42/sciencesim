# Jahresplanungen

Dieses Verzeichnis enthält Schulkalender und Klassenplanungen pro Schuljahr.

---

## Verzeichnisstruktur

```
jahresplanungen/
├── README.md                         ← Diese Datei
└── SJ-2025-26/
    ├── SCHULKALENDER-MV.md           ← Ferien, Feiertage, schulspezifische Termine
    ├── KLASSEN-UEBERSICHT.md         ← Stundenplan, alle Kurse, Differenzierung
    └── klassen/
        ├── 11-12GK-physik.md         ← Verlaufsplan für 11-12GK Physik
        ├── 10E-physik.md             ← Verlaufsplan für 10E Physik
        └── ...                       ← Weitere Klassenpläne
```

---

## Workflow

### 1. Neues Schuljahr anlegen

```bash
mkdir -p jahresplanungen/SJ-YYYY-YY/klassen
```

### 2. Schulkalender erstellen

1. Ferien von [Regierungsportal M-V](https://www.regierung-mv.de/Landesregierung/bm/Schule/Schulorganisation/Ferientermine/) holen
2. Schulspezifische Termine ergänzen (Projektwochen, Wandertage, etc.)
3. Notenstopp-Termine eintragen
4. Prüfungszeiträume markieren

### 3. Klassenübersicht pflegen

1. Stundenplan (Wochentage, Stundennummern) eintragen
2. Kursart (Sek I gemischt, GY, MR, GK) dokumentieren
3. Differenzierungssystem (★★★) vermerken
4. Material-Pfade verlinken

### 4. Verlaufspläne pro Klasse erstellen

Für jede Klasse einen Verlaufsplan im Ordner `klassen/` anlegen:

```markdown
# Verlaufsplan [KLASSE] [FACH] – SJ 20XX/XX

## Eckdaten
- **Wochentage:** Mi 3. Std, Fr 5+6. Std
- **Typ:** ES + DS
- **Kursart:** [GK/MR/GY/gemischt]
- **Notenstopp:** [Datum]

## Sequenzübersicht
| # | Datum | Thema | Material |
|---|-------|-------|----------|
| 1 | ... | ... | → projects/... |

## Tests & Klausuren
| Datum | Typ | Inhalt | BE |
|-------|-----|--------|-----|
```

---

## Verknüpfung mit Materialien

Die Verlaufspläne verweisen auf Materialien in `projects/`:

```
jahresplanungen/SJ-2025-26/klassen/11-12GK-physik.md
    ↓ verweist auf
projects/physik/kl12-GK/
    ├── STUNDENPLAN-Q4-2526.md    ← Detailplanung
    ├── STUNDENPLAN-Q4-2526.html  ← Visuelle Darstellung
    └── 01-photoeffekt/           ← Stundenmaterialien
        ├── AB-01-hallwachs.tex
        ├── LH-01-hallwachs.tex
        └── ...
```

---

## Relevante Templates

| Template | Pfad | Beschreibung |
|----------|------|--------------|
| Stundenplan (HTML) | `templates/stundenplan-template.html` | Visuelle Halbjahresübersicht |
| Stundenplan-Anleitung | `templates/README-STUNDENPLAN.md` | Platzhalter, CSS-Klassen |
| Langentwurf | `templates/lesson-plan/langentwurf-template.tex` | Unterrichtsentwurf |

---

## Schuljahre

| Schuljahr | Status | Bemerkung |
|-----------|--------|-----------|
| 2025/26 | ✅ aktiv | Ab 05.01.2026 (2. HJ) |

---

## Checkliste neues Halbjahr

- [ ] Ferien M-V aktualisieren
- [ ] Schulspezifische Termine eintragen
- [ ] Notenstopp-Termine prüfen
- [ ] Stundenplan aktualisieren (falls Änderungen)
- [ ] Verlaufspläne für neue Themenblöcke anlegen
- [ ] Materialien in `projects/` erstellen
