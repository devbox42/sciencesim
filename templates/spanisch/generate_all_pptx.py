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
# LESSON-DATEN für alle 32 Lektionen (erweitert: 12-15 Folien pro Lektion)
# ============================================================================

LESSONS = {
    # SEQUENZ 1: ¡Empezamos!
    '01a': {'title': '¡Hola!', 'subtitle': 'Begrüßung auf Spanisch', 'sequenz': 1,
            'slides': [
                ('title', {}),
                ('content', {'title': 'Lernziele', 'items': ['Begrüßen und verabschieden auf Spanisch', 'Tageszeiten unterscheiden', 'Spanische Sonderzeichen kennen']}),
                ('map', {'title': 'Wo spricht man Spanisch?', 'subtitle': '21 Länder, 480 Mio. Sprecher weltweit'}),
                ('content', {'title': 'Die spanischsprachige Welt', 'items': ['Spanien (Europa)', 'Mexiko, Argentinien, Chile... (Lateinamerika)', 'USA: 40 Mio. Sprecher!']}),
                ('vocab', {'title': 'Begrüßen am Tag', 'vocab': [('¡Hola!', 'Hallo!'), ('Buenos días', 'Guten Morgen (bis 12 Uhr)'), ('Buenas tardes', 'Guten Tag (12-20 Uhr)')], 'ab_ref': 'AB-01a: Kasten 1'}),
                ('vocab', {'title': 'Begrüßen am Abend', 'vocab': [('Buenas noches', 'Guten Abend / Gute Nacht'), ('¿Qué tal?', 'Wie geht\'s?'), ('¿Cómo estás?', 'Wie geht es dir?')], 'ab_ref': 'AB-01a: Kasten 1'}),
                ('vocab', {'title': 'Verabschieden', 'vocab': [('¡Adiós!', 'Tschüss!'), ('¡Hasta luego!', 'Bis später!'), ('¡Hasta mañana!', 'Bis morgen!'), ('¡Hasta pronto!', 'Bis bald!')], 'ab_ref': 'AB-01a: Kasten 2'}),
                ('grammar', {'title': 'Grammatik: Genus', 'blocks': [('Buenos días', '← maskulin Plural'), ('Buenas tardes', '← feminin Plural'), ('Buenas noches', '← feminin Plural')], 'info': 'día ist maskulin, tarde/noche feminin'}),
                ('grammar', {'title': 'Sonderzeichen', 'blocks': [('¡...!', 'Ausrufezeichen am Anfang UND Ende'), ('¿...?', 'Fragezeichen am Anfang UND Ende')], 'info': 'Nur im Spanischen!'}),
                ('exercise', {'title': 'Übung: Tageszeit zuordnen', 'exercises': [('8:00 Uhr →', '___'), ('15:00 Uhr →', '___'), ('21:00 Uhr →', '___')], 'options': 'Buenos días / Buenas tardes / Buenas noches', 'ab_ref': 'AB-01a: Aufgabe 1'}),
                ('solution', {'title': 'Lösung', 'solutions': [('8:00 Uhr', 'Buenos días'), ('15:00 Uhr', 'Buenas tardes'), ('21:00 Uhr', 'Buenas noches')]}),
                ('exercise', {'title': 'Übung: Übersetzen', 'exercises': [('Hallo!', '___'), ('Tschüss!', '___'), ('Bis morgen!', '___')], 'ab_ref': 'AB-01a: Aufgabe 2'}),
                ('solution', {'title': 'Lösung', 'solutions': [('Hallo!', '¡Hola!'), ('Tschüss!', '¡Adiós!'), ('Bis morgen!', '¡Hasta mañana!')]}),
                ('summary', {'title': 'Zusammenfassung', 'left_items': ['¡Hola! – Hallo', 'Buenos días – Guten Morgen', 'Buenas tardes – Guten Tag', 'Buenas noches – Gute Nacht'], 'right_items': ['¡Adiós! – Tschüss', '¡Hasta luego! – Bis später', '¡Hasta mañana! – Bis morgen']}),
                ('homework', {'tasks': ['AB-01a vollständig ausfüllen', 'Begrüßungsvokabeln auswendig lernen', 'Sonderzeichen ¡ ¿ üben']}),
            ]},

    '01b': {'title': '¿Cómo te llamas?', 'subtitle': 'Sich vorstellen', 'sequenz': 1,
            'slides': [
                ('title', {}),
                ('content', {'title': 'Lernziele', 'items': ['Sich vorstellen können', 'Das Verb ser konjugieren', 'Herkunft und Nationalität angeben']}),
                ('vocab', {'title': 'Sich vorstellen', 'vocab': [('¿Cómo te llamas?', 'Wie heißt du?'), ('Me llamo...', 'Ich heiße...'), ('Soy...', 'Ich bin...')], 'ab_ref': 'AB-01b: Kasten 1'}),
                ('vocab', {'title': 'Herkunft', 'vocab': [('¿De dónde eres?', 'Woher kommst du?'), ('Soy de...', 'Ich komme aus...'), ('Vivo en...', 'Ich wohne in...')], 'ab_ref': 'AB-01b: Kasten 1'}),
                ('grammar', {'title': 'Das Verb ser (sein)', 'blocks': [('yo soy', 'ich bin'), ('tú eres', 'du bist'), ('él/ella es', 'er/sie ist')], 'info': 'ser = dauerhafter Zustand'}),
                ('grammar', {'title': 'ser: Plural', 'blocks': [('nosotros/-as somos', 'wir sind'), ('vosotros/-as sois', 'ihr seid'), ('ellos/ellas son', 'sie sind')]}),
                ('vocab', {'title': 'Länder', 'vocab': [('España', 'Spanien'), ('Alemania', 'Deutschland'), ('Francia', 'Frankreich'), ('Italia', 'Italien')], 'ab_ref': 'AB-01b: Kasten 2'}),
                ('vocab', {'title': 'Nationalitäten', 'vocab': [('español/a', 'spanisch'), ('alemán/alemana', 'deutsch'), ('francés/francesa', 'französisch')], 'ab_ref': 'AB-01b: Kasten 2'}),
                ('content', {'title': 'Dialog: Kennenlernen', 'items': ['– ¡Hola! ¿Cómo te llamas?', '– Me llamo María. ¿Y tú?', '– Soy Carlos. ¿De dónde eres?', '– Soy de España. ¿Y tú?', '– Soy de Alemania.']}),
                ('exercise', {'title': 'Übung: ser ergänzen', 'exercises': [('Yo ___ María.', '(bin)'), ('Tú ___ de Rostock.', '(bist)'), ('Ella ___ española.', '(ist)')], 'ab_ref': 'AB-01b: Aufgabe 2'}),
                ('solution', {'title': 'Lösung', 'solutions': [('Yo soy María.', '✓'), ('Tú eres de Rostock.', '✓'), ('Ella es española.', '✓')]}),
                ('exercise', {'title': 'Übung: Übersetzen', 'exercises': [('Ich heiße Tim.', '___'), ('Ich komme aus Deutschland.', '___')], 'ab_ref': 'AB-01b: Aufgabe 3'}),
                ('solution', {'title': 'Lösung', 'solutions': [('Ich heiße Tim.', 'Me llamo Tim.'), ('Ich komme aus Deutschland.', 'Soy de Alemania.')]}),
                ('summary', {'title': 'Zusammenfassung', 'left_items': ['Me llamo... – Ich heiße...', 'Soy de... – Ich bin aus...', 'español/a, alemán/a'], 'right_items': ['soy, eres, es', 'somos, sois, son']}),
                ('homework', {'tasks': ['ser-Formen auswendig lernen', 'Steckbrief über dich schreiben', 'AB-01b Aufgaben 1-4']}),
            ]},

    '01c': {'title': 'El alfabeto', 'subtitle': 'Artikel und Alphabet', 'sequenz': 1,
            'slides': [
                ('title', {}),
                ('content', {'title': 'Lernziele', 'items': ['Das spanische Alphabet kennen', 'Bestimmte Artikel (el/la/los/las)', 'Unbestimmte Artikel (un/una)']}),
                ('grammar', {'title': 'Bestimmte Artikel: Singular', 'blocks': [('el chico', 'der Junge'), ('la chica', 'das Mädchen')], 'info': 'el = maskulin, la = feminin'}),
                ('grammar', {'title': 'Bestimmte Artikel: Plural', 'blocks': [('los chicos', 'die Jungen'), ('las chicas', 'die Mädchen')], 'info': 'los = mask. Pl., las = fem. Pl.'}),
                ('grammar', {'title': 'Unbestimmte Artikel', 'blocks': [('un libro', 'ein Buch'), ('una mesa', 'ein Tisch')], 'info': 'un = mask., una = fem. (kein Plural!)'}),
                ('vocab', {'title': 'Schulvokabeln', 'vocab': [('el libro', 'das Buch'), ('la mesa', 'der Tisch'), ('el profesor', 'der Lehrer'), ('la profesora', 'die Lehrerin')], 'ab_ref': 'AB-01c: Kasten 1'}),
                ('vocab', {'title': 'Mehr Vokabeln', 'vocab': [('el lápiz', 'der Bleistift'), ('la ventana', 'das Fenster'), ('el cuaderno', 'das Heft')], 'ab_ref': 'AB-01c: Kasten 1'}),
                ('content', {'title': 'Das spanische Alphabet', 'items': ['27 Buchstaben (wie Deutsch + ñ)', 'Besonder: ñ (eñe) = nj', 'ch und ll sind Buchstabenkombinationen', 'Alle Buchstaben sprechen sich gleich aus!']}),
                ('grammar', {'title': 'Aussprache-Tipps', 'blocks': [('j', 'wie deutsches ch in "Bach"'), ('z/ce/ci', 'wie englisches th'), ('ñ', 'wie nj in "Cognac"')]}),
                ('exercise', {'title': 'Übung: Artikel ergänzen', 'exercises': [('___ profesor', '(der)'), ('___ profesora', '(die)'), ('___ libros', '(die, Pl.)')], 'ab_ref': 'AB-01c: Aufgabe 2'}),
                ('solution', {'title': 'Lösung', 'solutions': [('el profesor', '✓'), ('la profesora', '✓'), ('los libros', '✓')]}),
                ('exercise', {'title': 'Buchstabieren', 'exercises': [('HOLA', 'h-o-l-a'), ('Dein Name', '___')], 'ab_ref': 'AB-01c: Aufgabe 3'}),
                ('summary', {'title': 'Zusammenfassung', 'left_items': ['el/la – der/die', 'los/las – die (Plural)', 'un/una – ein/eine'], 'right_items': ['Alphabet: 27 Buchstaben', 'Besonders: ñ, j, z']}),
                ('homework', {'tasks': ['Artikel el/la/los/las lernen', 'Alphabet üben', 'Deinen Namen buchstabieren können']}),
            ]},

    '01d': {'title': '¿Qué tal?', 'subtitle': 'Wiederholung Sequenz 1', 'sequenz': 1,
            'slides': [
                ('title', {}),
                ('content', {'title': 'Sequenz 1: Rückblick', 'items': ['Lektion 1a: Begrüßen & Verabschieden', 'Lektion 1b: Sich vorstellen, ser', 'Lektion 1c: Artikel, Alphabet']}),
                ('summary', {'title': 'Vokabeln Seq. 1', 'left_items': ['¡Hola! / ¡Adiós!', 'Buenos días/tardes/noches', 'Me llamo... / Soy de...'], 'right_items': ['el/la/los/las', 'un/una', 'español/a, alemán/a']}),
                ('grammar', {'title': 'Grammatik: ser', 'blocks': [('yo soy', 'ich bin'), ('tú eres', 'du bist'), ('él/ella es', 'er/sie ist'), ('nosotros somos', 'wir sind')]}),
                ('grammar', {'title': 'Grammatik: Artikel', 'blocks': [('el/los', 'maskulin'), ('la/las', 'feminin'), ('un/una', 'unbestimmt')]}),
                ('content', {'title': 'Minitest: Überblick', 'items': ['Teil 1: Begrüßung & Verabschiedung (8 P)', 'Teil 2: ser-Konjugation (6 P)', 'Teil 3: Artikel ergänzen (6 P)', 'Teil 4: Sich vorstellen (5 P)']}),
                ('exercise', {'title': 'Probe: Begrüßung', 'exercises': [('Guten Morgen =', '___'), ('Tschüss =', '___')], 'ab_ref': 'MT-01d'}),
                ('exercise', {'title': 'Probe: ser', 'exercises': [('Yo ___ de Alemania.', '___'), ('Ella ___ española.', '___')], 'ab_ref': 'MT-01d'}),
                ('exercise', {'title': 'Probe: Artikel', 'exercises': [('___ libro (m.)', '___'), ('___ profesora (f.)', '___')], 'ab_ref': 'MT-01d'}),
                ('content', {'title': 'Tipps für den Test', 'items': ['Begrüßungen nach Tageszeit unterscheiden', 'ser-Formen sicher können', 'Genus der Nomen beachten (el/la)']}),
                ('homework', {'tasks': ['Alle Vokabeln Seq. 1 wiederholen', 'ser-Tabelle auswendig', 'Artikel el/la üben'], 'closing': '¡Buena suerte!'}),
            ]},

    # SEQUENZ 2: La familia
    '02a': {'title': 'La familia', 'subtitle': 'Familienmitglieder', 'sequenz': 2,
            'slides': [
                ('title', {'flags': '👨‍👩‍👧‍👦'}),
                ('content', {'title': 'Lernziele', 'items': ['Familienmitglieder benennen', 'Verwandtschaftsbeziehungen verstehen', 'Plural bilden']}),
                ('vocab', {'title': 'Eltern & Kinder', 'vocab': [('el padre', 'der Vater'), ('la madre', 'die Mutter'), ('los padres', 'die Eltern'), ('el hijo / la hija', 'Sohn / Tochter')], 'ab_ref': 'AB-02a: Kasten 1'}),
                ('vocab', {'title': 'Geschwister', 'vocab': [('el hermano', 'der Bruder'), ('la hermana', 'die Schwester'), ('los hermanos', 'die Geschwister')], 'ab_ref': 'AB-02a: Kasten 1'}),
                ('vocab', {'title': 'Großeltern', 'vocab': [('el abuelo', 'der Großvater'), ('la abuela', 'die Großmutter'), ('los abuelos', 'die Großeltern')], 'ab_ref': 'AB-02a: Kasten 2'}),
                ('vocab', {'title': 'Erweiterte Familie', 'vocab': [('el tío / la tía', 'Onkel / Tante'), ('el primo / la prima', 'Cousin / Cousine'), ('el sobrino / la sobrina', 'Neffe / Nichte')], 'ab_ref': 'AB-02a: Kasten 2'}),
                ('grammar', {'title': 'Plural bilden', 'blocks': [('padre → padres', '+ s'), ('hermano → hermanos', '+ s')], 'info': 'Konsonant: + es (profesor → profesores)'}),
                ('grammar', {'title': 'Gemischter Plural', 'blocks': [('el padre + la madre', '= los padres'), ('el hermano + la hermana', '= los hermanos')], 'info': 'Gemischt = maskuliner Plural'}),
                ('content', {'title': 'Stammbaum-Beispiel', 'items': ['👴 abuelo + 👵 abuela', '├── 👨 padre + 👩 madre', '│   ├── 👦 yo', '│   └── 👧 hermana']}),
                ('exercise', {'title': 'Übung: Wer ist wer?', 'exercises': [('Der Bruder meiner Mutter =', '___'), ('Die Tochter meiner Tante =', '___')], 'ab_ref': 'AB-02a: Aufgabe 1'}),
                ('solution', {'title': 'Lösung', 'solutions': [('Der Bruder meiner Mutter', 'el tío'), ('Die Tochter meiner Tante', 'la prima')]}),
                ('exercise', {'title': 'Übung: Plural bilden', 'exercises': [('el padre →', '___'), ('la hermana →', '___'), ('el abuelo →', '___')], 'ab_ref': 'AB-02a: Aufgabe 2'}),
                ('summary', {'title': 'Zusammenfassung', 'left_items': ['padre/madre – Vater/Mutter', 'hijo/hija – Sohn/Tochter', 'hermano/a – Bruder/Schwester'], 'right_items': ['abuelo/a – Opa/Oma', 'tío/tía – Onkel/Tante', 'primo/a – Cousin/e']}),
                ('homework', {'tasks': ['Familienvokabeln auswendig lernen', 'Deinen Stammbaum auf Spanisch zeichnen', 'AB-02a vollständig']}),
            ]},

    '02b': {'title': 'Tengo 12 años', 'subtitle': 'tener und Alter', 'sequenz': 2,
            'slides': [
                ('title', {}),
                ('content', {'title': 'Lernziele', 'items': ['Das Verb tener konjugieren', 'Alter angeben (auf Spanisch!)', 'Zahlen 1–20']}),
                ('grammar', {'title': 'Das Verb tener (haben)', 'blocks': [('yo tengo', 'ich habe'), ('tú tienes', 'du hast'), ('él/ella tiene', 'er/sie hat')], 'info': 'Achtung: Stammwechsel e→ie'}),
                ('grammar', {'title': 'tener: Plural', 'blocks': [('nosotros tenemos', 'wir haben'), ('vosotros tenéis', 'ihr habt'), ('ellos tienen', 'sie haben')]}),
                ('grammar', {'title': 'Alter angeben', 'blocks': [('¿Cuántos años tienes?', 'Wie alt bist du?'), ('Tengo doce años.', 'Ich bin 12 (Jahre alt).')], 'info': 'Spanisch: Man "HAT" Jahre!'}),
                ('vocab', {'title': 'Zahlen 1–10', 'vocab': [('uno, dos, tres', '1, 2, 3'), ('cuatro, cinco, seis', '4, 5, 6'), ('siete, ocho, nueve, diez', '7, 8, 9, 10')], 'ab_ref': 'AB-02b: Kasten 2'}),
                ('vocab', {'title': 'Zahlen 11–20', 'vocab': [('once, doce, trece', '11, 12, 13'), ('catorce, quince', '14, 15'), ('dieciséis ... veinte', '16 ... 20')], 'ab_ref': 'AB-02b: Kasten 2'}),
                ('content', {'title': 'Dialog: Alter', 'items': ['– ¿Cuántos años tienes?', '– Tengo trece años. ¿Y tú?', '– Yo tengo doce años.', '– Mi hermana tiene quince años.']}),
                ('exercise', {'title': 'Übung: tener ergänzen', 'exercises': [('Yo ___ 13 años.', '(habe)'), ('Mi hermano ___ 10 años.', '(hat)'), ('Nosotros ___ un perro.', '(haben)')], 'ab_ref': 'AB-02b: Aufgabe 2'}),
                ('solution', {'title': 'Lösung', 'solutions': [('Yo tengo 13 años.', '✓'), ('Mi hermano tiene 10 años.', '✓'), ('Nosotros tenemos un perro.', '✓')]}),
                ('exercise', {'title': 'Übung: Zahlen', 'exercises': [('12 =', '___'), ('15 =', '___'), ('20 =', '___')], 'ab_ref': 'AB-02b: Aufgabe 3'}),
                ('solution', {'title': 'Lösung', 'solutions': [('12', 'doce'), ('15', 'quince'), ('20', 'veinte')]}),
                ('summary', {'title': 'Zusammenfassung', 'left_items': ['tengo, tienes, tiene', 'tenemos, tenéis, tienen', '¿Cuántos años tienes?'], 'right_items': ['1-10: uno...diez', '11-15: once...quince', '16-20: dieciséis...veinte']}),
                ('homework', {'tasks': ['tener-Formen auswendig lernen', 'Zahlen 1–20 üben', 'Alter deiner Familie aufschreiben']}),
            ]},

    '02c': {'title': 'Mi familia', 'subtitle': 'Possessivbegleiter', 'sequenz': 2,
            'slides': [
                ('title', {}),
                ('content', {'title': 'Lernziele', 'items': ['Possessivbegleiter (mein, dein, sein)', 'Familie beschreiben', 'Possessiv + Plural']}),
                ('grammar', {'title': 'Possessivbegleiter Singular', 'blocks': [('mi padre', 'mein Vater'), ('tu madre', 'deine Mutter'), ('su hermano', 'sein/ihr Bruder')]}),
                ('grammar', {'title': 'Possessivbegleiter Plural', 'blocks': [('mis padres', 'meine Eltern'), ('tus hermanos', 'deine Geschwister'), ('sus abuelos', 'seine/ihre Großeltern')], 'info': 'Vor Plural: mi→mis, tu→tus, su→sus'}),
                ('grammar', {'title': 'Übersicht Possessiv', 'blocks': [('mi / mis', 'mein/e'), ('tu / tus', 'dein/e'), ('su / sus', 'sein/e, ihr/e')]}),
                ('content', {'title': 'Beispiele', 'items': ['Mi hermana se llama Ana.', 'Mis padres son de España.', 'Tu primo tiene 14 años.', 'Sus abuelos viven en Madrid.']}),
                ('vocab', {'title': 'Haustiere', 'vocab': [('el perro', 'der Hund'), ('el gato', 'die Katze'), ('el pájaro', 'der Vogel')], 'ab_ref': 'AB-02c: Kasten 1'}),
                ('content', {'title': 'Meine Familie beschreiben', 'items': ['Mi familia es pequeña/grande.', 'Tengo un/a hermano/a.', 'No tengo hermanos. (keine)', 'Tenemos un perro.']}),
                ('exercise', {'title': 'Übung: Possessiv ergänzen', 'exercises': [('___ hermana (ich)', '___'), ('___ padres (du)', '___'), ('___ abuelos (er)', '___')], 'ab_ref': 'AB-02c: Aufgabe 2'}),
                ('solution', {'title': 'Lösung', 'solutions': [('meine Schwester', 'mi hermana'), ('deine Eltern', 'tus padres'), ('seine Großeltern', 'sus abuelos')]}),
                ('exercise', {'title': 'Übung: Übersetzen', 'exercises': [('Mein Bruder heißt Max.', '___'), ('Deine Eltern sind nett.', '___')], 'ab_ref': 'AB-02c: Aufgabe 3'}),
                ('summary', {'title': 'Zusammenfassung', 'left_items': ['mi / mis – mein/e', 'tu / tus – dein/e', 'su / sus – sein/e'], 'right_items': ['Singular: mi, tu, su', 'Plural: mis, tus, sus']}),
                ('homework', {'tasks': ['Possessivbegleiter lernen', 'Deine Familie beschreiben (5 Sätze)', 'AB-02c vollständig']}),
            ]},

    '02d': {'title': 'Test: La familia', 'subtitle': 'Minitest Sequenz 2', 'sequenz': 2,
            'slides': [
                ('title', {}),
                ('content', {'title': 'Sequenz 2: Rückblick', 'items': ['Lektion 2a: Familienmitglieder', 'Lektion 2b: tener, Zahlen, Alter', 'Lektion 2c: Possessivbegleiter']}),
                ('summary', {'title': 'Vokabeln Seq. 2', 'left_items': ['padre/madre, hijo/hija', 'hermano/a, abuelo/a', 'tío/tía, primo/a'], 'right_items': ['Zahlen 1–20', 'perro, gato, pájaro']}),
                ('grammar', {'title': 'Grammatik: tener', 'blocks': [('yo tengo', 'ich habe'), ('tú tienes', 'du hast'), ('él/ella tiene', 'er/sie hat')]}),
                ('grammar', {'title': 'Grammatik: Possessiv', 'blocks': [('mi / mis', 'mein/e'), ('tu / tus', 'dein/e'), ('su / sus', 'sein/e')]}),
                ('content', {'title': 'Minitest: Überblick', 'items': ['Teil 1: Familienvokabeln (6 P)', 'Teil 2: tener-Konjugation (6 P)', 'Teil 3: Zahlen 1–20 (4 P)', 'Teil 4: Possessivbegleiter (6 P)', 'Teil 5: Familie beschreiben (3 P)']}),
                ('exercise', {'title': 'Probe: Familie', 'exercises': [('der Bruder =', '___'), ('die Großmutter =', '___')], 'ab_ref': 'MT-02d'}),
                ('exercise', {'title': 'Probe: tener', 'exercises': [('Yo ___ 13 años.', '___'), ('Ella ___ dos hermanos.', '___')], 'ab_ref': 'MT-02d'}),
                ('exercise', {'title': 'Probe: Possessiv', 'exercises': [('___ madre (ich)', '___'), ('___ hermanos (du)', '___')], 'ab_ref': 'MT-02d'}),
                ('content', {'title': 'Tipps für den Test', 'items': ['Familienvokabeln mit Artikel lernen', 'tener: Stammwechsel e→ie beachten', 'Possessiv: Singular vs. Plural']}),
                ('homework', {'tasks': ['Alle Vokabeln Seq. 2 wiederholen', 'tener-Tabelle üben', 'mi/mis, tu/tus, su/sus'], 'closing': '¡Buena suerte!'}),
            ]},

    # SEQUENZ 3: La casa
    '03a': {'title': 'La casa', 'subtitle': 'Räume im Haus', 'sequenz': 3,
            'slides': [
                ('title', {'flags': '🏠'}),
                ('content', {'title': 'Lernziele', 'items': ['Räume im Haus benennen', 'Wohnungsbeschreibung verstehen', 'Vokabeln mit Artikel lernen']}),
                ('vocab', {'title': 'Haupträume', 'vocab': [('la cocina', 'die Küche'), ('el salón', 'das Wohnzimmer'), ('el dormitorio', 'das Schlafzimmer'), ('el baño', 'das Badezimmer')], 'ab_ref': 'AB-03a: Kasten 1'}),
                ('vocab', {'title': 'Weitere Räume', 'vocab': [('el comedor', 'das Esszimmer'), ('el pasillo', 'der Flur'), ('el jardín', 'der Garten'), ('el garaje', 'die Garage')], 'ab_ref': 'AB-03a: Kasten 1'}),
                ('vocab', {'title': 'Stockwerke', 'vocab': [('la planta baja', 'Erdgeschoss'), ('el primer piso', '1. Stock'), ('el ático', 'Dachgeschoss')], 'ab_ref': 'AB-03a: Kasten 2'}),
                ('content', {'title': 'Typisches spanisches Haus', 'items': ['Viele Häuser haben einen patio (Innenhof)', 'Balcón (Balkon) ist wichtig', 'Terraza (Terrasse) zum Essen im Freien']}),
                ('grammar', {'title': 'Genus beachten', 'blocks': [('EL: salón, dormitorio, baño', 'maskulin'), ('LA: cocina, terraza', 'feminin')], 'info': '-o meist maskulin, -a meist feminin'}),
                ('exercise', {'title': 'Übung: Wo macht man was?', 'exercises': [('Schlafen →', '___'), ('Kochen →', '___'), ('Fernsehen →', '___')], 'ab_ref': 'AB-03a: Aufgabe 1'}),
                ('solution', {'title': 'Lösung', 'solutions': [('Schlafen', 'el dormitorio'), ('Kochen', 'la cocina'), ('Fernsehen', 'el salón')]}),
                ('exercise', {'title': 'Übung: Artikel ergänzen', 'exercises': [('___ cocina', '___'), ('___ salón', '___'), ('___ baño', '___')], 'ab_ref': 'AB-03a: Aufgabe 2'}),
                ('summary', {'title': 'Zusammenfassung', 'left_items': ['la cocina – Küche', 'el salón – Wohnzimmer', 'el dormitorio – Schlafzimmer', 'el baño – Bad'], 'right_items': ['el comedor – Esszimmer', 'el jardín – Garten', 'el garaje – Garage']}),
                ('homework', {'tasks': ['Räume-Vokabeln mit Artikel lernen', 'Dein Zuhause beschreiben (Räume)', 'AB-03a vollständig']}),
            ]},

    '03b': {'title': 'Hay una mesa', 'subtitle': 'hay + Möbel', 'sequenz': 3,
            'slides': [
                ('title', {}),
                ('content', {'title': 'Lernziele', 'items': ['hay = es gibt', 'Möbel benennen', 'Zimmer beschreiben']}),
                ('grammar', {'title': 'hay = es gibt', 'blocks': [('Hay una mesa.', 'Es gibt einen Tisch.'), ('Hay dos sillas.', 'Es gibt zwei Stühle.')], 'info': 'hay ist UNVERÄNDERLICH!'}),
                ('grammar', {'title': 'hay: Verneinung', 'blocks': [('No hay televisor.', 'Es gibt keinen Fernseher.'), ('No hay ventanas.', 'Es gibt keine Fenster.')], 'info': 'Einfach "no" davor'}),
                ('vocab', {'title': 'Möbel 1', 'vocab': [('la mesa', 'der Tisch'), ('la silla', 'der Stuhl'), ('el sofá', 'das Sofa'), ('la cama', 'das Bett')], 'ab_ref': 'AB-03b: Kasten 1'}),
                ('vocab', {'title': 'Möbel 2', 'vocab': [('el armario', 'der Schrank'), ('la estantería', 'das Regal'), ('la lámpara', 'die Lampe'), ('la alfombra', 'der Teppich')], 'ab_ref': 'AB-03b: Kasten 1'}),
                ('vocab', {'title': 'Elektrogeräte', 'vocab': [('el televisor', 'der Fernseher'), ('el ordenador', 'der Computer'), ('la nevera', 'der Kühlschrank')], 'ab_ref': 'AB-03b: Kasten 2'}),
                ('content', {'title': 'Beispielbeschreibung', 'items': ['En mi dormitorio hay una cama.', 'Hay un armario grande.', 'También hay una mesa pequeña.', 'No hay televisor.']}),
                ('exercise', {'title': 'Übung: Beschreibe dein Zimmer', 'exercises': [('En mi dormitorio hay...', '___'), ('También hay...', '___'), ('No hay...', '___')], 'ab_ref': 'AB-03b: Aufgabe 2'}),
                ('exercise', {'title': 'Übung: Übersetzen', 'exercises': [('Es gibt ein Sofa.', '___'), ('Es gibt keinen Tisch.', '___')], 'ab_ref': 'AB-03b: Aufgabe 3'}),
                ('solution', {'title': 'Lösung', 'solutions': [('Es gibt ein Sofa.', 'Hay un sofá.'), ('Es gibt keinen Tisch.', 'No hay mesa.')]}),
                ('summary', {'title': 'Zusammenfassung', 'left_items': ['hay = es gibt', 'no hay = es gibt kein/e', 'hay + Singular/Plural'], 'right_items': ['mesa, silla, sofá, cama', 'armario, estantería', 'televisor, ordenador']}),
                ('homework', {'tasks': ['Möbelvokabeln lernen', 'Dein Zimmer beschreiben (hay)', 'AB-03b vollständig']}),
            ]},

    '03c': {'title': 'Los colores', 'subtitle': 'Farben', 'sequenz': 3,
            'slides': [
                ('title', {'flags': '🔴🟢🔵'}),
                ('content', {'title': 'Lernziele', 'items': ['Farben auf Spanisch', 'Adjektive angleichen', 'Dinge beschreiben']}),
                ('vocab', {'title': 'Farben 1', 'vocab': [('rojo/a', 'rot'), ('azul', 'blau'), ('verde', 'grün'), ('amarillo/a', 'gelb')], 'ab_ref': 'AB-03c: Kasten 1'}),
                ('vocab', {'title': 'Farben 2', 'vocab': [('blanco/a', 'weiß'), ('negro/a', 'schwarz'), ('gris', 'grau'), ('marrón', 'braun')], 'ab_ref': 'AB-03c: Kasten 1'}),
                ('vocab', {'title': 'Weitere Farben', 'vocab': [('rosa', 'rosa'), ('naranja', 'orange'), ('morado/a', 'lila')], 'ab_ref': 'AB-03c: Kasten 1'}),
                ('grammar', {'title': 'Adjektiv-Angleichung', 'blocks': [('el sofá rojo', 'das rote Sofa'), ('la silla roja', 'der rote Stuhl')], 'info': '-o → -a bei feminin'}),
                ('grammar', {'title': 'Unveränderliche Farben', 'blocks': [('azul, verde, gris', 'ändern sich NICHT'), ('el libro azul', 'la mesa azul')], 'info': 'Farben auf -e oder Kons. bleiben'}),
                ('grammar', {'title': 'Plural der Farben', 'blocks': [('los libros rojos', 'die roten Bücher'), ('las sillas azules', 'die blauen Stühle')]}),
                ('content', {'title': 'Beispiele', 'items': ['La cama es blanca.', 'El armario es marrón.', 'Las paredes son amarillas.', 'Los libros son azules.']}),
                ('exercise', {'title': 'Übung: Farbe angleichen', 'exercises': [('La mesa es ___ (weiß)', '___'), ('El sofá es ___ (grün)', '___'), ('Las sillas son ___ (rot)', '___')], 'ab_ref': 'AB-03c: Aufgabe 2'}),
                ('solution', {'title': 'Lösung', 'solutions': [('La mesa es blanca.', '✓'), ('El sofá es verde.', '✓'), ('Las sillas son rojas.', '✓')]}),
                ('summary', {'title': 'Zusammenfassung', 'left_items': ['rojo/a, amarillo/a, blanco/a', 'azul, verde, gris (unverändert)', 'marrón, rosa, naranja'], 'right_items': ['Angleichung: -o → -a', 'Plural: +s oder +es', 'Nach Nomen: el coche rojo']}),
                ('homework', {'tasks': ['Farben auswendig lernen', 'Zimmer mit Farben beschreiben', 'AB-03c vollständig']}),
            ]},

    '03d': {'title': 'Test: La casa', 'subtitle': 'Minitest Sequenz 3', 'sequenz': 3,
            'slides': [
                ('title', {}),
                ('content', {'title': 'Sequenz 3: Rückblick', 'items': ['Lektion 3a: Räume im Haus', 'Lektion 3b: hay + Möbel', 'Lektion 3c: Farben und Adjektive']}),
                ('summary', {'title': 'Vokabeln Seq. 3', 'left_items': ['cocina, salón, dormitorio', 'mesa, silla, cama, sofá', 'armario, estantería'], 'right_items': ['rojo, azul, verde', 'blanco, negro, gris', 'amarillo, marrón']}),
                ('grammar', {'title': 'Grammatik: hay', 'blocks': [('Hay una mesa.', 'Es gibt einen Tisch.'), ('No hay sofá.', 'Es gibt kein Sofa.')], 'info': 'hay = unveränderlich'}),
                ('grammar', {'title': 'Grammatik: Adjektive', 'blocks': [('el sofá rojo', 'mask. → -o'), ('la silla roja', 'fem. → -a'), ('azul, verde', 'unveränderlich')]}),
                ('content', {'title': 'Minitest: Überblick', 'items': ['Teil 1: Räume benennen (5 P)', 'Teil 2: Möbelvokabeln (6 P)', 'Teil 3: hay-Sätze bilden (6 P)', 'Teil 4: Farben angleichen (6 P)', 'Teil 5: Zimmer beschreiben (2 P)']}),
                ('exercise', {'title': 'Probe: Räume', 'exercises': [('Küche =', '___'), ('Schlafzimmer =', '___')], 'ab_ref': 'MT-03d'}),
                ('exercise', {'title': 'Probe: hay', 'exercises': [('Es gibt ein Bett. =', '___'), ('Es gibt keinen Fernseher. =', '___')], 'ab_ref': 'MT-03d'}),
                ('exercise', {'title': 'Probe: Farben', 'exercises': [('la mesa ___ (weiß)', '___'), ('el sofá ___ (rot)', '___')], 'ab_ref': 'MT-03d'}),
                ('content', {'title': 'Tipps für den Test', 'items': ['Vokabeln mit Artikel lernen (el/la)', 'hay: Singular UND Plural möglich', 'Farben: -o/-a nur bei manchen']}),
                ('homework', {'tasks': ['Alle Vokabeln Seq. 3 wiederholen', 'hay-Sätze üben', 'Adjektiv-Angleichung üben'], 'closing': '¡Buena suerte!'}),
            ]},

    # SEQUENZ 4: El colegio
    '04a': {'title': 'Las asignaturas', 'subtitle': 'Schulfächer', 'sequenz': 4,
            'slides': [
                ('title', {'flags': '📚'}),
                ('content', {'title': 'Lernziele', 'items': ['Schulfächer benennen', 'Lieblingsfach ausdrücken', 'Meinungen äußern']}),
                ('vocab', {'title': 'Hauptfächer', 'vocab': [('las matemáticas', 'Mathematik'), ('el español', 'Spanisch'), ('el inglés', 'Englisch'), ('el alemán', 'Deutsch')], 'ab_ref': 'AB-04a: Kasten 1'}),
                ('vocab', {'title': 'Nebenfächer 1', 'vocab': [('la historia', 'Geschichte'), ('la geografía', 'Erdkunde'), ('las ciencias', 'Naturwissenschaften'), ('la biología', 'Biologie')], 'ab_ref': 'AB-04a: Kasten 1'}),
                ('vocab', {'title': 'Nebenfächer 2', 'vocab': [('la música', 'Musik'), ('el arte', 'Kunst'), ('el deporte', 'Sport'), ('la informática', 'Informatik')], 'ab_ref': 'AB-04a: Kasten 2'}),
                ('grammar', {'title': 'Lieblingsfach', 'blocks': [('Mi asignatura favorita es...', 'Mein Lieblingsfach ist...'), ('Me gusta el español.', 'Ich mag Spanisch.')]}),
                ('grammar', {'title': 'Meinungen', 'blocks': [('Es interesante.', 'Es ist interessant.'), ('Es aburrido/a.', 'Es ist langweilig.'), ('Es difícil/fácil.', 'Es ist schwer/leicht.')]}),
                ('vocab', {'title': 'Adjektive für Fächer', 'vocab': [('interesante', 'interessant'), ('aburrido/a', 'langweilig'), ('difícil', 'schwierig'), ('fácil', 'leicht')], 'ab_ref': 'AB-04a: Kasten 2'}),
                ('content', {'title': 'Beispieldialog', 'items': ['– ¿Cuál es tu asignatura favorita?', '– Mi asignatura favorita es el deporte.', '– ¿Por qué?', '– Porque es divertido.']}),
                ('exercise', {'title': 'Übung: Fächer zuordnen', 'exercises': [('Musik =', '___'), ('Geschichte =', '___'), ('Sport =', '___')], 'ab_ref': 'AB-04a: Aufgabe 1'}),
                ('exercise', {'title': 'Übung: Meinung äußern', 'exercises': [('Mathe ist schwer.', '___'), ('Spanisch ist interessant.', '___')], 'ab_ref': 'AB-04a: Aufgabe 2'}),
                ('solution', {'title': 'Lösung', 'solutions': [('Mathe ist schwer.', 'Las matemáticas son difíciles.'), ('Spanisch ist interessant.', 'El español es interesante.')]}),
                ('summary', {'title': 'Zusammenfassung', 'left_items': ['matemáticas, español, inglés', 'historia, música, deporte', 'Mi asignatura favorita es...'], 'right_items': ['interesante, aburrido/a', 'difícil, fácil', 'divertido/a']}),
                ('homework', {'tasks': ['Schulfächer auswendig lernen', 'Lieblingsfach beschreiben', 'AB-04a vollständig']}),
            ]},

    '04b': {'title': 'El horario', 'subtitle': 'Stundenplan und Uhrzeiten', 'sequenz': 4,
            'slides': [
                ('title', {'flags': '⏰'}),
                ('content', {'title': 'Lernziele', 'items': ['Wochentage auf Spanisch', 'Uhrzeiten angeben', 'Stundenplan beschreiben']}),
                ('vocab', {'title': 'Wochentage', 'vocab': [('lunes', 'Montag'), ('martes', 'Dienstag'), ('miércoles', 'Mittwoch'), ('jueves', 'Donnerstag')], 'ab_ref': 'AB-04b: Kasten 1'}),
                ('vocab', {'title': 'Wochentage (Fortsetzung)', 'vocab': [('viernes', 'Freitag'), ('sábado', 'Samstag'), ('domingo', 'Sonntag')], 'ab_ref': 'AB-04b: Kasten 1'}),
                ('grammar', {'title': 'Uhrzeiten: volle Stunde', 'blocks': [('¿Qué hora es?', 'Wie spät ist es?'), ('Es la una.', 'Es ist 1 Uhr.'), ('Son las dos.', 'Es ist 2 Uhr.')], 'info': 'la una (Sg.) aber las dos+ (Pl.)'}),
                ('grammar', {'title': 'Uhrzeiten: Minuten', 'blocks': [('Son las tres y media.', 'Es ist halb 4.'), ('Son las cuatro y cuarto.', 'Es ist Viertel nach 4.'), ('Son las cinco menos cuarto.', 'Es ist Viertel vor 5.')]}),
                ('grammar', {'title': 'Wann findet etwas statt?', 'blocks': [('a las ocho', 'um 8 Uhr'), ('El lunes a las nueve.', 'Montag um 9 Uhr.')]}),
                ('content', {'title': 'Stundenplan-Beispiel', 'items': ['Lunes a las 8:00 – Matemáticas', 'Lunes a las 9:00 – Inglés', 'Martes a las 8:00 – Español']}),
                ('exercise', {'title': 'Übung: Wochentage', 'exercises': [('Montag =', '___'), ('Freitag =', '___'), ('Sonntag =', '___')], 'ab_ref': 'AB-04b: Aufgabe 1'}),
                ('exercise', {'title': 'Übung: Uhrzeiten', 'exercises': [('8:00 =', '___'), ('3:30 =', '___'), ('4:15 =', '___')], 'ab_ref': 'AB-04b: Aufgabe 2'}),
                ('solution', {'title': 'Lösung', 'solutions': [('8:00', 'Son las ocho.'), ('3:30', 'Son las tres y media.'), ('4:15', 'Son las cuatro y cuarto.')]}),
                ('summary', {'title': 'Zusammenfassung', 'left_items': ['lunes, martes, miércoles', 'jueves, viernes', 'sábado, domingo'], 'right_items': ['Es la una. / Son las...', 'y media, y cuarto', 'menos cuarto']}),
                ('homework', {'tasks': ['Wochentage auswendig', 'Uhrzeiten üben', 'Deinen Stundenplan auf Spanisch']}),
            ]},

    '04c': {'title': 'Verbos en -ar', 'subtitle': 'Regelmäßige Verben', 'sequenz': 4,
            'slides': [
                ('title', {}),
                ('content', {'title': 'Lernziele', 'items': ['Regelmäßige -ar-Verben konjugieren', 'Endungen lernen', 'Sätze mit -ar-Verben bilden']}),
                ('grammar', {'title': 'Infinitiv und Stamm', 'blocks': [('hablar', 'Infinitiv = sprechen'), ('habl-', 'Stamm (ohne -ar)')], 'info': 'Endungen an den Stamm anhängen'}),
                ('grammar', {'title': 'hablar: Konjugation', 'blocks': [('yo hablo', 'ich spreche'), ('tú hablas', 'du sprichst'), ('él/ella habla', 'er/sie spricht')]}),
                ('grammar', {'title': 'hablar: Plural', 'blocks': [('nosotros hablamos', 'wir sprechen'), ('vosotros habláis', 'ihr sprecht'), ('ellos hablan', 'sie sprechen')]}),
                ('grammar', {'title': '-ar Endungen', 'blocks': [('-o, -as, -a', 'Singular'), ('-amos, -áis, -an', 'Plural')], 'info': 'Für ALLE -ar-Verben gleich!'}),
                ('vocab', {'title': '-ar-Verben', 'vocab': [('estudiar', 'lernen, studieren'), ('escuchar', 'hören, zuhören'), ('trabajar', 'arbeiten'), ('tocar', 'spielen (Instrument)')], 'ab_ref': 'AB-04c: Kasten 1'}),
                ('vocab', {'title': 'Mehr -ar-Verben', 'vocab': [('cantar', 'singen'), ('bailar', 'tanzen'), ('cocinar', 'kochen'), ('comprar', 'kaufen')], 'ab_ref': 'AB-04c: Kasten 1'}),
                ('content', {'title': 'Beispielsätze', 'items': ['Yo estudio español.', 'Tú escuchas música.', 'Ella trabaja en una oficina.', 'Nosotros cantamos bien.']}),
                ('exercise', {'title': 'Übung: Konjugieren', 'exercises': [('Yo ___ español. (estudiar)', '___'), ('Tú ___ música. (escuchar)', '___'), ('Ella ___ bien. (cantar)', '___')], 'ab_ref': 'AB-04c: Aufgabe 2'}),
                ('solution', {'title': 'Lösung', 'solutions': [('Yo estudio español.', '✓'), ('Tú escuchas música.', '✓'), ('Ella canta bien.', '✓')]}),
                ('summary', {'title': 'Zusammenfassung', 'left_items': ['-o, -as, -a', '-amos, -áis, -an', 'hablar, estudiar, escuchar'], 'right_items': ['trabajar, tocar', 'cantar, bailar', 'cocinar, comprar']}),
                ('homework', {'tasks': ['-ar-Endungen auswendig', '10 Sätze mit -ar-Verben schreiben', 'AB-04c vollständig']}),
            ]},

    '04d': {'title': 'Test: El colegio', 'subtitle': 'Minitest Sequenz 4', 'sequenz': 4,
            'slides': [
                ('title', {}),
                ('content', {'title': 'Sequenz 4: Rückblick', 'items': ['Lektion 4a: Schulfächer', 'Lektion 4b: Wochentage, Uhrzeiten', 'Lektion 4c: -ar-Verben']}),
                ('summary', {'title': 'Vokabeln Seq. 4', 'left_items': ['matemáticas, español, inglés', 'historia, música, deporte', 'lunes–domingo'], 'right_items': ['hablar, estudiar, escuchar', 'trabajar, cantar, bailar']}),
                ('grammar', {'title': 'Grammatik: -ar-Verben', 'blocks': [('-o, -as, -a', 'Singular'), ('-amos, -áis, -an', 'Plural')]}),
                ('grammar', {'title': 'Grammatik: Uhrzeiten', 'blocks': [('Es la una.', '1 Uhr'), ('Son las dos/tres...', '2, 3... Uhr'), ('y media / y cuarto', 'halb / Viertel')]}),
                ('content', {'title': 'Minitest: Überblick', 'items': ['Teil 1: Schulfächer (5 P)', 'Teil 2: Wochentage (4 P)', 'Teil 3: Uhrzeiten (6 P)', 'Teil 4: -ar-Verben konjugieren (8 P)', 'Teil 5: Sätze bilden (2 P)']}),
                ('exercise', {'title': 'Probe: Fächer', 'exercises': [('Mathematik =', '___'), ('Sport =', '___')], 'ab_ref': 'MT-04d'}),
                ('exercise', {'title': 'Probe: -ar-Verben', 'exercises': [('Yo ___ (hablar)', '___'), ('Ella ___ (estudiar)', '___')], 'ab_ref': 'MT-04d'}),
                ('content', {'title': 'Tipps für den Test', 'items': ['-ar-Endungen sicher können', 'Wochentage OHNE Artikel', 'Uhrzeiten: la una vs. las dos+']}),
                ('homework', {'tasks': ['Alle Vokabeln Seq. 4 wiederholen', '-ar-Konjugation üben', 'Uhrzeiten üben'], 'closing': '¡Buena suerte!'}),
            ]},

    # SEQUENZ 5: Tiempo libre
    '05a': {'title': 'Los hobbys', 'subtitle': 'Freizeitaktivitäten', 'sequenz': 5,
            'slides': [
                ('title', {'flags': '⚽🎸🎮'}),
                ('content', {'title': 'Lernziele', 'items': ['Hobbys benennen', 'Über Freizeit sprechen', 'jugar a / tocar unterscheiden']}),
                ('vocab', {'title': 'Sport', 'vocab': [('jugar al fútbol', 'Fußball spielen'), ('jugar al baloncesto', 'Basketball spielen'), ('nadar', 'schwimmen'), ('correr', 'laufen')], 'ab_ref': 'AB-05a: Kasten 1'}),
                ('vocab', {'title': 'Musik', 'vocab': [('tocar la guitarra', 'Gitarre spielen'), ('tocar el piano', 'Klavier spielen'), ('escuchar música', 'Musik hören'), ('cantar', 'singen')], 'ab_ref': 'AB-05a: Kasten 1'}),
                ('vocab', {'title': 'Weitere Hobbys', 'vocab': [('ver la tele', 'fernsehen'), ('leer libros', 'Bücher lesen'), ('jugar a videojuegos', 'Videospiele spielen'), ('dibujar', 'zeichnen')], 'ab_ref': 'AB-05a: Kasten 2'}),
                ('grammar', {'title': 'jugar a + Artikel', 'blocks': [('jugar al fútbol', 'Fußball spielen'), ('jugar a la pelota', 'Ball spielen')], 'info': 'a + el = al'}),
                ('grammar', {'title': 'tocar + Artikel', 'blocks': [('tocar la guitarra', 'Gitarre spielen'), ('tocar el piano', 'Klavier spielen')], 'info': 'Instrumente mit tocar'}),
                ('content', {'title': 'Beispieldialog', 'items': ['– ¿Qué haces en tu tiempo libre?', '– Juego al fútbol y toco la guitarra.', '– ¿Y tú?', '– Me gusta leer libros.']}),
                ('exercise', {'title': 'Übung: jugar oder tocar?', 'exercises': [('___ al tenis', '___'), ('___ el violín', '___'), ('___ a videojuegos', '___')], 'ab_ref': 'AB-05a: Aufgabe 1'}),
                ('solution', {'title': 'Lösung', 'solutions': [('Jugar al tenis', '✓'), ('Tocar el violín', '✓'), ('Jugar a videojuegos', '✓')]}),
                ('exercise', {'title': 'Übung: Übersetzen', 'exercises': [('Ich spiele Fußball.', '___'), ('Sie spielt Gitarre.', '___')], 'ab_ref': 'AB-05a: Aufgabe 2'}),
                ('summary', {'title': 'Zusammenfassung', 'left_items': ['jugar al fútbol/baloncesto', 'tocar la guitarra/el piano', 'ver la tele, leer libros'], 'right_items': ['jugar a + Sport/Spiel', 'tocar + Instrument', 'nadar, correr, dibujar']}),
                ('homework', {'tasks': ['Hobby-Vokabeln lernen', 'Deine Hobbys aufschreiben', 'AB-05a vollständig']}),
            ]},

    '05b': {'title': 'Verbos en -er/-ir', 'subtitle': 'Weitere Verben', 'sequenz': 5,
            'slides': [
                ('title', {}),
                ('content', {'title': 'Lernziele', 'items': ['Regelmäßige -er-Verben', 'Regelmäßige -ir-Verben', 'Unterschied zu -ar-Verben']}),
                ('grammar', {'title': 'comer (essen): Konjugation', 'blocks': [('yo como', 'ich esse'), ('tú comes', 'du isst'), ('él/ella come', 'er/sie isst')]}),
                ('grammar', {'title': 'comer: Plural', 'blocks': [('nosotros comemos', 'wir essen'), ('vosotros coméis', 'ihr esst'), ('ellos comen', 'sie essen')]}),
                ('grammar', {'title': '-er Endungen', 'blocks': [('-o, -es, -e', 'Singular'), ('-emos, -éis, -en', 'Plural')], 'info': 'Ähnlich wie -ar, aber -e- statt -a-'}),
                ('grammar', {'title': 'vivir (leben): Konjugation', 'blocks': [('yo vivo', 'ich lebe'), ('tú vives', 'du lebst'), ('él/ella vive', 'er/sie lebt')]}),
                ('grammar', {'title': '-ir Endungen', 'blocks': [('-o, -es, -e', 'Singular'), ('-imos, -ís, -en', 'Plural')], 'info': 'Fast wie -er, nur 1./2. Pl. anders'}),
                ('vocab', {'title': '-er-Verben', 'vocab': [('comer', 'essen'), ('beber', 'trinken'), ('leer', 'lesen'), ('comprender', 'verstehen')], 'ab_ref': 'AB-05b: Kasten 1'}),
                ('vocab', {'title': '-ir-Verben', 'vocab': [('vivir', 'leben, wohnen'), ('escribir', 'schreiben'), ('abrir', 'öffnen'), ('subir', 'hochgehen')], 'ab_ref': 'AB-05b: Kasten 1'}),
                ('exercise', {'title': 'Übung: -er konjugieren', 'exercises': [('Yo ___ pizza. (comer)', '___'), ('Tú ___ agua. (beber)', '___')], 'ab_ref': 'AB-05b: Aufgabe 2'}),
                ('exercise', {'title': 'Übung: -ir konjugieren', 'exercises': [('Yo ___ en Rostock. (vivir)', '___'), ('Ella ___ una carta. (escribir)', '___')], 'ab_ref': 'AB-05b: Aufgabe 3'}),
                ('solution', {'title': 'Lösung', 'solutions': [('Yo como pizza.', '✓'), ('Tú bebes agua.', '✓'), ('Yo vivo en Rostock.', '✓'), ('Ella escribe una carta.', '✓')]}),
                ('summary', {'title': 'Zusammenfassung', 'left_items': ['-er: -o, -es, -e', '-emos, -éis, -en', 'comer, beber, leer'], 'right_items': ['-ir: -o, -es, -e', '-imos, -ís, -en', 'vivir, escribir']}),
                ('homework', {'tasks': ['-er und -ir Endungen lernen', '10 Sätze schreiben', 'AB-05b vollständig']}),
            ]},

    '05c': {'title': 'Me gusta...', 'subtitle': 'Vorlieben mit gustar', 'sequenz': 5,
            'slides': [
                ('title', {'flags': '❤️'}),
                ('content', {'title': 'Lernziele', 'items': ['gustar = gefallen', 'gusta vs. gustan', 'Vorlieben ausdrücken']}),
                ('grammar', {'title': 'gustar = gefallen', 'blocks': [('Me gusta el fútbol.', 'Mir gefällt Fußball.'), ('Me gusta leer.', 'Mir gefällt (es) zu lesen.')], 'info': 'Das Subjekt gefällt MIR'}),
                ('grammar', {'title': 'gusta vs. gustan', 'blocks': [('Me gusta el libro.', 'Singular → gusta'), ('Me gustan los libros.', 'Plural → gustan')], 'info': 'Verb richtet sich nach dem Subjekt!'}),
                ('grammar', {'title': 'Pronomen', 'blocks': [('me gusta', 'mir gefällt'), ('te gusta', 'dir gefällt'), ('le gusta', 'ihm/ihr gefällt')], 'info': 'nos, os, les für Plural'}),
                ('vocab', {'title': 'Abstufungen', 'vocab': [('Me encanta...', 'Ich liebe...'), ('Me gusta mucho...', 'Ich mag sehr...'), ('No me gusta...', 'Ich mag nicht...')], 'ab_ref': 'AB-05c: Kasten 1'}),
                ('vocab', {'title': 'Meinungen', 'vocab': [('Me gusta bastante.', 'Ich mag es ziemlich.'), ('No me gusta nada.', 'Ich mag es gar nicht.'), ('Me da igual.', 'Es ist mir egal.')], 'ab_ref': 'AB-05c: Kasten 1'}),
                ('content', {'title': 'Beispiele', 'items': ['Me gusta la música.', 'Me gustan los deportes.', 'No me gusta estudiar.', 'A María le gusta bailar.']}),
                ('exercise', {'title': 'Übung: gusta oder gustan?', 'exercises': [('Me ___ la pizza.', '___'), ('Me ___ los videojuegos.', '___'), ('Te ___ leer.', '___')], 'ab_ref': 'AB-05c: Aufgabe 2'}),
                ('solution', {'title': 'Lösung', 'solutions': [('Me gusta la pizza.', '✓'), ('Me gustan los videojuegos.', '✓'), ('Te gusta leer.', '✓')]}),
                ('exercise', {'title': 'Übung: Übersetzen', 'exercises': [('Ich mag Fußball.', '___'), ('Sie mag nicht Mathe.', '___')], 'ab_ref': 'AB-05c: Aufgabe 3'}),
                ('summary', {'title': 'Zusammenfassung', 'left_items': ['gusta + Singular/Infinitiv', 'gustan + Plural', 'me, te, le, nos, os, les'], 'right_items': ['Me encanta...', 'Me gusta mucho...', 'No me gusta nada...']}),
                ('homework', {'tasks': ['gustar-Struktur lernen', 'Deine Vorlieben aufschreiben', 'AB-05c vollständig']}),
            ]},

    '05d': {'title': 'Test: Tiempo libre', 'subtitle': 'Minitest Sequenz 5', 'sequenz': 5,
            'slides': [
                ('title', {}),
                ('content', {'title': 'Sequenz 5: Rückblick', 'items': ['Lektion 5a: Hobbys', 'Lektion 5b: -er/-ir-Verben', 'Lektion 5c: gustar']}),
                ('summary', {'title': 'Vokabeln Seq. 5', 'left_items': ['jugar al fútbol, nadar', 'tocar la guitarra', 'ver la tele, leer'], 'right_items': ['comer, beber, vivir', 'escribir, leer', 'Me gusta/gustan...']}),
                ('grammar', {'title': 'Grammatik: -er/-ir', 'blocks': [('-er: -o, -es, -e, -emos, -éis, -en', ''), ('-ir: -o, -es, -e, -imos, -ís, -en', '')]}),
                ('grammar', {'title': 'Grammatik: gustar', 'blocks': [('gusta + Singular', 'Me gusta el libro.'), ('gustan + Plural', 'Me gustan los libros.')]}),
                ('content', {'title': 'Minitest: Überblick', 'items': ['Teil 1: Hobby-Vokabeln (6 P)', 'Teil 2: -er/-ir konjugieren (6 P)', 'Teil 3: gustar-Sätze (8 P)', 'Teil 4: Freizeit beschreiben (5 P)']}),
                ('exercise', {'title': 'Probe: Hobbys', 'exercises': [('Fußball spielen =', '___'), ('Gitarre spielen =', '___')], 'ab_ref': 'MT-05d'}),
                ('exercise', {'title': 'Probe: gustar', 'exercises': [('Mir gefällt Musik. =', '___'), ('Mir gefallen Bücher. =', '___')], 'ab_ref': 'MT-05d'}),
                ('content', {'title': 'Tipps für den Test', 'items': ['jugar a vs. tocar beachten', 'gustar: Verb nach Subjekt richten', 'Infinitiv → gusta (Sg.)']}),
                ('homework', {'tasks': ['Alle Vokabeln Seq. 5 wiederholen', '-er/-ir Endungen üben', 'gustar-Sätze üben'], 'closing': '¡Buena suerte!'}),
            ]},

    # SEQUENZ 6: La ciudad
    '06a': {'title': 'Los lugares', 'subtitle': 'Orte in der Stadt', 'sequenz': 6,
            'slides': [
                ('title', {'flags': '🏙️'}),
                ('content', {'title': 'Lernziele', 'items': ['Orte in der Stadt benennen', 'Einkaufsorte kennen', 'Freizeitorte kennen']}),
                ('vocab', {'title': 'Zentrale Orte', 'vocab': [('el centro', 'das Zentrum'), ('la plaza', 'der Platz'), ('la calle', 'die Straße'), ('el parque', 'der Park')], 'ab_ref': 'AB-06a: Kasten 1'}),
                ('vocab', {'title': 'Einkaufen', 'vocab': [('el supermercado', 'der Supermarkt'), ('la tienda', 'das Geschäft'), ('el mercado', 'der Markt'), ('el centro comercial', 'das Einkaufszentrum')], 'ab_ref': 'AB-06a: Kasten 1'}),
                ('vocab', {'title': 'Freizeit', 'vocab': [('el cine', 'das Kino'), ('el teatro', 'das Theater'), ('el museo', 'das Museum'), ('la piscina', 'das Schwimmbad')], 'ab_ref': 'AB-06a: Kasten 2'}),
                ('vocab', {'title': 'Öffentliche Orte', 'vocab': [('la biblioteca', 'die Bibliothek'), ('el hospital', 'das Krankenhaus'), ('la estación', 'der Bahnhof'), ('el aeropuerto', 'der Flughafen')], 'ab_ref': 'AB-06a: Kasten 2'}),
                ('vocab', {'title': 'Weitere Orte', 'vocab': [('la iglesia', 'die Kirche'), ('el restaurante', 'das Restaurant'), ('el banco', 'die Bank'), ('la farmacia', 'die Apotheke')], 'ab_ref': 'AB-06a: Kasten 2'}),
                ('exercise', {'title': 'Übung: Was macht man wo?', 'exercises': [('Filme sehen →', '___'), ('Bücher leihen →', '___'), ('Einkaufen →', '___')], 'ab_ref': 'AB-06a: Aufgabe 1'}),
                ('solution', {'title': 'Lösung', 'solutions': [('Filme sehen', 'el cine'), ('Bücher leihen', 'la biblioteca'), ('Einkaufen', 'el supermercado')]}),
                ('exercise', {'title': 'Übung: Übersetzen', 'exercises': [('der Bahnhof =', '___'), ('das Krankenhaus =', '___')], 'ab_ref': 'AB-06a: Aufgabe 2'}),
                ('summary', {'title': 'Zusammenfassung', 'left_items': ['centro, plaza, calle', 'supermercado, tienda', 'cine, museo, piscina'], 'right_items': ['biblioteca, hospital', 'estación, aeropuerto', 'restaurante, banco']}),
                ('homework', {'tasks': ['Ortsvokabeln lernen', 'Orte in deiner Stadt', 'AB-06a vollständig']}),
            ]},

    '06b': {'title': 'Ir y estar', 'subtitle': 'Gehen und sein', 'sequenz': 6,
            'slides': [
                ('title', {}),
                ('content', {'title': 'Lernziele', 'items': ['ir (gehen) konjugieren', 'estar (sich befinden) konjugieren', 'ir a vs. estar en']}),
                ('grammar', {'title': 'ir (gehen): Konjugation', 'blocks': [('yo voy', 'ich gehe'), ('tú vas', 'du gehst'), ('él/ella va', 'er/sie geht')], 'info': 'Unregelmäßig!'}),
                ('grammar', {'title': 'ir: Plural', 'blocks': [('nosotros vamos', 'wir gehen'), ('vosotros vais', 'ihr geht'), ('ellos van', 'sie gehen')]}),
                ('grammar', {'title': 'ir a + Ort', 'blocks': [('Voy al cine.', 'Ich gehe ins Kino.'), ('Vamos a la playa.', 'Wir gehen zum Strand.')], 'info': 'a + el = al'}),
                ('grammar', {'title': 'estar (sich befinden)', 'blocks': [('yo estoy', 'ich bin'), ('tú estás', 'du bist'), ('él/ella está', 'er/sie ist')]}),
                ('grammar', {'title': 'estar: Plural', 'blocks': [('nosotros estamos', 'wir sind'), ('vosotros estáis', 'ihr seid'), ('ellos están', 'sie sind')]}),
                ('grammar', {'title': 'estar en + Ort', 'blocks': [('Estoy en casa.', 'Ich bin zu Hause.'), ('Está en el parque.', 'Er ist im Park.')], 'info': 'estar = Ort, ser = Eigenschaft'}),
                ('content', {'title': 'Zusammenfassung ir vs. estar', 'items': ['ir a = wohin? (Bewegung)', 'estar en = wo? (Ort)', 'Voy al cine. Estoy en el cine.']}),
                ('exercise', {'title': 'Übung: ir oder estar?', 'exercises': [('___ al supermercado. (ich gehe)', '___'), ('___ en casa. (ich bin)', '___')], 'ab_ref': 'AB-06b: Aufgabe 2'}),
                ('solution', {'title': 'Lösung', 'solutions': [('Voy al supermercado.', '✓'), ('Estoy en casa.', '✓')]}),
                ('exercise', {'title': 'Übung: Übersetzen', 'exercises': [('Wir gehen ins Kino.', '___'), ('Sie ist im Park.', '___')], 'ab_ref': 'AB-06b: Aufgabe 3'}),
                ('summary', {'title': 'Zusammenfassung', 'left_items': ['voy, vas, va', 'vamos, vais, van', 'ir a + Ort'], 'right_items': ['estoy, estás, está', 'estamos, estáis, están', 'estar en + Ort']}),
                ('homework', {'tasks': ['ir und estar konjugieren', 'Sätze mit ir a / estar en', 'AB-06b vollständig']}),
            ]},

    '06c': {'title': 'Las direcciones', 'subtitle': 'Wegbeschreibungen', 'sequenz': 6,
            'slides': [
                ('title', {'flags': '🧭'}),
                ('content', {'title': 'Lernziele', 'items': ['Nach dem Weg fragen', 'Richtungen verstehen', 'Wegbeschreibung geben']}),
                ('vocab', {'title': 'Richtungen', 'vocab': [('a la derecha', 'rechts'), ('a la izquierda', 'links'), ('todo recto', 'geradeaus'), ('al final', 'am Ende')], 'ab_ref': 'AB-06c: Kasten 1'}),
                ('vocab', {'title': 'Orientierung', 'vocab': [('la primera calle', 'die erste Straße'), ('la segunda calle', 'die zweite Straße'), ('en la esquina', 'an der Ecke'), ('al lado de', 'neben')], 'ab_ref': 'AB-06c: Kasten 1'}),
                ('vocab', {'title': 'Präpositionen', 'vocab': [('delante de', 'vor'), ('detrás de', 'hinter'), ('entre', 'zwischen'), ('cerca de', 'in der Nähe von')], 'ab_ref': 'AB-06c: Kasten 2'}),
                ('grammar', {'title': 'Nach dem Weg fragen', 'blocks': [('¿Dónde está...?', 'Wo ist...?'), ('¿Cómo llego a...?', 'Wie komme ich zu...?'), ('¿Hay un banco cerca?', 'Gibt es eine Bank in der Nähe?')]}),
                ('grammar', {'title': 'Imperativ (Höflich)', 'blocks': [('Siga todo recto.', 'Gehen Sie geradeaus.'), ('Gire a la derecha.', 'Biegen Sie rechts ab.'), ('Tome la primera calle.', 'Nehmen Sie die erste Straße.')]}),
                ('content', {'title': 'Beispieldialog', 'items': ['– Perdone, ¿dónde está el banco?', '– Siga todo recto y gire a la derecha.', '– El banco está al lado de la farmacia.', '– Muchas gracias.']}),
                ('exercise', {'title': 'Übung: Richtungen', 'exercises': [('rechts =', '___'), ('geradeaus =', '___'), ('an der Ecke =', '___')], 'ab_ref': 'AB-06c: Aufgabe 1'}),
                ('exercise', {'title': 'Übung: Wegbeschreibung', 'exercises': [('Zum Kino:', '___')], 'ab_ref': 'AB-06c: Aufgabe 2'}),
                ('summary', {'title': 'Zusammenfassung', 'left_items': ['a la derecha/izquierda', 'todo recto, al final', '¿Dónde está...?'], 'right_items': ['delante de, detrás de', 'al lado de, cerca de', 'Siga, Gire, Tome']}),
                ('homework', {'tasks': ['Richtungsvokabeln lernen', 'Wegbeschreibung üben', 'AB-06c vollständig']}),
            ]},

    '06d': {'title': 'Test: La ciudad', 'subtitle': 'Minitest Sequenz 6', 'sequenz': 6,
            'slides': [
                ('title', {}),
                ('content', {'title': 'Sequenz 6: Rückblick', 'items': ['Lektion 6a: Orte in der Stadt', 'Lektion 6b: ir und estar', 'Lektion 6c: Wegbeschreibungen']}),
                ('summary', {'title': 'Vokabeln Seq. 6', 'left_items': ['centro, cine, museo', 'supermercado, biblioteca', 'estación, hospital'], 'right_items': ['a la derecha/izquierda', 'todo recto, al final', 'delante de, detrás de']}),
                ('grammar', {'title': 'Grammatik: ir vs. estar', 'blocks': [('ir a + Ort', 'Bewegung (wohin?)'), ('estar en + Ort', 'Position (wo?)'), ('a + el = al', '')]}),
                ('content', {'title': 'Minitest: Überblick', 'items': ['Teil 1: Ortsvokabeln (6 P)', 'Teil 2: ir konjugieren (4 P)', 'Teil 3: estar konjugieren (4 P)', 'Teil 4: Richtungen (6 P)', 'Teil 5: Wegbeschreibung (5 P)']}),
                ('exercise', {'title': 'Probe: Orte', 'exercises': [('Kino =', '___'), ('Bibliothek =', '___')], 'ab_ref': 'MT-06d'}),
                ('exercise', {'title': 'Probe: ir/estar', 'exercises': [('Yo ___ al cine. (ir)', '___'), ('Ella ___ en casa. (estar)', '___')], 'ab_ref': 'MT-06d'}),
                ('content', {'title': 'Tipps für den Test', 'items': ['ir a vs. estar en unterscheiden', 'a + el = al nicht vergessen', 'Richtungen mit Artikeln']}),
                ('homework', {'tasks': ['Alle Vokabeln Seq. 6 wiederholen', 'ir und estar üben', 'Wegbeschreibung üben'], 'closing': '¡Buena suerte!'}),
            ]},

    # SEQUENZ 7: Las compras
    '07a': {'title': 'La comida', 'subtitle': 'Lebensmittel', 'sequenz': 7,
            'slides': [
                ('title', {'flags': '🍎🥖🧀'}),
                ('content', {'title': 'Lernziele', 'items': ['Lebensmittel benennen', 'Getränke kennen', 'Mahlzeiten beschreiben']}),
                ('vocab', {'title': 'Grundnahrungsmittel', 'vocab': [('el pan', 'das Brot'), ('el arroz', 'der Reis'), ('la pasta', 'die Nudeln'), ('el huevo', 'das Ei')], 'ab_ref': 'AB-07a: Kasten 1'}),
                ('vocab', {'title': 'Obst & Gemüse', 'vocab': [('la fruta', 'das Obst'), ('la manzana', 'der Apfel'), ('el plátano', 'die Banane'), ('la verdura', 'das Gemüse')], 'ab_ref': 'AB-07a: Kasten 1'}),
                ('vocab', {'title': 'Fleisch & Fisch', 'vocab': [('la carne', 'das Fleisch'), ('el pollo', 'das Hähnchen'), ('el pescado', 'der Fisch'), ('el jamón', 'der Schinken')], 'ab_ref': 'AB-07a: Kasten 2'}),
                ('vocab', {'title': 'Milchprodukte', 'vocab': [('la leche', 'die Milch'), ('el queso', 'der Käse'), ('el yogur', 'der Joghurt'), ('la mantequilla', 'die Butter')], 'ab_ref': 'AB-07a: Kasten 2'}),
                ('vocab', {'title': 'Getränke', 'vocab': [('el agua', 'das Wasser'), ('el zumo', 'der Saft'), ('el café', 'der Kaffee'), ('el té', 'der Tee')], 'ab_ref': 'AB-07a: Kasten 2'}),
                ('content', {'title': 'Mahlzeiten', 'items': ['el desayuno – das Frühstück', 'la comida / el almuerzo – das Mittagessen', 'la cena – das Abendessen']}),
                ('exercise', {'title': 'Übung: Kategorisieren', 'exercises': [('Obst:', '___'), ('Fleisch:', '___'), ('Getränk:', '___')], 'ab_ref': 'AB-07a: Aufgabe 1'}),
                ('exercise', {'title': 'Übung: Übersetzen', 'exercises': [('das Brot =', '___'), ('der Käse =', '___'), ('der Saft =', '___')], 'ab_ref': 'AB-07a: Aufgabe 2'}),
                ('summary', {'title': 'Zusammenfassung', 'left_items': ['pan, arroz, pasta, huevo', 'fruta, verdura, carne', 'pollo, pescado, jamón'], 'right_items': ['leche, queso, yogur', 'agua, zumo, café', 'desayuno, comida, cena']}),
                ('homework', {'tasks': ['Lebensmittelvokabeln lernen', 'Was isst du zum Frühstück?', 'AB-07a vollständig']}),
            ]},

    '07b': {'title': 'Los números', 'subtitle': 'Zahlen 20–100', 'sequenz': 7,
            'slides': [
                ('title', {'flags': '💶'}),
                ('content', {'title': 'Lernziele', 'items': ['Zahlen bis 100', 'Preise verstehen', 'Einkaufsgespräche führen']}),
                ('vocab', {'title': 'Zehner', 'vocab': [('veinte', '20'), ('treinta', '30'), ('cuarenta', '40'), ('cincuenta', '50')], 'ab_ref': 'AB-07b: Kasten 1'}),
                ('vocab', {'title': 'Zehner (Fortsetzung)', 'vocab': [('sesenta', '60'), ('setenta', '70'), ('ochenta', '80'), ('noventa', '90')], 'ab_ref': 'AB-07b: Kasten 1'}),
                ('grammar', {'title': 'Zusammengesetzte Zahlen', 'blocks': [('veintiuno (21)', 'veinti + uno'), ('treinta y dos (32)', 'treinta + y + dos')], 'info': '21-29 ein Wort, ab 30 mit "y"'}),
                ('vocab', {'title': 'Besondere Zahlen', 'vocab': [('cien', '100'), ('ciento uno', '101'), ('doscientos', '200')], 'ab_ref': 'AB-07b: Kasten 2'}),
                ('grammar', {'title': 'Preise fragen', 'blocks': [('¿Cuánto cuesta?', 'Wie viel kostet es?'), ('¿Cuánto cuestan?', 'Wie viel kosten sie?')], 'info': 'cuesta (Sg.) / cuestan (Pl.)'}),
                ('grammar', {'title': 'Preise angeben', 'blocks': [('Cuesta dos euros.', 'Es kostet 2€.'), ('Cuestan cinco euros.', 'Sie kosten 5€.'), ('Cuesta tres euros con cincuenta.', '3,50€')]}),
                ('content', {'title': 'Einkaufsdialog', 'items': ['– Buenos días. ¿Cuánto cuesta el pan?', '– Cuesta un euro con veinte.', '– ¿Y el queso?', '– El queso cuesta tres euros.']}),
                ('exercise', {'title': 'Übung: Zahlen', 'exercises': [('25 =', '___'), ('47 =', '___'), ('83 =', '___')], 'ab_ref': 'AB-07b: Aufgabe 1'}),
                ('solution', {'title': 'Lösung', 'solutions': [('25', 'veinticinco'), ('47', 'cuarenta y siete'), ('83', 'ochenta y tres')]}),
                ('exercise', {'title': 'Übung: Preise', 'exercises': [('2,50€ =', '___'), ('4,75€ =', '___')], 'ab_ref': 'AB-07b: Aufgabe 2'}),
                ('summary', {'title': 'Zusammenfassung', 'left_items': ['20-29: veinti...', '30-99: ... y ...', 'cien, ciento...'], 'right_items': ['¿Cuánto cuesta?', 'Cuesta ... euros.', 'con = Komma']}),
                ('homework', {'tasks': ['Zahlen 20-100 üben', 'Preise lesen können', 'AB-07b vollständig']}),
            ]},

    '07c': {'title': 'Querer y poder', 'subtitle': 'Wollen und können', 'sequenz': 7,
            'slides': [
                ('title', {}),
                ('content', {'title': 'Lernziele', 'items': ['querer (wollen) konjugieren', 'poder (können) konjugieren', 'Stammwechsel verstehen']}),
                ('grammar', {'title': 'querer: Stammwechsel e→ie', 'blocks': [('yo quiero', 'ich will'), ('tú quieres', 'du willst'), ('él/ella quiere', 'er/sie will')], 'info': 'e wird zu ie!'}),
                ('grammar', {'title': 'querer: Plural', 'blocks': [('nosotros queremos', 'wir wollen'), ('vosotros queréis', 'ihr wollt'), ('ellos quieren', 'sie wollen')], 'info': '1. + 2. Plural: KEIN Wechsel'}),
                ('grammar', {'title': 'poder: Stammwechsel o→ue', 'blocks': [('yo puedo', 'ich kann'), ('tú puedes', 'du kannst'), ('él/ella puede', 'er/sie kann')], 'info': 'o wird zu ue!'}),
                ('grammar', {'title': 'poder: Plural', 'blocks': [('nosotros podemos', 'wir können'), ('vosotros podéis', 'ihr könnt'), ('ellos pueden', 'sie können')]}),
                ('grammar', {'title': 'Verwendung', 'blocks': [('querer + Infinitiv', 'Quiero comprar pan.'), ('poder + Infinitiv', 'Puedo pagar con tarjeta.')]}),
                ('vocab', {'title': 'Einkaufsdialog', 'vocab': [('Quiero un kilo de...', 'Ich möchte 1kg...'), ('¿Puedo pagar con tarjeta?', 'Kann ich mit Karte zahlen?'), ('¿Algo más?', 'Sonst noch etwas?')], 'ab_ref': 'AB-07c: Dialog'}),
                ('content', {'title': 'Beispieldialog', 'items': ['– Buenos días. ¿Qué quiere?', '– Quiero medio kilo de manzanas.', '– ¿Algo más?', '– No, gracias. ¿Puedo pagar con tarjeta?', '– Sí, claro.']}),
                ('exercise', {'title': 'Übung: querer/poder', 'exercises': [('Yo ___ comprar pan. (querer)', '___'), ('Tú ___ hablar español. (poder)', '___')], 'ab_ref': 'AB-07c: Aufgabe 2'}),
                ('solution', {'title': 'Lösung', 'solutions': [('Yo quiero comprar pan.', '✓'), ('Tú puedes hablar español.', '✓')]}),
                ('summary', {'title': 'Zusammenfassung', 'left_items': ['querer: e→ie', 'quiero, quieres, quiere', 'queremos, queréis, quieren'], 'right_items': ['poder: o→ue', 'puedo, puedes, puede', 'podemos, podéis, pueden']}),
                ('homework', {'tasks': ['querer und poder konjugieren', 'Stammwechsel lernen', 'AB-07c vollständig']}),
            ]},

    '07d': {'title': 'Test: Las compras', 'subtitle': 'Minitest Sequenz 7', 'sequenz': 7,
            'slides': [
                ('title', {}),
                ('content', {'title': 'Sequenz 7: Rückblick', 'items': ['Lektion 7a: Lebensmittel', 'Lektion 7b: Zahlen, Preise', 'Lektion 7c: querer, poder']}),
                ('summary', {'title': 'Vokabeln Seq. 7', 'left_items': ['pan, arroz, huevo', 'fruta, verdura, carne', 'leche, queso, agua'], 'right_items': ['veinte...noventa', '¿Cuánto cuesta?', 'Quiero..., Puedo...']}),
                ('grammar', {'title': 'Stammwechsel', 'blocks': [('querer: e→ie', 'quiero, quieres, quiere'), ('poder: o→ue', 'puedo, puedes, puede')]}),
                ('content', {'title': 'Minitest: Überblick', 'items': ['Teil 1: Lebensmittel (6 P)', 'Teil 2: Zahlen 20-100 (5 P)', 'Teil 3: Preise verstehen (4 P)', 'Teil 4: querer/poder konjugieren (6 P)', 'Teil 5: Einkaufsdialog (4 P)']}),
                ('exercise', {'title': 'Probe: Lebensmittel', 'exercises': [('Brot =', '___'), ('Milch =', '___')], 'ab_ref': 'MT-07d'}),
                ('exercise', {'title': 'Probe: querer/poder', 'exercises': [('Yo ___ (querer)', '___'), ('Tú ___ (poder)', '___')], 'ab_ref': 'MT-07d'}),
                ('content', {'title': 'Tipps für den Test', 'items': ['Stammwechsel nur im Singular + 3. Pl.', 'Preise: cuesta/cuestan', 'Zahlen: 21-29 ein Wort']}),
                ('homework', {'tasks': ['Alle Vokabeln Seq. 7 wiederholen', 'Stammwechselverben üben', 'Zahlen üben'], 'closing': '¡Buena suerte!'}),
            ]},

    # SEQUENZ 8: Las vacaciones
    '08a': {'title': 'Viajar', 'subtitle': 'Reisen', 'sequenz': 8,
            'slides': [
                ('title', {'flags': '✈️🚗🚂'}),
                ('content', {'title': 'Lernziele', 'items': ['Verkehrsmittel benennen', 'Reiseziele beschreiben', 'ir en + Verkehrsmittel']}),
                ('vocab', {'title': 'Verkehrsmittel', 'vocab': [('el avión', 'das Flugzeug'), ('el tren', 'der Zug'), ('el coche', 'das Auto'), ('el autobús', 'der Bus')], 'ab_ref': 'AB-08a: Kasten 1'}),
                ('vocab', {'title': 'Weitere Verkehrsmittel', 'vocab': [('el barco', 'das Schiff'), ('la bicicleta', 'das Fahrrad'), ('el metro', 'die U-Bahn'), ('a pie', 'zu Fuß')], 'ab_ref': 'AB-08a: Kasten 1'}),
                ('grammar', {'title': 'Reisen mit...', 'blocks': [('Voy en avión.', 'Ich fliege. (mit Flugzeug)'), ('Voy en tren.', 'Ich fahre mit dem Zug.'), ('Voy a pie.', 'Ich gehe zu Fuß.')], 'info': 'ir + en + Verkehrsmittel'}),
                ('vocab', {'title': 'Reiseziele', 'vocab': [('la playa', 'der Strand'), ('la montaña', 'das Gebirge'), ('la ciudad', 'die Stadt'), ('el campo', 'das Land')], 'ab_ref': 'AB-08a: Kasten 2'}),
                ('vocab', {'title': 'Unterkunft', 'vocab': [('el hotel', 'das Hotel'), ('el apartamento', 'die Ferienwohnung'), ('el camping', 'der Campingplatz')], 'ab_ref': 'AB-08a: Kasten 2'}),
                ('content', {'title': 'Beispielsätze', 'items': ['Voy a España en avión.', 'Mis padres van a Italia en coche.', 'Nos quedamos en un hotel.', 'La playa es muy bonita.']}),
                ('exercise', {'title': 'Übung: Verkehrsmittel', 'exercises': [('Mit dem Zug =', '___'), ('Mit dem Auto =', '___'), ('Zu Fuß =', '___')], 'ab_ref': 'AB-08a: Aufgabe 1'}),
                ('solution', {'title': 'Lösung', 'solutions': [('Mit dem Zug', 'en tren'), ('Mit dem Auto', 'en coche'), ('Zu Fuß', 'a pie')]}),
                ('exercise', {'title': 'Übung: Übersetzen', 'exercises': [('Ich fliege nach Spanien.', '___'), ('Wir fahren ans Meer.', '___')], 'ab_ref': 'AB-08a: Aufgabe 2'}),
                ('summary', {'title': 'Zusammenfassung', 'left_items': ['avión, tren, coche', 'autobús, barco, bicicleta', 'ir en + Verkehrsmittel'], 'right_items': ['playa, montaña, ciudad', 'hotel, apartamento', 'a pie = zu Fuß']}),
                ('homework', {'tasks': ['Verkehrsmittel lernen', 'Reiseziel beschreiben', 'AB-08a vollständig']}),
            ]},

    '08b': {'title': 'El tiempo', 'subtitle': 'Das Wetter', 'sequenz': 8,
            'slides': [
                ('title', {'flags': '☀️🌧️❄️'}),
                ('content', {'title': 'Lernziele', 'items': ['Wetter beschreiben', 'hacer + Wetter', 'Jahreszeiten kennen']}),
                ('grammar', {'title': 'Wetter mit hace', 'blocks': [('Hace sol.', 'Die Sonne scheint.'), ('Hace calor.', 'Es ist heiß.'), ('Hace frío.', 'Es ist kalt.')], 'info': 'hace = es macht'}),
                ('grammar', {'title': 'Wetter mit hace (2)', 'blocks': [('Hace buen tiempo.', 'Das Wetter ist gut.'), ('Hace mal tiempo.', 'Das Wetter ist schlecht.'), ('Hace viento.', 'Es ist windig.')]}),
                ('grammar', {'title': 'Wetter ohne hace', 'blocks': [('Llueve.', 'Es regnet.'), ('Nieva.', 'Es schneit.'), ('Está nublado.', 'Es ist bewölkt.')], 'info': 'Eigene Verben/estar'}),
                ('vocab', {'title': 'Wettervokabeln', 'vocab': [('el sol', 'die Sonne'), ('la lluvia', 'der Regen'), ('la nieve', 'der Schnee'), ('la nube', 'die Wolke')], 'ab_ref': 'AB-08b: Kasten 1'}),
                ('vocab', {'title': 'Jahreszeiten', 'vocab': [('la primavera', 'der Frühling'), ('el verano', 'der Sommer'), ('el otoño', 'der Herbst'), ('el invierno', 'der Winter')], 'ab_ref': 'AB-08b: Kasten 2'}),
                ('grammar', {'title': 'Wetter fragen', 'blocks': [('¿Qué tiempo hace?', 'Wie ist das Wetter?'), ('¿Hace calor o frío?', 'Ist es heiß oder kalt?')]}),
                ('content', {'title': 'Beispieldialog', 'items': ['– ¿Qué tiempo hace en España?', '– En verano hace mucho calor.', '– ¿Y en invierno?', '– Hace frío, pero no nieva mucho.']}),
                ('exercise', {'title': 'Übung: Wetter', 'exercises': [('Es ist heiß. =', '___'), ('Es regnet. =', '___'), ('Es ist windig. =', '___')], 'ab_ref': 'AB-08b: Aufgabe 1'}),
                ('solution', {'title': 'Lösung', 'solutions': [('Es ist heiß.', 'Hace calor.'), ('Es regnet.', 'Llueve.'), ('Es ist windig.', 'Hace viento.')]}),
                ('summary', {'title': 'Zusammenfassung', 'left_items': ['Hace sol/calor/frío', 'Hace viento/buen tiempo', 'Llueve, Nieva'], 'right_items': ['primavera, verano', 'otoño, invierno', '¿Qué tiempo hace?']}),
                ('homework', {'tasks': ['Wettervokabeln lernen', 'Wetter in deiner Stadt beschreiben', 'AB-08b vollständig']}),
            ]},

    '08c': {'title': 'El pretérito', 'subtitle': 'Vergangenheit', 'sequenz': 8,
            'slides': [
                ('title', {}),
                ('content', {'title': 'Lernziele', 'items': ['Pretérito indefinido kennenlernen', 'Regelmäßige Verben in der Vergangenheit', 'Zeitangaben für Vergangenheit']}),
                ('grammar', {'title': 'Pretérito: -ar-Verben', 'blocks': [('yo hablé', 'ich sprach'), ('tú hablaste', 'du sprachst'), ('él habló', 'er sprach')], 'info': '-é, -aste, -ó'}),
                ('grammar', {'title': 'Pretérito -ar: Plural', 'blocks': [('nosotros hablamos', 'wir sprachen'), ('vosotros hablasteis', 'ihr spracht'), ('ellos hablaron', 'sie sprachen')], 'info': '-amos, -asteis, -aron'}),
                ('grammar', {'title': 'Pretérito: -er/-ir-Verben', 'blocks': [('yo comí / viví', 'ich aß / lebte'), ('tú comiste / viviste', 'du aßt / lebtest'), ('él comió / vivió', 'er aß / lebte')], 'info': '-í, -iste, -ió'}),
                ('grammar', {'title': 'Pretérito -er/-ir: Plural', 'blocks': [('nosotros comimos', 'wir aßen'), ('vosotros comisteis', 'ihr aßt'), ('ellos comieron', 'sie aßen')], 'info': '-imos, -isteis, -ieron'}),
                ('vocab', {'title': 'Zeitangaben', 'vocab': [('ayer', 'gestern'), ('anteayer', 'vorgestern'), ('la semana pasada', 'letzte Woche'), ('el año pasado', 'letztes Jahr')], 'ab_ref': 'AB-08c: Kasten 2'}),
                ('content', {'title': 'Beispielsätze', 'items': ['Ayer estudié mucho.', 'La semana pasada viajé a Madrid.', 'El verano pasado fuimos a la playa.', 'Comí paella en España.']}),
                ('exercise', {'title': 'Übung: Pretérito -ar', 'exercises': [('Ayer yo ___ (hablar)', '___'), ('Tú ___ mucho. (estudiar)', '___')], 'ab_ref': 'AB-08c: Aufgabe 1'}),
                ('exercise', {'title': 'Übung: Pretérito -er/-ir', 'exercises': [('Yo ___ paella. (comer)', '___'), ('Ella ___ en Madrid. (vivir)', '___')], 'ab_ref': 'AB-08c: Aufgabe 2'}),
                ('solution', {'title': 'Lösung', 'solutions': [('Ayer yo hablé.', '✓'), ('Tú estudiaste mucho.', '✓'), ('Yo comí paella.', '✓'), ('Ella vivió en Madrid.', '✓')]}),
                ('summary', {'title': 'Zusammenfassung', 'left_items': ['-ar: -é, -aste, -ó', '-amos, -asteis, -aron', 'hablé, hablaste, habló'], 'right_items': ['-er/-ir: -í, -iste, -ió', '-imos, -isteis, -ieron', 'ayer, la semana pasada']}),
                ('homework', {'tasks': ['Pretérito-Endungen lernen', 'Über gestern schreiben', 'AB-08c vollständig']}),
            ]},

    '08d': {'title': 'Repaso final', 'subtitle': 'Abschlusstest', 'sequenz': 8,
            'slides': [
                ('title', {}),
                ('content', {'title': 'Jahresrückblick', 'items': ['8 Sequenzen abgeschlossen', '32 Doppelstunden', 'Niveau A1 (GER) erreicht!']}),
                ('content', {'title': 'Sequenz 1-4', 'items': ['Seq 1: Begrüßen, ser, Artikel', 'Seq 2: Familie, tener, Possessiv', 'Seq 3: Haus, hay, Farben', 'Seq 4: Schule, Uhrzeiten, -ar-Verben']}),
                ('content', {'title': 'Sequenz 5-8', 'items': ['Seq 5: Hobbys, -er/-ir, gustar', 'Seq 6: Stadt, ir/estar, Richtungen', 'Seq 7: Einkaufen, Zahlen, querer/poder', 'Seq 8: Reisen, Wetter, Pretérito']}),
                ('grammar', {'title': 'Grammatik-Überblick', 'blocks': [('Verben', 'ser, tener, ir, estar'), ('Endungen', '-ar, -er, -ir, Pretérito'), ('Besondere', 'gustar, querer, poder')]}),
                ('summary', {'title': 'Wichtige Strukturen', 'left_items': ['Me llamo... Soy de...', 'Tengo ... años.', 'Me gusta/n...', 'Quiero... Puedo...'], 'right_items': ['Hay... No hay...', 'Voy a... Estoy en...', 'Hace calor/frío...', 'Ayer hablé...']}),
                ('content', {'title': 'Abschlusstest: Überblick', 'items': ['Alle Themen des Jahres', 'Vokabeln + Grammatik', 'Leseverstehen', 'Schreiben: Über dich erzählen']}),
                ('content', {'title': 'Tipps für den Abschlusstest', 'items': ['Alle Vokabellisten wiederholen', 'Verbtabellen auswendig lernen', 'gustar-Struktur üben', 'Pretérito-Endungen']}),
                ('content', {'title': 'Was du jetzt kannst', 'items': ['Dich vorstellen auf Spanisch', 'Familie, Haus, Schule beschreiben', 'Hobbys und Vorlieben äußern', 'Einkaufen und nach dem Weg fragen', 'Über Vergangenes berichten']}),
                ('homework', {'tasks': ['ALLE Vokabeln wiederholen', 'ALLE Verbtabellen üben', 'Texte laut lesen'], 'closing': '¡Felices vacaciones!'}),
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
