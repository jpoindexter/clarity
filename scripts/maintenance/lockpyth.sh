#!/bin/bash

echo "🚀 Setting PYTHONPATH to match the new structure..."

# Remove any existing PYTHONPATH
sed -i '' '/export PYTHONPATH/d' ~/.zshrc

# Add the correct PYTHONPATH
echo 'export PYTHONPATH=/Users/jasonpoindexter/Documents/GitHub/clairity/backend' >> ~/.zshrc

# Apply changes immediately
source ~/.zshrc

echo "✅ PYTHONPATH set to backend/"

# Confirm path
echo "📂 Current PYTHONPATH:"
echo $PYTHONPATH
