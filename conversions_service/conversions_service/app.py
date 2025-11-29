from flask import Flask, request, jsonify
from conversions_service.services.encode_api import EncodeApi
import logging
import os

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
encode_api = EncodeApi.get_instance()

@app.route('/hello', methods=['GET'])
def hello_world():
    return 'Hello, World!'

@app.route('/encode', methods=['POST'])
def encode():
    if not request.is_json:
        return jsonify({"error": "Content type must be application/json"}), 400

    data = request.get_json()
    try:
        result = encode_api.encode(data)
        return jsonify({"result": result})
    except Exception as e:
        app.logger.exception("Error in /encode")
        return jsonify({"error": str(e)}), 400

@app.route('/decode', methods=['POST'])
def decode():
    if not request.is_json:
        return jsonify({"error": "Content type must be application/json"}), 400

    data = request.get_json()
    try:
        result = encode_api.decode(data)
        return jsonify({"result": result})
    except Exception as e:
        app.logger.exception("Error in /decode")
        return jsonify({"error": str(e)}), 400


@app.route('/encode/ciphers_list', methods=['GET'])
def encode_ciphers_list():
    return jsonify(encode_api.available_encode_ciphers)

@app.route('/decode/ciphers_list', methods=['GET'])
def decode_ciphers_list():
    return jsonify(encode_api.available_decode_ciphers)

if __name__ == '__main__' and os.getenv('ENV') == 'prod':
    import waitress
    waitress.serve(app, host='0.0.0.0', port=8080)
else:
    app.run(host='0.0.0.0', port=8080, debug=True)
