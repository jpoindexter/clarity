#!/bin/bash

echo "🚀 Updating imports to match the new backend structure..."

# Find and replace all `from src.` references → Change to `from backend.`
find backend/ -type f -name "*.py" -exec sed -i '' 's/from src./from backend./g' {} +

# Find and replace all `import src.` references → Change to `import backend.`
find backend/ -type f -name "*.py" -exec sed -i '' 's/import src./import backend./g' {} +

echo "✅ Imports updated successfully!"

# Final check for incorrect imports
echo "🔍 Checking for any remaining incorrect imports..."
grep -rnw backend/ -e "from src." -e "import src."

echo "✅ Import cleanup complete!"
