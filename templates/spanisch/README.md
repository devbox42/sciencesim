# Spanisch-Templates (Klasse 7)

## Übersicht

Diese Templates sind optimiert für den Spanischunterricht Klasse 7 (Gesamtschule MV).

**Verbindliche Spezifikation:** `/projects/spanisch/kl07/ANLEITUNG-SPANISCH.md`

## Templates

| Datei | Beschreibung |
|-------|--------------|
| `lernpfad-spanisch.html` | ES5-kompatibler Lernpfad mit Eingabetoleranz |
| `langentwurf-spanisch.tex` | Tier-1-Langentwurf für Doppelstunden |
| `arbeitsblatt-spanisch.tex` | AB mit Punkteformat `_/X` und Merkkästen |
| `musterloesung-spanisch.tex` | ML mit roten Lösungen |
| `lehrerhinweise-spanisch.tex` | LH mit Differenzierung [B]/[S]/[E] |

## Fachspezifika

- **Fachfarbe:** `#c41e3a` (Karminrot)
- **Eingabetoleranz:** Akzente, ñ, ¿¡ optional
- **JavaScript:** ES5 (kein let/const/Arrow)
- **Bewertung:** 14-NP-Skala (Sek I)
- **Differenzierung:** Intern ([B]/[S]/[E]), nicht auf Schülermaterial

## Verwendung

1. Template kopieren in Zielordner
2. Platzhalter ersetzen:
   - `[SEQUENZ]` → z.B. "01"
   - `[BLOCK]` → z.B. "a"
   - `[THEMA]` → z.B. "Rally + Begrüßung"
   - `[LERNZIELE]` → Aus Jahressequenz

## Siehe auch

- `/CLAUDE.md` → Design-System
- `/projects/spanisch/kl07/JAHRESSEQUENZ.md` → Jahresplanung
- `/projects/spanisch/kl07/ANLEITUNG-SPANISCH.md` → Technische Spezifikation
