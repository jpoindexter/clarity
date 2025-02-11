#!/bin/bash

echo "🚀 Moving files to match project standardization..."

# Ensure backend/ exists
mkdir -p backend

# Move key folders inside backend/
mv backend/src/api backend/
mv backend/src/database backend/
mv backend/src/models backend/
mv backend/src/schemas backend/
mv backend/src/utils backend/
mv backend/src/rss backend/
mv backend/src/config backend/

# Remove old `src/` folder
rm -rf backend/src

echo "✅ Files moved successfully!"

# Ensure __init__.py exists everywhere
find backend -type d -exec touch {}/__init__.py \;

echo "✅ Ensured all __init__.py files exist."

# Final folder check
echo "📂 Final Backend Structure:"
tree backend/
