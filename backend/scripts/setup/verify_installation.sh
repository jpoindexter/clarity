#!/bin/bash
echo "🔍 Verifying installation..."

# Check Python dependencies
if python3 -c "import fastapi, uvicorn, sqlalchemy" &> /dev/null; then
    echo "✅ Backend dependencies are installed."
else
    echo "❌ Backend dependencies missing!"
fi

# Check Node.js dependencies
if [ -d "frontend/node_modules" ]; then
    echo "✅ Frontend dependencies are installed."
else
    echo "❌ Frontend dependencies missing!"
fi

# Check environment variables
if [ -f ".env" ]; then
    echo "✅ .env file is set up."
else
    echo "❌ .env file missing!"
fi
