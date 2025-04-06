from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    return f"Received Name: {name}, Email: {email}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
