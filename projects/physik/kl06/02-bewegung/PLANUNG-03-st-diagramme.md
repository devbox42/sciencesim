# Planung: s(t)-Diagramme verstehen (Kl. 6, Std. 3)

**Stand:** 12.01.2026
**Ziel:** Erarbeitung + digitale Stundenleistung in 45 min

---

## Feinziele (aus RP Kl. 6)

| FZ | Inhalt | AFB | Prüfung |
|----|--------|-----|---------|
| FZ1 | Achsen eines s(t)-Diagramms **benennen** | I | MT |
| FZ2 | Werte aus s(t)-Diagramm **ablesen** | I | MT |
| FZ3 | Bewegungsart aus Diagramm **erkennen** (gleichförmig/ungleichförmig) | I/II | MT |
| FZ4 | Zwei Bewegungen im Diagramm **vergleichen** | II | MT |
| FZ5 | Punkte in Koordinatensystem **eintragen** | II | AB (Übung) |

---

## Materialien

| Typ | Datei | Zweck |
|-----|-------|-------|
| LB | `LB-003-st-diagramme.tex` | Kurze Einführung (1 Seite, ~5 min lesen) |
| AB | `AB-003-st-diagramme.tex` | Übung Zeichnen (NICHT einsammeln) |
| MT | `MT-003-st-diagramme.html` | **Stundenleistung (25 BE, digital)** |
| ML | `ML-003-st-diagramme.tex` | Lösungen für AB (Selbstkontrolle) |

---

## Verlauf (45 min)

| Min | Phase | Aktivität | SF | Material |
|-----|-------|-----------|-----|----------|
| 0-3 | Einstieg | "Was zeigt dieses Bild?" – s(t)-Diagramm an Tafel | PL | Tafel |
| 3-10 | Input | LB-003 lesen: Achsen, Beispiel, Merksatz | EA | LB-003 |
| 10-20 | Übung | AB-003: 2 Diagramme zeichnen (Selbstkontrolle mit ML) | EA | AB-003, ML |
| 20-22 | Übergang | Tablets holen, MT-Link aufrufen | — | QR-Code |
| 22-45 | **Test** | MT-003 digital bearbeiten (25 BE) | EA | MT-003 |
| 45 | Ende | Automatische Auswertung → Ergebnis sichtbar | — | — |

---

## MT-003 Struktur (25 BE, digital)

### Aufgabenverteilung

| # | Typ | Inhalt | BE | AFB |
|---|-----|--------|-----|-----|
| 1 | MC | Achsen benennen (x=?, y=?) | 2 | I |
| 2 | Numeric | Wert ablesen: "Welcher Weg bei t = 4 s?" | 3 | I |
| 3 | Numeric | Wert ablesen: "Welche Zeit bei s = 20 m?" | 3 | I |
| 4 | MC | Bewegungsart erkennen (Diagramm A) | 2 | I |
| 5 | MC | Bewegungsart erkennen (Diagramm B) | 2 | I |
| 6 | Matching | 3 Diagramme → 3 Beschreibungen zuordnen | 6 | II |
| 7 | MC | Vergleich: "Wer ist schneller?" (2 Linien) | 3 | II |
| 8 | Numeric | "Um wie viel Meter ist A nach 6 s weiter als B?" | 4 | II |
| | | **Summe Pflicht** | **25** | |

### Differenzierung (Zusatz)

| # | Typ | Inhalt | BE | AFB |
|---|-----|--------|-----|-----|
| 9★★ | MC | Steigung erkennen: "Welches Diagramm zeigt die größte Geschwindigkeit?" | 3 | II |
| 10★★★ | Freitext | "Beschreibe die Bewegung in eigenen Worten" | 4 | III |
| | | **Maximum** | **32** | |

---

## Bewertung

| Punkte | Note (Kl. 6) |
|--------|--------------|
| 25-32 | 1 |
| 20-24 | 2 |
| 15-19 | 3 |
| 10-14 | 4 |
| 5-9 | 5 |
| 0-4 | 6 |

---

## Technische Anforderungen MT-003

- [ ] ES5-JavaScript (kein let/const)
- [ ] Responsive (iPad-tauglich)
- [ ] Interaktive SVG-Diagramme (hover = Werte)
- [ ] Dezimalkomma akzeptieren
- [ ] localStorage für Zwischenspeicherung
- [ ] Auto-Auswertung mit Notentabelle
- [ ] Fachfarbe `#2c5aa0`

---

## Diagramme für MT-003

### Diagramm A (gleichförmig)
```
s(m)
40 ┼─────────────────●
30 ┼───────────●
20 ┼─────●
10 ┼───●
 0 ┼●────────────────────
   0   2   4   6   8  t(s)
```
→ Gerade durch Ursprung, v = 5 m/s

### Diagramm B (schneller, gleichförmig)
```
s(m)
40 ┼───────────●
30 ┼─────●
20 ┼───●
10 ┼─●
 0 ┼●────────────────────
   0   2   4   6   8  t(s)
```
→ Steilere Gerade, v = 10 m/s

### Diagramm C (Stillstand)
```
s(m)
20 ┼●────●────●────●────●
10 ┼
 0 ┼─────────────────────
   0   2   4   6   8  t(s)
```
→ Horizontale Linie, v = 0

---

## LB-003 Inhalt (1 Seite)

1. **Was ist ein s(t)-Diagramm?**
   - x-Achse = Zeit t in Sekunden (s)
   - y-Achse = Weg s in Metern (m)

2. **Beispiel mit Bild**
   - Auto fährt gleichförmig
   - Tabelle: t | s
   - Diagramm dazu

3. **Merksatz (Kasten)**
   > "Je steiler die Linie, desto schneller die Bewegung."
   > "Waagerechte Linie = Stillstand."

---

## AB-003 anpassen

Aktuelles AB-003 enthält zu viel → **Reduzieren auf:**
- 1× leeres Koordinatensystem + Wertetabelle → Punkte eintragen + verbinden
- 1× fertiges Diagramm → 3 Werte ablesen (Selbstkontrolle)

**Nicht mehr:** komplexe Aufgaben (die sind jetzt im MT)

---

## Nächste Schritte

1. [ ] LB-003 erstellen (1 Seite, kurz)
2. [ ] AB-003 reduzieren (nur Übung, 2 Aufgaben)
3. [ ] MT-003 erstellen (25 BE, Struktur wie oben)
4. [ ] QR-Code für MT-003 generieren

---

## Notizen

- Kein Papier einsammeln → weniger Korrekturaufwand
- MT-003 ersetzt SL-004 für Diagramme
- SL-004 kann dann Gesamttest "Bewegungen" werden (oder entfällt)
