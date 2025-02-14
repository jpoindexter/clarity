#!/bin/bash
echo "🚀 Running first-time setup..."

# Run backend and frontend installers
./setup/install_backend.sh
./setup/install_frontend.sh
./setup/setup_env.sh

echo "✅ First-time setup complete!"
