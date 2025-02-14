#!/bin/bash
echo "🚀 Setting up backend..."
cd backend || exit

# Ensure virtual environment exists
if [ ! -d "../venv" ]; then
    echo "🛠️ Creating virtual environment..."
    python3 -m venv ../venv
fi

# Activate virtual environment
source ../venv/bin/activate

# Install dependencies
echo "📦 Installing backend dependencies..."
pip install -r ../setup/requirements.txt

echo "✅ Backend setup complete!"
