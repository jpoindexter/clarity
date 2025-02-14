#!/bin/bash
echo "📦 Backing up logs and database before deployment..."
BACKUP_DIR="backups/$(date +'%Y-%m-%d_%H-%M-%S')"

# Create backup directory
mkdir -p "$BACKUP_DIR"

# Copy logs
cp -r logs/ "$BACKUP_DIR/"

# Backup database (if using SQLite)
if [ -f "test.db" ]; then
    cp test.db "$BACKUP_DIR/test.db.bak"
fi

echo "✅ Backup completed: $BACKUP_DIR"
