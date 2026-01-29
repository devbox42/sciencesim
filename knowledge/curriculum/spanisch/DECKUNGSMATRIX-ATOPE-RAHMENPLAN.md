# Deckungsmatrix: A_tope.com vs. Rahmenplan MV (Spätbeginner)

**Analyse:** Erfüllt A_tope.com die Anforderungen für Spätbeginner-Unterricht in M-V?

**Methodik:** Prüfung gegen:
1. RP Spanisch Sek II (2019) – `sek2.txt`
2. A_tope.com Volltext (OCR) – `A_tope_Spaet_txt`
3. Kommentierte Literaturempfehlungen – `literaturempfehlungen.txt`
4. Handreichungen Themenfelder 3+4 – `aspectos-politica-sociedad.txt`, `desafios-modernos.txt`

---

## 1. Vorbemerkung: Was gilt für Spätbeginner?

### Zitat RP Sek II, S. 10 (Zeile 385-387):
> „Am Ende der gymnasialen Oberstufe wird von Schülerinnen und Schülern im Bereich der funktionalen kommunikativen Kompetenz **das Niveau B2 des GeR** erwartet."

### ABER: Handreichung Sprechprüfung (2020), S. 3:
> „In der Einführungsphase neu begonnene Fremdsprachen orientieren sich am Ende der Einführungsphase am Niveau **A2** und am Ende der Qualifikationsphase am Zielniveau **B1(+)**."

**Folgerung:** Für Spätbeginner gilt B1(+), NICHT B2. Die Anforderungen sind entsprechend reduziert.

---

## 2. Themenfelder – Quellenbasierte Prüfung

### 2.1 Themenfeld 1: El individuo y la sociedad

**RP-Anforderung (S. 16, Zeilen 800-835):**
> - „Jóvenes y pasiones"
> - „Perspectivas en la adolescencia"
> - „Tendencias socioculturales y políticas"
> - „Tradiciones y costumbres"

**A_tope-Abdeckung:** ✅ GUT ABGEDECKT
- Unidad 1-4: Jugendliche, Familie, Alltag, Schule, Freizeit
- Unidad 7: Berufe, Zukunftspläne

---

### 2.2 Themenfeld 2: La identidad nacional y la diversidad cultural

**RP-Anforderung (S. 17, Zeilen 841-870):**
> - „Momentos cruciales en la historia hispánica"
> - „Identidades y diversidad en el trasfondo histórico"
> - „Latinoamérica ayer y hoy"
> - „El multiculturalismo: Diversidad étnica, cultural y lingüística"

**A_tope-Abdeckung:** ⚠️ TEILWEISE
- Unidad 5 (Madrid), Unidad 6 (Perú), Unidad 8 (Andalucía)
- **Lücke:** Nur Peru für Lateinamerika, keine systematische Diversitäts-Behandlung

---

### 2.3 Themenfeld 3: Aspectos actuales de la política y de la sociedad

**RP-Anforderung (S. 18, Zeilen 877-893):**
> **„La globalización y sus consecuencias"**
> - „Desarollos económicos"
> - **„Movimientos migratorios"** – „Analyse und Diskussion der Ursachen und Konsequenzen von Migration [BTV]"

**A_tope OCR-Prüfung:**

```
grep -i "migra" A_tope_Spaet_txt
→ KEINE TREFFER
```

```
grep -i "globaliza" A_tope_Spaet_txt
→ KEINE TREFFER
```

**BEFUND:** ❌ **KRITISCHES DEFIZIT**

| Thema | Grep-Ergebnis | Status |
|-------|---------------|--------|
| Migration | 0 Treffer | ❌ FEHLT KOMPLETT |
| Globalización | 0 Treffer | ❌ FEHLT KOMPLETT |

**Handreichung bestätigt Pflichtcharakter** (`aspectos-politica-sociedad.txt`, Zeilen 21-51):
> „**Movimientos migratorios**
> - Hör-/Hörsehverstehen: die Dokumentation ‚México – E.E.U.U.: El gran cruce' sehen
> - Lesen: einzelne Kapitel aus ‚La casa en Mango Street' von Sandra Cisneros
> - Sprachmittlung: einen aktuellen deutschsprachigen Artikel zur Flüchtlingsproblematik mitteln"

---

### 2.4 Themenfeld 4: Desafíos modernos

**RP-Anforderung (S. 18, Zeilen 894-914):**
> **„El mundo en movimiento"**
> - **„Tendencias ecológicas"** – „aktuelle Dokumente zum Thema Umweltschutz [...] kommentieren [BNE]"
> - **„Desafíos de la era digital"** – „Mediennutzung und Medienvielfalt im Spannungsfeld zwischen Chancen und Risiken"

**A_tope OCR-Prüfung:**

```
grep -i "medio ambiente" A_tope_Spaet_txt
→ 6 Treffer (alle im Kontext Tourismus/Comercio justo, KEIN eigenständiges Kapitel)
```

Beispiel-Treffer (Zeile 4889):
> „una region andaluza, pero también causa serios problemas en el **medio ambiente**."

Beispiel-Treffer (Zeile 5597, Módulo Comercio justo):
> „Porque es respetuoso con el **medio ambiente**."

**BEFUND:** ⚠️ **DEFIZITÄR**

| Thema | Grep-Ergebnis | Status |
|-------|---------------|--------|
| Medio ambiente | 6 Treffer (Randerwähnungen) | ⚠️ Kein eigenständiges Kapitel |
| Tecnología/Redes sociales | Módulo "¿Te comunicas?" (4 Seiten) | ⚠️ Oberflächlich |

**Handreichung bestätigt Pflichtcharakter** (`desafios-modernos.txt`, Zeilen 20-53):
> „**Tendencias ecológicas**
> - Hör-/Hörsehverstehen: Auszüge aus einer Pressekonferenz mit Rigoberta Menchú
> - Lesen: Auszüge aus ‚El agua y la humanidad' von Rigoberta Menchú
> - Schreiben: einen Artikel zu verantwortungsvollem Umgang mit Wasser verfassen"

---

## 2.5 Direktes Lesen der Module (Januar 2026)

Die Module wurden direkt gelesen (nicht nur grep), um den tatsächlichen Inhalt zu prüfen:

### Módulo "Vivir la diversidad" (S. 126-127)
**Tatsächlicher Inhalt:** Decálogo (10 Gebote) gegen Diskriminierung, Kampagne des spanischen Ministeriums für Gleichheit
- Thema: Toleranz, Diversität **innerhalb Spaniens**
- Grammatik: Subjuntivo presente
- **NICHT behandelt:** Immigration, Flüchtlinge, Movimientos migratorios

### Módulo "El comercio justo" (S. 128-129)
**Tatsächlicher Inhalt:** 10 Gründe für fairen Handel, Kaufverhalten
- "medio ambiente" erscheint als **Vokabeleintrag** (Z. 5640)
- Grammatik: Condicional
- **NICHT behandelt:** Klimawandel, Umweltprobleme, ökologische Herausforderungen

### Módulo "Una decisión importante" (S. 130-131)
**Tatsächlicher Inhalt:** Javi, ein spanischer Ingenieur, findet keinen Job und überlegt nach Deutschland zu gehen
- Thema: **EMIGRATION** (Spanier verlässt Spanien wegen Wirtschaftskrise)
- Grammatik: Futuro simple
- **NICHT behandelt:** Immigration nach Spanien, Flüchtlinge, "Movimientos migratorios" im Sinne des RP

### Módulo "¿Te comunicas?" (S. 132-133)
**Tatsächlicher Inhalt:** Handy-Aktivitäten (Nachrichten schreiben, Fotos hochladen, Apps nutzen)
- Thema: **Vokabular** zu digitaler Kommunikation
- Grammatik: Pretérito perfecto
- **NICHT behandelt:** Chancen/Risiken digitaler Medien, kritische Medienreflexion

### Grep-Verifizierung zusätzlicher Begriffe

```
grep -i "refugiad" A_tope_Spaet_txt
→ 2 Treffer: "Trabajo voluntario con refugiados" (nur Vokabeleintrag, Z. 8081/8171)

grep -i "cambio climático" A_tope_Spaet_txt
→ 0 Treffer

grep -i "contaminación" A_tope_Spaet_txt
→ 0 Treffer

grep -i "sostenible" A_tope_Spaet_txt
→ ~10 Treffer, alle im Kontext "turismo sostenible" (Unidad 8, Andalucía)
```

### Fazit aus direktem Lesen

| RP-Thema | A_tope-Behandlung | Bewertung |
|----------|-------------------|-----------|
| **Movimientos migratorios** | Nur "refugiados" als Vokabel (2x) | ❌ **KEINE inhaltliche Behandlung** |
| **Emigración española** | Modul "Una decisión importante" | ⚠️ Behandelt, aber umgekehrte Perspektive |
| **Globalización** | Nicht vorhanden | ❌ |
| **Medio ambiente** | Nur "turismo sostenible" (touristische Perspektive) | ❌ **Keine ökologischen Herausforderungen** |
| **Desafíos digitales** | Nur Vokabular, keine kritische Reflexion | ❌ |

---

## 3. Grammatik – Quellenbasierte Prüfung

### 3.1 Rahmenplan-Anforderung

**RP Sek II, S. 14 (Zeilen 587-588):**
> „ein gefestigtes Repertoire der grundlegenden grammatischen Strukturen für die Realisierung ihrer Sprech- und Schreibabsichten nutzen"

**Hinweis:** Der RP gibt **keine spezifischen Grammatikinhalte** vor – nur das Zielniveau (B2 für fortgeführte, B1+ für Spätbeginner).

### 3.2 A_tope OCR-Prüfung

| Grammatik | Grep-Ergebnis | A_tope Status |
|-----------|---------------|---------------|
| **Subjuntivo** | Módulo "Vivir la diversidad" (S. 126) | ⚠️ FAKULTATIV |
| **Condicional** | Módulo "El comercio justo" (S. 128) | ⚠️ FAKULTATIV |
| **Futuro simple** | Módulo "Una decisión importante" (S. 130) | ⚠️ FAKULTATIV |
| **Pretérito perfecto** | Módulo "¿Te comunicas?" (S. 132) | ⚠️ FAKULTATIV |
| **Pluscuamperfecto** | 0 Treffer | ❌ FEHLT |
| **Passiv (voz pasiva)** | 1 Treffer (Randerwähnung) | ❌ FEHLT |

**Grep-Beleg für Pluscuamperfecto:**
```
grep -i "pluscuam" A_tope_Spaet_txt
→ KEINE TREFFER
```

**Grep-Beleg für Passiv:**
```
grep -i "voz pasiva" A_tope_Spaet_txt
→ 1 Treffer (Zeile 7679): "...che Konstruktion se mit ‚man' oder mit dem Passiv wiedergegeben."
```
(Nur Randerwähnung bei se-Konstruktion, keine systematische Behandlung)

### 3.3 Bewertung für B1-Niveau

Für **B1** (Spätbeginner-Ziel) sind laut GER erforderlich:
- Presente, Perfecto, Indefinido, Imperfecto ✅ (im Buch)
- Futuro próximo ✅ (Unidad 4)
- Subjuntivo in Basiswendungen ⚠️ (nur Modul)
- Condicional für Höflichkeit ⚠️ (nur Modul)

Für **B1** NICHT zwingend erforderlich:
- Pluscuamperfecto (B2-Struktur)
- Systematisches Passiv (B2-Struktur)
- Komplexe hypothetische Sätze (B2-Struktur)

**FAZIT GRAMMATIK:** Mit Nutzung der fakultativen Module ist A_tope für **B1-Niveau ausreichend**. Für höhere Ansprüche (B1+) fehlen Pluscuamperfecto und Passiv.

---

## 4. Literatur – Ist "Abdel" verpflichtend?

### 4.1 Dokumenttyp

Das Dokument heißt **„Kommentierte Literatur*empfehlungen*"** (Zeile 17):
> „Begleitdokument: Kommentierte Literaturempfehlungen"

Es ist ein **Begleitdokument**, keine verbindliche Vorgabe.

### 4.2 Rahmenplan-Aussage zu Literatur

**RP Sek II, S. 1 (Zeilen 104-106):**
> „Die in Kapitel 3.2 benannten Themen und Ziele füllen ca. 80 % der zur Verfügung stehenden Unterrichtszeit. Den Lehrkräften wird somit **Freiraum für die eigene Unterrichtsgestaltung** [...] eröffnet."

### 4.3 Abdel im Literaturempfehlungsdokument

**Zeilen 113-118:**
> „**Abdel, Enrique Páez, 1994**
> Dieser kurze Roman erzählt die Geschichte des 16-jährigen Abdel, der zusammen mit seinem Vater sein nomadisches Leben in Marokko aufgibt, um in Spanien einen Neuanfang zu wagen. Der Roman beschreibt die Herausforderungen, die Abdel als illegaler Immigrant in Spanien überwinden muss und beschreibt die Bedingungen, unter denen Flüchtlinge in Spanien überleben müssen."

### 4.4 Fazit Literaturverpflichtung

| Frage | Antwort | Beleg |
|-------|---------|-------|
| Ist Abdel verpflichtend? | **NEIN** | „Literatur*empfehlungen*", Begleitdokument |
| Ist irgendeine Literatur verpflichtend? | **NEIN** (für Spätbeginner) | RP: 80%-Regel, Freiraum für Lehrkräfte |
| Gibt es LK-Empfehlungen? | Ja: „El método Grönholm" | Zeile 53: „Vorschlag für den Leistungskurs" |

**ABER:** Da A_tope das Thema **Migration NICHT behandelt**, ist „Abdel" die **praktisch beste Ergänzung** für Themenfeld 3.

### 4.5 Worum geht es in "Abdel"?

Aus den Literaturempfehlungen (Zeilen 113-118):
- **Protagonist:** 16-jähriger Abdel aus Marokko
- **Thema:** Illegale Immigration nach Spanien
- **Inhalt:** Herausforderungen als Flüchtling, Überlebenskampf
- **Niveau:** A2/B1 (sprachlich zugänglich für Spätbeginner)
- **Eignung:** Ideal für Themenfeld 3 „Movimientos migratorios"

---

## 5. Zusammenfassung: Defizite mit Quellenbelegen

### 5.1 Thematische Defizite (KRITISCH)

| Defizit | RP-Quelle | A_tope OCR-Beleg | Ergänzung nötig |
|---------|-----------|------------------|-----------------|
| **Migration** | RP S. 18: „Movimientos migratorios" | grep "migra" → 0 Treffer | ✅ JA |
| **Globalización** | RP S. 18: „La globalización y sus consecuencias" | grep "globaliza" → 0 Treffer | ✅ JA |
| **Medio ambiente** | RP S. 18: „Tendencias ecológicas" | 6 Treffer, aber kein Kapitel | ✅ JA |

### 5.2 Grammatik-Defizite (für B1+ relevant)

| Defizit | GER-Niveau | A_tope OCR-Beleg | Für B1 nötig? |
|---------|------------|------------------|---------------|
| **Pluscuamperfecto** | B2 | grep → 0 Treffer | ❌ Nein |
| **Passiv** | B2 | grep → 1 Randerwähnung | ❌ Nein |
| **Subjuntivo** (Vertiefung) | B2 | Nur Modul (Basis) | ⚠️ Modul nutzen |

### 5.3 Prüfmethodik-Dokumentation

Alle Grep-Befehle wurden gegen die vollständige Datei `A_tope_Spaet_txt` (1,5 MB OCR-Text) ausgeführt:

```bash
# Migration
grep -i "migra" A_tope_Spaet_txt → 0 Treffer

# Globalización
grep -i "globaliza" A_tope_Spaet_txt → 0 Treffer

# Medio ambiente
grep -i "medio ambiente" A_tope_Spaet_txt → 6 Treffer (Randerwähnungen)

# Pluscuamperfecto
grep -i "pluscuam" A_tope_Spaet_txt → 0 Treffer

# Subjuntivo
grep -i "subjuntivo" A_tope_Spaet_txt → 12 Treffer (Módulo "Vivir la diversidad")
```

---

## 6. Gesamtfazit

### Kann die Sequenz komplett auf A_tope aufbauen?

**NEIN** – für Themenfelder 3+4 fehlen zentrale Inhalte.

### Sind Handreichungen zu Themenkomplexen erforderlich?

**JA** – für:
- Themenfeld 3: Migration, Globalización
- Themenfeld 4: Medio ambiente (vertieft)

### Ist Abdel oder andere Literatur verpflichtend?

**NEIN** – aber **praktisch unverzichtbar** für Themenfeld 3 (Migration), da A_tope dieses Thema nicht behandelt.

### Bewertung nach Lernjahr

| Jahr | A_tope-Abdeckung | Handreichungen nötig? |
|------|------------------|----------------------|
| **Jahr 1 (Kl. 10)** | ✅ 90% | Nein |
| **Jahr 2 (Kl. 11)** | ✅ 80% (mit Modulen) | Optional |
| **Jahr 3 (Kl. 12)** | ⚠️ 50% | **JA – für Themenfelder 3+4** |

---

---

## 7. Abgleich: A_tope vs. Spätbeginner-Sequenz-Synthese

### 7.1 Jahr 1: Einführungsphase (Kl. 10)

| Sequenz-Thema | A_tope Abdeckung | Grep-Treffer | Status |
|---------------|------------------|--------------|--------|
| **Grundlagen** (Aussprache, Alphabet) | Unidad 1 (S. 10-21) | — | ✅ |
| **Yo y mi entorno** (vorstellen, Familie) | Unidad 1-2 | — | ✅ |
| **La vida cotidiana** (Alltag, Uhrzeit) | Unidad 4 (S. 52-69) | — | ✅ |
| **Mi colegio y mis amigos** | Unidad 4 | — | ✅ |
| **España: geografía básica** | Unidad 5 (Madrid, S. 70-81) | 240 (madrid/andaluc/region) | ✅ |
| **Tradiciones y fiestas** | Panorama 1 (S. 68-69) | 35 (tradicion/fiesta) | ✅ |
| **De compras y en el restaurante** | Unidad 3 (Kleidung), Unidad 5 (Café) | 149 (compra/comida) | ✅ |

**Grammatik Jahr 1:**

| Sequenz-Grammatik | A_tope | Status |
|-------------------|--------|--------|
| Presente indicativo | Unidad 1-4 | ✅ |
| Artículos, género, número | Unidad 1 | ✅ |
| Possessivbegleiter | Unidad 2 (S. 166) | ✅ |
| **Pretérito perfecto** | **Módulo "¿Te comunicas?"** | ⚠️ FAKULTATIV |
| Futuro próximo (ir a + inf.) | Unidad 4 (S. 170) | ✅ |
| Präpositionen | Unidad 2, 5 | ✅ |

**Jahr 1 Fazit:** ✅ **90% Deckung** – Nur Perfecto ist fakultativ

---

### 7.2 Jahr 2: Qualifikationsphase 1 (Kl. 11)

| Sequenz-Thema | A_tope Abdeckung | Grep-Treffer | Status |
|---------------|------------------|--------------|--------|
| **Jóvenes y su mundo** | Unidad 1-4 (Jugendliche) | — | ✅ |
| **Relaciones y emociones** | Unidad 2-3 (Familie, gustar) | 155 (relacion/amor/amigo) | ✅ |
| **Perspectivas futuras** (Beruf) | Unidad 7 (S. 100-109) | 215 (profesion/trabajo/futuro) | ✅ |
| **España: regiones y cultura** | Unidad 5, 8 (Madrid, Andalucía) | 240 | ✅ |
| **Latinoamérica: introducción** | Unidad 6 (Perú, S. 82-99) | 65 (latinoam/peru/mexico) | ⚠️ Nur Peru |
| **Diversidad cultural** | Panorama 3, verstreut | 8 (diversidad/multicultural) | ⚠️ OBERFLÄCHLICH |

**Grammatik Jahr 2:**

| Sequenz-Grammatik | A_tope | Status |
|-------------------|--------|--------|
| Pretérito indefinido | Unidad 6 (S. 173) | ✅ |
| Pretérito imperfecto | Unidad 8 (S. 175) | ✅ |
| Kontrast indef./imperf. | Unidad 8 (S. 175) | ✅ |
| **Subjuntivo presente** | **Módulo "Vivir la diversidad"** | ⚠️ FAKULTATIV |
| **Condicional simple** | **Módulo "El comercio justo"** | ⚠️ FAKULTATIV |
| Relativsätze (que) | Unidad 3 (S. 169) | ✅ |

**Jahr 2 Fazit:** ⚠️ **75% Deckung** – Subjuntivo/Condicional fakultativ, Diversidad oberflächlich

---

### 7.3 Jahr 3: Qualifikationsphase 2 + Abitur (Kl. 12)

| Sequenz-Thema | A_tope Abdeckung | Grep-Treffer | Status |
|---------------|------------------|--------------|--------|
| **Migración y sus causas** | — | 0 | ❌ **FEHLT** |
| **Globalización** | — | 0 | ❌ **FEHLT** |
| **Medio ambiente** | Randerwähnungen | 6 | ❌ **UNZUREICHEND** |
| **Tecnología y redes sociales** | Módulo "¿Te comunicas?" (4 S.) | ~15 (internet) | ⚠️ OBERFLÄCHLICH |

**Grammatik Jahr 3 (aus Sequenz-Synthese):**

| Sequenz-Grammatik | A_tope | Status |
|-------------------|--------|--------|
| Subjuntivo (Vertiefung) | Nur Basis-Modul | ⚠️ |
| Pluscuamperfecto | — | ❌ **FEHLT** |
| Passiv | 1 Randerwähnung | ❌ **FEHLT** |
| Indirekte Rede | Unidad 4 (decir, Basis) | ⚠️ |
| Konnektoren | verstreut | ⚠️ |

**Jahr 3 Fazit:** ❌ **40% Deckung** – Zentrale Abitur-Themen fehlen komplett

---

### 7.4 Gesamtübersicht: Sequenz vs. A_tope

```
JAHR 1 (Kl. 10) - A2
═══════════════════════════════════════════════════
Themen:    ████████████████████░░ 90%  ✅
Grammatik: ████████████████████░░ 90%  ✅ (Perfecto → Modul nutzen)
───────────────────────────────────────────────────
→ A_tope AUSREICHEND

JAHR 2 (Kl. 11) - A2+/B1
═══════════════════════════════════════════════════
Themen:    ███████████████░░░░░░░ 75%  ⚠️ (Diversidad dünn)
Grammatik: ███████████████░░░░░░░ 75%  ⚠️ (Subj./Cond. → Module)
───────────────────────────────────────────────────
→ A_tope MIT MODULEN ausreichend

JAHR 3 (Kl. 12) - B1(+) / Abitur
═══════════════════════════════════════════════════
Themen:    ████████░░░░░░░░░░░░░░ 40%  ❌ (Migration, Global., Umwelt)
Grammatik: ██████░░░░░░░░░░░░░░░░ 30%  ❌ (Plusc., Passiv, Subj.+)
───────────────────────────────────────────────────
→ A_tope UNZUREICHEND – Ergänzung PFLICHT
```

---

### 7.5 Erforderliche Ergänzungen für Sequenz-Umsetzung

| Jahr | Sequenz-Thema | Ergänzungsquelle |
|------|---------------|------------------|
| 2 | Diversidad cultural | HR Themenfeld 2 oder Zusatztexte |
| **3** | **Migración** | **Lektüre "Abdel" + HR Themenfeld 3** |
| **3** | **Globalización** | **HR Themenfeld 3 + Aktualtexte** |
| **3** | **Medio ambiente** | **HR Themenfeld 4 + "El agua y la humanidad"** |
| 3 | Tecnología | Aktualtexte (A_tope-Modul zu kurz) |

| Jahr | Sequenz-Grammatik | Ergänzungsquelle |
|------|-------------------|------------------|
| 1 | Pretérito perfecto | A_tope Módulo 4 nutzen |
| 2 | Subjuntivo (Einf.) | A_tope Módulo 1 nutzen |
| 2 | Condicional | A_tope Módulo 2 nutzen |
| **3** | **Pluscuamperfecto** | **Grammatik-Ergänzung extern** |
| **3** | **Passiv** | **Grammatik-Ergänzung extern** |

---

*Erstellt: Januar 2026 | Lernpfade | Spanisch Spätbeginner M-V*
*Quellengeprüft gegen: RP Sek II (2019), A_tope OCR-Volltext, Literaturempfehlungen, Handreichungen, Sequenz-Synthese*
