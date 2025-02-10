#!/bin/bash

echo "🚀 Starting AI News Platform (Development Mode)..."

# Ensure we're in the correct directory
if [ ! -d "backend" ] || [ ! -d "frontend" ]; then
  echo "⚠️ Error: Run this script from the project root!"
  exit 1
fi

# Activate virtual environment
source venv/bin/activate

# Start backend
echo "📡 Launching backend..."
cd backend
uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload &
cd ..

# Start frontend
echo "🖥️ Launching frontend..."
cd frontend
npm start &
cd ..

echo "✅ AI News Platform is running!"
echo "🔗 Backend: http://localhost:8000/docs"
echo "🔗 Frontend: http://localhost:3000"
