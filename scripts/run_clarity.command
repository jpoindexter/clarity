#!/bin/bash

CLARITY_ROOT="$HOME/Documents/GitHub/clarity"

/usr/bin/osascript <<EOF
tell application "iTerm"
    activate
    set newWindow to (create window with default profile)
    tell current session of newWindow
        write text "lsof -ti:8000 | xargs kill -9; /Users/jasonpoindexter/.global-venv/bin/python3 -m pip show requests || echo '❌ requests not installed in this Python'; cd \"$CLARITY_ROOT\" && /Users/jasonpoindexter/.global-venv/bin/python3 -m uvicorn backend.main:app --reload"
        set name to "Backend"
    end tell
 
    delay 1
    tell current window
        create tab with default profile
        tell current session
            write text "cd \"$CLARITY_ROOT/frontend\" && npm run dev"
            set name to "Frontend"
        end tell
    end tell
  
    delay 1 
    tell current window
        create tab with default profile
        tell current session
            write text "ollama run deepseek-coder"
            set name to "Ollama"
        end tell
    end tell
end tell
EOF