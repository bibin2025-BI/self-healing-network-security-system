# app/routes.py
from flask import Blueprint, render_template, jsonify

app_routes = Blueprint('app_routes', __name__)

@app_routes.route('/')
def home():
    return render_template('index.html')

@app_routes.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app_routes.route('/api/system_status', methods=['GET'])
def system_status():
    # Mock system status data
    data = {
        'status': 'Healthy',
        'active_nodes': 25,
        'isolated_nodes': 2,
        'anomalies_detected': 5
    }
    return jsonify(data)

@app_routes.route('/api/isolate_node/<node_id>', methods=['POST'])
def isolate_node(node_id):
    # Simulated response for node isolation
    return jsonify({'message': f'Node {node_id} has been isolated successfully.'})
