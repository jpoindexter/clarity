#!/bin/bash

echo "🚀 Starting full project cleanup..."

# ✅ Remove duplicate/misplaced Alembic folders
rm -rf backend/alembic backend/backend/alembic backend/migrations_backup
rm -rf backend/database/migrations/README backend/database/migrations/script.py.mako

# ✅ Remove frontend-related files (if mistakenly added to backend)
rm -rf backend/node_modules backend/package-lock.json backend/package.json
rm -rf backend/public backend/src

# ✅ Remove logs and old database files
rm -rf backend/logs backend/test_clarity.db backend/test_clarity_backup.db

# ✅ Remove compiled Python files and cache
find backend -name "__pycache__" -type d -exec rm -rf {} +
find backend -name "*.pyc" -delete

# ✅ Remove system junk files
find backend -name ".DS_Store" -delete
rm -rf backend/.pytest_cache

# ✅ Remove the virtual environment (should not be in repo)
rm -rf venv
echo "venv/" >> .gitignore

# ✅ Remove unnecessary scripts (if unused)
rm -rf backend/fix_project.py backend/fix_routes.py backend/detect_circular_imports.py

# ✅ Verify final structure
echo "🚀 Final project structure:"
tree backend || ls -R backend

# ✅ Stage and commit cleanup changes
echo "🚀 Staging and committing changes..."
git add .
git commit -m "chore: remove unnecessary files, venv, and fix project structure"
git push origin main  # Change `main` if using a different branch

echo "✅ Cleanup complete! 🎯"