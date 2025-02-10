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
)

# Scan for missing files
echo "🔍 Checking for missing files..."
for FILE in "${EXPECTED_FILES[@]}"; do
    if [ ! -f "$FILE" ]; then
        echo "❌ Missing: $FILE" | tee -a "$MISSING_LOG"
    fi
done

# Scan for orphaned files
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
