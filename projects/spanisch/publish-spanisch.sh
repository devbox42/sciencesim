#!/bin/bash
# ═══════════════════════════════════════════════════════════════
# PUBLISH SPANISCH: Kopiert Spanisch-Materialien nach iCloud
#
# Verwendung:
#   ./publish-spanisch.sh          # Alle Klassen
#   ./publish-spanisch.sh kl07     # Nur Klasse 7
#   ./publish-spanisch.sh kl12     # Nur Klasse 12
#   ./publish-spanisch.sh --open   # Nach Kopieren Finder öffnen
# ═══════════════════════════════════════════════════════════════

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ICLOUD_BASE="$HOME/Library/Mobile Documents/com~apple~CloudDocs/Spanisch-Materialien"

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
NC='\033[0m'

OPEN_FINDER=false
TARGET_CLASS=""

# Parameter parsen
for arg in "$@"; do
    case $arg in
        --open)
            OPEN_FINDER=true
            ;;
        kl*)
            TARGET_CLASS="$arg"
            ;;
    esac
done

# Ordnernamen umwandeln: kl07 -> Klasse-07, kl12 -> Klasse-12
convert_classname() {
    local name="$1"
    case "$name" in
        kl07) echo "Klasse-07" ;;
        kl08) echo "Klasse-08" ;;
        kl09) echo "Klasse-09" ;;
        kl10) echo "Klasse-10" ;;
        kl11) echo "Klasse-11" ;;
        kl12) echo "Klasse-12" ;;
        spaetbeginner) echo "spaetbeginner" ;;
        *) echo "$name" ;;
    esac
}

# Dateien kopieren
copy_materials() {
    local src_dir="$1"
    local dest_dir="$2"
    local copied=0

    # Erstelle Zielordner
    mkdir -p "$dest_dir"

    # Kopiere nur finale Outputs
    for pattern in "AB-*.pdf" "ML-*.pdf" "LH-*.pdf" "LB-*.pdf" "SLIDES-*.pdf" "LP-*.html" "MT-*.html" "PLATZKARTEN-*.pdf" "QR-*.pdf" "PLANUNG-*.md"; do
        for file in "$src_dir"/$pattern; do
            if [ -f "$file" ]; then
                filename=$(basename "$file")
                dest_file="$dest_dir/$filename"

                # Prüfe ob Datei neuer ist oder nicht existiert
                if [ ! -f "$dest_file" ] || [ "$file" -nt "$dest_file" ]; then
                    cp "$file" "$dest_file"
                    echo -e "  ${GREEN}✓${NC} $filename"
                    ((copied++))
                else
                    echo -e "  ${YELLOW}○${NC} $filename (unverändert)"
                fi
            fi
        done
    done

    return $copied
}

echo ""
echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${BLUE}  Spanisch → iCloud${NC}"
echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
echo ""

TOTAL_COPIED=0

# Durchsuche alle Klassen-Ordner
for class_dir in "$SCRIPT_DIR"/kl*/ "$SCRIPT_DIR"/spaetbeginner/; do
    [ ! -d "$class_dir" ] && continue

    class_name=$(basename "$class_dir")

    # Filter nach Zielklasse wenn angegeben
    if [ -n "$TARGET_CLASS" ] && [ "$class_name" != "$TARGET_CLASS" ]; then
        continue
    fi

    dest_class=$(convert_classname "$class_name")

    # Durchsuche Unterordner (Themen/Einheiten)
    for topic_dir in "$class_dir"*/; do
        [ ! -d "$topic_dir" ] && continue

        topic_name=$(basename "$topic_dir")
        dest_path="$ICLOUD_BASE/$dest_class/$topic_name"

        # Prüfe ob es relevante Dateien gibt
        has_files=false
        for pattern in "AB-*.pdf" "ML-*.pdf" "LH-*.pdf" "LB-*.pdf" "LP-*.html" "MT-*.html" "PLATZKARTEN-*.pdf" "QR-*.pdf"; do
            if ls "$topic_dir"/$pattern 1>/dev/null 2>&1; then
                has_files=true
                break
            fi
        done

        if $has_files; then
            echo -e "${BLUE}$dest_class/$topic_name:${NC}"
            copy_materials "$topic_dir" "$dest_path"
            TOTAL_COPIED=$((TOTAL_COPIED + $?))
            echo ""
        fi
    done
done

echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${GREEN}$TOTAL_COPIED Datei(en) kopiert nach:${NC}"
echo -e "${YELLOW}$ICLOUD_BASE${NC}"
echo ""

if $OPEN_FINDER; then
    open "$ICLOUD_BASE"
fi
