# app/detection_model/test_model.py
import pandas as pd
import numpy as np
import joblib
from sklearn.metrics import classification_report
from app.utils import log_event
from app.detection_model.preprocess import preprocess_data

def load_model():
    """Load the trained model from model.pkl."""
    try:
        model = joblib.load('app/detection_model/model.pkl')
        print("Model loaded successfully.")
        return model
    except FileNotFoundError:
        print("Error: model.pkl not found. Please train the model first.")
        return None

def test_model(file_path):
    """Test the trained model using provided data."""
    model = load_model()
    if model is None:
        return

    X_test, y_test = preprocess_data(file_path)
    if X_test is None or y_test is None:
        print("Invalid test data.")
        return

    predictions = model.predict(X_test)
    predictions = np.where(predictions == 1, 0, 1)  # 1 for anomaly, 0 for normal
    print("Testing completed.")
    print(classification_report(y_test, predictions))

    log_event('TEST', f'Model tested on {file_path}.')

if __name__ == '__main__':
    test_data_path = 'data/sample_data.csv'
    test_model(test_data_path)
