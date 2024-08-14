from flask import Flask, render_template, request
import os

app = Flask(__name__)

def get_text_files():
  """Retrieves a list of text files from the current directory."""
  text_folder = os.path.dirname(__file__)
  return [f for f in os.listdir(text_folder) if f.endswith(".txt")]  # Filter for .txt files

@app.route("/")
def index():
  text_files = get_text_files()
  return render_template("index.html", text_files=text_files)


@app.route("/show_file/<filename>")
def show_file(filename):
  text_folder = os.path.dirname(__file__)
  filepath = os.path.join(text_folder, filename)
  if not os.path.isfile(filepath):
    return f"File '{filename}' not found."
  try:
    with open(filepath, "r") as f:
      file_content = f.read()
  except FileNotFoundError:
    return f"Error accessing file '{filename}'"
  return render_template("file.html", content=file_content)

@app.route("/clear_content/<filename>", methods=["POST"])
def clear_content(filename):
  text_folder = os.path.dirname(__file__)
  filepath = os.path.join(text_folder, filename)
  if not os.path.isfile(filepath):
    return f"File '{filename}' not found.", 404  # Return 404 Not Found status code

  try:
    with open(filepath, "w") as f:  # Open in write mode to clear content
      f.write("")  # Write an empty string to clear the file
    return "", 204  # No Content status code on successful clearing
  except PermissionError:
    return "Error deleting file: Insufficient permissions.", 403  # Return 403 Forbidden
  except OSError as e:
    return f"Error clearing file: {e}", 500  # Return 500 Internal Server Error


if __name__ == "__main__":
  app.run(debug=False,host="0.0.0.0", port=3500)
