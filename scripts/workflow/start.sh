#!/bin/bash

# Define log directory and create it if it doesn't exist
LOG_DIR="$(pwd)/logs/startup"
mkdir -p "$LOG_DIR"
LOG_FILE="$LOG_DIR/$(date +'%Y-%m-%d_%H-%M-%S').log"

log() {
    echo "$(date +'%Y-%m-%d %H:%M:%S') - $1" | tee -a "$LOG_FILE"
}

{
  log "🚀 Stopping any existing processes on ports 8000 and 3000..."
  lsof -ti:8000 | xargs kill -9 2>/dev/null && log "✅ Stopped processes on port 8000" || log "⚠️ No processes found on port 8000"
  lsof -ti:3000 | xargs kill -9 2>/dev/null && log "✅ Stopped processes on port 3000" || log "⚠️ No processes found on port 3000"

  # Navigate to project root dynamically
  ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
  if cd "$ROOT_DIR"; then
      log "📂 Navigated to project root: $ROOT_DIR"
  else
      log "❌ Failed to navigate to project root"
      exit 1
  fi

  # Ensure tmux session exists
  TMUX_SESSION="clairity"
  if tmux has-session -t $TMUX_SESSION 2>/dev/null; then
      log "🔄 Attaching to existing tmux session: $TMUX_SESSION"
  else
      log "🔄 Creating new tmux session: $TMUX_SESSION..."
      tmux new-session -d -s $TMUX_SESSION -n Backend
      tmux send-keys -t $TMUX_SESSION:0 "cd $ROOT_DIR && source backend/venv/bin/activate && uvicorn backend.src.api.main:app --host 127.0.0.1 --port 8000 --reload | tee -a $LOG_FILE" C-m
      log "⚡ Backend started in tmux Pane 1"

      # 🟢 Create a new pane for Frontend
      tmux split-window -h -t $TMUX_SESSION
      tmux send-keys -t $TMUX_SESSION:1 "cd $ROOT_DIR/frontend && npm run dev | tee -a $LOG_FILE" C-m
      log "🖥️ Frontend started in tmux Pane 2"

      # 🟢 Create another pane for logs/debugging
      tmux split-window -v -t $TMUX_SESSION
      tmux send-keys -t $TMUX_SESSION:2 "tail -f $LOG_FILE" C-m
      log "📜 Logs running in tmux Pane 3"
  fi

  # Open the frontend in the browser
  log "🌍 Opening the frontend in the browser..."
  open "http://127.0.0.1:3000" && log "✅ Frontend opened in browser" || log "⚠️ Failed to open browser"

  # Attach to the tmux session
  log "✅ Clairity is now running in tmux. Use 'tmux attach -t $TMUX_SESSION' to view."
  tmux attach -t $TMUX_SESSION
} | tee -a "$LOG_FILE"
