from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello_world():
    return 'Hello, World!'

app.run(host='0.0.0.0', port=8080)