# Greenhouse Lernpfade

Digitale Lernpfade, Quizze und Arbeitsblätter für Greenhouse Schools Rostock.

---

## 🚀 Quick Start

```bash
# In Claude Code:
cd /path/to/greenhouse-lernpfade
cat CLAUDE.md  # Lies die Regeln!

# Quiz erstellen:
cp templates/quiz/quiz-template.html projects/physik/mein-quiz/index.html
# → CONFIG und QUESTIONS anpassen
# → Im Browser testen

# Für GitHub Pages deployen
```

---

## 📁 Struktur

```
greenhouse-lernpfade/
├── CLAUDE.md                 ← Master-Instruktion für Claude
├── README.md                 ← Diese Datei
│
├── knowledge/                ← Referenzmaterial (read-only)
│   ├── curriculum/           ← Rahmenpläne MV
│   │   ├── physik-mv-sek1.md
│   │   ├── physik-mv-sek2.md
│   │   ├── chemie-mv.md
│   │   └── informatik-mv.md
│   └── frameworks/           ← Didaktische Regeln
│       ├── differentiation.md
│       └── grading.md
│
├── templates/                ← Wiederverwendbare Vorlagen
│   ├── quiz/
│   │   ├── quiz-template.html
│   │   └── decoder.html
│   ├── learning-path/
│   │   └── lernpfad-template.html
│   └── worksheet-tex/
│       └── arbeitsblatt.tex
│
└── projects/                 ← Echte Inhalte
    ├── physik/
    ├── chemie/
    └── informatik/
```

---

## 🎨 Design System

**sciencesim-konform** = Clean, functional, keine AI-typischen Effekte.

| ✅ Verwenden | ❌ Vermeiden |
|-------------|-------------|
| `border: 1px solid #ddd` | Box-shadows |
| `background: #f5f5f5` | Gradients |
| System-Fonts | Fancy Fonts |
| Dezente Hover-Effekte | Animationen |
| Fachfarben als Akzent | Bunte Buttons |

### Fachfarben

| Fach | Hex | CSS-Variable |
|------|-----|--------------|
| **Physik** | `#2c5aa0` | `--physik` |
| **Chemie** | `#2a7a4b` | `--chemie` |
| **Informatik** | `#b35c00` | `--informatik` |

---

## ★ Differenzierung

| Niveau | Symbol | Zielgruppe |
|--------|--------|------------|
| ★ | `niveau: 1` | Berufsreife (BR) |
| ★★ | `niveau: 2` | Mittlere Reife (MR) |
| ★★★ | `niveau: 3` | Gymnasium (GY) |

---

## 📊 Bewertung

| Klassenstufe | Skala |
|--------------|-------|
| 6-9 | 14-NP |
| 10 MR | 6-Noten |
| 10 GY - 12 | 15-NP |

---

## 🧮 Kopfrechenbar

**IMMER: g = 10 m/s²** (nicht 9,81!)

| Größe | Erlaubte Werte |
|-------|----------------|
| Geschwindigkeiten | 36, 72, 90, 108 km/h |
| Zeiten | 2, 3, 4, 5, 6, 8, 10 s |
| Beschleunigungen | 2, 4, 5, 10 m/s² |

---

## 🔧 Workflow

1. **Template kopieren** → `projects/{fach}/{thema}/`
2. **CONFIG anpassen** (ID, Titel, Fach, Punkte)
3. **QUESTIONS schreiben** (alle Typen möglich)
4. **Im Browser testen**
5. **Git commit**
6. **Deploy auf GitHub Pages**

---

## 📱 Templates

### Quiz (`quiz-template.html`)

- Sitzplatzwahl (P01-P30)
- Timer mit Warnfarben
- 6 Fragetypen
- QR-Code zur Abgabe
- Auto-Bewertung
- Musterlösung nach Unlock

### Lernpfad (`lernpfad-template.html`)

- Interleaved: Content ↔ Exercise
- Fortschrittsanzeige
- Instant Feedback
- Simulation-Einbettung
- localStorage-Speicherung

### Decoder (`decoder.html`)

- QR-Scanner für Lehrkräfte
- Manuelle Code-Eingabe
- Statistik-Übersicht
- CSV/JSON-Export
- Druckansicht

### LaTeX (`arbeitsblatt.tex`)

- Notenspiegel im Kopf
- Sternchen-Differenzierung
- Punkteplatzhalter
- Formelsammlung
- Serifenlose Schrift

---

## 📚 Rahmenpläne

Alle Curricula in `/knowledge/curriculum/`:

- **Physik Sek I**: Kl. 7-10 (Gym/Ges)
- **Physik Sek II**: Q1-Q4 (Abitur)
- **Chemie**: Kl. 7-10 + Sek II
- **Informatik**: Kl. 5-10 + Sek II

---

## 🛡️ Datenschutz (DSGVO)

- **Nur Sitzplatznummern** (P01-P30)
- **Keine Namen** im System
- **localStorage** = lokal auf Gerät
- **QR-Code** = komprimierte Punkte, keine Personendaten

---

## 📖 Dokumentation

| Datei | Inhalt |
|-------|--------|
| `CLAUDE.md` | Alle Regeln für Claude Code |
| `knowledge/frameworks/differentiation.md` | ★-System erklärt |
| `knowledge/frameworks/grading.md` | Notenskalen |
| `knowledge/curriculum/*.md` | Lehrplaninhalte |

---

## 🤝 Beitragen

1. Neues Projekt in `projects/{fach}/{thema}/`
2. Template verwenden
3. `spec.md` mit Lernzielen schreiben
4. Inhalte erstellen
5. Testen
6. Pull Request

---

## 📜 Lizenz

Interne Nutzung für Greenhouse Schools Rostock.

---

*Erstellt mit Claude • sciencesim Design System*
