#!/bin/bash

CLARITY_ROOT="$HOME/Documents/GitHub/clarity"

/usr/bin/osascript <<EOF
tell application "iTerm"
    activate
    set currentWindow to (create window with default profile)

    -- Backend only
    tell current session of currentWindow
        write text "cd $CLARITY_ROOT; PYTHONPATH=. /Users/jasonpoindexter/.global-venv/bin/python3 -m uvicorn backend.main:app --reload --log-level debug"
        set name to "Backend"
    end tell

    delay 1
    -- Frontend tab
    tell currentWindow
        create tab with default profile
        tell current session
            write text "cd \"$CLARITY_ROOT/frontend\" && npm run dev"
            set name to "Frontend"
        end tell
    end tell

    delay 1
    -- Ollama tab
    tell currentWindow
        create tab with default profile
        tell current session
            write text "ollama run deepseek-r1:14b"
            set name to "Ollama"
        end tell
    end tell
end tell
EOF