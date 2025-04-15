from flask import Flask, request, render_template, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.json["message"]
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "llama2", "prompt": user_input}
    )
    return jsonify({"response": response.json()["response"]})

if __name__ == "__main__":
    app.run(debug=True)
