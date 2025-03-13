#!/bin/bash
echo "🔄 Resetting frontend..."
cd frontend || exit
rm -rf .next node_modules
npm install
echo "✅ Frontend reset complete."
