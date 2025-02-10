#!/bin/bash

echo "🚀 Setting up development environment..."

# Check if inside project directory
if [ ! -f "requirements.txt" ] || [ ! -d "backend" ] || [ ! -d "frontend" ]; then
  echo "⚠️ Error: Run this script from the project root!"
  exit 1
fi

# Create a virtual environment if not exists
if [ ! -d "venv" ]; then
  echo "📦 Creating virtual environment..."
  python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install backend dependencies
echo "📦 Installing backend dependencies..."
pip install -r backend/requirements.txt

# Install frontend dependencies
echo "📦 Installing frontend dependencies..."
cd frontend
npm install
cd ..

# Copy environment variables (if template exists)
if [ ! -f ".env" ] && [ -f ".env.example" ]; then
  cp .env.example .env
  echo "🔧 Copied .env.example to .env"
fi

echo "✅ Development environment setup complete!"
