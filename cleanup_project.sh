#!/bin/bash

echo "🚀 Starting full project cleanup..."

# ✅ Remove duplicate/misplaced Alembic folders
rm -rf backend/alembic
rm -rf backend/backend/alembic
rm -rf backend/migrations_backup

# ✅ Remove old migration backups
rm -rf backend/database/migrations/README
rm -rf backend/database/migrations/script.py.mako

# ✅ Ensure `alembic.ini` is in the correct place
mv backend/database/migrations/alembic.ini backend/database/ 2>/dev/null

# ✅ Remove logs and old database files
rm -rf backend/logs
rm -rf backend/test_clarity.db

# ✅ Remove compiled Python files and cache
find backend -name "__pycache__" -type d -exec rm -rf {} +
find backend -name "*.pyc" -delete

# ✅ Remove system junk files
find backend -name ".DS_Store" -delete
rm -rf backend/.pytest_cache

# ✅ Move `.env` file to the project root
if [ -f "backend/.env" ]; then
    mv backend/.env .env
    echo "✅ Moved .env to project root"
fi

# ✅ Remove unnecessary scripts (if unused)
rm -rf backend/fix_project.py backend/fix_routes.py backend/detect_circular_imports.py

# ✅ Verify final structure
echo "🚀 Final project structure:"
tree backend

# ✅ Commit changes to Git
echo "🚀 Staging and committing changes..."
git add .
git commit -m "chore: full cleanup of unnecessary files and structure"
git push origin main  # Change `main` if using a different branch

echo "✅ Cleanup complete! 🎯"
