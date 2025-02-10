#!/bin/bash

# Define backup location
BACKUP_DIR="backups"
TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")
BACKUP_PATH="$BACKUP_DIR/backup_$TIMESTAMP.tar.gz"

# Create backup directory if it doesn't exist
mkdir -p "$BACKUP_DIR"

echo "📦 Creating project backup..."

# Archive the project, excluding unnecessary files
tar --exclude='backups' \
    --exclude='logs' \
    --exclude='node_modules' \
    --exclude='__pycache__' \
    -czf "$BACKUP_PATH" .

echo "✅ Backup created at: $BACKUP_PATH"
