#!/bin/bash
echo "🔍 Checking deployment status..."

if curl --output /dev/null --silent --head --fail "http://127.0.0.1:8000/docs"; then
    echo "✅ Backend is running at http://127.0.0.1:8000"
else
    echo "❌ Backend is NOT running."
fi

if curl --output /dev/null --silent --head --fail "http://127.0.0.1:3000"; then
    echo "✅ Frontend is running at http://127.0.0.1:3000"
else
    echo "❌ Frontend is NOT running."
fi
