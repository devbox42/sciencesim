---
titel: Caesar-Chiffre – Codierscheibe
fach: Informatik
thema: Codierung
unterthema: Verschlüsselung
klassenstufe: 7
kurzbeschreibung: Interaktive Codierscheibe für die Caesar-Verschlüsselung – digitale Alternative zur Papiervorlage.
stichworte: Caesar, Chiffre, Verschlüsselung, Kryptographie, Codierung, Geheimschrift, Codierscheibe
---

## Beschreibung

Diese Simulation bietet eine interaktive digitale Codierscheibe für die Caesar-Verschlüsselung. Schülerinnen und Schüler können:

- Den inneren Ring per Drag & Drop oder Schieberegler drehen
- Texte in Echtzeit ver- und entschlüsseln
- Die vollständige Buchstaben-Zuordnung in einer Tabelle ablesen
- Zwischen Verschlüsselungs- und Entschlüsselungsmodus wechseln

Die Simulation ist eine Alternative zur klassischen Papier-Codierscheibe und kann parallel oder ergänzend im Unterricht eingesetzt werden.

## Lernziele

- Das Prinzip der monoalphabetischen Substitution verstehen
- Die Caesar-Verschlüsselung praktisch anwenden können
- Den Begriff „Schlüssel" im Kontext der Verschlüsselung kennen
- Die Schwächen einfacher Verschlüsselungsverfahren erkennen (Brute-Force)
- Mathematische Grundlagen der Verschiebechiffre verstehen (Modulo-Rechnung)

## Fachlicher Hintergrund

Die Caesar-Chiffre ist eines der ältesten bekannten Verschlüsselungsverfahren. Sie wurde nach dem römischen Feldherrn Gaius Julius Caesar benannt, der sie laut dem Historiker Sueton für seine militärische Korrespondenz verwendete.

### Funktionsweise

Bei der Caesar-Chiffre wird jeder Buchstabe des Klartextes um eine feste Anzahl von Positionen im Alphabet verschoben. Der Schlüssel ist die Anzahl der Verschiebungen.

**Formel:**
- Verschlüsselung: C = (P + K) mod 26
- Entschlüsselung: P = (C - K) mod 26

Wobei:
- P = Position des Klartextbuchstabens (A=0, B=1, ..., Z=25)
- C = Position des Geheimtextbuchstabens
- K = Schlüssel (Verschiebung)

### Sicherheitsanalyse

Die Caesar-Chiffre ist extrem unsicher, da:
1. Es nur 25 sinnvolle Schlüssel gibt (Verschiebung 0 = keine Verschlüsselung)
2. Ein Angreifer alle Möglichkeiten in Sekunden durchprobieren kann (Brute-Force)
3. Häufigkeitsanalysen die Entschlüsselung ermöglichen

## Bedienung

1. **Verschiebung einstellen:** Schieberegler ziehen oder +/- Buttons klicken
2. **Ring drehen:** Den roten inneren Ring mit der Maus oder per Touch ziehen
3. **Schlüssel ablesen:** Der Schlüssel ist der rote Buchstabe unter dem grünen Pfeil
4. **Modus wählen:** „Verschlüsseln" oder „Entschlüsseln" auswählen
5. **Text eingeben:** Im Textfeld den zu wandelnden Text eintippen
6. **Ergebnis:** Der umgewandelte Text erscheint automatisch im rechten Feld

## Gestaltung der Codierscheibe

Die digitale Codierscheibe orientiert sich an klassischen Papiervorlagen:

- **Äußerer Ring (blau):** Klartext-Alphabet
- **Innerer Ring (rot):** Geheimschrift-Alphabet  
- **Leitlinien:** Kleine Striche zwischen den Buchstaben zur besseren Zuordnung
- **Schlüsselmarkierung:** Grüner Pfeil zeigt auf den aktuellen Schlüsselbuchstaben
- **Zentrum:** Beschriftung mit Hinweis zur Schlüsselablesung

## Unterrichtshinweise

### Einstieg (10 min)
- Historische Einführung: Julius Caesar und geheime Militärbotschaften
- Problem: Wie kann man Nachrichten sicher übermitteln?

### Erarbeitung (20 min)
- Schüler erkunden die Codierscheibe (erst Papier, dann digital)
- Partner-Arbeit: Geheime Nachrichten austauschen

### Vertiefung (10 min)
- „Knack den Code": Verschlüsselte Nachricht ohne Schlüssel entschlüsseln
- Diskussion: Warum ist die Caesar-Chiffre unsicher?

### Sicherung (5 min)
- Begriffe: Klartext, Geheimtext, Schlüssel, Verschlüsselung, Entschlüsselung
