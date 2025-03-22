# app/detection_model/preprocess.py
import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_data(file_path):
    """Load dataset from CSV file."""
    try:
        df = pd.read_csv(file_path)
        print(f"Data loaded successfully from {file_path}")
        return df
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None

def clean_data(df):
    """Clean data by filling missing values and removing duplicates."""
    df = df.drop_duplicates()
    df.fillna(0, inplace=True)
    print("Data cleaned: Missing values filled and duplicates removed.")
    return df

def scale_data(X):
    """Scale data using StandardScaler for normalization."""
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    print("Data scaled using StandardScaler.")
    return X_scaled

def preprocess_data(file_path):
    """Full preprocessing pipeline: load, clean, and scale data."""
    df = load_data(file_path)
    if df is None:
        return None, None
    
    df = clean_data(df)
    X = df.drop(columns=['label'], errors='ignore')
    y = df['label'] if 'label' in df.columns else None
    X_scaled = scale_data(X)

    print("Preprocessing complete.")
    return X_scaled, y

if __name__ == '__main__':
    file_path = 'data/sample_data.csv'
    X, y = preprocess_data(file_path)
    print(f"Processed Data: {X.shape}, Labels: {y.shape if y is not None else 'N/A'}")
