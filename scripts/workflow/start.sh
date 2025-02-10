#!/bin/bash

echo "🚀 Stopping any existing processes..."
lsof -ti:8000 | xargs kill -9 2>/dev/null
lsof -ti:3000 | xargs kill -9 2>/dev/null

# Navigate to the project root dynamically
cd "$(dirname "$0")/.." || exit

# Activate the backend virtual environment
echo "🐍 Activating virtual environment..."
source backend/venv/bin/activate

# Ensure PYTHONPATH is correctly set
export PYTHONPATH=$(pwd)/backend

# Start Backend API
echo "⚡ Starting Backend API..."
nohup uvicorn backend.src.api.main:app --host 127.0.0.1 --port 8000 --reload > backend.log 2>&1 &

# Start Frontend UI
echo "🖥️ Starting Next.js Frontend..."
cd frontend || exit
nohup npm run dev > frontend.log 2>&1 &

# Wait a few seconds to ensure services start
sleep 5

# Open the frontend in the browser
echo "🌍 Opening the frontend in the browser..."
open "http://127.0.0.1:3000"

echo "✅ Clairity is now running!"
