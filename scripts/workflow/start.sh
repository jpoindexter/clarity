#!/bin/bash

# ✅ Define log directory and create it if it doesn't exist
LOG_DIR="$(pwd)/logs/startup"
mkdir -p "$LOG_DIR"
LOG_FILE="$LOG_DIR/$(date +'%Y-%m-%d_%H-%M-%S').log"

log() {
    echo "$(date +'%Y-%m-%d %H:%M:%S') - $1" | tee -a "$LOG_FILE"
}

log "🚀 Starting Clarity Startup Process..."
log "------------------------------------------"

# ✅ **Step 1: Pre-Check Mode**
MISSING_FILES=()
MISSING_DEPS=()

# ✅ Check if Node.js, npm, Python, and Uvicorn are installed
for cmd in node npm python3 uvicorn; do
    if ! command -v $cmd &> /dev/null; then
        MISSING_DEPS+=("$cmd")
    fi
done

# ✅ Log missing dependencies and prompt user
if [ ${#MISSING_DEPS[@]} -ne 0 ]; then
    log "❌ Missing dependencies:"
    for dep in "${MISSING_DEPS[@]}"; do
        log "   - $dep (Not Installed)"
    done
    log "⚠️ Install missing dependencies before running the script again."
    exit 1
fi

# ✅ Check if backend and frontend files exist
if [ ! -f "backend/src/main.py" ]; then
    MISSING_FILES+=("backend/src/main.py")
fi
if [ ! -f "frontend/src/app/page.tsx" ]; then
    MISSING_FILES+=("frontend/src/app/page.tsx")
fi
if [ ! -f "frontend/package.json" ]; then
    MISSING_FILES+=("frontend/package.json")
fi

# ✅ Log missing files but continue running
if [ ${#MISSING_FILES[@]} -ne 0 ]; then
    log "⚠️ Missing critical files:"
    for file in "${MISSING_FILES[@]}"; do
        log "   - $file"
    done
fi

# ✅ **Step 2: Stop Only Relevant Processes**
log "🔄 Checking for existing Clarity processes..."
if lsof -i :8000 | grep LISTEN &> /dev/null; then
    log "✅ Backend is already running on port 8000"
else
    log "⚠️ Backend not detected. It will be started."
fi

if lsof -i :3000 | grep LISTEN &> /dev/null; then
    log "✅ Frontend is already running on port 3000"
else
    log "⚠️ Frontend not detected. It will be started."
fi

# ✅ **Step 3: Ensure Backend Virtual Environment Exists**
if [ ! -d "venv" ]; then
    log "⚠️ Backend virtual environment not found. You need to create it."
    log "👉 Run: python3 -m venv venv && source venv/bin/activate && pip install -r backend/requirements.txt"
    exit 1
fi

# ✅ **Step 4: Ensure Frontend Dependencies Exist**
if [ ! -d "frontend/node_modules" ]; then
    log "⚠️ Node modules missing. Running npm install..."
    cd frontend && npm install && cd ..
fi

# ✅ **Step 5: Ensure macOS Terminal is Running**
osascript -e 'tell application "Terminal" to activate'

# ✅ **Step 6: Open Terminal Windows for Each Process**
log "🖥️ Opening separate terminal windows for backend, frontend, logs, and an extra manual terminal..."

osascript <<EOF
tell application "Terminal"
    do script "cd $(pwd)/backend && source ../venv/bin/activate && uvicorn src.api.main:app --host 127.0.0.1 --port 8000 --reload 2>&1 | tee -a $LOG_FILE"
    delay 1
    do script "cd $(pwd)/frontend && npm run dev 2>&1 | tee -a $LOG_FILE"
    delay 1
    do script "tail -f $LOG_FILE"
    delay 1
    do script "echo '✅ This is your manual testing window. Use it for commands.'"
end tell
EOF

# ✅ **Step 7: Open All Required Browser Tabs in Safari (Ensuring Localhost is Included)**
log "🌍 Opening browser tabs in Safari..."

osascript <<EOF
tell application "Safari"
    make new document
    set URL of document 1 to "http://127.0.0.1:3000"
    tell window 1
        set current tab to (make new tab with properties {URL:"http://127.0.0.1:8000/docs"})
        set current tab to (make new tab with properties {URL:"http://127.0.0.1:8000/api/news"})
    end tell
end tell
EOF

# ✅ **Step 8: Confirm Startup Success**
log "✅ Verifying services are running..."
sleep 5  # Give servers time to start

if curl --output /dev/null --silent --head --fail "http://127.0.0.1:8000/docs"; then
    log "✅ Backend is running at http://127.0.0.1:8000"
else
    log "❌ Backend failed to start. Check logs for errors."
fi

if curl --output /dev/null --silent --head --fail "http://127.0.0.1:3000"; then
    log "✅ Frontend is running at http://127.0.0.1:3000"
else
    log "❌ Frontend failed to start. Check logs for errors."
    log "⚠️ Attempting to fix: Removing .next/ and restarting frontend..."
    rm -rf frontend/.next && cd frontend && npm run dev & cd ..
fi

log "✅ Startup complete! Backend, frontend, logs, and manual terminal are all open."
log "🚀 Happy coding! 🎉"

# ✅ **Step 9: Open Manual Terminal**
osascript -e 'tell application "Terminal" to activate'  # Bring manual terminal to front
