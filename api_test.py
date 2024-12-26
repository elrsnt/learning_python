from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the API!"

# Example endpoint to fetch data
@app.route('/api/data', methods=['GET'])
def get_data():
    data = {"message": "Hello, World!", "status": "success"}
    return jsonify(data)

# Example endpoint to post data
@app.route('/api/data', methods=['POST'])
def post_data():
    input_data = request.json
    response = {"received_data": input_data, "status": "success"}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
