# Self-Healing Network Security System

The Self-Healing Network Security System detects network anomalies, isolates compromised devices, and attempts to heal them using automated processes.

## Features
- Real-time network anomaly detection
- Device isolation and healing
- Logging and reporting
- Model training and testing

## Project Structure
```
Self-Healing-Network-Security-System/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── utils.py
│   ├── config.py
│   ├── detection_model/
│   │   ├── preprocess.py
│   │   ├── train_model.py
│   │   ├── test_model.py
│   │   ├── model.pkl
│   ├── network_management/
│   │   ├── isolate_device.py
│   │   ├── heal_system.py
│   ├── tests/
│   │   ├── test_routes.py
├── data/
│   ├── sample_data.csv
├── static/
│   ├── css/
│   │   ├── style.css
│   ├── js/
│   │   ├── script.js
├── templates/
│   ├── index.html
│   ├── result.html
├── logs.db
├── create_logs_db.py
├── run.py
├── requirements.txt
└── README.md
```

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/your-repo/self-healing-network-security-system.git
    cd self-healing-network-security-system
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up the database:
    ```bash
    python create_logs_db.py
    ```

4. Train the model:
    ```bash
    python app/detection_model/train_model.py
    ```

5. Run the application:
    ```bash
    python run.py
    ```

## API Endpoints
- `GET /` - Home Page
- `POST /api/isolate_node/<device_id>` - Isolate a device
- `POST /api/heal_node/<device_id>` - Heal a device

## Testing
Run tests using:
```bash
python -m unittest app/tests/test_routes.py
```

## Contributing
Feel free to submit issues and pull requests.

## License
This project is licensed under the MIT License.
