from flask import Flask, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

@app.route("/")
def home():
    return "Bot is running"

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    prompt = data.get("prompt")

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return jsonify({
        "answer": response.choices[0].message.content
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
