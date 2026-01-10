#!/bin/bash
# ═══════════════════════════════════════════════════════════════
# PUBLISH-SPANISCH.SH
# Kopiert finale Spanisch-Materialien nach iCloud
# ═══════════════════════════════════════════════════════════════

# Farben für Output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Pfade
SOURCE_DIR="$(cd "$(dirname "$0")" && pwd)"
ICLOUD_BASE="$HOME/Library/Mobile Documents/com~apple~CloudDocs"
TARGET_DIR="$ICLOUD_BASE/Spanisch-Materialien"

# Zu kopierende Dateitypen (nur finale Outputs)
FILE_PATTERNS=("AB-*.pdf" "ML-*.pdf" "LH-*.pdf" "SLIDES-*.pdf" "LP-*.pdf" "LP-*.html" "LB-*.pdf" "LB-*.html" "QR-*.pdf" "PLANUNG-*.md")

echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${BLUE}  SPANISCH-MATERIALIEN → iCloud${NC}"
echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
echo ""

# Prüfe ob iCloud verfügbar
if [ ! -d "$ICLOUD_BASE" ]; then
    echo -e "${YELLOW}Fehler: iCloud Drive nicht gefunden unter:${NC}"
    echo "$ICLOUD_BASE"
    exit 1
fi

# Zähler
copied=0
skipped=0

# Funktion: Kopiere Dateien für ein Verzeichnis
publish_folder() {
    local src_folder="$1"
    local rel_path="${src_folder#$SOURCE_DIR/}"

    # Konvertiere Pfad für iCloud (lesbare Namen)
    # kl07 → Klasse-07, kl08 → Klasse-08, etc.
    local target_path="$rel_path"
    target_path=$(echo "$target_path" | sed 's/kl\([0-9]\{2\}\)/Klasse-\1/g')
    # unidad2-mi-instituto-v2 → Unidad-2-Mi-Instituto
    target_path=$(echo "$target_path" | sed 's/unidad\([0-9]\)-\([^/]*\)-v[0-9]*/Unidad-\1-\2/g')
    target_path=$(echo "$target_path" | sed 's/unidad\([0-9]\)-\([^/]*\)/Unidad-\1-\2/g')

    local full_target="$TARGET_DIR/$target_path"

    # Prüfe ob relevante Dateien existieren
    local has_files=false
    for pattern in "${FILE_PATTERNS[@]}"; do
        if ls "$src_folder"/$pattern 1> /dev/null 2>&1; then
            has_files=true
            break
        fi
    done

    if [ "$has_files" = false ]; then
        return
    fi

    # Erstelle Zielverzeichnis
    mkdir -p "$full_target"

    # Kopiere passende Dateien
    for pattern in "${FILE_PATTERNS[@]}"; do
        for file in "$src_folder"/$pattern; do
            if [ -f "$file" ]; then
                filename=$(basename "$file")
                target_file="$full_target/$filename"

                # Nur kopieren wenn neuer oder nicht vorhanden
                if [ ! -f "$target_file" ] || [ "$file" -nt "$target_file" ]; then
                    cp "$file" "$target_file"
                    echo -e "  ${GREEN}✓${NC} $rel_path/$filename"
                    ((copied++))
                else
                    ((skipped++))
                fi
            fi
        done
    done
}

echo -e "Quelle:  ${SOURCE_DIR}"
echo -e "Ziel:    ${TARGET_DIR}"
echo ""
echo -e "${YELLOW}Kopiere Materialien...${NC}"
echo ""

# Durchsuche alle Unterverzeichnisse
find "$SOURCE_DIR" -type d | while read -r folder; do
    publish_folder "$folder"
done

echo ""
echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
echo -e "  ${GREEN}Fertig!${NC}"
echo -e "  Kopiert: $copied Dateien"
echo -e "  Übersprungen (unverändert): $skipped Dateien"
echo ""
echo -e "  iCloud-Ordner: ${TARGET_DIR}"
echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"

# Öffne iCloud-Ordner im Finder (optional)
if [ "$1" = "--open" ] || [ "$1" = "-o" ]; then
    open "$TARGET_DIR"
fi
