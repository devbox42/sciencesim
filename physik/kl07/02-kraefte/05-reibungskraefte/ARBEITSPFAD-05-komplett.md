# ARBEITSPFAD: LP-05-komplett (Doppelstunde Reibung)

**Stand:** 05.02.2026
**Zielgruppe:** Klasse 7A (Doppelstunde, 2×40 Min mit 5 Min Pause)

---

## Konzept

Kombination aus LP-05 (Grundlagen) + LP-05b (Formel/Rechnen) in 15 Schritten.
Erkenntnisweg: Phänomen → Hypothese → Experiment → Beobachtung → Auswertung → Deutung → Verallgemeinerung.
Pflicht: Schritte 1–11 (~70 Min). Zusatz (★★★): Schritte 12–15 für Schnelle.

## Struktur

| # | Inhalt | Phase | Zeit | Quelle |
|---|--------|-------|------|--------|
| 1 | Einstieg: Reibung im Alltag | Phänomen | 3' | LP-05 |
| 2 | Animation: Haft → Gleit | Phänomen | 5' | LP-05 |
| 3 | **Hypothese: Welche Reibungsart ist am stärksten?** | Hypothese | 3' | neu |
| 4 | Simulation: 3 Arten messen (Federkraftmesser) | Experiment | 8' | LP-05 |
| 5 | Erkenntnis: Reihenfolge (interaktives Quiz) | Auswertung | 5' | LP-05 |
| 6 | Simulation: Einflussfaktoren + Messwerttabelle | Experiment+Auswertung | 10' | LP-05 |
| 7 | Erwünscht/Unerwünscht (interaktiv) | Deutung/Transfer | 8' | LP-05 |
| **PAUSE** | | | 5' | |
| 8 | Formel F_R = μ·F_N + Dreieck (★★) | Verallgemeinerung | 8' | LP-05b |
| 9 | Rechenaufgaben R1★/R2★★/R3★★★ | Anwendung | 10' | LP-05b |
| 10 | Anwendung: Bremsweg + Merksatz | Transfer | 5' | LP-05 |
| 11 | Pflicht geschafft! Selbstcheck | Sicherung | 3' | neu |
| **Summe Pflicht** | | | **~73'** | |
| 12 | Zusatz: Rollreibung im Detail (★★★) | Experiment | 8' | LP-05b |
| 13 | Zusatz: Reifendruck und Haftung (★★★) | Experiment | 5' | LP-05b |
| 14 | Zusatz: ABS-System (★★★) | Transfer | 8' | LP-05b |
| 15 | Alles geschafft + Memory | Sicherung | 5' | neu |

## Erkenntnisweg-Zuordnung

```
Schritte 1-2:  PHÄNOMEN (schwerer Schrank, Haft→Gleit-Animation)
Schritt 3:     HYPOTHESE (Vermutung Reihenfolge)
Schritt 4:     EXPERIMENT (Federkraftmesser-Simulation)
Schritt 5:     AUSWERTUNG/DEUTUNG (Reihenfolge bestimmen)
Schritt 6:     EXPERIMENT+AUSWERTUNG (Einflussfaktoren, μ entdecken)
Schritte 7-8:  VERALLGEMEINERUNG (Merksätze, Formel)
Schritte 9-10: ANWENDUNG (Rechnen, Bremsweg)
```

## Differenzierung

- **★ Basis:** Schritte 1–7, 10–11 (qualitativ, keine Formel)
- **★★ Standard:** + Formel verstehen (Schritt 8), R1+R2 rechnen
- **★★★ Erweitert:** + R3 umstellen, Zusatz (Schritte 12–15)

## AB-LP-Verzahnung (Hefter-Hinweise)

| LP-Schritt | AB-Aufgaben |
|------------|-------------|
| 1 | K1 (Infokasten lesen) |
| 2 | B1 (Beobachtung) |
| 3 | H1 (Hypothese ankreuzen) |
| 4 | T1 (Messwerte) |
| 5 | B2 + K2 (Reihenfolge + Merksatz) |
| 6 | B3/B4 + K4 (Einflussfaktoren + Messwerttabelle + Merksatz) |
| 7 | T2 + A1 + K5 (Erwünscht/Unerwünscht + Fahrrad + Merksatz Verringerung) |
| 8 | K3 (Formel + Dreieck) |
| 9 | R1, R2, R3 (Rechenaufgaben) |
| 10 | A2 + K6 (Bremsweg + Merksatz) |
| 12 | Zusatz-AB B5 (Rollreibung) |
| 13 | Zusatz-AB B6 (Reifendruck) |
| 14 | Zusatz-AB B7 + T3 (ABS) |

## Dateien

| Datei | Inhalt | Seiten |
|-------|--------|--------|
| `LP-05-komplett.html` | Lernpfad (15 Schritte, STORAGE_KEY v3) | — |
| `AB-05-komplett.tex/.pdf` | Arbeitsblatt Pflicht | 2 |
| `ML-05-komplett.tex/.pdf` | Musterlösung Pflicht | 2 |
| `AB-05-zusatz.tex/.pdf` | Zusatz-Arbeitsblatt (★★★) | 1 |
| `ML-05-zusatz.tex/.pdf` | Musterlösung Zusatz | 1 |
| `QR-05-komplett.pdf` | QR-Code für AB | 1 |

## Simulations-Übersicht

| Simulation | Schritt | Typ | Parameter |
|-----------|---------|-----|-----------|
| Haft/Gleit-Animation | 2 | CSS-Animation | Play/Reset |
| Federkraftmesser | 4 | SVG+CSS | Dropdown (3 Modi) |
| Einflussfaktoren | 6 | CSS+Slider | Gewicht + Rauheit |
| Bremsweg | 10 | CSS-Animation | 3 Buttons (Straßentyp) |
| Rollreibung | 12 | SVG+CSS | Dropdown + Kraft-Slider |
| Reifendruck | 13 | Dynamisches SVG | Druck-Slider |
| ABS | 14 | SVG+CSS | Dropdown + 2 Buttons |
| Memory | 15 | DOM-Grid | 6 Paare, Tap |
