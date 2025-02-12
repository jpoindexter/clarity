#!/bin/bash
echo "🔄 Syncing with GitHub..."

# Ensure there are no uncommitted changes
if [[ $(git status --porcelain) ]]; then
    echo "⚠️ You have uncommitted changes. Please commit or stash them first."
    exit 1
fi

# Pull latest changes
git pull origin main

# Reinstall dependencies if needed
./setup/install_backend.sh
./setup/install_frontend.sh

echo "✅ Code sync complete!"
