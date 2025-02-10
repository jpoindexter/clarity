#!/bin/bash

# Set retention period (default: 7 days)
RETENTION_DAYS=7
SCAN_LOGS_DIR="logs/scan/"

echo "🗑 Cleaning up logs older than $RETENTION_DAYS days..."

# Find and delete old log folders
find "$SCAN_LOGS_DIR" -type d -mtime +$RETENTION_DAYS -exec rm -rf {} \;

echo "✅ Log cleanup complete!"
