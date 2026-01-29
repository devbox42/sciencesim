#!/bin/bash
# ═══════════════════════════════════════════════════════════════
# PUBLISH PHYSIK: Veröffentlicht Physik-Materialien auf GitHub
#
# Verwendung (aus dem physik-Ordner):
#   ./publish.sh kl9E/magnetismus/MT-08b-elektromagnetismus.html
#   ./publish.sh kl9E/magnetismus/
#   ./publish.sh   # Alle bereits online vorhandenen Dateien aktualisieren
# ═══════════════════════════════════════════════════════════════

REPO="devbox42/sciencesim"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REMOTE_PREFIX="physik"

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
NC='\033[0m'

publish_file() {
    local local_file="$1"
    local remote_path="$2"

    echo -n "  $remote_path ... "

    # Prüfe ob Datei bereits online existiert
    RESPONSE=$(gh api "repos/$REPO/contents/$remote_path" 2>&1)

    if echo "$RESPONSE" | grep -q '"sha"'; then
        # Datei existiert - Update
        SHA=$(echo "$RESPONSE" | grep -o '"sha": "[^"]*"' | head -1 | cut -d'"' -f4)

        RESULT=$(gh api "repos/$REPO/contents/$remote_path" \
            --method PUT \
            --field message="update: $remote_path" \
            --field content="$(base64 -i "$local_file")" \
            --field sha="$SHA" 2>&1)

        if echo "$RESULT" | grep -q '"commit"'; then
            echo -e "${GREEN}aktualisiert${NC}"
            return 0
        elif echo "$RESULT" | grep -q 'does not match'; then
            echo -e "${YELLOW}unverändert${NC}"
            return 0
        else
            echo -e "${RED}Fehler${NC}"
            return 1
        fi
    else
        # Datei existiert nicht - Neu erstellen
        gh api "repos/$REPO/contents/$remote_path" \
            --method PUT \
            --field message="add: $remote_path" \
            --field content="$(base64 -i "$local_file")" \
            --silent 2>/dev/null

        if [ $? -eq 0 ]; then
            echo -e "${BLUE}neu erstellt${NC}"
            return 0
        else
            echo -e "${RED}Fehler${NC}"
            return 1
        fi
    fi
}

echo ""
echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${BLUE}  Physik → GitHub ($REPO)${NC}"
echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
echo ""

# Ohne Argument: Sync alle online vorhandenen Dateien
if [ -z "$1" ]; then
    echo "Hole online vorhandene Physik-Dateien..."
    echo ""

    REMOTE_FILES=$(gh api "repos/$REPO/git/trees/main?recursive=1" \
        --jq '.tree[] | select(.type=="blob") | select(.path | startswith("physik/")) | .path' 2>/dev/null)

    if [ -z "$REMOTE_FILES" ]; then
        echo -e "${YELLOW}Keine Physik-Dateien online gefunden.${NC}"
        exit 0
    fi

    UPDATED=0
    while IFS= read -r remote_path; do
        # Remote: physik/kl9E/... -> Local: kl9E/...
        local_relative="${remote_path#physik/}"
        local_file="$SCRIPT_DIR/$local_relative"

        if [ -f "$local_file" ]; then
            publish_file "$local_file" "$remote_path"
            [ $? -eq 0 ] && ((UPDATED++))
        fi
    done <<< "$REMOTE_FILES"

    echo ""
    echo -e "${GREEN}$UPDATED Datei(en) aktualisiert${NC}"
    exit 0
fi

# Mit Argument: Spezifischer Pfad
TARGET="$1"
LOCAL_PATH="$SCRIPT_DIR/$TARGET"

if [ ! -e "$LOCAL_PATH" ]; then
    echo -e "${RED}Fehler: $LOCAL_PATH existiert nicht${NC}"
    exit 1
fi

if [ -f "$LOCAL_PATH" ]; then
    # Einzelne Datei
    REMOTE_PATH="$REMOTE_PREFIX/$TARGET"
    publish_file "$LOCAL_PATH" "$REMOTE_PATH"
elif [ -d "$LOCAL_PATH" ]; then
    # Ordner - nur HTML Dateien
    echo "Ordner: $TARGET"
    echo ""

    find "$LOCAL_PATH" -type f -name "*.html" | while read file; do
        relative="${file#$SCRIPT_DIR/}"
        remote_path="$REMOTE_PREFIX/$relative"
        publish_file "$file" "$remote_path"
    done
fi

echo ""
echo -e "${GREEN}Fertig!${NC}"
echo ""
echo "URL: https://devbox42.github.io/sciencesim/$REMOTE_PREFIX/$TARGET"
