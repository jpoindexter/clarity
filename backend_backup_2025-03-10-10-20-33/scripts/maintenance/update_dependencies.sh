#!/bin/bash
echo "⬆️ Updating dependencies..."
cd backend || exit
pip install --upgrade -r requirements.txt
cd ../frontend || exit
npm update
echo "✅ Dependencies updated."
