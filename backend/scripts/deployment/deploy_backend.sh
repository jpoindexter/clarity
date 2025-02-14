#!/bin/bash
echo "🚀 Deploying backend..."
cd backend || exit

# Ensure virtual environment is activated
source ../venv/bin/activate

# Install latest dependencies
pip install -r requirements.txt

# Restart backend service (assuming running with systemd)
echo "🔄 Restarting backend service..."
sudo systemctl restart Clarity-backend.service

echo "✅ Backend deployed successfully!"
