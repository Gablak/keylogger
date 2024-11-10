#!/bin/bash

# Stop server.py if running
if pgrep -f "server.py" > /dev/null; then
    pkill -f "server.py"
    echo "Stopped server.py"
else
    echo "server.py was not running"
fi

# Stop UI.py if running
if pgrep -f "UI.py" > /dev/null; then
    pkill -f "UI.py"
    echo "Stopped UI.py"
else
    echo "UI.py was not running"
fi
