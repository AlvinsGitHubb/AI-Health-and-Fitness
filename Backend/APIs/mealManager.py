from MySQLDatabase import MySQLInterface, mealManager

db = MySQLInterface("localhost", "your_username", "your_password", "your_database")
db.ConnectToDatabase()

# mealManager.py
class MealManager:
    @staticmethod
    def add_meal(data):
        # Simulate adding a meal recommendation
        #sqlInterface, userId, mealType, calories, protien, carbs, fat, date
        userId = data.get("userId")
        mealType = data.get("mealType")
        calories = data.get("calories")
        protien = data.get("protein")
        carbs = data.get("carbs")
        fats = data.get("fats")
        date = data.get("date")
        
        mealManager.LogMeal(db, userId, mealType, calories, protien, carbs, fats, date)

        return {"status": "Meal added"}

    @staticmethod
    def get_all_meals(data):
        # Simulate retrieving meals
        userId = data.get("userId")
        meals = mealManager.GetMeals(db, userId)
        return meals
