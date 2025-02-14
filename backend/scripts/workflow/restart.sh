#!/bin/bash
echo "🔄 Restarting all services..."

./scripts/workflow/stop.sh
sleep 2
./scripts/workflow/start.sh

echo "✅ Services restarted!"
