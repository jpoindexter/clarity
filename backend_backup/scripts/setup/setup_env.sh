#!/bin/bash
echo "🔑 Setting up environment variables..."
ENV_FILE=".env"

# Create the file if it doesn’t exist
if [ ! -f "$ENV_FILE" ]; then
    cat <<EOL > "$ENV_FILE"
# Database Config
DATABASE_URL=postgresql://user:password@localhost:5432/Clarity

# API Keys

# Server Config
BACKEND_HOST=127.0.0.1
BACKEND_PORT=8000
FRONTEND_HOST=127.0.0.1
FRONTEND_PORT=3000
EOL
    echo "✅ .env file created successfully!"
else
    echo "⚠️ .env file already exists, skipping..."
fi
