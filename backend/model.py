import tensorflow as tf
import cv2
import numpy as np

# Load the model
model = tf.keras.models.load_model('backend/model.h5')

def predict_frame(frame):
    frame = cv2.resize(frame, (64, 64))
    frame = np.expand_dims(frame, axis=0) / 255.0
    prediction = model.predict(frame)
    return "Fake" if prediction[0][0] > 0.5 else "Real"
