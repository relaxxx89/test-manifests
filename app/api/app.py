from flask import Flask, jsonify
from flask_cors import CORS
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'}), 200

@app.route('/health-readiness', methods=['GET'])
def health_readiness():
    return jsonify({'status': 'healthy'}), 200

@app.route('/health-startup', methods=['GET'])
def health_startup():
    return jsonify({'status': 'healthy'}), 200

@app.route('/info', methods=['GET'])
def info():
    return jsonify({
        'app': 'Simple Training App',
        'version': '1.0',
        'timestamp': datetime.now().isoformat(),
        'hostname': os.getenv('HOSTNAME', 'unknown')
    }), 200

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        'message': 'Hello from Kubernetes!',
        'endpoints': ['/health', '/info']
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
