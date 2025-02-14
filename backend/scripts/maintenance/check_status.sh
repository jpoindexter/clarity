#!/bin/bash
echo "🔍 Checking services..."

if lsof -i :8000 | grep LISTEN &> /dev/null; then
    echo "✅ Backend is running on port 8000"
else
    echo "❌ Backend is NOT running."
fi

if lsof -i :3000 | grep LISTEN &> /dev/null; then
    echo "✅ Frontend is running on port 3000"
else
    echo "❌ Frontend is NOT running."
fi
