#!/bin/bash
echo "🔄 Resetting backend..."
cd backend || exit
rm -rf __pycache__
pip install -r requirements.txt
echo "✅ Backend reset complete."
