#!/usr/bin/env python3
"""
PowerPoint Generator: Repaso La ropa y los adjetivos
Klasse 8 - 45 Minuten Einzelstunde
"""

import sys
sys.path.insert(0, '/Users/jpc/claudecode/sciencesim-lernpfade/templates/spanisch')

from spanisch_pptx_generator import SpanischPPTX, PRIMARY, SUCCESS, WARNING, DARK_TEXT, MEDIUM_TEXT
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN

# Anpassung für Klasse 8
class SpanischPPTX8(SpanischPPTX):
    def _header_footer(self, slide):
        from pptx.dml.color import RGBColor
        # Header
        self._rect(slide, 0, 0, 13.333, 0.5, PRIMARY)
        self._text(slide, f"Spanisch Klasse 8 · {self.lesson_id}", 0.3, 0.1, 4, 0.3,
                   size=14, bold=True, color=RGBColor(0xff, 0xff, 0xff))
        # Footer
        self._rect(slide, 0, 7.2, 13.333, 0.3, RGBColor(0xf5, 0xf5, 0xf5))
        self._text(slide, self.title, 0.3, 7.22, 5, 0.25, size=10, color=MEDIUM_TEXT)
        self._text(slide, "Unidad 5 · Repaso", 10, 7.22, 3, 0.25,
                   size=10, color=MEDIUM_TEXT, align=PP_ALIGN.RIGHT)

    def add_title_slide(self, flags="🇪🇸"):
        from pptx.dml.color import RGBColor
        slide = self._slide()
        self._rect(slide, 0, 0, 13.333, 4.5, PRIMARY)
        self._text(slide, self.title, 0.5, 1.5, 12.33, 1.2, size=56, bold=True, color=RGBColor(0xff,0xff,0xff))
        if self.subtitle:
            self._text(slide, self.subtitle, 0.5, 2.8, 12.33, 0.6, size=24, color=RGBColor(0xff,0xcc,0xcc))
        self._text(slide, "Unidad 5 · Repaso · 45 Min", 0.5, 3.6, 12.33, 0.5,
                   size=14, color=RGBColor(0xee,0xaa,0xaa))
        self._text(slide, "Spanisch Klasse 8", 0.5, 5.5, 6, 0.5, size=20, bold=True, color=PRIMARY)
        if flags:
            self._text(slide, flags, 0.5, 6.2, 12.33, 0.8, size=36)
        return slide


def main():
    pptx = SpanischPPTX8(
        lesson_id="Repaso-Ropa",
        title="La ropa y los adjetivos",
        subtitle="Kleidung beschreiben mit Adjektiven",
        sequenz=5
    )

    # 1. Titelfolie
    pptx.add_title_slide()

    # 2. Lernziele
    pptx.add_content_slide(
        "🎯 Hoy aprendemos...",
        [
            "• Kleidungsvokabeln wiederholen (la ropa)",
            "• Adjektive zur Beschreibung verwenden",
            "• Genus-Anpassung: -o/-a und -e",
            "• Kleidung mündlich beschreiben",
            "",
            "📝 Material: LB + AB"
        ]
    )

    # 3. Vokabeln Teil 1
    pptx.add_vocab_slide(
        "La ropa (1/2)",
        [
            ("la camiseta", "das T-Shirt"),
            ("la camisa", "das Hemd"),
            ("el jersey", "der Pullover"),
            ("la sudadera", "der Kapuzenpulli"),
            ("los pantalones", "die Hose"),
            ("el vestido", "das Kleid"),
        ],
        subtitle="Kleidungsstücke · Wiederholung",
        ab_ref="→ LB Abschnitt 1"
    )

    # 4. Vokabeln Teil 2
    pptx.add_vocab_slide(
        "La ropa (2/2)",
        [
            ("la falda", "der Rock"),
            ("la chaqueta", "die Jacke"),
            ("el abrigo", "der Mantel"),
            ("los zapatos", "die Schuhe"),
            ("las botas", "die Stiefel"),
            ("las zapatillas", "die Turnschuhe"),
        ],
        ab_ref="→ AB Aufgabe 1"
    )

    # 5. Adjektive Teil 1
    pptx.add_vocab_slide(
        "Los adjetivos (1/2)",
        [
            ("bonito/a", "hübsch"),
            ("moderno/a", "modern"),
            ("cómodo/a", "bequem"),
            ("elegante", "elegant"),
            ("deportivo/a", "sportlich"),
        ],
        subtitle="Adjektive zur Beschreibung",
        ab_ref="→ LB Abschnitt 2"
    )

    # 6. Adjektive Teil 2
    pptx.add_vocab_slide(
        "Los adjetivos (2/2)",
        [
            ("largo/a", "lang"),
            ("corto/a", "kurz"),
            ("ancho/a", "weit"),
            ("estrecho/a", "eng"),
            ("sencillo/a", "schlicht"),
        ],
        ab_ref="→ LB Abschnitt 2"
    )

    # 7. Grammatik
    pptx.add_grammar_slide(
        "Adjektive anpassen",
        [
            ("Regel 1: -o/-a", "passt sich an!"),
            ("el jersey bonito / la camiseta bonita", "mask. -o / fem. -a"),
            ("Regel 2: -e", "bleibt gleich!"),
            ("el vestido elegante / la falda elegante", "(keine Änderung)"),
        ],
        info="Merksatz: Das Adjektiv ist der Schatten des Nomens!"
    )

    # 8. Übung
    pptx.add_exercise_slide(
        "Ergänze das Adjektiv",
        [
            ("La camiseta es muy ___.", "(cómodo)"),
            ("El vestido es muy ___.", "(elegante)"),
            ("Los pantalones son muy ___.", "(moderno)"),
            ("La falda es demasiado ___.", "(corto)"),
        ],
        options="Achte auf die Endung!",
        ab_ref="→ AB Aufgabe 2"
    )

    # 9. Lösung
    pptx.add_solution_slide(
        "Lösung",
        [
            ("La camiseta es muy", "cómoda"),
            ("El vestido es muy", "elegante"),
            ("Los pantalones son muy", "modernos"),
            ("La falda es demasiado", "corta"),
        ]
    )

    # 10. Redemittel
    pptx.add_content_slide(
        "💬 Über Kleidung sprechen",
        [
            "Beschreiben:  El/La ... es muy ...  ·  Llevo un/una ...",
            "",
            "Bewerten:  Me gusta el/la ... porque es ...",
            "                El/La ... es demasiado caro/a.",
        ],
        ab_ref="→ LB Abschnitt 4 · AB Aufgabe 3"
    )

    # 11. Partnerübung
    pptx.add_content_slide(
        "👥 Partnerübung (5 Min)",
        [
            "Beschreibe deinem Partner 2-3 Kleidungsstücke!",
            "",
            "A: Hoy llevo una camiseta blanca. Es muy cómoda.",
            "B: Yo llevo un jersey azul. Es moderno y bonito.",
        ]
    )

    # 12. Zusammenfassung
    pptx.add_summary_slide(
        "Zusammenfassung",
        left_items=[
            "la camiseta, el jersey",
            "los pantalones, el vestido",
            "la falda, la chaqueta",
            "los zapatos, las botas",
        ],
        right_items=[
            "-o/-a: passt sich an",
            "-e: bleibt gleich",
            "Plural: -os/-as",
        ],
        left_title="La ropa",
        right_title="Adjektive"
    )

    # 13. Abschluss
    pptx.add_homework_slide(
        [
            "Vokabeln wiederholen (Kleidung + Adjektive)",
            "AB fertigstellen (falls nicht geschafft)",
            "Optional: Eigenes Outfit beschreiben (3 Sätze)",
        ],
        closing="¡Muy bien! ¡Hasta luego!"
    )

    # Speichern
    output_path = "/Users/jpc/claudecode/sciencesim-lernpfade/projects/spanisch/kl08/unidad5-repaso-ropa/PPT-05-repaso-ropa.pptx"
    count = pptx.save(output_path)
    print(f"✓ PPT erstellt: {output_path}")
    print(f"  {count} Folien")


if __name__ == "__main__":
    main()
