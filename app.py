from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import json

app = Flask(__name__)
CORS(app)

JSON_FILE = 'data.json'

@app.route('/data', methods=['GET', 'POST'])
def get_json():
    if request.method == 'POST':
        try:
            # Get JSON data from request
            new_data = request.get_json()
            if not new_data:
                return jsonify({"error": "No JSON data received"}), 400
            
            # Save the new JSON data to file
            with open(JSON_FILE, 'w') as file:
                json.dump(new_data, file, indent=4)

            return jsonify({"message": "JSON file updated successfully"}), 200

        except Exception as e:
            return jsonify({"error": str(e)}), 500

    # Read and return JSON file content
    if os.path.exists(JSON_FILE):
        with open(JSON_FILE, 'r') as file:
            data = json.load(file)
        return jsonify(data)
    else:
        return jsonify({"message": "JSON file not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)

