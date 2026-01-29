# KOMPAKT-Planung: 01b Mechanische Energie

## Rahmenplan-Bezug
RP RS/GES 2021, Kl. 10: Energie – Energiegewinnung

## Lernziele (Feinziele)

| FZ | AFB | Inhalt |
|----|-----|--------|
| FZ1 | I | SuS nennen die Definition von Energie |
| FZ2 | I | SuS geben die Formel E_pot = m·g·h an |
| FZ3 | I | SuS geben die Formel E_kin = ½mv² an |
| FZ4 | II | SuS berechnen E_pot und E_kin |
| FZ5 | II | SuS wenden den Energieerhaltungssatz an |
| FZ6 | II | SuS zeichnen Energieflussdiagramme |
| FZ7 | III | SuS erklären Energieumwandlungen (ideal + real) |
| FZ8 | III | SuS berechnen v aus h bzw. h aus v (Transfer) |

## Änderungen gegenüber v1

### 1. Einstieg: "Was hat das mit mir zu tun?"
- **Neu:** Motivations-Einstieg mit Alltagsbezug
- Beispiele: Fahrrad bergab, Achterbahn, Skifahren, Auto abbremsen
- Kernfrage: "Woher kommt die Geschwindigkeit beim Fallen?"

### 2. Erweiterte Aufgaben (AB)
- **Aufgabe 4a (★★★):** Auto mit E_kin → wie hoch kann es rollen?
  - Gegeben: m = 1000 kg, v = 36 km/h (= 10 m/s)
  - E_kin = ½·1000·100 = 50.000 J
  - h = E_kin / (m·g) = 50.000 / 10.000 = 5 m
  - Hinweis: "Probiere verschiedene Werte für h!"

- **Aufgabe 4b (★★★):** Körper fällt aus h → wie schnell vor Aufprall?
  - Gegeben: m = 2 kg, h = 5 m
  - E_pot = 2·10·5 = 100 J = E_kin
  - 100 = ½·2·v² → v² = 100 → v = 10 m/s
  - Hinweis: "Tipp: Berechne zuerst E_pot!"

### 3. Simulationen (Bugfixes + Neu)

**Bugfixes:**
- Ball-Aspect-Ratio: `arc()` mit gleichem Radius für x und y
- Beschleunigungsbug: `cancelAnimationFrame()` vor neuem Start

**Neue Simulationen:**
- **Rampen-Simulation:** Ball rollt Rampe hoch/runter
  - Energiebalken zeigen E_pot ↔ E_kin
  - Slider für Starthöhe

- **Reales Verhalten:**
  - Toggle "Ideal/Real" bei Fall-Simulation
  - Bei "Real": Teil der Energie → Wärme (grauer Balken)
  - Energieflussdiagramm: E_pot → E_kin + E_Wärme

### 4. Beobachtungsexperimente
- **Experiment 1:** Ball prellt nicht auf Ausgangshöhe zurück
- **Experiment 2:** Auto kommt auf Gegenhang nicht gleich hoch
- Erklärung: Energieverlust durch Reibung/Verformung → Wärme

### 5. Entfernen
- MT-Verweis am Ende des LP (Schritt 9)

## Arbeitspfad (optimiert)

| LP-Schritt | Zeit | AB-Element | Aktion |
|------------|------|------------|--------|
| 1: Was hat das mit mir zu tun? | 0–5' | – | Motivation |
| 2: Was ist Energie? | 5–10' | Kasten 1 | Übertragen |
| 3: E_pot einführen | 10–17' | Kasten 2 | Übertragen |
| 4: Sim Lageenergie + Übung | 17–25' | Aufgabe 1a | Bearbeiten |
| 5: E_kin einführen | 25–32' | Kasten 3 | Übertragen |
| 6: Sim Bewegungsenergie + Übung | 32–40' | Aufgabe 1b | Bearbeiten |
| 7: Erhaltungssatz | 40–45' | Kasten 4 | Übertragen |
| 8: Sim Rampe + Energieumwandlung | 45–52' | Aufgabe 2 | Bearbeiten |
| 9: Reales Verhalten (Reibung) | 52–58' | Aufgabe 3 | Bearbeiten |
| 10: Erweiterte Aufgaben | 58–68' | Aufgabe 4 | Bearbeiten (★★★) |
| 11: Zusammenfassung | 68–70' | – | AB-Check |

## Material-Übersicht

| Datei | Änderungen |
|-------|------------|
| LP-01b-energie.html | +Einstieg, +Rampen-Sim, +Real-Toggle, Bugfixes, -MT-Verweis |
| AB-01b-energie.tex | +Aufgabe 4 (Transfer: v aus h, h aus v) |
| ML-01b-energie.tex | +Lösungen Aufgabe 4 |
| LH-01b-energie.tex | +FZ8, Zeitplan anpassen |

## Notizen
- g = 10 m/s² (immer!)
- ES5 JavaScript (var, function)
- Fachfarbe: #2c5aa0
- Niemals MT im LP erwähnen!
