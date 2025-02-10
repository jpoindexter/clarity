#!/bin/bash

echo "🚀 Starting Import Check..."

LOG_DIR="logs/system/$(date +"%Y-%m-%d_%H-%M-%S")"
mkdir -p "$LOG_DIR"

IMPORT_LOG="$LOG_DIR/import_check.log"

echo "🔍 Checking Python imports..." > "$IMPORT_LOG"

# Check Python files for import errors
find backend/src -name "*.py" | while read file; do
    python3 -m py_compile "$file" 2>> "$IMPORT_LOG"
done

echo "🔍 Checking JavaScript imports..." >> "$IMPORT_LOG"

# Check JavaScript files for import errors
find frontend/src -name "*.js" | while read file; do
    node -c "$file" 2>> "$IMPORT_LOG"
done

echo "✅ Import Check Complete! Logs saved in: $IMPORT_LOG"
