#!/bin/bash
echo "🔄 Restarting all services..."

sudo systemctl restart clairity-backend.service
sudo systemctl restart clairity-frontend.service

echo "✅ Services restarted successfully!"
