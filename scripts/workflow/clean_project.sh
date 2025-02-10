#!/bin/bash

echo "🧹 Cleaning up project..."

# Remove Python cache
echo "🗑️ Removing __pycache__ directories..."
find . -type d -name "__pycache__" -exec rm -rf {} +

# Remove logs older than 7 days
echo "🗑️ Cleaning up old logs..."
find logs/ -type f -mtime +7 -exec rm {} +

# Remove unused dependencies (Node)
echo "🗑️ Cleaning up node_modules..."
rm -rf frontend/node_modules

echo "✅ Project cleanup complete!"
