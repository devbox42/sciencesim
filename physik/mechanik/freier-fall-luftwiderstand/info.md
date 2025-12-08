---
titel: Freier Fall mit Luftwiderstand
fach: Physik
thema: Mechanik
unterthema: Kinematik und Dynamik
klassenstufe: 10-12
kurzbeschreibung: Interaktive Simulation zum Vergleich von freiem Fall im Vakuum und in Luft. Zeigt Grenzgeschwindigkeit, Kräfteverhältnisse und den Einfluss des Luftwiderstands.
stichworte: freier Fall, Luftwiderstand, Grenzgeschwindigkeit, Fallbeschleunigung, Newton, Kräfte, Vakuum, Fallschirmspringer
materialien:
  - datei: arbeitsblatt-einfuehrung.html
    titel: Arbeitsblatt
    beschreibung: Beobachtungsaufgaben und Berechnungen zum freien Fall
  - datei: unterrichtshinweise.html
    titel: Unterrichtshinweise
    beschreibung: Verlaufsvorschlag, Lösungen und didaktische Hinweise
  - datei: tafelbild.html
    titel: Tafelbild
    beschreibung: Druckbares Tafelbild (A4 quer)
---

## Beschreibung

Diese Simulation ermöglicht den direkten Vergleich zwischen dem freien Fall im Vakuum und dem Fall in Luft mit Luftwiderstand. Verschiedene Objekte können fallen gelassen werden, wobei Geschwindigkeit, Beschleunigung und die wirkenden Kräfte in Echtzeit dargestellt werden.

Ein besonderes Feature ist der Fallschirmspringer mit Zweiphasen-Sprung: In der ersten Phase fällt er mit hoher Grenzgeschwindigkeit (~54 m/s), nach der einstellbaren Schirmöffnung reduziert sich diese auf etwa 5 m/s.

## Lernziele

- Die Bewegungsgleichungen des freien Falls im Vakuum verstehen
- Den Einfluss des Luftwiderstands auf die Fallbewegung erkennen
- Das Konzept der Grenzgeschwindigkeit verstehen (Kräftegleichgewicht)
- Die Formel für den Luftwiderstand anwenden: F_L = ½·ρ·c_w·A·v²
- Kräftediagramme interpretieren (F_G, F_L, F_Res)

## Fachlicher Hintergrund

### Freier Fall im Vakuum

Im Vakuum wirkt nur die Gewichtskraft F_G = m·g. Die Beschleunigung ist konstant:
- a = g
- v(t) = g·t
- h(t) = h₀ − ½gt²

### Fall mit Luftwiderstand

In Luft wirkt zusätzlich die Luftwiderstandskraft:
- F_L = ½·ρ·c_w·A·v²

Die Beschleunigung nimmt mit steigender Geschwindigkeit ab.

### Grenzgeschwindigkeit

Bei Kräftegleichgewicht (F_L = F_G) wird a = 0:
- v_gr = √(2mg / ρ·c_w·A)

## Bedienung

1. **Medium wählen**: Vakuum oder Luft
2. **Parameter einstellen**: Fallhöhe, Anfangsgeschwindigkeit, Planet, Objekt
3. **Simulation starten**: Start-Button oder Einzelschritt
4. **Beobachten**: Live-Werte, Kraftvektoren und Diagramme

### Funktionen

- Kraftvektoren: Visualisierung von F_G, F_L und F_Res
- Zeitlupe: Verlangsamte Darstellung
- Einzelschritt: Schrittweise Simulation (0,1 s)
- Fallschirmspringer: Zweiphasen-Sprung mit einstellbarer Schirmöffnungshöhe

## Physikalische Werte der Objekte

| Objekt | Masse | c_w | A | v_gr (Luft) |
|--------|-------|-----|---|-------------|
| Tennisball | 0,15 kg | 0,47 | 0,0038 m² | ~37 m/s |
| Apfel | 0,18 kg | 0,50 | 0,0030 m² | ~44 m/s |
| Stein | 0,50 kg | 0,80 | 0,0020 m² | ~72 m/s |
| Springer (Freifall) | 80 kg | 0,9 | 0,5 m² | ~54 m/s |
| Springer (Schirm) | 80 kg | 1,4 | 35 m² | ~5 m/s |
| Feder | 0,003 kg | 1,2 | 0,0015 m² | ~5 m/s |
