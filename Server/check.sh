#!/bin/bash

# Check if server.py is running
if pgrep -f "server.py" > /dev/null; then
    echo "server.py is running"
else
    echo "server.py is not running"
fi

# Check if UI.py is running
if pgrep -f "UI.py" > /dev/null; then
    echo "UI.py is running"
else
    echo "UI.py is not running"
fi
