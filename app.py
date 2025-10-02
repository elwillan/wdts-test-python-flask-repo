from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/v1/greetings', methods=['GET'])
def get_greetings():
    """
    Endpoint that returns a list of greetings
    """
    greetings = ["hello", "world"]
    return jsonify(greetings)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
