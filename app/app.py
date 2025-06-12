from flask import Flask, request, jsonify
from flask_cors import CORS
from cryptobuddy import crypto_buddy_response


app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/')
def home():
    return "Welcome to CryptoBuddy API! Use POST /chat to interact."

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_input = data.get('message', '')
    bot_reply = crypto_buddy_response(user_input)
    return jsonify({'response': bot_reply})

if __name__ == '__main__':
    app.run(debug=True)
