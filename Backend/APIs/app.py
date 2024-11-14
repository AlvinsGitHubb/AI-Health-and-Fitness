# app.py
from flask import Flask, jsonify, request
from flask_cors import CORS
from user import Login, CreateAccount  # Import the Login and CreateAccount functions
from MySQLInterface import MySQLInterface

app = Flask(__name__)
CORS(app)

# Initialize database connection
db = MySQLInterface("localhost", "your_username", "your_password", "your_database")
db.ConnectToDatabase()

# User Login API endpoint
@app.route('/api/user/login', methods=['POST'])
def login_user():
    data = request.json
    try:
        user_id = Login(db, data.get("email"), data.get("password"))
        if user_id != -1:
            return jsonify({"status": "success", "user_id": user_id}), 200
        else:
            return jsonify({"status": "failure", "message": "Invalid credentials"}), 401
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# User Account Creation API endpoint
@app.route('/api/user/create', methods=['POST'])
def create_account():
    data = request.json
    try:
        user_id = CreateAccount(db, data.get("email"), data.get("password"))
        return jsonify({"status": "success", "user_id": user_id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
