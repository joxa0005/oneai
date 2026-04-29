from flask import Flask, request
import requests
import os

app = Flask(__name__)

HF_TOKEN = os.environ.get("HF_TOKEN")
API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-base"

headers = {"Authorization": f"Bearer {HF_TOKEN}"}

@app.route("/", methods=["GET"])
def home():
    return "OneAI bot ishlayapti!"

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    prompt = data.get("prompt")

    response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
    return response.json()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
