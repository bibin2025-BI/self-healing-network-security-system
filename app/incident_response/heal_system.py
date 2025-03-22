# app/network_management/heal_system.py
import requests
from app.utils import log_event

def heal_system(device_id):
    """Simulate healing a compromised device on the network."""
    try:
        response = requests.post(f'http://localhost:5000/api/heal_node/{device_id}')
        if response.status_code == 200:
            log_event('ACTION', f'Device {device_id} healed successfully.')
            return response.json()
        else:
            log_event('ERROR', f'Failed to heal device {device_id}. Status: {response.status_code}')
            return {'error': 'Device healing failed'}
    except Exception as e:
        log_event('ERROR', f'Exception while healing device {device_id}: {e}')
        return {'error': str(e)}

if __name__ == '__main__':
    device_id = input("Enter device ID to heal: ")
    result = heal_system(device_id)
    print(result)