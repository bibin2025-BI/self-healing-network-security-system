# app/network_management/isolate_device.py
import requests
from app.utils import log_event

def isolate_device(device_id):
    """Simulate isolating a compromised device on the network."""
    try:
        response = requests.post(f'http://localhost:5000/api/isolate_node/{device_id}')
        if response.status_code == 200:
            log_event('ACTION', f'Device {device_id} isolated successfully.')
            return response.json()
        else:
            log_event('ERROR', f'Failed to isolate device {device_id}. Status: {response.status_code}')
            return {'error': 'Device isolation failed'}
    except Exception as e:
        log_event('ERROR', f'Exception while isolating device {device_id}: {e}')
        return {'error': str(e)}

if __name__ == '__main__':
    device_id = input("Enter device ID to isolate: ")
    result = isolate_device(device_id)
    print(result)
