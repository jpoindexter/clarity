#!/bin/bash

# Set timestamp and log directory
TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")
LOG_DIR="logs/scan/$TIMESTAMP"
mkdir -p "$LOG_DIR"

# Define log file paths
FULL_SCAN_LOG="$LOG_DIR/full_scan.log"
MISSING_LOG="$LOG_DIR/missing.log"
ORPHANED_LOG="$LOG_DIR/orphaned.log"
IMPORT_ISSUES_LOG="$LOG_DIR/import_issues.log"
EMPTY_FILES_LOG="$LOG_DIR/empty.log"
ERRORS_LOG="$LOG_DIR/errors.log"

touch "$FULL_SCAN_LOG" "$MISSING_LOG" "$ORPHANED_LOG" "$IMPORT_ISSUES_LOG" "$EMPTY_FILES_LOG" "$ERRORS_LOG"

echo "🚀 Starting Project Scan at $(date)"

# List of required files (Minimal)
EXPECTED_FILES=(
    "backend/src/database/models/__init__.py"
    "backend/src/database/models/article.py"
    "backend/src/database/db_helper.py"
    "backend/src/database/db_connection.py"
    "backend/src/database/seed_db.py"
    "backend/src/api/endpoints/fetch.py"
    "backend/src/api/endpoints/search.py"
    "backend/src/api/endpoints/analyze.py"
    "backend/src/rss/feed_parser.py"
    "backend/src/rss/summarizer.py"
    "backend/src/config/config.py"
    "frontend/src/components/graph/treemap.js"
    "frontend/src/components/graph/force_graph.js"
    "frontend/src/components/news/news_list.js"
    "frontend/src/styles/global.css"
    "frontend/src/pages/index.js"
    "frontend/public/error_page.html"
    "frontend/public/favicon.ico"
    "frontend/public/global_styles.css"
    "frontend/public/Logo.svg"
    "frontend/.prettierrc.json"
    "frontend/src/components/filters/filterpanel.js"
    "frontend/src/components/filters/data_filter.js"
    "frontend/src/components/filters/source_filter.js"
    "frontend/src/components/filters/keyword_filter.js"
    "frontend/src/components/filters/index.js"
    "frontend/src/components/filters/time_filter.js"
    "frontend/src/components/ui/cards.js"
    "frontend/src/components/ui/index.js"
    "frontend/src/components/ui/inputs.js"
    "frontend/src/components/ui/modals.js"
    "frontend/src/components/ui/buttons.js"
    "frontend/src/components/layout/index.js"
    "frontend/src/components/layout/header.js"
    "frontend/src/components/layout/footer.js"
    "frontend/src/components/graph/graph.js"
    "frontend/src/components/graph/index.js"
    "frontend/src/components/graph/graph_container.js"
    "frontend/src/components/index.js"
    "frontend/src/components/common/Loader.css"
    "frontend/src/components/common/index.js"
    "frontend/src/components/common/Button.js"
    "frontend/src/components/common/Card.js"
    "frontend/src/components/common/Loader.js"
    "frontend/src/components/news/news_topic_tag.js"
    "frontend/src/components/news/news_source.js"
    "frontend/src/components/news/news_card.js"
    "frontend/src/components/news/index.js"
    "frontend/src/components/news/news_summary.js"
    "frontend/src/components/news/news_sentiment.js"
)

# Scan for missing files
echo "🔍 Checking for missing files..."
for FILE in "${EXPECTED_FILES[@]}"; do
    if [ ! -f "$FILE" ]; then
        echo "❌ Missing: $FILE" | tee -a "$MISSING_LOG"
    fi
done

# Scan for orphaned files (only flag files not in the EXPECTED_FILES list)
echo "🔍 Checking for orphaned files..."
find . -type f | while read -r FILE; do
    if [[ ! " ${EXPECTED_FILES[*]} " =~ " ${FILE#./} " ]]; then
        echo "🗑️ Orphaned: $FILE" | tee -a "$ORPHANED_LOG"
    fi
done

# Scan for empty files
echo "🔍 Checking for empty files..."
find . -type f -empty | while read -r FILE; do
    echo "⚠️ Empty File: $FILE" | tee -a "$EMPTY_FILES_LOG"
done

# Scan for import issues
echo "🔍 Checking for import issues..."
PYTHON_FILES=$(find backend/src -name "*.py")
for FILE in $PYTHON_FILES; do
    python3 -m py_compile "$FILE" 2>>"$IMPORT_ISSUES_LOG"
done

echo "✅ Scan Complete! Logs saved in: $LOG_DIR"
