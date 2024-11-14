# mealManager.py
class MealManager:
    @staticmethod
    def add_meal(data):
        # Simulate adding a meal recommendation
        meal = {
            "id": 1,
            "name": data.get("name", "Balanced Meal"),
            "calories": data.get("calories", 500),
            "protein": data.get("protein", 30),
            "carbs": data.get("carbs", 50),
            "fats": data.get("fats", 15),
            "notes": data.get("notes", "Recommended meal based on dietary needs.")
        }
        return {"status": "Meal added", "meal": meal}

    @staticmethod
    def get_all_meals():
        # Simulate retrieving meals
        meals = [
            {"id": 1, "name": "Salad with Grilled Chicken", "calories": 400},
            {"id": 2, "name": "Pasta Primavera", "calories": 600}
        ]
        return meals
