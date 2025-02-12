#!/bin/bash
echo "🚀 Deploying frontend..."
cd frontend || exit

# Install dependencies & build the project
npm install
npm run build

# Restart frontend service (assuming running with systemd)
echo "🔄 Restarting frontend service..."
sudo systemctl restart clairity-frontend.service

echo "✅ Frontend deployed successfully!"
