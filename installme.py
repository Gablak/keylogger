import subprocess
import sys

# List of packages to install
packages = [
    "thread",
    "pynput",
    "pywin32",
    "pyperclip",
    "secure-smtplib",
    "requests",
    "sockets",
    "jsons",
    "os-sys",
    "time",
    "flask",
    "pyinstaller",
    "winshell",
]

# Install packages
for package in packages:
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    except subprocess.CalledProcessError:
        print(f"Failed to install {package}")
    else:
        print(f"{package} installed successfully!")

print("All packages processed!")
print("Press ENTER ot continue...")

input()