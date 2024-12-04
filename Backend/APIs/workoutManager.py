# workoutManager.py

# Correct imports
from MySQLDatabase import MySQLInterface, workoutManager, user
from AI import openAPIIntegration, aiModelAccess
from MySQLDatabase.user import Login, CreateAccount
from APIs.config import DATABASE_CONFIG


db = MySQLInterface.MySQLInterface(
    DATABASE_CONFIG["host"],
    DATABASE_CONFIG["user"],
    DATABASE_CONFIG["password"],
    DATABASE_CONFIG["database"]
)
db.ConnectToDatabase()

# workoutManager.py
class WorkoutManager:
    @staticmethod
    def add_workout(data):
        # Simulate adding a workout recommendation
        # Here, you would typically save this to a database or generate a workout recommendation
        #sqlInterface, userId, workoutType, caloriesBurned, duration, date, sets
        userId = data.get("userId")
        workoutType = data.get("workoutType", "Weights")
        caloriesBurned = data.get("caloriesBurned")
        duration = data.get("duration")
        date = data.get("date")
        sets = data.get("sets")

        workoutManager.LogWorkout(db, userId, workoutType, caloriesBurned, duration, date, sets)

        return {"status": "Workout added"}

    @staticmethod
    def get_all_workouts(data):
        # Simulate retrieving workouts
        userId = data.get("userId")
        workouts = workoutManager.GetWorkouts(db, userId)
        return workouts
    
    @staticmethod
    def get_workout_recommendation(data):
        userId = data.get("userId")
        userData = user.GetUserAttributesForAI(db, userId)
        workoutType = aiModelAccess.GetWorkoutType(userData)
        exercises = aiModelAccess.GetExercises(userData)
        lastExcercise = data.get("lastExercise")
        recommendation = openAPIIntegration.GetWorkoutRecommendation(workoutType, exercises, lastExcercise, db, userId)
        return recommendation
