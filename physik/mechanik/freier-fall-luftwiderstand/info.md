---
titel: Freier Fall mit Luftwiderstand
fach: Physik
thema: Mechanik
unterthema: Kinematik und Dynamik
klassenstufe: 10-12
kurzbeschreibung: Interaktive Simulation zum Vergleich von freiem Fall im Vakuum und in Luft. Zeigt Grenzgeschwindigkeit, Kräfteverhältnisse und den Einfluss des Luftwiderstands.
stichworte: freier Fall, Luftwiderstand, Grenzgeschwindigkeit, Fallbeschleunigung, Newton, Kräfte, Vakuum, Fallschirmspringer
---

## Beschreibung

Diese Simulation ermöglicht den direkten Vergleich zwischen dem freien Fall im Vakuum und dem Fall in Luft mit Luftwiderstand. Schülerinnen und Schüler können verschiedene Objekte fallen lassen und beobachten, wie sich Geschwindigkeit, Beschleunigung und die wirkenden Kräfte über die Zeit verändern.

Ein besonderes Feature ist der Fallschirmspringer mit Zweiphasen-Sprung: In der ersten Phase fällt er mit hoher Grenzgeschwindigkeit (~53 m/s), nach der einstellbaren Schirmöffnung reduziert sich diese auf etwa 6 m/s.

## Lernziele

- Die Bewegungsgleichungen des freien Falls im Vakuum verstehen (h(t), v(t), a = const)
- Den Einfluss des Luftwiderstands auf die Fallbewegung erkennen
- Das Konzept der Grenzgeschwindigkeit verstehen (F_L = F_G → a = 0)
- Die Formel für den Luftwiderstand anwenden: F_L = ½ · ρ · c_w · A · v²
- Kräftediagramme interpretieren (F_G, F_L, F_Res)
- Den Zusammenhang zwischen Masse, Querschnittsfläche und Grenzgeschwindigkeit erkennen

## Fachlicher Hintergrund

### Freier Fall im Vakuum
Im Vakuum wirkt nur die Gewichtskraft F_G = m · g. Die Beschleunigung ist konstant:
- a = g (etwa 9,81 m/s² auf der Erde)
- v(t) = v₀ + g · t
- h(t) = h₀ + v₀ · t + ½ · g · t²

### Fall mit Luftwiderstand
In Luft wirkt zusätzlich die Luftwiderstandskraft:
- F_L = ½ · ρ · c_w · A · v²

Die Beschleunigung ist nicht mehr konstant:
- a = g - F_L/m = g - (ρ · c_w · A · v²) / (2m)

### Grenzgeschwindigkeit
Wenn F_L = F_G, wird a = 0. Das Objekt fällt mit konstanter Geschwindigkeit:
- v_gr = √(2mg / (ρ · c_w · A))

Je größer die Masse und je kleiner die Querschnittsfläche, desto höher die Grenzgeschwindigkeit.

## Bedienung

1. **Medium wählen**: Vakuum oder Luft (Umschalter oben)
2. **Parameter einstellen**: Fallhöhe, Anfangsgeschwindigkeit, Planet, Objekt
3. **Simulation starten**: Start-Button oder Einzelschritt für detaillierte Analyse
4. **Beobachten**: Live-Werte, Kraftvektoren (optional) und Diagramme

### Spezielle Funktionen
- **Fallschirmspringer**: Zeigt Zweiphasen-Sprung mit einstellbarer Schirmöffnungshöhe
- **Kraftvektoren**: Visualisierung von F_G, F_L und F_Res
- **Zeitlupe**: Verlangsamte Darstellung für detaillierte Beobachtung
- **Einzelschritt**: Schrittweise Simulation mit 0,1 s Intervallen

## Didaktische Hinweise

### Einstieg (Phänomenologisch)
- Verschiedene Objekte im Vakuum fallen lassen → alle gleich schnell!
- Dann auf "Luft" umschalten → unterschiedliche Geschwindigkeiten

### Erarbeitung
- Kraftvektoren aktivieren und beobachten, wie F_L mit v wächst
- Grenzgeschwindigkeit verschiedener Objekte vergleichen
- Einfluss von Masse und Querschnittsfläche diskutieren

### Vertiefung
- Fallschirmspringer: Warum öffnet man den Schirm nicht sofort?
- Mathematische Herleitung der Grenzgeschwindigkeit
- Vergleich mit realen Daten (z.B. Felix Baumgartner)

## Physikalische Grundwerte

| Objekt | Masse | c_w | A | v_gr (Luft) |
|--------|-------|-----|---|-------------|
| Tennisball | 0,15 kg | 0,47 | 0,0038 m² | ~37 m/s |
| Apfel | 0,18 kg | 0,50 | 0,0030 m² | ~44 m/s |
| Stein | 0,50 kg | 0,80 | 0,0020 m² | ~72 m/s |
| Springer (Freifall) | 80 kg | 0,9 | 0,5 m² | ~54 m/s |
| Springer (Schirm) | 80 kg | 1,4 | 35 m² | ~5 m/s |
| Feder | 0,003 kg | 1,2 | 0,0015 m² | ~5 m/s |

Die Werte sind so gewählt, dass sie physikalisch plausible Grenzgeschwindigkeiten ergeben. Die tatsächlichen Werte in der Realität können je nach Objektform und -größe variieren.

## Bezug zum Rahmenplan MV

**Klasse 10E/Sek II - Mechanik:**
- Gleichförmige und gleichmäßig beschleunigte Bewegung
- Newtonsche Axiome und Kräftegleichgewicht
- Anwendung der Kinematik auf reale Bewegungen

**Kompetenzbereich Erkenntnisgewinnung:**
- Nutzen von Simulationen zur Untersuchung physikalischer Phänomene
- Auswerten von Diagrammen und Messdaten
