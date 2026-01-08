# Knowledge: Äußerer lichtelektrischer Effekt (Photoeffekt)

**Quellen:**
- DDR-Lehrbuch Physik Klasse 12 (S. 134-144)
- Folien Quantenphysik

---

## 1. Historischer Kontext

### Lichtmodelle vor 1905

| Modell | Vertreter | Erklärt | Grenzen |
|--------|-----------|---------|---------|
| **Korpuskulartheorie** | Newton | Reflexion, Linsen | Beugung, Interferenz |
| **Wellentheorie** | Huygens | Beugung, Interferenz, Polarisation | Photoeffekt! |

> "Die Experimente zur Interferenz hatten gezeigt, daß das Licht Welleneigenschaften besitzt. In Zusammenhang mit dem äußeren lichtelektrischen Effekt treten jedoch Erscheinungen auf, die mit dem Wellenmodell unvereinbar sind."

---

## 2. Phänomen: Äußerer lichtelektrischer Effekt

### Hallwachs-Versuch (1888)

**Aufbau:**
- Negativ aufgeladene Zinkplatte
- Elektrometer/Elektroskop
- UV-Lampe

**Beobachtungen:**
1. UV-Licht auf negative Zinkplatte → Ladung verringert sich
2. UV-Licht auf positive Zinkplatte → keine Änderung
3. Sichtbares Licht → keine Wirkung (bei Zink)

**Definition:**
> "Kurzwelliges Licht kann aus Metallen Elektronen herauslösen. Man nennt diese Erscheinung den **äußeren lichtelektrischen Effekt**."

---

## 3. Experimentelle Untersuchung (Vakuumfotozelle)

### Aufbau (Bild 135/1)
- Vakuumfotozelle mit Kathode (Metall)
- Lichtquelle (Glühlampe + Farbfilter)
- Strommesser
- Spannungsquelle

### Qualitative Ergebnisse

**Experiment 1:** Glühlampe nähern
- Stromstärke nimmt zu
- → Mehr Elektronen bei mehr Licht

**Experiment 2:** Farbfilter wechseln
| Farbe | Fotostrom? |
|-------|------------|
| violett | ✅ ja |
| blau | ✅ ja |
| grün | ✅ ja |
| gelb | ✅ ja |
| orange | ❌ nein |
| rot | ❌ nein |

**Experiment 3:** Intensität bei rotem Licht erhöhen
- **Kein Fotostrom**, auch bei maximaler Intensität!

### Zentrale Ergebnisse (S. 135)

> "- Der Fotostrom nimmt mit der Beleuchtungsstärke des eingestrahlten Lichtes zu.
> - Nur bei Bestrahlung mit kurzwelligem Licht tritt ein Fotostrom auf. Langwelliges Licht bewirkt selbst bei noch so großer Beleuchtungsstärke keinen Strom."

---

## 4. Widerspruch zum Wellenmodell

### Erwartung nach Wellenmodell
- Amplitude größer → mehr Energie pro Zeiteinheit
- Auch rotes Licht müsste bei genug Intensität Elektronen auslösen

### Beobachtung
- Intensität bei rotem Licht hilft NICHT
- Frequenz ist entscheidend, nicht Intensität

> "Das zweite Ergebnis ist allein auf der Grundlage des Wellenmodells des Lichtes nicht erklärbar."

---

## 5. Energie der Fotoelektronen (Gegenfeldmethode)

### Prinzip (Bild 136/1)
- Elektrisches Gegenfeld bremst Elektronen
- Spannung erhöhen, bis Strom auf 0 geht
- Diese Spannung = **Grenzspannung U_G**

### Energiegleichung

$$\frac{1}{2} m_e \cdot v^2 = e \cdot U$$

**Einheit Elektronenvolt:**
> "Wird ein Elektron mittels einer Spannung von 1 V beschleunigt oder abgebremst, so nimmt seine kinetische Energie um ein Elektronenvolt zu oder ab."

$$1 \text{ Ws} = 1 \text{ V} \cdot 1 \text{ As} = 6{,}24 \cdot 10^{18} \text{ eV}$$

---

## 6. Messreihe (Tabelle 137/1)

| Lichtfarbe | Frequenz f in 10¹⁴ s⁻¹ | Gegenspannung U in V |
|------------|------------------------|----------------------|
| violett | 7,4 | 1,00 |
| blau | 6,5 | 0,85 |
| grünblau | 6,1 | 0,56 |
| grün | 5,5 | 0,26 |
| gelb | 4,9 | 0,10 |

### Erkenntnisse aus der Messreihe (S. 138)

> "- Mit zunehmender Beleuchtungsstärke nimmt die Anzahl der je Zeiteinheit ausgelösten Fotoelektronen zu.
> - Die kinetische Energie der einzelnen Fotoelektronen ist von der Beleuchtungsstärke unabhängig.
> - Die Energie der Fotoelektronen wächst linear mit der Frequenz des eingestrahlten Lichtes."

### Grenzfrequenz

> "Die Gerade schneidet die Abszissenachse bei etwa 4·10¹⁴ Hz. Wird die Fotozelle mit Licht dieser Frequenz bestrahlt, so besitzen die Elektronen die kinetische Energie 0."

Diese Frequenz heißt **Grenzfrequenz f_G**.

---

## 7. Lichtquanten (Einstein 1905)

### Einsteins Hypothese

> "Das Licht besteht aus einzelnen, nicht weiter zerlegbaren 'Energieportionen', den **Lichtquanten** oder **Photonen**."

### Photonenenergie

$$E = h \cdot f \tag{103}$$

### Plancksches Wirkungsquantum

$$\boxed{h = 6{,}6256 \cdot 10^{-34} \text{ W·s}^2}$$

(Moderne Notation: h = 6,626·10⁻³⁴ J·s)

---

## 8. Austrittsarbeit und Einsteinsche Gleichung

### Austrittsarbeit W_A

> "Zum Herauslösen des Elektrons aus dem Metall ist eine bestimmte Arbeit W_A erforderlich, die man **Austrittsarbeit** nennt."

### Fallunterscheidung

| Bedingung | Ergebnis |
|-----------|----------|
| h·f < W_A | Kein Photoeffekt |
| h·f = W_A | Grenzfrequenz (E_kin = 0) |
| h·f > W_A | Photoeffekt mit E_kin > 0 |

### Grenzfrequenz

$$h \cdot f_G = W_A \tag{105}$$

### Einsteinsche Gleichung (Photogleichung)

$$\boxed{h \cdot f = \frac{1}{2} m_e \cdot v^2 + W_A} \tag{108}$$

Oder mit Gegenspannung:

$$h \cdot f = e \cdot U_G + W_A$$

---

## 9. Bestimmung des Planckschen Wirkungsquantums

### Zwei-Frequenzen-Methode (S. 141)

Mit zwei verschiedenen Frequenzen f₁ und f₂:

$$h \cdot f_1 = e \cdot U_1 + W_A \tag{109}$$
$$h \cdot f_2 = e \cdot U_2 + W_A \tag{110}$$

Subtraktion ergibt:

$$\boxed{h = e \cdot \frac{U_1 - U_2}{f_1 - f_2}} \tag{111}$$

### Beispielrechnung (S. 141-142)

**Gegeben:**
- λ₁ = 405 nm (violette Hg-Linie) → f₁ = 7,41·10¹⁴ s⁻¹, U₁ = 1,07 V
- λ₂ = 546 nm (grüne Hg-Linie) → f₂ = 5,49·10¹⁴ s⁻¹, U₂ = 0,28 V

**Lösung:**
$$h = 1{,}602 \cdot 10^{-19} \text{ As} \cdot \frac{0{,}79 \text{ V}}{1{,}92 \cdot 10^{14} \text{ s}^{-1}}$$

$$h = 6{,}6 \cdot 10^{-34} \text{ W·s}^2$$

---

## 10. Einsteinsche Gerade (Bild 142/1)

### Grafische Darstellung

```
E_kin (eV)
    │
  3 ┤
    │           /
  2 ┤         /
    │       /
  1 ┤     / ← Steigung = h/e
    │   /
  0 ┼─/────────────────→ f (10¹⁴ Hz)
    │ ↑      4     6     8
    │ f_G
```

### Interpretation

| Element | Physikalische Bedeutung |
|---------|------------------------|
| **Steigung** | h (Plancksches Wirkungsquantum) |
| **x-Achsenabschnitt** | f_G (Grenzfrequenz, materialabhängig) |
| **y-Achsenabschnitt** | -W_A/e (negative Austrittsarbeit) |

> "Die Gerade ist Ausdruck der linearen Beziehung zwischen kinetischer Energie und Frequenz in der Einsteinschen Gleichung. Sie wird deshalb auch **Einsteinsche Gerade** genannt."

---

## 11. Zusammenfassung (S. 144)

### Zentrale Aussagen

1. **Licht besteht aus einzelnen, nicht weiter zerlegbaren Lichtquanten.**

2. **Die Energie eines Lichtquants beträgt E = h·f.**

3. **Beim äußeren lichtelektrischen Effekt tritt ein Lichtquant nur mit einem Elektron in Wechselwirkung und gibt an dieses seine gesamte Energie ab.**

4. **Es gilt die Einsteinsche Gleichung:**
   $$h \cdot f = \frac{1}{2} m_e \cdot v^2 + W_A$$

5. **Der äußere lichtelektrische Effekt gestattet die Bestimmung der Austrittsarbeit der Elektronen.** Sie ist von Stoff zu Stoff verschieden.

6. **Der äußere lichtelektrische Effekt ermöglicht die Bestimmung des Planckschen Wirkungsquantums**, eine für die gesamte Mikrophysik bedeutsame Konstante. Sie ist gleich dem Anstieg der Einsteinschen Geraden im Energie-Frequenz-Diagramm.

---

## 12. Welle-Teilchen-Dualismus

> "Weder das Wellenmodell noch das Teilchenmodell allein sind geeignet, um die vielfältigen Erscheinungen des Lichtes vollständig zu beschreiben."

> "A. Einstein hat mit der Einführung des Begriffes 'Lichtquant' eine Synthese geschaffen, die es gestattet, die experimentellen Ergebnisse zu deuten. Das Lichtquant besitzt nur ganz bestimmte Wellen- und ganz bestimmte Teilcheneigenschaften."

---

## Anhang: Messwerte für Aufgaben

### Aus Folien (Tab. 1)

| λ in nm | f in 10¹⁴ Hz | E_kin,max in eV |
|---------|--------------|-----------------|
| 444 | 6,75 | 0,66 |
| 480 | 6,25 | 0,44 |
| 523 | 5,73 | 0,25 |
| 605 | 4,96 | — |
| 640 | 4,68 | — |

**Aufgaben (aus Folien):**
a) Skizziere Versuchsanordnung (7 BE)
b) Erkläre warum bei 605/640 nm kein PE (6 BE)
c) Zeichne f-E_kin-Diagramm, erkläre Schnittpunkte (6 BE)
d) Ermittle h aus Diagramm (5 BE)
e) Berechne Photostromstärke bei 523 nm, 2,0 mW, 0,010% Quantenausbeute (6 BE)

---

## Konstanten

| Konstante | Symbol | Wert |
|-----------|--------|------|
| Plancksches Wirkungsquantum | h | 6,626·10⁻³⁴ J·s |
| Elementarladung | e | 1,602·10⁻¹⁹ C |
| Elektronenmasse | m_e | 9,109·10⁻³¹ kg |
| Lichtgeschwindigkeit | c | 2,998·10⁸ m/s |

**Praktisch:** h = 4,136·10⁻¹⁵ eV·s

---

## Austrittsarbeiten (Tabelle)

| Metall | W_A in eV |
|--------|-----------|
| Natrium | 2,3 |
| Kalium | 2,3 |
| Calcium | 2,9 |
| Zink | 4,3 |
| Kupfer | 4,7 |
| Silber | 4,7 |
| Platin | 5,3 |

---

*Stand: 08.01.2026*
