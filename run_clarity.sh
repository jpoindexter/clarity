#!/bin/bash

echo "🚀 Starting Clarity stack..."

# 1. Launch Ollama AI model (Mistral)
echo "🧠 Launching Mistral via Ollama..."
ollama run mistral &
sleep 2

# 2. Start the FastAPI backend
echo "⚙️ Launching FastAPI backend..."
uvicorn backend.main:app --reload &
 
# 3. Start the Next.js frontend
echo "🌐 Launching Next.js frontend..."
cd frontend
npm run dev