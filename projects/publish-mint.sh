#!/bin/bash
# ═══════════════════════════════════════════════════════════════
# PUBLISH-MINT.SH
# Kopiert finale MINT-Materialien (Physik, Chemie, Informatik) nach iCloud
# und prüft GitHub-Sync für Online-Materialien
#
# Verwendung:
#   ./publish-mint.sh              # Alle MINT-Fächer publizieren
#   ./publish-mint.sh physik       # Nur Physik
#   ./publish-mint.sh chemie       # Nur Chemie
#   ./publish-mint.sh informatik   # Nur Informatik
#   ./publish-mint.sh --check      # Nur GitHub-Sync prüfen
#   ./publish-mint.sh --check-qr   # Nur QR-Code-URLs validieren
#   ./publish-mint.sh -o           # Nach Kopieren Finder öffnen
#
# Das Script:
#   1. Kopiert nach iCloud:
#      - Alle PDFs (AB, ML, LH, LB, LP, MT, QR, LE, etc.)
#      - Alle HTMLs (LP, MT, SIM, STUNDENPLAN, etc.)
#      - Alle TEX-Quelldateien (OHNE Residuals wie .aux, .log, .out, etc.)
#      - Alle MD-Dateien (PLANUNG, README, etc.)
#      - Subfolders: img/, images/, assets/, css/, js/
#   2. Prüft ob LP-*.html, MT-*.html, SIM-*.html auf GitHub liegen
#   3. Validiert ob QR-Code-URLs mit GitHub-Dateien übereinstimmen
# ═══════════════════════════════════════════════════════════════

# Farben für Output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Pfade
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ICLOUD_BASE="$HOME/Library/Mobile Documents/com~apple~CloudDocs/MINT-Materialien"
GITHUB_REPO="devbox42/sciencesim"

# Fächer (Bash 3.x kompatibel)
FAECHER="physik chemie informatik"

# Mapping Fach → Zielordner
get_target_name() {
    case "$1" in
        physik) echo "Physik" ;;
        chemie) echo "Chemie" ;;
        informatik) echo "Informatik" ;;
        *) echo "$1" ;;
    esac
}

# Zu kopierende Dateitypen (finale Outputs + Quellen)
FILE_PATTERNS="*.pdf *.html *.tex *.md"

# LaTeX-Residualdateien (werden NICHT kopiert)
TEX_RESIDUALS=".aux .log .out .synctex.gz .fls .fdb_latexmk .toc .lof .lot .bbl .blg .nav .snm .vrb"

# Subfolders die mitkopiert werden sollen
SUBFOLDERS="img images assets css js"

# Zähler
copied=0
skipped=0
github_ok=0
github_missing=0

# ═══════════════════════════════════════════════════════════════
# Hilfsfunktionen
# ═══════════════════════════════════════════════════════════════

# Konvertiert Ordnernamen in lesbare iCloud-Struktur
# Beispiele:
#   kl06/01-bewegungsarten → Klasse-06/01-bewegungsarten
#   kl8-ohm → Klasse-08/ohm
#   kl9E/magnetismus → Klasse-09-E/magnetismus
#   kl12-GK/01-photoeffekt → Klasse-12-GK/01-photoeffekt
#   10E_Gym/klausurvorbereitung → Klasse-10E-Gym/klausurvorbereitung
convert_path() {
    local path="$1"
    local result="$path"

    # Spezialfälle zuerst (ganze Ordnernamen am Anfang)
    # 10E_Gym → Klasse-10E-Gym
    result=$(echo "$result" | sed -E 's/^10E_Gym/Klasse-10E-Gym/g')
    result=$(echo "$result" | sed -E 's/\/10E_Gym/\/Klasse-10E-Gym/g')

    # 10MR → Klasse-10-MR
    result=$(echo "$result" | sed -E 's/^10MR/Klasse-10-MR/g')
    result=$(echo "$result" | sed -E 's/\/10MR/\/Klasse-10-MR/g')

    # kl9E → Klasse-09-E (E-Kurs)
    result=$(echo "$result" | sed -E 's/kl([0-9])E(\/|$)/Klasse-0\1-E\2/g')
    result=$(echo "$result" | sed -E 's/kl([0-9]{2})E(\/|$)/Klasse-\1-E\2/g')

    # kl12-GK, kl10-MR → Klasse-12-GK, Klasse-10-MR
    result=$(echo "$result" | sed -E 's/kl([0-9]{2})-([A-Z]+)(\/|$)/Klasse-\1-\2\3/g')
    result=$(echo "$result" | sed -E 's/kl([0-9])-([A-Z]+)(\/|$)/Klasse-0\1-\2\3/g')

    # kl8-ohm, kl8-ladung → Klasse-08/ohm, Klasse-08/ladung (Thema als Unterordner)
    result=$(echo "$result" | sed -E 's/kl([0-9])-([a-z][a-z0-9-]*)(\/|$)/Klasse-0\1\/\2\3/g')
    result=$(echo "$result" | sed -E 's/kl([0-9]{2})-([a-z][a-z0-9-]*)(\/|$)/Klasse-\1\/\2\3/g')

    # Einfache Klassen: kl06, kl07, kl7 → Klasse-06, Klasse-07
    result=$(echo "$result" | sed -E 's/kl([0-9]{2})(\/|$)/Klasse-\1\2/g')
    result=$(echo "$result" | sed -E 's/kl([0-9])(\/|$)/Klasse-0\1\2/g')

    echo "$result"
}

# Prüft ob eine HTML-Datei auf GitHub existiert
check_github() {
    local fach="$1"
    local relative_path="$2"
    local remote_path="$fach/$relative_path"

    RESPONSE=$(gh api "repos/$GITHUB_REPO/contents/$remote_path" 2>&1)

    if echo "$RESPONSE" | grep -q '"sha"'; then
        return 0  # Existiert
    else
        return 1  # Existiert nicht
    fi
}

# Prüft ob QR-Code-URLs mit GitHub-Struktur übereinstimmen
check_qr_urls() {
    local fach="$1"
    local fach_source="$SCRIPT_DIR/$fach"
    local qr_ok=0
    local qr_mismatch=0

    if [ ! -d "$fach_source" ]; then
        return
    fi

    echo -e "\n${CYAN}QR-Code-Validierung: $fach${NC}"

    # Finde alle QR-*.tex Dateien
    find "$fach_source" -type f -name "QR-*.tex" 2>/dev/null | while read qr_file; do
        # Extrahiere URL aus dem .tex File
        local url=$(grep -oE 'https://devbox42\.github\.io/sciencesim/[^}]+' "$qr_file" 2>/dev/null | head -1)

        if [ -z "$url" ]; then
            echo -e "  ${YELLOW}?${NC} $(basename "$qr_file") - keine URL gefunden"
            continue
        fi

        # Extrahiere den relativen Pfad aus der URL
        local remote_path=$(echo "$url" | sed 's|https://devbox42.github.io/sciencesim/||')
        local filename=$(basename "$remote_path")

        # Prüfe ob die Datei auf GitHub existiert
        if check_github "" "$remote_path"; then
            echo -e "  ${GREEN}✓${NC} $(basename "$qr_file") → $filename"
        else
            echo -e "  ${RED}✗${NC} $(basename "$qr_file") → $remote_path ${YELLOW}(nicht auf GitHub!)${NC}"
        fi
    done
}

# Prüft ob Datei eine LaTeX-Residualdatei ist
is_tex_residual() {
    local filename="$1"
    for ext in $TEX_RESIDUALS; do
        case "$filename" in
            *"$ext") return 0 ;;
        esac
    done
    return 1
}

# Kopiert Dateien für einen Ordner
publish_folder() {
    local fach="$1"
    local src_folder="$2"
    local fach_source="$SCRIPT_DIR/$fach"
    local rel_path="${src_folder#$fach_source/}"

    # Wenn src_folder == fach_source, dann rel_path leer
    if [ "$src_folder" = "$fach_source" ]; then
        rel_path=""
    fi

    # Konvertiere Pfad für iCloud
    local target_rel=$(convert_path "$rel_path")
    local target_name=$(get_target_name "$fach")
    local full_target="$ICLOUD_BASE/$target_name"

    if [ -n "$target_rel" ]; then
        full_target="$full_target/$target_rel"
    fi

    # Prüfe ob relevante Dateien existieren
    local has_files=false
    for pattern in $FILE_PATTERNS; do
        if ls "$src_folder"/$pattern 1> /dev/null 2>&1; then
            has_files=true
            break
        fi
    done

    if [ "$has_files" = "false" ]; then
        return
    fi

    # Erstelle Zielverzeichnis
    mkdir -p "$full_target"

    # Kopiere passende Dateien (außer LaTeX-Residuals)
    for pattern in $FILE_PATTERNS; do
        for file in "$src_folder"/$pattern; do
            if [ -f "$file" ]; then
                filename=$(basename "$file")

                # Überspringe LaTeX-Residualdateien
                if is_tex_residual "$filename"; then
                    continue
                fi

                target_file="$full_target/$filename"

                # Nur kopieren wenn neuer oder nicht vorhanden
                if [ ! -f "$target_file" ] || [ "$file" -nt "$target_file" ]; then
                    cp "$file" "$target_file"
                    echo -e "  ${GREEN}✓${NC} $fach/$rel_path/$filename"
                    copied=$((copied + 1))
                else
                    skipped=$((skipped + 1))
                fi
            fi
        done
    done

    # Kopiere Subfolders (img, images, assets, css, js)
    for subfolder in $SUBFOLDERS; do
        if [ -d "$src_folder/$subfolder" ]; then
            local target_subfolder="$full_target/$subfolder"

            # rsync für effizienten Ordner-Sync (nur neuere Dateien)
            if command -v rsync &> /dev/null; then
                rsync -a --update "$src_folder/$subfolder/" "$target_subfolder/" 2>/dev/null
                echo -e "  ${GREEN}✓${NC} $fach/$rel_path/$subfolder/ (Ordner)"
            else
                # Fallback: cp -r
                mkdir -p "$target_subfolder"
                cp -r "$src_folder/$subfolder/"* "$target_subfolder/" 2>/dev/null
                echo -e "  ${GREEN}✓${NC} $fach/$rel_path/$subfolder/ (Ordner)"
            fi
        fi
    done
}

# Prüft GitHub-Sync für ein Fach
check_github_sync() {
    local fach="$1"
    local fach_source="$SCRIPT_DIR/$fach"

    if [ ! -d "$fach_source" ]; then
        return
    fi

    echo -e "\n${CYAN}GitHub-Sync: $fach${NC}"

    # Finde alle HTML-Dateien die online sein sollten (LP-*, MT-*, SIM-*)
    find "$fach_source" -type f \( -name "LP-*.html" -o -name "MT-*.html" -o -name "SIM-*.html" \) 2>/dev/null | while read file; do
        relative="${file#$fach_source/}"

        if check_github "$fach" "$relative"; then
            echo -e "  ${GREEN}✓${NC} $relative"
            github_ok=$((github_ok + 1))
        else
            echo -e "  ${RED}✗${NC} $relative ${YELLOW}(nicht auf GitHub)${NC}"
            github_missing=$((github_missing + 1))
        fi
    done
}

# Publiziert ein einzelnes Fach
publish_fach() {
    local fach="$1"
    local fach_source="$SCRIPT_DIR/$fach"
    local target_name=$(get_target_name "$fach")

    if [ ! -d "$fach_source" ]; then
        echo -e "${YELLOW}Warnung: $fach_source existiert nicht${NC}"
        return
    fi

    echo -e "\n${BLUE}━━━ $target_name ━━━${NC}"
    echo -e "Quelle: $fach_source"
    echo -e "Ziel:   $ICLOUD_BASE/$target_name"
    echo ""

    # Durchsuche alle Unterverzeichnisse
    find "$fach_source" -type d 2>/dev/null | while read -r folder; do
        publish_folder "$fach" "$folder"
    done
}

# ═══════════════════════════════════════════════════════════════
# Hauptprogramm
# ═══════════════════════════════════════════════════════════════

echo ""
echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${BLUE}  MINT-MATERIALIEN → iCloud${NC}"
echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"

# Prüfe ob iCloud verfügbar
ICLOUD_ROOT="$HOME/Library/Mobile Documents/com~apple~CloudDocs"
if [ ! -d "$ICLOUD_ROOT" ]; then
    echo -e "${RED}Fehler: iCloud Drive nicht gefunden unter:${NC}"
    echo "$ICLOUD_ROOT"
    exit 1
fi

# Erstelle MINT-Materialien-Ordner falls nötig
if [ ! -d "$ICLOUD_BASE" ]; then
    mkdir -p "$ICLOUD_BASE"
    echo -e "${BLUE}Erstelle: $ICLOUD_BASE${NC}"
fi

# Argumente parsen
OPEN_FINDER=false
CHECK_ONLY=false
CHECK_QR_ONLY=false
SELECTED_FACH=""

for arg in "$@"; do
    case $arg in
        -o|--open)
            OPEN_FINDER=true
            ;;
        --check)
            CHECK_ONLY=true
            ;;
        --check-qr)
            CHECK_QR_ONLY=true
            ;;
        physik|chemie|informatik)
            SELECTED_FACH="$arg"
            ;;
    esac
done

# Nur GitHub-Check?
if [ "$CHECK_ONLY" = "true" ]; then
    echo -e "\n${YELLOW}Prüfe GitHub-Sync...${NC}"

    if [ -n "$SELECTED_FACH" ]; then
        check_github_sync "$SELECTED_FACH"
    else
        for fach in $FAECHER; do
            check_github_sync "$fach"
        done
    fi

    echo ""
    echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
    echo -e "  GitHub-Sync abgeschlossen"
    echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
    exit 0
fi

# Nur QR-Check?
if [ "$CHECK_QR_ONLY" = "true" ]; then
    echo -e "\n${YELLOW}Prüfe QR-Code-URLs...${NC}"

    if [ -n "$SELECTED_FACH" ]; then
        check_qr_urls "$SELECTED_FACH"
    else
        for fach in $FAECHER; do
            check_qr_urls "$fach"
        done
    fi

    echo ""
    echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
    echo -e "  QR-Code-Validierung abgeschlossen"
    echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
    exit 0
fi

# Materialien kopieren
if [ -n "$SELECTED_FACH" ]; then
    publish_fach "$SELECTED_FACH"
else
    for fach in $FAECHER; do
        publish_fach "$fach"
    done
fi

# GitHub-Sync prüfen
echo -e "\n${YELLOW}Prüfe GitHub-Sync für Online-Materialien...${NC}"

if [ -n "$SELECTED_FACH" ]; then
    check_github_sync "$SELECTED_FACH"
else
    for fach in $FAECHER; do
        check_github_sync "$fach"
    done
fi

# QR-Codes validieren
echo -e "\n${YELLOW}Prüfe QR-Code-URLs...${NC}"

if [ -n "$SELECTED_FACH" ]; then
    check_qr_urls "$SELECTED_FACH"
else
    for fach in $FAECHER; do
        check_qr_urls "$fach"
    done
fi

# Zusammenfassung
echo ""
echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
echo -e "  ${GREEN}Fertig!${NC}"
echo -e "  iCloud: $copied kopiert, $skipped unverändert"
echo ""
echo -e "  Zielordner:"
for fach in $FAECHER; do
    target=$(get_target_name "$fach")
    if [ -d "$ICLOUD_BASE/$target" ]; then
        echo -e "    • $ICLOUD_BASE/$target"
    fi
done
echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"

# Finder öffnen?
if [ "$OPEN_FINDER" = "true" ]; then
    if [ -n "$SELECTED_FACH" ]; then
        open "$ICLOUD_BASE/$(get_target_name "$SELECTED_FACH")"
    else
        open "$ICLOUD_BASE"
    fi
fi
