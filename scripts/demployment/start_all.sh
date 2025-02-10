#!/bin/bash

LOGFILE="start_all.log"
PORT=8000
FRONTEND_PORT=3000
PROJECT_DIR="/Users/jasonpoindexter/Documents/GitHub/ai_news"
BACKEND_DIR="$PROJECT_DIR/backend"
FRONTEND_DIR="$PROJECT_DIR/frontend"
VENV_DIR="$BACKEND_DIR/venv"

# Redirect all output to log file
exec > >(tee -a $LOGFILE) 2>&1

echo "🚀 Starting All Services..."

# Check if brew is installed
if ! command -v brew &> /dev/null; then
    echo "❌ Homebrew is not installed. Please install Homebrew first."
    exit 1
fi

echo "🐘 Restarting PostgreSQL..."
brew services restart postgresql@14

# Ensure all necessary ports are free
echo "🛠️ Checking if port $PORT is in use..."
if lsof -i:$PORT -t > /dev/null; then
    echo "⚠️ Port $PORT is in use. Freeing it up..."
    kill -9 $(lsof -i:$PORT -t)
    echo "✅ Port $PORT is now free."
else
    echo "✅ Port $PORT is free."
fi

echo "🛠️ Checking if port $FRONTEND_PORT is in use..."
if lsof -i:$FRONTEND_PORT -t > /dev/null; then
    echo "⚠️ Port $FRONTEND_PORT is in use. Freeing it up..."
    kill -9 $(lsof -i:$FRONTEND_PORT -t)
    echo "✅ Port $FRONTEND_PORT is now free."
else
    echo "✅ Port $FRONTEND_PORT is free."
fi

# Check if osascript is available
if ! command -v osascript &> /dev/null; then
    echo "❌ osascript is not available. Please ensure you are running this on macOS."
    exit 1
fi

# Open a new terminal for FastAPI
echo "🖥️ Opening a New Terminal for FastAPI..."
osascript <<EOF
tell application "Terminal"
    do script "cd $PROJECT_DIR && source $VENV_DIR/bin/activate && uvicorn backend.main:app --host 0.0.0.0 --port $PORT --reload | tee -a $LOGFILE"
end tell
EOF

# Open a new terminal for Next.js Frontend
echo "🖥️ Opening a New Terminal for Frontend..."
osascript <<EOF
tell application "Terminal"
    do script "cd $FRONTEND_DIR && npm run dev | tee -a $LOGFILE"
end tell
EOF

# Open a new terminal for (venv) environment
echo "🖥️ Opening a New Terminal with Environment Activated..."
osascript <<EOF
tell application "Terminal"
    do script "cd $PROJECT_DIR && source $VENV_DIR/bin/activate && echo '✅ Virtual Environment Ready!'"
end tell
EOF

# Open a new terminal for logging all output
echo "📜 Opening a New Terminal for Logs..."
osascript <<EOF
tell application "Terminal"
    do script "tail -f $LOGFILE"
end tell
EOF

echo "✅ All services started successfully! Check '$LOGFILE' for details."
