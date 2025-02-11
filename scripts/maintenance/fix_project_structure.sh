#!/bin/bash

echo "🚀 Fixing project structure..."

# Define project root
PROJECT_ROOT="/Users/jasonpoindexter/Documents/GitHub/clairity"
SRC_DIR="$PROJECT_ROOT/src"
BACKEND_DIR="$PROJECT_ROOT/backend"

# Ensure src exists
mkdir -p "$SRC_DIR"

# Move misplaced directories into src/
declare -a MOVE_DIRS=("api" "database" "models" "schemas" "utils")

for dir in "${MOVE_DIRS[@]}"; do
    if [ -d "$BACKEND_DIR/$dir" ]; then
        echo "🔄 Moving $dir to src/"
        mv "$BACKEND_DIR/$dir" "$SRC_DIR/"
    fi
done

# Remove redundant backend directory (keeping logs & tests)
echo "🧹 Cleaning up backend/"
find "$BACKEND_DIR" -maxdepth 1 -type d ! -name "logs" ! -name "tests" ! -name "backend" -exec rm -rf {} +

# Ensure all __init__.py files exist
echo "✅ Ensuring __init__.py files exist in all directories..."
find "$SRC_DIR" -type d -exec touch {}/__init__.py \;

# Fix imports after restructuring
echo "🔧 Running import fixer..."
bash "$PROJECT_ROOT/scripts/maintenance/fix_imports.sh"

echo "✅ Project structure fixed! Re-run the debug script to verify."
