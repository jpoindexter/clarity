#!/bin/bash
echo "🔄 Restarting all services..."

sudo systemctl restart Clarity-backend.service
sudo systemctl restart Clarity-frontend.service

echo "✅ Services restarted successfully!"
