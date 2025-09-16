from flask import Flask, request, jsonify
from flask_cors import CORS
from model import predict_calories

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Nutri.ai Backend Running"

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400
    image = request.files['image']
    result = predict_calories(image)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
