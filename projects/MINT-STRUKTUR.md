# MINT-Materialien: Ordnerstruktur

> **Stand:** 2026-01-12
> **Ziel:** iCloud/MINT-Materialien/

Diese Datei dokumentiert die Rahmenplan-basierte Ordnerstruktur für die Publikation von MINT-Unterrichtsmaterialien.

---

## Workflow

**Publish nur auf Anfrage!** Claude fragt immer:
> "Wohin soll [Material X] kopiert werden?
> Vorschlag: `Physik/Klasse-08/02-Stromkreise/`"

**Skript:** `./publish-mint.sh` (manueller Aufruf mit Zielpfad)

---

## Physik (Rahmenplan MV)

### Klasse 6 (Orientierungsstufe, ~30 USt)

| Nr | Ordner | Rahmenplan-Thema | USt |
|----|--------|------------------|-----|
| 01 | `01-Materie` | Körper und Teilchen | ~6 |
| 02 | `02-Bewegungen` | Geradlinige, gleichförmige Bewegung | ~4 |
| 03 | `03-Licht` | Wechselwirkung Licht | ~9 |
| 04 | `04-Temperatur` | Temperatur und Temperaturveränderungen | ~5 |
| 05 | `05-Stromkreise` | Stromkreise und Schaltungen | ~6 |

**Quellordner → Ziel:**
- `kl06/01-bewegungsarten` → `Klasse-06/02-Bewegungen/`
- `kl06/02-bewegung` → `Klasse-06/02-Bewegungen/`

---

### Klasse 7 (~60 USt)

| Nr | Ordner | Rahmenplan-Thema | USt |
|----|--------|------------------|-----|
| 01 | `01-Dichte` | Materie – Dichte | ~8 |
| 02 | `02-Kraefte` | Wechselwirkung – Kräfte | ~18 |
| 03 | `03-Energie` | Arbeit, Leistung, Wirkungsgrad | ~20 |
| 04 | `04-Kraftumformung` | Kraftumformende Einrichtungen | ~8 |
| — | *(Reserve)* | Kontext: Baustellenphysik | ~6 |

**Hinweis:** Baustellenphysik wird implizit in 03-Energie und 04-Kraftumformung behandelt (Hubarbeit, Rampen, Flaschenzüge). Als eigenständiges Thema nur bei Zeitreserve.

**Quellordner → Ziel:**
- `kl07/01-dichte` → `Klasse-07/01-Dichte/`
- `kl7/kraft` → `Klasse-07/02-Kraefte/`

---

### Klasse 8 (~60 USt)

| Nr | Ordner | Rahmenplan-Thema | USt |
|----|--------|------------------|-----|
| 01 | `01-Ladung` | Materie – Elektrische Ladung | ~10 |
| 02 | `02-Stromkreise` | System – Stromkreise (Ohmsches Gesetz) | ~12 |
| 03 | `03-Waerme` | Energie – Temperatur und Wärme | ~24 |
| 04 | `04-Licht` | Wechselwirkung – Licht (Optik) | ~10 |

**Quellordner → Ziel:**
- `kl8-ladung` → `Klasse-08/01-Ladung/`
- `kl8-ohm` → `Klasse-08/02-Stromkreise/`

---

### Klasse 9 (~30 USt)

| Nr | Ordner | Rahmenplan-Thema | USt |
|----|--------|------------------|-----|
| 01 | `01-Magnetismus` | Wechselwirkung – Magnetismus | ~8 |
| 02 | `02-Motor-Induktion` | Energie – Motor und Induktion | ~8 |
| 03 | `03-Bewegungen` | Bewegungen – Gleichförmig | ~6 |
| — | *(Kontext)* | Mit dem E-Bike unterwegs | ~8 |

**Quellordner → Ziel:**
- `kl9E/magnetismus` → `Klasse-09-E/01-Magnetismus/`
- `kl09/motor-induktion` → `Klasse-09/02-Motor-Induktion/`

---

### Klasse 10 (~60 USt)

| Nr | Ordner | Rahmenplan-Thema | USt |
|----|--------|------------------|-----|
| 01 | `01-Bewegungslehre` | Gleichmäßig beschleunigte Bewegung | ~18 |
| 02 | `02-Impuls-Kraft` | Impuls und Kraft, Newton'sche Axiome | ~12 |
| 03 | `03-Schwingungen` | Mechanische Schwingungen | ~12 |
| 04 | `04-Wellen` | Mechanische Wellen | ~10 |
| 05 | `05-Kernphysik` | Atom- und Kernphysik | ~8 |

**Impuls im RP Gym Kl. 10:**
- p = m · v
- Impulserhaltung
- F = Δp/Δt
- Newton'sche Axiome

**Quellordner → Ziel:**
- `kl10/06-bewegungslehre` → `Klasse-10/01-Bewegungslehre/`
- `kl10/05-kernphysik` → `Klasse-10/05-Kernphysik/`

---

### Klasse 12 GK (Qualifikationsphase)

| Nr | Ordner | Thema |
|----|--------|-------|
| 01 | `01-Photoeffekt` | Quantenphysik – Photoeffekt |

**Quellordner → Ziel:**
- `kl12-GK/01-photoeffekt` → `Klasse-12-GK/01-Photoeffekt/`

---

## Kurs-Kürzel

| Quellordner | Bedeutung | Zielordner |
|-------------|-----------|------------|
| `kl9E` | Klasse 9 E-Kurs (Gymnasium) | `Klasse-09-E/` |
| `kl10-MR` | Klasse 10 Mittlere Reife | `Klasse-10-MR/` |
| `10E_Gym` | Klasse 10 E-Kurs Gymnasium | `Klasse-10E-Gym/` |
| `kl12-GK` | Klasse 12 Grundkurs | `Klasse-12-GK/` |

---

## Chemie (Rahmenplan MV)

*Struktur noch zu ergänzen*

### Klasse 8

| Nr | Ordner | Rahmenplan-Thema |
|----|--------|------------------|
| 01 | `01-Reaktionsgleichungen` | Chemische Reaktionen |

---

## Informatik (Rahmenplan MV)

*Struktur noch zu ergänzen*

---

## Änderungshistorie

| Datum | Änderung |
|-------|----------|
| 2026-01-12 | Initiale Struktur Physik nach Rahmenplan MV |
