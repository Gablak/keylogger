#!/bin/bash

# Define the path to the logs directory
LOG_DIR="./logs"

# Create the logs directory if it doesn't exist
mkdir -p "$LOG_DIR"

# Start server.py in the background, logging to logs/server.log
nohup python3.12 server.py > "$LOG_DIR/server_latest.log" 2>&1 &

# Start UI.py in the background, logging to logs/ui.log
nohup python3.12 UI.py > "$LOG_DIR/ui_latest.log" 2>&1 &

# Display message and return to the prompt
echo "Server running!"
