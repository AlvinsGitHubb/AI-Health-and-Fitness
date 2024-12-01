# mealManager.py

from MySQLDatabase import MySQLInterface, mealManager, user
from AI import openAPIIntegration, aiModelAccess
from APIs.config import DATABASE_CONFIG

# Initialize database connection
db = MySQLInterface.MySQLInterface(
    DATABASE_CONFIG["host"],
    DATABASE_CONFIG["user"],
    DATABASE_CONFIG["password"],
    DATABASE_CONFIG["database"]
)
db.ConnectToDatabase()

class MealManager:
    @staticmethod
    def add_meal(data):
        """
        Adds a meal to the database.
        """
        userId = data.get("userId")
        mealType = data.get("mealType")
        calories = data.get("calories")
        protein = data.get("protein")  # Fixed typo: 'protien' to 'protein'
        carbs = data.get("carbs")
        fats = data.get("fats")
        date = data.get("date")
        
        mealManager.LogMeal(db, userId, mealType, calories, protein, carbs, fats, date)
        return {"status": "Meal added"}

    @staticmethod
    def get_all_meals(data):
        """
        Retrieves all meals for a specific user.
        """
        userId = data.get("userId")
        meals = mealManager.GetMeals(db, userId)  # Correctly calls the method
        return meals
    
    @staticmethod
    def get_meal_recommendation(data):
        userId = data.get("userId")
        cuisine = data.get("cuisine")
        dietaryRestrictions = data.get("dietaryRestrictions")
        ingredients = data.get("ingredients")
        fitnessGoal = user.GetUserAttribute(db, "fitnessGoal", userId)
        recommendation = openAPIIntegration.GetMealRecommendation(cuisine, dietaryRestrictions, ingredients, fitnessGoal)
        return recommendation
