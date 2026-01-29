# ARBEITSPFAD UE 06: Reibung Vertiefung – ABS, Haftreibungsgrenze, Anwendungen

> **Fach:** Physik
> **Klasse:** 7 (Sek I gemischt)
> **Dauer:** 45 min (Einzelstunde) oder 90 min (Doppelstunde)
> **Voraussetzung:** UE 05 Reibungskräfte (phänomenologisch)
> **Ziel:** Alle SuS abholen, quantitative Vertiefung, technische Anwendungen

---

## 1. Lernziele

### 1.1 Feinziele

| # | Lernziel | AFB | Niveau |
|---|----------|-----|--------|
| FZ1 | SuS wenden die Formel F_R = μ · F_N auf einfache Beispiele an | II | ★★ |
| FZ2 | SuS erklären die Haftreibungsgrenze als kritischen Punkt | II | ★★ |
| FZ3 | SuS beschreiben die Funktion des ABS anhand der Haftreibungsgrenze | II/III | ★★/★★★ |
| FZ4 | SuS vergleichen Rollreibung bei Gummi/Asphalt vs. Stahl/Stahl | II | ★★ |
| FZ5 | SuS berechnen Reibungskräfte mit verschiedenen μ-Werten | III | ★★★ |

### 1.2 Kompetenzerwartungen (RP MV)

- **Fachwissen:** Zusammenhang zwischen Reibungskraft, Normalkraft und Reibungszahl
- **Erkenntnisgewinnung:** Aus Simulationen Gesetzmäßigkeiten ableiten
- **Kommunikation:** Fachsprache (Haftreibungsgrenze, ABS) verwenden
- **Bewertung:** Technische Anwendungen der Physik erkennen

---

## 2. Didaktische Struktur

### 2.1 Epistemischer Aufbau

```
┌─────────────────────────────────────────────────────────────────┐
│ Phase 1: AKTIVIEREN (5 min)                                     │
│ → Wiederholung der drei Reibungsarten                           │
│ → Gemeinsamer Start: Alle auf gleichem Stand                    │
├─────────────────────────────────────────────────────────────────┤
│ Phase 2: ERKUNDEN – Haftreibungsgrenze (10 min)                 │
│ → Simulation: Kraft erhöhen bis zum "Abreißen"                  │
│ → Erkenntnis: Es gibt einen kritischen Punkt                    │
├─────────────────────────────────────────────────────────────────┤
│ Phase 3: ANWENDEN – ABS-Funktion (10 min)                       │
│ → Animation: Blockierte vs. geregelte Bremsung                  │
│ → Erkenntnis: ABS hält Rad knapp unter Haftreibungsgrenze       │
├─────────────────────────────────────────────────────────────────┤
│ Phase 4: VERGLEICHEN – Reifen vs. Eisenbahn (8 min)             │
│ → Simulation: Rollreibung bei verschiedenen Materialpaarungen   │
│ → Erkenntnis: Stahl/Stahl = geringe Rollreibung = energieeffizient │
├─────────────────────────────────────────────────────────────────┤
│ Phase 5: BERECHNEN – Formelanwendung (10 min)                   │
│ → Geführte Rechnungen mit Simulation                            │
│ → Differenzierung: ★★ Einsetzen, ★★★ Umstellen                  │
├─────────────────────────────────────────────────────────────────┤
│ Phase 6: SICHERN (2 min)                                        │
│ → AB abgeben, Zusammenfassung                                   │
└─────────────────────────────────────────────────────────────────┘
```

### 2.2 Zentrale Erkenntnisse

1. **Haftreibungsgrenze:** Es gibt einen maximalen Kraftwert – darüber "reißt" die Haftreibung ab und wird zu (schwächerer) Gleitreibung
2. **ABS-Prinzip:** Das Rad knapp unter der Haftreibungsgrenze halten = maximale Bremskraft ohne Blockieren
3. **Rollreibung-Vergleich:** Stahl/Stahl (Eisenbahn) hat viel geringere Rollreibung als Gummi/Asphalt → energieeffizienter Transport
4. **Formel:** F_R = μ · F_N gilt für alle Reibungsarten (mit unterschiedlichem μ)

---

## 3. Simulationen & Animationen

### 3.1 Simulation: Haftreibungsgrenze (Schritt 2)

**Konzept:** Slider für Zugkraft, Klotz beginnt bei Überschreitung der Haftreibung zu gleiten

```
┌─────────────────────────────────────────────────────────────────┐
│  Zugkraft: ═══════════○─────── [F = 6.0 N]                      │
│                                                                 │
│      ←F_Zug          ┌───────┐                                  │
│  ●════════════════►  │ KLOTZ │  ◄════════════ F_R →             │
│                      │ 10 N  │                                  │
│                      └───────┘                                  │
│  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  │
│                                                                 │
│  Status: [HAFTEN] ● Haftreibung aktiv                           │
│  F_Haft,max = μ · F_N = 0.8 · 10 N = 8 N                        │
│                                                                 │
│  ┌─────────────────────────────────────────────────┐            │
│  │ ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ │ ← Kraftbalken│
│  │ ███████████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░ │   75% von max│
│  └─────────────────────────────────────────────────┘            │
└─────────────────────────────────────────────────────────────────┘
```

**Verhalten:**
- 0–8 N: Klotz haftet, Balken füllt sich (grün → gelb → rot)
- >8 N: Klotz gleitet los! Status wechselt zu "GLEITEN", Animation startet
- Gleitreibung (μ=0.5) reicht nicht mehr → Klotz beschleunigt

### 3.2 Animation: ABS-Funktion (Schritt 3)

**Konzept:** Split-Screen – links blockiertes Rad, rechts ABS-geregeltes Rad

```
┌───────────────────────────────────────────────────────────────────┐
│  OHNE ABS                    │  MIT ABS                          │
│                              │                                    │
│    🚗→→→→→→→                 │    🚗→→→→→→→                       │
│    ████  ⚫                  │    ████  🔄                        │
│    blockiert                 │    geregelt                        │
│                              │                                    │
│  Rad: ⬛ (steht)             │  Rad: 🔄 (rollt/bremst/rollt...)   │
│  Reibung: Gleitreibung       │  Reibung: Haftreibung (max!)       │
│  μ = 0.5                     │  μ = 0.8                           │
│                              │                                    │
│  F_Brems = 500 N             │  F_Brems = 800 N                   │
│  ████████████░░░░░░░░░░      │  ████████████████████              │
│                              │                                    │
│  Bremsweg: ████████████      │  Bremsweg: ██████                  │
│            [16.0 m]          │            [10.0 m]                │
└───────────────────────────────────────────────────────────────────┘
```

**Animation:**
1. Beide Autos starten mit gleicher Geschwindigkeit
2. Links: Rad blockiert → Gleitreibung → längerer Bremsweg
3. Rechts: ABS regelt → Haftreibung bleibt → kürzerer Bremsweg
4. Zeitlupe zeigt "Pulsieren" des ABS-Rades

### 3.3 Simulation: Rollreibung Vergleich (Schritt 4)

**Konzept:** Zwei Fahrzeuge auf verschiedenen Untergründen

```
┌───────────────────────────────────────────────────────────────────┐
│  ROLLREIBUNG IM VERGLEICH                                         │
│                                                                   │
│  Auto (Gummi/Asphalt):        Zug (Stahl/Stahl):                  │
│                                                                   │
│    🚗═══════◯◯               🚃═══════◯◯◯◯                       │
│    ▓▓▓▓▓▓▓▓▓▓▓▓▓             ═══════════════                      │
│    Asphalt                   Schiene                              │
│                                                                   │
│    μ_Roll = 0.015            μ_Roll = 0.001                       │
│    F_Roll = 150 N            F_Roll = 10 N                        │
│                                                                   │
│  Gleiche Last: 10.000 N                                           │
│                                                                   │
│  Rollwiderstand:             Rollwiderstand:                      │
│  ███████████████████████     ██                                   │
│  [150 N = 100%]              [10 N = 6.7%]                        │
│                                                                   │
│  → Eisenbahn: 15x weniger Rollreibung!                            │
└───────────────────────────────────────────────────────────────────┘
```

### 3.4 Simulation: Rechner (Schritt 5)

**Konzept:** Interaktiver Formelrechner mit Eingabefeldern

```
┌───────────────────────────────────────────────────────────────────┐
│  REIBUNGSKRAFT BERECHNEN                                          │
│                                                                   │
│  Formel: F_R = μ · F_N                                            │
│                                                                   │
│  ┌─────────────────────────────────────────────────────────────┐  │
│  │ Materialpaarung:  [Gummi/Asphalt ▼]  → μ = 0.8              │  │
│  │                                                              │  │
│  │ Normalkraft F_N:  [____500____] N                            │  │
│  │                                                              │  │
│  │                   [ BERECHNEN ]                              │  │
│  │                                                              │  │
│  │ Rechnung:  F_R = 0.8 · 500 N                                 │  │
│  │                                                              │  │
│  │ Ergebnis:  F_R = 400 N                                       │  │
│  └─────────────────────────────────────────────────────────────┘  │
│                                                                   │
│  ★★★ Umstellen: Welche Normalkraft braucht man für F_R = 600 N?   │
│      F_N = F_R / μ = 600 N / 0.8 = [______] N                     │
└───────────────────────────────────────────────────────────────────┘
```

---

## 4. AB-Struktur

### 4.1 Elemente

| ID | Typ | Inhalt | LP-Schritt |
|----|-----|--------|------------|
| K1 | Info | Haftreibungsgrenze | 2 |
| B1 | Beobachtung | Simulation: Wann reißt Haftreibung ab? | 2 |
| K2 | Info | ABS-Funktion | 3 |
| T1 | Tabelle | ABS: Bremsweg-Vergleich | 3 |
| B2 | Beobachtung | Rollreibung Auto vs. Zug | 4 |
| R1 | Rechnung | F_R = μ · F_N (★★) | 5 |
| R2 | Rechnung | Umstellen (★★★) | 5 |

### 4.2 Differenzierung

| Niveau | Pflicht | Inhalt |
|--------|---------|--------|
| ★ (Basis) | K1, K2, B1, B2, T1 | Qualitativ, Beobachten, Zuordnen |
| ★★ (Standard) | + R1 | Formel einsetzen |
| ★★★ (Erweitert) | + R2 | Formel umstellen |

---

## 5. Digitale Diagnostik

### 5.1 Eingebettete Checks im LP

| Schritt | Check | Typ | Kriterium |
|---------|-------|-----|-----------|
| 2 | Haftreibungsgrenze ablesen | Eingabe | ±0.5 N |
| 3 | ABS-Vorteil benennen | MC | Richtige Auswahl |
| 5 | Berechnung F_R | Eingabe | ±5 N |
| 5 | Umstellung F_N (★★★) | Eingabe | ±10 N |

### 5.2 Sofort-Feedback

- Richtig: Grüner Rahmen + "Korrekt!"
- Falsch: Roter Rahmen + Hinweis + erneuter Versuch

---

## 6. Materialien

### 6.1 Zu erstellen

| Datei | Beschreibung | Status |
|-------|--------------|--------|
| LP-06-reibung-vertiefung.html | Lernpfad (6 Schritte) | ⏳ |
| AB-06-reibung-vertiefung.tex | Arbeitsblatt (1 Seite) | ⏳ |
| ML-06-reibung-vertiefung.tex | Musterlösung | ⏳ |
| QR-LP-06-reibung-vertiefung.tex | QR-Code für LP | ⏳ |

### 6.2 Technische Anforderungen

- ES5-JavaScript (var, function)
- localStorage für Fortschritt
- Fachfarbe: #2c5aa0 (Physik)
- Light-Mode Animationen (weißer Hintergrund)
- Responsive (min-width: 320px)

---

## 7. Stundenverlauf (45 min)

| Zeit | Phase | Inhalt | Sozialform | Material |
|------|-------|--------|------------|----------|
| 0-5 | Einstieg | LP Schritt 1: Wiederholung | EA | LP-06, AB |
| 5-15 | Erarbeitung I | LP Schritt 2: Haftreibungsgrenze | EA | LP-06 Simulation |
| 15-25 | Erarbeitung II | LP Schritt 3: ABS-Animation | EA | LP-06 Animation |
| 25-33 | Vergleich | LP Schritt 4: Rollreibung | EA | LP-06 Simulation |
| 33-43 | Übung | LP Schritt 5: Rechnungen | EA | LP-06, AB |
| 43-45 | Sicherung | AB abgeben, Ausblick | Plenum | AB |

---

## 8. Differenzierter Verlauf (90 min Doppelstunde)

| Zeit | Phase | Inhalt | Zusatz für DS |
|------|-------|--------|---------------|
| 0-10 | Einstieg | Wiederholung + Warm-up Quiz | Quiz auf LP |
| 10-25 | Erarbeitung I | Haftreibungsgrenze | + Partnerarbeit |
| 25-40 | Erarbeitung II | ABS-Animation | + Video (real) |
| 40-50 | Pause/Puffer | — | — |
| 50-65 | Vergleich | Rollreibung | + Diskussion |
| 65-85 | Übung | Rechnungen (differenziert) | + ★★★ Zusatzaufgaben |
| 85-90 | Sicherung | AB, Zusammenfassung | |

---

## 9. Erwartete Schwierigkeiten

| Problem | Lösung |
|---------|--------|
| SuS verstehen "Abreißen" nicht | Animation zeigt Übergang deutlich |
| ABS-Funktion zu abstrakt | Split-Screen macht Vergleich sichtbar |
| Formel umstellen schwer (★★★) | Vorgerechnetes Beispiel im LP |
| Unterschied μ_Haft vs μ_Gleit | Farbcodierung: Grün=Haften, Rot=Gleiten |

---

## 10. Checkliste

- [ ] LP-06 erstellt mit 6 Schritten
- [ ] 4 Simulationen/Animationen implementiert
- [ ] AB auf 1 Seite (★/★★/★★★ differenziert)
- [ ] ML erstellt
- [ ] QR-Code generiert
- [ ] Lokaler Test (Chrome, Safari)
- [ ] Responsive Test (Handy)
- [ ] PRUEFPLAN durchlaufen

---

*Erstellt: 2026-01-28*
