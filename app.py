from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/actuator/health', methods=['GET'])
def health_check():
    """
    Health check endpoint for monitoring
    """
    # Get available endpoints (excluding static files and health endpoint itself)
    endpoints = []
    for rule in app.url_map.iter_rules():
        # Filter out static files and the health endpoint itself
        if 'static' not in rule.endpoint and 'health_check' not in rule.endpoint:
            endpoints.append({
                "path": rule.rule,
                "methods": list(rule.methods - {'OPTIONS', 'HEAD'})
            })
    
    return jsonify({
        "status": "UP",
        "endpoints": endpoints
    }), 200

@app.route('/api/v1/greetings', methods=['GET'])
def get_greetings():
    """
    Endpoint that returns a list of greetings
    """
    greetings = ["Hi, I'm a Flask API! wdts python flask repo", "hello", "world"]
    return jsonify(greetings)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
