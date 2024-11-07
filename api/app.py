from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import cv2
from backend.model import predict_frame

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    video = request.files['file']
    cap = cv2.VideoCapture(video)
    
    # Process a few frames from the video
    predictions = []
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        predictions.append(predict_frame(frame))
    
    # Simple majority voting
    result = max(set(predictions), key=predictions.count)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
