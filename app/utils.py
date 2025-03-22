# app/utils.py
import logging
from datetime import datetime

# Configure Logging
logging.basicConfig(filename='app_logs.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def log_event(event_type, message):
    """Logs events with a timestamp."""
    log_message = f"{event_type}: {message}"
    logging.info(log_message)

def current_timestamp():
    """Returns the current timestamp."""
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def analyze_packet(packet_data):
    """Mock function to analyze packet data for anomalies."""
    # Example packet analysis (replace with actual logic)
    if 'malicious' in packet_data:
        log_event('ALERT', 'Malicious activity detected in packet data.')
        return True
    log_event('INFO', 'Packet analyzed successfully.')
    return False
