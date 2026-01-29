# Projekt: Dichte (Klasse 7)

## Übersicht

| Eigenschaft | Wert |
|-------------|------|
| Fach | Physik |
| Klassenstufe | 7 |
| Thema | Materie - Dichte |
| Umfang | ~8 Ustd. (laut Rahmenplan MV) |

---

## Dateien

| Datei | Beschreibung |
|-------|--------------|
| `lernpfad.html` | Interaktiver Lernpfad (12 Schritte, integrierte Simulation) |
| `stundenleistung.html` | Simulation + Kurztest (75 BE, 14-NP) |
| `arbeitsblatt-dichte.tex` | Begleitendes Arbeitsblatt (2-spaltig, 2 Seiten) |

---

## Hinweise

### Neutralität

**Materialien sind schulneutral zu halten.**

- Keine Schulnamen, Logos oder spezifisches Branding
- QR-Code-URL im Arbeitsblatt muss vor Nutzung angepasst werden
- Footer im Arbeitsblatt ist leer (kann bei Bedarf ergänzt werden)

### Anpassungen

**Arbeitsblatt (`arbeitsblatt-dichte.tex`):**
- Zeile 69: `\lfoot{}` - hier kann ein Schulname eingefügt werden
- Zeile 451: QR-Code URL anpassen

**Stundenleistung (`stundenleistung.html`):**
- Zeile 755: Header-Meta kann ergänzt werden

---

## Inhalte

### Lernpfad (12 Schritte)

1. Content: Ein Rätsel zum Einstieg
2. Content: Was ist Dichte? (Definition)
3. Exercise: Dichte verstehen (★)
4. Content: Die Dichte-Formel
5. Exercise: Einfache Berechnung (★)
6. Content: Typische Dichtewerte
7. Content: Schwimmen, Schweben, Sinken
8. Exercise: Schwimmen oder Sinken? (★/★★)
9. Simulation: Integrierte Canvas-Simulation
10. Content: Die Formel umstellen
11. Exercise: Mit der Formel rechnen (★★/★★★)
12. Exercise: Abschlussübung (★/★★)

### Simulation

- 10 Materialien (Kork, Holz, Öl, Fisch, U-Boot, Plastik, Stein, Alu, Eisen, Blei)
- Wasser (ρ=1,0) und Salzwasser (ρ=1,03)
- Eigener Körper mit Dichte-Slider
- Physik: Plumpsen → Mitte → Sinken/Schweben/Schwimmen

### Kurztest (75 BE)

| Niveau | Punkte | Aufgaben |
|--------|--------|----------|
| ★ | 30 BE | T1–T9 |
| ★★ | 25 BE | T10–T16 |
| ★★★ | 20 BE | T17–T21 |

Bewertung: 14-NP Skala (Sek I)

---

## Differenzierung

Klasse 7: Sternchen werden angezeigt
- (*) Basis
- (**) Erweiterung
- (***) Gymnasium

---

## Kompilieren (LaTeX)

```bash
pdflatex arbeitsblatt-dichte.tex
```

Benötigte Pakete: `qrcode`, `tcolorbox`, `siunitx`, `tikz`
