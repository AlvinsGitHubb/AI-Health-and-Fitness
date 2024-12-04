from flask import Flask, jsonify, request
from flask_cors import CORS

# Corrected imports based on the new structure
from MySQLDatabase.user import Login, CreateAccount
from MySQLDatabase.MySQLInterface import MySQLInterface
from APIs.workoutManager import WorkoutManager
from APIs.mealManager import MealManager
from APIs.config import DATABASE_CONFIG

# Import AI recommendation logic
from AI.openAPIIntegration import GetMealRecommendation

import sys
import os
# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

app = Flask(__name__)
CORS(app)

# Initialize database connection
db = MySQLInterface(
    DATABASE_CONFIG["host"],
    DATABASE_CONFIG["user"],
    DATABASE_CONFIG["password"],
    DATABASE_CONFIG["database"]
)
db.ConnectToDatabase()

# User Login API endpoint
@app.route('/api/user/login_user', methods=['POST'])
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
@app.route('/api/user/create_account', methods=['POST'])
def create_account():
    data = request.json
    try:
        user_id = CreateAccount(db, data.get("email"), data.get("password"))
        return jsonify({"status": "success", "user_id": user_id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Add a Meal API endpoint
@app.route('/api/meal/add', methods=['POST'])
def add_meal():
    data = request.json
    try:
        result = MealManager.add_meal(data)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Get Meals API endpoint
@app.route('/api/meal/get', methods=['GET'])
def get_meals():
    userId = request.args.get("userId")
    try:
        meals = MealManager.get_all_meals({"userId": userId})
        return jsonify(meals), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Add a Workout API endpoint
@app.route('/api/workout/add', methods=['POST'])
def add_workout():
    data = request.json
    try:
        result = WorkoutManager.add_workout(data)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Get Workouts API endpoint
@app.route('/api/workout/get', methods=['GET'])
def get_workouts():
    userId = request.args.get("userId")
    try:
        workouts = WorkoutManager.get_all_workouts({"userId": userId})
        return jsonify(workouts), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# New API endpoint for AI meal recommendations
@app.route('/api/meal/recommend', methods=['POST'])
def recommend_meal():
    data = request.json
    try:
        # Extract meal details from the request
        cuisine = data.get("cuisine", "any")
        dietary_restrictions = data.get("dietary_restrictions", [])
        ingredients = data.get("ingredients", [])
        fitness_goal = data.get("fitnessGoal", "maintain weight")

        # Call the AI meal recommendation logic
        recommendation = GetMealRecommendation(cuisine, dietary_restrictions, ingredients, fitness_goal)

        # Return the recommendation as JSON
        return jsonify({"recommendation": recommendation}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=8080)
