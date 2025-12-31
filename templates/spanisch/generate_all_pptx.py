#!/usr/bin/env python3
"""
Batch-Generator für alle Spanisch Klasse 7 PowerPoints
Verwendet: spanisch_pptx_generator.py (ohne Repair-Warnungen)
"""

import os
import sys

script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, script_dir)

from spanisch_pptx_generator import SpanischPPTX

# ============================================================================
# LESSON-DATEN für alle 32 Lektionen
# ============================================================================

LESSONS = {
    # SEQUENZ 1: ¡Empezamos!
    '01a': {'title': '¡Hola!', 'subtitle': 'Begrüßung auf Spanisch', 'sequenz': 1,
            'slides': [
                ('title', {}),
                ('map', {'title': 'Wo spricht man Spanisch?', 'subtitle': '21 Länder, 480 Mio. Sprecher', 'image_path': 'img/hispanophone-world.png'}),
                ('vocab', {'title': 'Begrüßen', 'vocab': [('¡Hola!', 'Hallo!'), ('Buenos días', 'Guten Morgen'), ('Buenas tardes', 'Guten Tag'), ('Buenas noches', 'Guten Abend')], 'ab_ref': 'AB-01a: Kasten 1'}),
                ('vocab', {'title': 'Verabschieden', 'vocab': [('¡Adiós!', 'Tschüss!'), ('¡Hasta luego!', 'Bis später!'), ('¡Hasta mañana!', 'Bis morgen!')], 'ab_ref': 'AB-01a: Kasten 2'}),
                ('grammar', {'title': 'Grammatik', 'blocks': [('Buenos días', '← maskulin'), ('Buenas tardes', '← feminin')], 'info': '¡...! und ¿...? am Anfang UND Ende'}),
                ('exercise', {'title': 'Zuordnung', 'exercises': [('1. ¡Hola!', '___'), ('2. Buenos días', '___'), ('3. ¡Hasta mañana!', '___')], 'ab_ref': 'AB-01a: Aufgabe 1'}),
                ('solution', {'title': 'Lösung', 'solutions': [('¡Hola!', 'Hallo!'), ('Buenos días', 'Guten Morgen'), ('¡Hasta mañana!', 'Bis morgen!')]}),
                ('homework', {'tasks': ['AB-01a ausfüllen', 'Vokabeln lernen']}),
            ]},
    '01b': {'title': '¿Cómo te llamas?', 'subtitle': 'Sich vorstellen', 'sequenz': 1,
            'slides': [
                ('title', {}),
                ('vocab', {'title': 'Vorstellung', 'vocab': [('Me llamo...', 'Ich heiße...'), ('Soy...', 'Ich bin...'), ('Soy de...', 'Ich komme aus...')], 'ab_ref': 'AB-01b: Kasten 1'}),
                ('grammar', {'title': 'Das Verb ser', 'blocks': [('yo soy', 'ich bin'), ('tú eres', 'du bist'), ('él/ella es', 'er/sie ist')]}),
                ('vocab', {'title': 'Länder', 'vocab': [('España → español/a', 'Spanien'), ('Alemania → alemán/a', 'Deutschland'), ('México → mexicano/a', 'Mexiko')], 'ab_ref': 'AB-01b: Kasten 2'}),
                ('exercise', {'title': 'Ergänze ser', 'exercises': [('Yo ___ María.', '(soy)'), ('Tú ___ de Rostock.', '(eres)')], 'ab_ref': 'AB-01b: Aufgabe 2'}),
                ('homework', {'tasks': ['ser-Formen lernen', 'Steckbrief schreiben']}),
            ]},
    '01c': {'title': 'El alfabeto', 'subtitle': 'Artikel und Alphabet', 'sequenz': 1,
            'slides': [
                ('title', {}),
                ('grammar', {'title': 'Bestimmte Artikel', 'blocks': [('el chico', 'der Junge'), ('la chica', 'das Mädchen'), ('los/las', 'Plural')]}),
                ('grammar', {'title': 'Unbestimmte Artikel', 'blocks': [('un libro', 'ein Buch'), ('una mesa', 'ein Tisch')]}),
                ('content', {'title': 'Das spanische Alphabet', 'items': ['Besondere Buchstaben: ñ, ll, ch']}),
                ('exercise', {'title': 'Artikel ergänzen', 'exercises': [('___ profesor', '(el)'), ('___ profesora', '(la)')], 'ab_ref': 'AB-01c: Aufgabe 2'}),
                ('homework', {'tasks': ['Artikel lernen', 'Alphabet üben']}),
            ]},
    '01d': {'title': '¿Qué tal?', 'subtitle': 'Minitest Sequenz 1', 'sequenz': 1,
            'slides': [
                ('title', {}),
                ('content', {'title': 'Testübersicht', 'items': ['Teil 1: Begrüßung (8P)', 'Teil 2: ser (6P)', 'Teil 3: Artikel (6P)']}),
                ('summary', {'title': 'Wiederholung', 'left_items': ['Begrüßungen', 'Verabschiedungen'], 'right_items': ['ser', 'el/la/los/las']}),
                ('homework', {'tasks': ['Alle Vokabeln', 'ser üben'], 'closing': '¡Buena suerte!'}),
            ]},

    # SEQUENZ 2: La familia
    '02a': {'title': 'La familia', 'subtitle': 'Familienmitglieder', 'sequenz': 2,
            'slides': [
                ('title', {'flags': '👨‍👩‍👧‍👦'}),
                ('vocab', {'title': 'Kernfamilie', 'vocab': [('el padre / la madre', 'Vater / Mutter'), ('el hijo / la hija', 'Sohn / Tochter'), ('el hermano / la hermana', 'Bruder / Schwester')], 'ab_ref': 'AB-02a: Kasten 1'}),
                ('vocab', {'title': 'Erweiterte Familie', 'vocab': [('el abuelo / la abuela', 'Opa / Oma'), ('el tío / la tía', 'Onkel / Tante'), ('el primo / la prima', 'Cousin / Cousine')], 'ab_ref': 'AB-02a: Kasten 2'}),
                ('grammar', {'title': 'Plural', 'blocks': [('padre → padres', '+es'), ('hermana → hermanas', '+s')]}),
                ('exercise', {'title': 'Zuordnung', 'exercises': [('el abuelo', '___'), ('la hermana', '___')], 'ab_ref': 'AB-02a: Aufgabe 1'}),
                ('homework', {'tasks': ['Familienvokabeln lernen', 'Stammbaum zeichnen']}),
            ]},
    '02b': {'title': 'Tengo 12 años', 'subtitle': 'tener und Alter', 'sequenz': 2,
            'slides': [
                ('title', {}),
                ('grammar', {'title': 'Das Verb tener', 'blocks': [('yo tengo', 'ich habe'), ('tú tienes', 'du hast'), ('él/ella tiene', 'er/sie hat')]}),
                ('vocab', {'title': 'Zahlen 1–20', 'vocab': [('uno–cinco', '1–5'), ('seis–diez', '6–10'), ('once–quince', '11–15')], 'ab_ref': 'AB-02b: Kasten 2'}),
                ('grammar', {'title': 'Alter angeben', 'blocks': [('¿Cuántos años tienes?', 'Wie alt bist du?'), ('Tengo doce años.', 'Ich bin 12.')], 'info': 'Im Spanischen "hat" man Jahre!'}),
                ('exercise', {'title': 'Ergänze tener', 'exercises': [('Yo ___ 13 años.', '(tengo)'), ('Mi hermano ___ 10 años.', '(tiene)')], 'ab_ref': 'AB-02b: Aufgabe 2'}),
                ('homework', {'tasks': ['tener lernen', 'Zahlen 1–20']}),
            ]},
    '02c': {'title': 'Mi familia', 'subtitle': 'Possessivbegleiter', 'sequenz': 2,
            'slides': [
                ('title', {}),
                ('grammar', {'title': 'Possessivbegleiter Sg.', 'blocks': [('mi padre', 'mein Vater'), ('tu madre', 'deine Mutter'), ('su hermano', 'sein Bruder')]}),
                ('grammar', {'title': 'Possessivbegleiter Pl.', 'blocks': [('mis padres', 'meine Eltern'), ('tus hermanos', 'deine Geschwister')], 'info': 'mi→mis, tu→tus, su→sus vor Plural'}),
                ('exercise', {'title': 'Ergänze', 'exercises': [('___ hermana (ich)', 'mi'), ('___ padres (du)', 'tus')], 'ab_ref': 'AB-02c: Aufgabe 2'}),
                ('homework', {'tasks': ['Possessivbegleiter lernen', 'Familie beschreiben']}),
            ]},
    '02d': {'title': 'Test: La familia', 'subtitle': 'Minitest Sequenz 2', 'sequenz': 2,
            'slides': [
                ('title', {}),
                ('summary', {'title': 'Wiederholung', 'left_items': ['Familienmitglieder', 'Zahlen 1–20'], 'right_items': ['tener', 'mi/tu/su']}),
                ('homework', {'tasks': ['Alle Vokabeln', 'tener + Possessiv'], 'closing': '¡Buena suerte!'}),
            ]},

    # SEQUENZ 3: La casa
    '03a': {'title': 'La casa', 'subtitle': 'Räume im Haus', 'sequenz': 3,
            'slides': [
                ('title', {'flags': '🏠'}),
                ('vocab', {'title': 'Räume', 'vocab': [('la cocina', 'Küche'), ('el salón', 'Wohnzimmer'), ('el dormitorio', 'Schlafzimmer'), ('el baño', 'Bad')], 'ab_ref': 'AB-03a: Kasten 1'}),
                ('exercise', {'title': 'Räume benennen', 'exercises': [('Hier schläft man:', '___'), ('Hier kocht man:', '___')], 'ab_ref': 'AB-03a: Aufgabe 1'}),
                ('homework', {'tasks': ['Räume-Vokabeln lernen']}),
            ]},
    '03b': {'title': 'Hay una mesa', 'subtitle': 'hay + Möbel', 'sequenz': 3,
            'slides': [
                ('title', {}),
                ('grammar', {'title': 'hay = es gibt', 'blocks': [('Hay una mesa.', 'Es gibt einen Tisch.'), ('Hay dos sillas.', 'Es gibt zwei Stühle.')], 'info': 'hay ist unveränderlich!'}),
                ('vocab', {'title': 'Möbel', 'vocab': [('la mesa', 'Tisch'), ('la silla', 'Stuhl'), ('el sofá', 'Sofa'), ('la cama', 'Bett')], 'ab_ref': 'AB-03b: Kasten 1'}),
                ('exercise', {'title': 'Beschreibe', 'exercises': [('En mi dormitorio hay...', '___')], 'ab_ref': 'AB-03b: Aufgabe 2'}),
                ('homework', {'tasks': ['Möbelvokabeln', 'hay-Sätze']}),
            ]},
    '03c': {'title': 'Los colores', 'subtitle': 'Farben', 'sequenz': 3,
            'slides': [
                ('title', {'flags': '🔴🟢🔵'}),
                ('vocab', {'title': 'Farben', 'vocab': [('rojo/a', 'rot'), ('azul', 'blau'), ('verde', 'grün'), ('amarillo/a', 'gelb')], 'ab_ref': 'AB-03c: Kasten 1'}),
                ('grammar', {'title': 'Adjektiv-Angleichung', 'blocks': [('el sofá rojo', 'das rote Sofa'), ('la silla roja', 'der rote Stuhl')], 'info': '-o/-a passt sich an'}),
                ('exercise', {'title': 'Farben', 'exercises': [('La mesa es ___.', '(blanca)')], 'ab_ref': 'AB-03c: Aufgabe 2'}),
                ('homework', {'tasks': ['Farben lernen', 'Zimmer beschreiben']}),
            ]},
    '03d': {'title': 'Test: La casa', 'subtitle': 'Minitest Sequenz 3', 'sequenz': 3,
            'slides': [
                ('title', {}),
                ('summary', {'title': 'Wiederholung', 'left_items': ['Räume', 'Möbel', 'Farben'], 'right_items': ['hay', 'Adjektive -o/-a']}),
                ('homework', {'tasks': ['Alle Vokabeln', 'hay-Sätze'], 'closing': '¡Buena suerte!'}),
            ]},

    # SEQUENZ 4: El colegio
    '04a': {'title': 'Las asignaturas', 'subtitle': 'Schulfächer', 'sequenz': 4,
            'slides': [
                ('title', {'flags': '📚'}),
                ('vocab', {'title': 'Schulfächer', 'vocab': [('las matemáticas', 'Mathe'), ('el español', 'Spanisch'), ('el inglés', 'Englisch'), ('la música', 'Musik')], 'ab_ref': 'AB-04a: Kasten 1'}),
                ('vocab', {'title': 'Weitere Fächer', 'vocab': [('la historia', 'Geschichte'), ('el arte', 'Kunst'), ('el deporte', 'Sport')], 'ab_ref': 'AB-04a: Kasten 2'}),
                ('grammar', {'title': 'Lieblingsfach', 'blocks': [('Mi asignatura favorita es...', 'Mein Lieblingsfach ist...')]}),
                ('homework', {'tasks': ['Schulfächer lernen']}),
            ]},
    '04b': {'title': 'El horario', 'subtitle': 'Stundenplan und Uhrzeiten', 'sequenz': 4,
            'slides': [
                ('title', {'flags': '⏰'}),
                ('vocab', {'title': 'Wochentage', 'vocab': [('lunes, martes, miércoles', 'Mo, Di, Mi'), ('jueves, viernes', 'Do, Fr')], 'ab_ref': 'AB-04b: Kasten 1'}),
                ('grammar', {'title': 'Uhrzeiten', 'blocks': [('¿Qué hora es?', 'Wie spät?'), ('Es la una.', 'Es ist 1 Uhr.'), ('Son las dos.', 'Es ist 2 Uhr.')], 'info': 'la una (Sg.) aber las dos (Pl.)'}),
                ('exercise', {'title': 'Stundenplan', 'exercises': [('Lunes a las 8:00:', '___')], 'ab_ref': 'AB-04b: Aufgabe 2'}),
                ('homework', {'tasks': ['Wochentage', 'Uhrzeiten']}),
            ]},
    '04c': {'title': 'Verbos en -ar', 'subtitle': 'Regelmäßige Verben', 'sequenz': 4,
            'slides': [
                ('title', {}),
                ('grammar', {'title': 'hablar (sprechen)', 'blocks': [('yo hablo', 'ich spreche'), ('tú hablas', 'du sprichst'), ('él/ella habla', 'er/sie spricht')]}),
                ('vocab', {'title': '-ar-Verben', 'vocab': [('estudiar', 'lernen'), ('escuchar', 'hören'), ('trabajar', 'arbeiten')], 'ab_ref': 'AB-04c: Kasten 1'}),
                ('exercise', {'title': 'Konjugiere', 'exercises': [('Yo ___ español. (estudiar)', '(estudio)')], 'ab_ref': 'AB-04c: Aufgabe 2'}),
                ('homework', {'tasks': ['-ar-Endungen lernen']}),
            ]},
    '04d': {'title': 'Test: El colegio', 'subtitle': 'Minitest Sequenz 4', 'sequenz': 4,
            'slides': [
                ('title', {}),
                ('summary', {'title': 'Wiederholung', 'left_items': ['Schulfächer', 'Wochentage'], 'right_items': ['-ar-Verben', 'Uhrzeiten']}),
                ('homework', {'tasks': ['Alle Vokabeln', '-ar-Konjugation'], 'closing': '¡Buena suerte!'}),
            ]},

    # SEQUENZ 5: Tiempo libre
    '05a': {'title': 'Los hobbys', 'subtitle': 'Freizeitaktivitäten', 'sequenz': 5,
            'slides': [
                ('title', {'flags': '⚽🎸🎮'}),
                ('vocab', {'title': 'Hobbys', 'vocab': [('jugar al fútbol', 'Fußball spielen'), ('tocar la guitarra', 'Gitarre spielen'), ('ver la tele', 'fernsehen'), ('leer libros', 'Bücher lesen')], 'ab_ref': 'AB-05a: Kasten 1'}),
                ('exercise', {'title': 'Zuordnen', 'exercises': [('⚽', 'jugar al fútbol'), ('🎸', 'tocar la guitarra')], 'ab_ref': 'AB-05a: Aufgabe 1'}),
                ('homework', {'tasks': ['Hobby-Vokabeln lernen']}),
            ]},
    '05b': {'title': 'Verbos en -er/-ir', 'subtitle': 'Weitere Verben', 'sequenz': 5,
            'slides': [
                ('title', {}),
                ('grammar', {'title': 'comer (essen)', 'blocks': [('yo como', 'ich esse'), ('tú comes', 'du isst'), ('él/ella come', 'er/sie isst')]}),
                ('grammar', {'title': 'vivir (leben)', 'blocks': [('yo vivo', 'ich lebe'), ('tú vives', 'du lebst')]}),
                ('vocab', {'title': '-er/-ir-Verben', 'vocab': [('leer', 'lesen'), ('beber', 'trinken'), ('escribir', 'schreiben')], 'ab_ref': 'AB-05b: Kasten 1'}),
                ('homework', {'tasks': ['-er/-ir-Endungen lernen']}),
            ]},
    '05c': {'title': 'Me gusta...', 'subtitle': 'Vorlieben mit gustar', 'sequenz': 5,
            'slides': [
                ('title', {'flags': '❤️'}),
                ('grammar', {'title': 'gustar', 'blocks': [('Me gusta el fútbol.', 'Mir gefällt Fußball.'), ('Me gustan los libros.', 'Mir gefallen Bücher.')], 'info': 'gusta (Sg.) vs. gustan (Pl.)'}),
                ('vocab', {'title': 'Meinungen', 'vocab': [('Me encanta...', 'Ich liebe...'), ('No me gusta...', 'Ich mag nicht...')], 'ab_ref': 'AB-05c: Kasten 1'}),
                ('exercise', {'title': 'gusta/gustan?', 'exercises': [('Me ___ la música.', '(gusta)'), ('Me ___ los libros.', '(gustan)')], 'ab_ref': 'AB-05c: Aufgabe 2'}),
                ('homework', {'tasks': ['gustar-Struktur lernen']}),
            ]},
    '05d': {'title': 'Test: Tiempo libre', 'subtitle': 'Minitest Sequenz 5', 'sequenz': 5,
            'slides': [
                ('title', {}),
                ('summary', {'title': 'Wiederholung', 'left_items': ['Hobbys', 'Meinungen'], 'right_items': ['-er/-ir-Verben', 'gustar']}),
                ('homework', {'tasks': ['Hobby-Vokabeln', 'gustar-Sätze'], 'closing': '¡Buena suerte!'}),
            ]},

    # SEQUENZ 6: La ciudad
    '06a': {'title': 'Los lugares', 'subtitle': 'Orte in der Stadt', 'sequenz': 6,
            'slides': [
                ('title', {'flags': '🏙️'}),
                ('vocab', {'title': 'Orte', 'vocab': [('el centro', 'Zentrum'), ('la plaza', 'Platz'), ('el supermercado', 'Supermarkt'), ('el cine', 'Kino')], 'ab_ref': 'AB-06a: Kasten 1'}),
                ('vocab', {'title': 'Weitere Orte', 'vocab': [('la biblioteca', 'Bibliothek'), ('el hospital', 'Krankenhaus'), ('la estación', 'Bahnhof')], 'ab_ref': 'AB-06a: Kasten 2'}),
                ('homework', {'tasks': ['Ortsvokabeln lernen']}),
            ]},
    '06b': {'title': 'Ir y estar', 'subtitle': 'Gehen und sein', 'sequenz': 6,
            'slides': [
                ('title', {}),
                ('grammar', {'title': 'ir = gehen', 'blocks': [('yo voy', 'ich gehe'), ('tú vas', 'du gehst'), ('Voy al cine.', 'Ich gehe ins Kino.')]}),
                ('grammar', {'title': 'estar = sich befinden', 'blocks': [('yo estoy', 'ich bin'), ('Estoy en el parque.', 'Ich bin im Park.')], 'info': 'ir + a(l) / estar + en'}),
                ('exercise', {'title': 'ir oder estar?', 'exercises': [('___ al supermercado.', '(Voy)'), ('___ en casa.', '(Estoy)')], 'ab_ref': 'AB-06b: Aufgabe 2'}),
                ('homework', {'tasks': ['ir und estar konjugieren']}),
            ]},
    '06c': {'title': 'Las direcciones', 'subtitle': 'Wegbeschreibungen', 'sequenz': 6,
            'slides': [
                ('title', {'flags': '🧭'}),
                ('vocab', {'title': 'Richtungen', 'vocab': [('a la derecha', 'rechts'), ('a la izquierda', 'links'), ('todo recto', 'geradeaus')], 'ab_ref': 'AB-06c: Kasten 1'}),
                ('grammar', {'title': 'Nach dem Weg fragen', 'blocks': [('¿Dónde está...?', 'Wo ist...?'), ('¿Cómo llego a...?', 'Wie komme ich zu...?')]}),
                ('exercise', {'title': 'Wegbeschreibung', 'exercises': [('Zum Kino:', '___')], 'ab_ref': 'AB-06c: Aufgabe 2'}),
                ('homework', {'tasks': ['Richtungsvokabeln lernen']}),
            ]},
    '06d': {'title': 'Test: La ciudad', 'subtitle': 'Minitest Sequenz 6', 'sequenz': 6,
            'slides': [
                ('title', {}),
                ('summary', {'title': 'Wiederholung', 'left_items': ['Orte', 'Richtungen'], 'right_items': ['ir + a(l)', 'estar + en']}),
                ('homework', {'tasks': ['Ortsvokabeln', 'ir/estar'], 'closing': '¡Buena suerte!'}),
            ]},

    # SEQUENZ 7: Las compras
    '07a': {'title': 'La comida', 'subtitle': 'Lebensmittel', 'sequenz': 7,
            'slides': [
                ('title', {'flags': '🍎🥖🧀'}),
                ('vocab', {'title': 'Lebensmittel', 'vocab': [('el pan', 'Brot'), ('la fruta', 'Obst'), ('la verdura', 'Gemüse'), ('la carne', 'Fleisch')], 'ab_ref': 'AB-07a: Kasten 1'}),
                ('vocab', {'title': 'Getränke', 'vocab': [('el agua', 'Wasser'), ('el zumo', 'Saft'), ('la leche', 'Milch')], 'ab_ref': 'AB-07a: Kasten 2'}),
                ('homework', {'tasks': ['Lebensmittelvokabeln lernen']}),
            ]},
    '07b': {'title': 'Los números', 'subtitle': 'Zahlen 20–100', 'sequenz': 7,
            'slides': [
                ('title', {'flags': '💶'}),
                ('vocab', {'title': 'Zahlen', 'vocab': [('veinte, treinta, cuarenta', '20, 30, 40'), ('cincuenta, sesenta', '50, 60'), ('setenta, ochenta, noventa, cien', '70–100')], 'ab_ref': 'AB-07b: Kasten 1'}),
                ('grammar', {'title': 'Preise', 'blocks': [('¿Cuánto cuesta?', 'Wie viel kostet es?'), ('Cuesta dos euros.', 'Es kostet 2€.')], 'info': 'cuesta (Sg.) vs. cuestan (Pl.)'}),
                ('homework', {'tasks': ['Zahlen bis 100', 'Preise üben']}),
            ]},
    '07c': {'title': 'Querer y poder', 'subtitle': 'Wollen und können', 'sequenz': 7,
            'slides': [
                ('title', {}),
                ('grammar', {'title': 'querer = wollen', 'blocks': [('yo quiero', 'ich will'), ('tú quieres', 'du willst')], 'info': 'Stammwechsel e→ie'}),
                ('grammar', {'title': 'poder = können', 'blocks': [('yo puedo', 'ich kann'), ('tú puedes', 'du kannst')]}),
                ('vocab', {'title': 'Einkaufsdialog', 'vocab': [('Quiero un kilo de...', 'Ich möchte 1kg...'), ('¿Puedo pagar con tarjeta?', 'Kann ich mit Karte zahlen?')], 'ab_ref': 'AB-07c: Dialog'}),
                ('homework', {'tasks': ['querer/poder konjugieren']}),
            ]},
    '07d': {'title': 'Test: Las compras', 'subtitle': 'Minitest Sequenz 7', 'sequenz': 7,
            'slides': [
                ('title', {}),
                ('summary', {'title': 'Wiederholung', 'left_items': ['Lebensmittel', 'Zahlen 20–100'], 'right_items': ['querer (e→ie)', 'poder (o→ue)']}),
                ('homework', {'tasks': ['Lebensmittel', 'Stammwechselverben'], 'closing': '¡Buena suerte!'}),
            ]},

    # SEQUENZ 8: Las vacaciones
    '08a': {'title': 'Viajar', 'subtitle': 'Reisen', 'sequenz': 8,
            'slides': [
                ('title', {'flags': '✈️🚗🚂'}),
                ('vocab', {'title': 'Verkehrsmittel', 'vocab': [('el avión', 'Flugzeug'), ('el tren', 'Zug'), ('el coche', 'Auto'), ('el autobús', 'Bus')], 'ab_ref': 'AB-08a: Kasten 1'}),
                ('grammar', {'title': 'Reisen mit...', 'blocks': [('Voy en avión.', 'Ich fliege.'), ('Voy en tren.', 'Ich fahre mit dem Zug.')], 'info': 'ir + en + Verkehrsmittel'}),
                ('homework', {'tasks': ['Verkehrsmittel lernen']}),
            ]},
    '08b': {'title': 'El tiempo', 'subtitle': 'Das Wetter', 'sequenz': 8,
            'slides': [
                ('title', {'flags': '☀️🌧️❄️'}),
                ('vocab', {'title': 'Wetter', 'vocab': [('Hace sol.', 'Sonnig.'), ('Hace calor/frío.', 'Heiß/Kalt.'), ('Llueve.', 'Es regnet.'), ('Nieva.', 'Es schneit.')], 'ab_ref': 'AB-08b: Kasten 1'}),
                ('grammar', {'title': 'Wetter beschreiben', 'blocks': [('¿Qué tiempo hace?', 'Wie ist das Wetter?'), ('Hace buen tiempo.', 'Gutes Wetter.')]}),
                ('homework', {'tasks': ['Wettervokabeln lernen']}),
            ]},
    '08c': {'title': 'El pretérito', 'subtitle': 'Vergangenheit', 'sequenz': 8,
            'slides': [
                ('title', {}),
                ('grammar', {'title': 'Pretérito: -ar', 'blocks': [('yo hablé', 'ich sprach'), ('tú hablaste', 'du sprachst'), ('él habló', 'er sprach')]}),
                ('grammar', {'title': 'Pretérito: -er/-ir', 'blocks': [('yo comí', 'ich aß'), ('yo viví', 'ich lebte')]}),
                ('vocab', {'title': 'Zeitangaben', 'vocab': [('ayer', 'gestern'), ('la semana pasada', 'letzte Woche')], 'ab_ref': 'AB-08c: Kasten 2'}),
                ('homework', {'tasks': ['Pretérito-Endungen lernen']}),
            ]},
    '08d': {'title': 'Repaso final', 'subtitle': 'Abschlusstest', 'sequenz': 8,
            'slides': [
                ('title', {}),
                ('content', {'title': 'Jahresübersicht', 'items': ['Seq 1: Empezamos', 'Seq 2: La familia', 'Seq 3: La casa', 'Seq 4: El colegio', 'Seq 5: Tiempo libre', 'Seq 6: La ciudad', 'Seq 7: Las compras', 'Seq 8: Las vacaciones']}),
                ('homework', {'tasks': ['Alle Vokabeln', 'Alle Verben'], 'closing': '¡Felices vacaciones!'}),
            ]},
}

FOLDER_MAP = {
    1: 'sequenz-01-empezamos',
    2: 'sequenz-02-familia',
    3: 'sequenz-03-casa',
    4: 'sequenz-04-colegio',
    5: 'sequenz-05-tiempo-libre',
    6: 'sequenz-06-ciudad',
    7: 'sequenz-07-compras',
    8: 'sequenz-08-vacaciones',
}


def generate_presentation(lesson_id, lesson_data, output_path):
    """Generiert eine einzelne Präsentation"""
    pptx = SpanischPPTX(
        lesson_id,
        lesson_data['title'],
        lesson_data.get('subtitle', ''),
        lesson_data['sequenz']
    )

    for slide_type, params in lesson_data['slides']:
        if slide_type == 'title':
            pptx.add_title_slide(params.get('flags', '🇪🇸'))
        elif slide_type == 'vocab':
            pptx.add_vocab_slide(params['title'], params['vocab'],
                                 params.get('subtitle'), params.get('ab_ref'))
        elif slide_type == 'grammar':
            pptx.add_grammar_slide(params['title'], params['blocks'], params.get('info'))
        elif slide_type == 'exercise':
            pptx.add_exercise_slide(params['title'], params['exercises'],
                                    params.get('options'), params.get('ab_ref'))
        elif slide_type == 'solution':
            pptx.add_solution_slide(params['title'], params['solutions'])
        elif slide_type == 'summary':
            pptx.add_summary_slide(params['title'], params['left_items'],
                                   params.get('right_items'))
        elif slide_type == 'homework':
            pptx.add_homework_slide(params['tasks'], params.get('ab_ref'),
                                    params.get('closing', '¡Hasta luego!'))
        elif slide_type == 'map':
            pptx.add_map_slide(params['title'], params.get('subtitle'),
                               params.get('image_path'))
        elif slide_type == 'content':
            pptx.add_content_slide(params['title'], params['items'],
                                   params.get('ab_ref'))

    return pptx.save(output_path)


def generate_all(base_path):
    """Generiert alle 32 Präsentationen"""
    print("=" * 60)
    print("PowerPoint-Generator für Spanisch Klasse 7")
    print("=" * 60 + "\n")

    success, errors = 0, 0

    for lesson_id, data in LESSONS.items():
        folder = FOLDER_MAP.get(data['sequenz'])
        parent = os.path.join(base_path, folder)

        if not os.path.exists(parent):
            print(f"✗ {lesson_id}: Ordner fehlt")
            errors += 1
            continue

        subdirs = [d for d in os.listdir(parent)
                   if os.path.isdir(os.path.join(parent, d)) and d.startswith(lesson_id)]

        if not subdirs:
            print(f"✗ {lesson_id}: Unterordner fehlt")
            errors += 1
            continue

        output_dir = os.path.join(parent, subdirs[0])
        output_path = os.path.join(output_dir, f"PPT-{lesson_id}.pptx")

        try:
            count = generate_presentation(lesson_id, data, output_path)
            print(f"✓ {lesson_id}: {count} Folien → PPT-{lesson_id}.pptx")
            success += 1
        except Exception as e:
            print(f"✗ {lesson_id}: {e}")
            errors += 1

    print(f"\n{'=' * 60}")
    print(f"Fertig: {success} erfolgreich, {errors} Fehler")
    print("=" * 60)


if __name__ == "__main__":
    base = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../projects/spanisch/kl07"))
    if os.path.exists(base):
        print(f"Basis: {base}\n")
        generate_all(base)
    else:
        print(f"Pfad nicht gefunden: {base}")
