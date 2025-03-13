#!/bin/bash

set -e  # Exit immediately on error

# 📌 Timestamped backup
TIMESTAMP=$(date +"%Y-%m-%d-%H-%M-%S")
BACKUP_DIR="backend_backup_$TIMESTAMP"
mkdir -p "$BACKUP_DIR"
cp -r backend/* "$BACKUP_DIR"

echo "🚀 Backup created at $BACKUP_DIR"

# ✅ Move files to match Clarity standards
echo "📂 Restructuring backend..."

# Move `api` files into `backend/api`
mkdir -p backend/api
mv backend/src/api/* backend/api/ 2>/dev/null || true

# Move `services` into `backend/services`
mkdir -p backend/services
mv backend/src/services/* backend/services/ 2>/dev/null || true

# Move `models` into `backend/models`
mkdir -p backend/models
mv backend/src/models/* backend/models/ 2>/dev/null || true

# Move `schemas` into `backend/schemas`
mkdir -p backend/schemas
mv backend/src/schemas/* backend/schemas/ 2>/dev/null || true

# Move `database` into `backend/database`
mkdir -p backend/database
mv backend/src/database/* backend/database/ 2>/dev/null || true

# Move `utils` into `backend/utils`
mkdir -p backend/utils
mv backend/src/utils/* backend/utils/ 2>/dev/null || true

# Remove empty `src` folder
rmdir backend/src 2>/dev/null || true

echo "✅ Folder structure updated."

# 🔄 Fix import paths automatically
echo "🔍 Updating imports..."
find backend/ -type f -name "*.py" -exec sed -i '' \
  -e 's/from src.api/from backend.api/g' \
  -e 's/from src.services/from backend.services/g' \
  -e 's/from src.models/from backend.models/g' \
  -e 's/from src.schemas/from backend.schemas/g' \
  -e 's/from src.database/from backend.database/g' \
  -e 's/from src.utils/from backend.utils/g' {} +

echo "✅ Imports updated."

# 🎯 Done
echo "🎉 Migration complete! Restart your server and test."

exit 0