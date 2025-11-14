from flask import Flask, request, jsonify
from encoder import Encoder
from decoder import Decoder

app = Flask(__name__)

#singleton classes that contains methods to encode and decode 
enc = Encoder.get_instance()
dec = Decoder.get_instance()

@app.route('/hello', methods=['GET'])
def hello_world():
    return 'Hello, World!'

@app.route('/encode', methods=['POST'])
def encode():
    if not request.is_json:
        return jsonify({"error":"Content type must be application/json"}), 400

    data = request.json

    cipher = data["cipher"] 
    if cipher not in enc.available_ciphers:
        return jsonify({"error":"Cipher not available"}), 406
    
    #getting proper cipher method to invoke 
    enc_cipher_method = getattr(enc, cipher)
    result_txt = enc_cipher_method(data["text"], data["key"])

    return jsonify({"text": result_txt})

@app.route('/decode', methods=['POST'])
def decode():
    raise NotImplementedError

@app.route('/encode/ciphers_list', methods=['GET'])
def encode_ciphers_list():
    return enc.available_ciphers

@app.route('/decode/ciphers_list', methods=['GET'])
def decode_ciphers_list():
    raise NotImplementedError

app.run(host='0.0.0.0', port=8080)