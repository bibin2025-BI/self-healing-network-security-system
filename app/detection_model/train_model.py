# app/detection_model/train_model.py
import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib

def load_data(file_path):
    """Load dataset from CSV file."""
    return pd.read_csv(file_path)

def preprocess_data(df):
    """Preprocess data for model training."""
    df.fillna(0, inplace=True)
    X = df.drop(columns=['label'])
    y = df['label']
    return X, y

def train_model(X, y):
    """Train an Isolation Forest model for anomaly detection."""
    model = IsolationForest(n_estimators=100, contamination=0.1, random_state=42)
    model.fit(X)
    joblib.dump(model, 'app/detection_model/model.pkl')
    print("Model saved as model.pkl")

def evaluate_model(X, y):
    """Evaluate model performance."""
    model = joblib.load('app/detection_model/model.pkl')
    predictions = model.predict(X)
    predictions = np.where(predictions == 1, 0, 1)  # 1 for anomaly, 0 for normal
    print(classification_report(y, predictions))

def main():
    data = load_data('data/sample_data.csv')
    X, y = preprocess_data(data)
    train_model(X, y)
    evaluate_model(X, y)

if __name__ == '__main__':
    main()
