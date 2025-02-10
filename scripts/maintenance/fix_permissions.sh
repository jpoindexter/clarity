#!/bin/bash

# Fix executable permissions
echo "🔧 Fixing script permissions..."
chmod +x scripts/maintenance/*.sh

# Fix log write permissions
echo "🔧 Ensuring logs are writable..."
chmod -R 755 logs/

echo "✅ Permissions fixed!"
