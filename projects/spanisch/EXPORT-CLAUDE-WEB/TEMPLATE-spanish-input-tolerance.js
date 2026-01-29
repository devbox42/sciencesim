/**
 * Spanish Input Tolerance Utility
 * ================================
 *
 * Dieses Modul ermöglicht tolerante Eingabeprüfung für Spanisch-Übungen,
 * da Schüler deutsche Tastaturen verwenden und keine einfachen Zugang zu
 * spanischen Sonderzeichen haben.
 *
 * VERWENDUNG:
 * 1. Script einbinden: <script src="spanish-input-tolerance.js"></script>
 * 2. Vergleich: if (spanishMatch(userInput, correctAnswer)) { ... }
 *
 * TOLERIERT:
 * - ñ ↔ n (tilde)
 * - á, é, í, ó, ú ↔ a, e, i, o, u (Akzente)
 * - ü ↔ u (Umlaut im Spanischen, z.B. "vergüenza")
 * - ¿ und ¡ am Satzanfang optional
 * - Groß-/Kleinschreibung
 * - Führende/nachfolgende Leerzeichen
 *
 * BEISPIELE:
 * spanishMatch("Cómo estás", "como estas") → true
 * spanishMatch("espanol", "español") → true
 * spanishMatch("Que tal", "¿Qué tal?") → true
 * spanishMatch("manana", "mañana") → true
 */

const SpanishTolerance = {
    /**
     * Normalisiert spanischen Text für toleranten Vergleich
     * @param {string} text - Eingabetext
     * @returns {string} - Normalisierter Text
     */
    normalize: function(text) {
        if (!text) return '';

        return text
            // Zu Kleinbuchstaben
            .toLowerCase()
            // Leerzeichen trimmen
            .trim()
            // Führende spanische Satzzeichen entfernen
            .replace(/^[¿¡]+/, '')
            // Nachfolgende Satzzeichen entfernen
            .replace(/[?!.]+$/, '')
            // Akzente normalisieren
            .normalize('NFD')
            .replace(/[\u0300-\u036f]/g, '')
            // ñ separat behandeln (wird durch NFD zu n + combining tilde)
            // Nach NFD-Normalisierung ist ñ bereits zu n geworden
            // Mehrfache Leerzeichen zu einem
            .replace(/\s+/g, ' ')
            .trim();
    },

    /**
     * Prüft ob zwei spanische Texte übereinstimmen (tolerant)
     * @param {string} userInput - Schülereingabe
     * @param {string} correct - Korrekte Antwort
     * @returns {boolean} - true wenn Match
     */
    match: function(userInput, correct) {
        return this.normalize(userInput) === this.normalize(correct);
    },

    /**
     * Prüft ob Eingabe einer von mehreren korrekten Antworten entspricht
     * @param {string} userInput - Schülereingabe
     * @param {string[]} acceptedAnswers - Array korrekter Antworten
     * @returns {boolean} - true wenn Match mit einer Antwort
     */
    matchAny: function(userInput, acceptedAnswers) {
        const normalizedInput = this.normalize(userInput);
        return acceptedAnswers.some(answer =>
            this.normalize(answer) === normalizedInput
        );
    },

    /**
     * Gibt Feedback zur Eingabe
     * @param {string} userInput - Schülereingabe
     * @param {string} correct - Korrekte Antwort
     * @returns {object} - {correct: boolean, feedback: string, correctedVersion: string}
     */
    checkWithFeedback: function(userInput, correct) {
        const isCorrect = this.match(userInput, correct);

        if (isCorrect) {
            // Prüfen ob Akzente fehlen
            const hasAccentDifference = userInput.toLowerCase().trim() !== correct.toLowerCase().trim();

            return {
                correct: true,
                feedback: hasAccentDifference
                    ? '¡Correcto! (Tipp: Die korrekte Schreibweise ist: ' + correct + ')'
                    : '¡Muy bien!',
                correctedVersion: correct
            };
        }

        return {
            correct: false,
            feedback: 'Nicht ganz. Die richtige Antwort ist: ' + correct,
            correctedVersion: correct
        };
    },

    /**
     * Erstellt eine Liste aller akzeptierten Varianten einer Antwort
     * Nützlich für Dokumentation oder erweiterte Prüfung
     * @param {string} correct - Korrekte Antwort
     * @returns {string[]} - Alle akzeptierten Varianten
     */
    generateAcceptedVariants: function(correct) {
        const variants = new Set();
        variants.add(correct);
        variants.add(correct.toLowerCase());
        variants.add(this.normalize(correct));

        // Version ohne führende ¿¡
        const withoutLeading = correct.replace(/^[¿¡]+\s*/, '');
        variants.add(withoutLeading);
        variants.add(withoutLeading.toLowerCase());

        // Version ohne Akzente
        const withoutAccents = correct
            .normalize('NFD')
            .replace(/[\u0300-\u036f]/g, '');
        variants.add(withoutAccents);
        variants.add(withoutAccents.toLowerCase());

        return Array.from(variants);
    }
};

// Shorthand-Funktionen für einfache Verwendung
function spanishMatch(input, correct) {
    return SpanishTolerance.match(input, correct);
}

function spanishMatchAny(input, acceptedAnswers) {
    return SpanishTolerance.matchAny(input, acceptedAnswers);
}

function spanishNormalize(text) {
    return SpanishTolerance.normalize(text);
}

// Export für Module (Node.js / ES6)
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { SpanishTolerance, spanishMatch, spanishMatchAny, spanishNormalize };
}

/*
 * INTEGRATION IN QUIZ-HTML:
 *
 * <script src="../../../templates/spanisch/spanish-input-tolerance.js"></script>
 * <script>
 *     function checkAnswer(inputId, correctAnswer) {
 *         const userInput = document.getElementById(inputId).value;
 *         const result = SpanishTolerance.checkWithFeedback(userInput, correctAnswer);
 *
 *         if (result.correct) {
 *             showSuccess(result.feedback);
 *         } else {
 *             showError(result.feedback);
 *         }
 *     }
 * </script>
 *
 * BEISPIEL FÜR LÜCKENTEXT:
 *
 * <input type="text" id="gap1" placeholder="...">
 * <button onclick="checkAnswer('gap1', '¿Cómo te llamas?')">Prüfen</button>
 *
 * Akzeptiert: "como te llamas", "Cómo te llamas", "¿Cómo te llamas?" etc.
 */
