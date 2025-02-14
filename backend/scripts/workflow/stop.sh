#!/bin/bash
echo "🛑 Stopping all services..."

if pgrep -f "uvicorn" > /dev/null; then
    pkill -f "uvicorn"
    echo "✅ Backend stopped."
else
    echo "⚠️ Backend was not running."
fi

if pgrep -f "npm run dev" > /dev/null; then
    pkill -f "npm run dev"
    echo "✅ Frontend stopped."
else
    echo "⚠️ Frontend was not running."
fi
