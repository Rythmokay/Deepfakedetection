<<<<<<< HEAD
# Deepfake Detection Model

## Overview
This project detects deepfakes using a deep learning model trained on real and fake videos.

## Project Structure
- `backend/`: Model training, prediction, and utilities.
- `api/`: Flask API for serving the model with a basic HTML frontend.
- `dataset/`: Contains real and fake videos for training.

## Setup and Installation

1. Clone the repository:
    ```bash
    git clone 
    cd deepfake-detection
    ```

2. Install dependencies:
    ```bash
    pip install -r backend/requirements.txt
    ```

3. Download the dataset from [Kaggle](https://www.kaggle.com/c/deepfake-detection-challenge/data) and place videos in `dataset/`.

4. Train the model (optional):
    Open `backend/model_training.ipynb` to train the model on the downloaded dataset.

5. Run the API:
    ```bash
    cd api
    python app.py
    ```

6. Access the UI:
   Visit `http://localhost:5000` in your browser to upload and detect deepfake videos.

## Usage
- Use the HTML form to upload a video and get the prediction result as "Real" or "Fake."

## Notes
- **Model**: This project uses a simple CNN model and processes individual frames of videos.
- **Frontend**: Basic HTML form to upload videos.
=======
# Deepfakedetection
>>>>>>> e55cdd5bf47d8c78e0436c3dac924a30bbf9978d
