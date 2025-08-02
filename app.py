from flask import Flask, request, jsonify
from flask_cors import CORS
from process_file import process_file

app = Flask(__name__)
CORS(app)  # Allow WordPress to connect

@app.route('/process', methods=['POST'])
def process():
    if 'file' not in request.files:
        return jsonify({"output": "No file uploaded", "status": "error"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"output": "No file selected", "status": "error"}), 400
    
    # Read file content
    file_content = file.read()
    
    # Process the file
    result = process_file(file_content)
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)