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

# ✅ Log missing dependencies and exit if any are missing
if [ ${#MISSING_DEPS[@]} -ne 0 ]; then
    log "❌ Missing dependencies:"
    for dep in "${MISSING_DEPS[@]}"; do
        log "   - $dep (Not Installed)"
    done
    log "⚠️ Install missing dependencies before running the script again."
    exit 1
fi

# ✅ **Step 2: Stop Any Previous Sessions**
log "🔄 Stopping existing Clarity processes..."
pkill -f "uvicorn" || true
pkill -f "npm run dev" || true

# ✅ **Step 3: Ensure Required Files Exist**
REQUIRED_FILES=("backend/main.py" "frontend/src/app/page.tsx" "frontend/package.json")

for file in "${REQUIRED_FILES[@]}"; do
    if [ ! -f "$file" ]; then
        log "⚠️ Missing: $file"
    fi
done

# ✅ **Step 4: Ensure Backend Virtual Environment Exists**
if [ ! -d "venv" ]; then
    log "⚠️ Backend virtual environment not found."
    log "👉 Run: python3 -m venv venv && source venv/bin/activate && pip install -r backend/requirements.txt"
    exit 1
fi

# ✅ **Step 5: Ensure Frontend Dependencies Exist**
if [ ! -d "frontend/node_modules" ]; then
    log "⚠️ Node modules missing. Running npm install..."
    cd frontend && npm install && cd ..
fi

# ✅ **Step 6: Open Terminal Tabs for Backend, Frontend, Logs, and Manual Terminal**
log "🖥️ Opening Terminal window with multiple tabs..."

osascript <<EOF &
tell application "Terminal"
    if (count of windows) > 0 then
        close (every window)
    end if
    do script "cd $(pwd)/backend && source ../venv/bin/activate && uvicorn src.api.main:app --host 127.0.0.1 --port 8000 --reload 2>&1 | tee -a $LOG_FILE"
    delay 1
    tell application "System Events" to keystroke "t" using {command down}
    delay 1
    do script "cd $(pwd)/frontend && npm run dev 2>&1 | tee -a $LOG_FILE" in front window
    delay 1
    tell application "System Events" to keystroke "t" using {command down}
    delay 1
    do script "tail -f $LOG_FILE" in front window
    delay 1
    tell application "System Events" to keystroke "t" using {command down}
    delay 1
    do script "echo '✅ This is your manual testing window. Use it for commands.'" in front window
end tell
EOF
disown

# ✅ **Step 7: Open Browser Tabs (No Duplicates)**
log "🌍 Opening browser tabs..."

osascript <<EOF &
tell application "Safari"
    set isRunning to (count of windows) > 0
    if not isRunning then
        make new document
    end if
    set found to false
    repeat with w in every window
        repeat with t in every tab of w
            if URL of t contains "127.0.0.1:3000" then set found to true
        end repeat
    end repeat
    if not found then
        tell window 1
            set current tab to (make new tab with properties {URL:"http://127.0.0.1:3000"})
            set current tab to (make new tab with properties {URL:"http://127.0.0.1:8000/docs"})
            set current tab to (make new tab with properties {URL:"http://127.0.0.1:8000/api/news"})
        end tell
    end if
end tell
EOF
disown

# ✅ **Step 8: Verify Services Without Blocking Execution**
(
    sleep 5
    log "✅ Verifying services..."
    if curl --output /dev/null --silent --head --fail "http://127.0.0.1:8000/docs"; then
        log "✅ Backend is running at http://127.0.0.1:8000"
    else
        log "❌ Backend failed to start. Check logs for errors."
    fi

    if curl --output /dev/null --silent --head --fail "http://127.0.0.1:3000"; then
        log "✅ Frontend is running at http://127.0.0.1:3000"
    else
        log "❌ Frontend failed to start. Attempting to fix..."
        rm -rf frontend/.next && cd frontend && npm run dev & cd ..
    fi
) & disown  # ✅ Runs in background and exits immediately

log "✅ Startup complete! Backend, frontend, logs, and manual terminal are all open. 🚀"

exit 0  # ✅ Ensures script exits IMMEDIATELY
