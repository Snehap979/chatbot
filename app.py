from flask import Flask, request, jsonify
from flask_cors import CORS

import subprocess

app = Flask(__name__)
CORS(app)
def ask_ollama(prompt):
    result = subprocess.run(
        ["ollama", "run", "mistral", prompt],
        capture_output=True, text=True
    )
    return result.stdout.strip()

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    prompt = data.get("prompt", "")
    response = ask_ollama(prompt)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
