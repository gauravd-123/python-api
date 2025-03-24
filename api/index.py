import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load API key from environment variable
TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY", "008f5f36c3fa637d9d8b466296843fb89c60259741ee712f149223653bf54b87")

# TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")
if not TOGETHER_API_KEY:
    raise ValueError("Missing API key! Set TOGETHER_API_KEY in environment variables.")

@app.route("/ai", methods=["POST"])
def process_message():
    data = request.get_json()
    user_message = data.get("message", "")

    # Call Together AI (Free)
    response = requests.post(
        "https://api.together.xyz/v1/chat/completions",
        headers={"Authorization": f"Bearer {TOGETHER_API_KEY}"},
        json={
            "model": "meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
            "messages": [{"role": "user", "content": user_message}]
        }
    )

    return jsonify(response.json())

@app.route("/test", methods=["GET"])
def test_route():
    return "Working fine"

# Required for Vercel
handler = app

if __name__ == "__main__":
    app.run(debug=True)
    # import os
    # port = int(os.environ.get("VERCEL_DEV_SERVER_PORT", 8000))  # Use Vercel's port
    # app.run(host="0.0.0.0", port=port)

