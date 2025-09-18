from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "FoodCal AI Backend is running!"})

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    food_name = data.get("food")
    return jsonify({
        "food": food_name,
        "api_key_used": "6914b0e746aa4b13858ca0583e9e0ae7"  # remove later
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
