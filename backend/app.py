from flask import Flask, request, jsonify
from flask_cors import CORS
from model import analyze_food_image

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests from frontend

@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        if "image" not in request.files:
            return jsonify({"error": "No image provided"}), 400

        image = request.files["image"]
        result = analyze_food_image(image)

        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
