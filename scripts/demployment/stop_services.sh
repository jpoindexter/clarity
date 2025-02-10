#!/bin/bash

echo "🛑 Stopping AI News services..."

# Kill FastAPI (backend)
pkill -f "uvicorn"

# Kill React (frontend)
pkill -f "npm start"

echo "✅ All services stopped."
