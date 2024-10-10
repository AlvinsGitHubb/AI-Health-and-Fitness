from . import MySQLInterface

def LogMeal(sqlInterface, userId, mealType, calories, protien, carbs, fat, date):
     sqlInterface.AddItem("meals", ("userId", "mealType", "calories", "protien", "carbs", "fat", "date"), (userId, mealType, calories, protien, carbs, fat, date))

def GetMeals(sqlInterface, userId):
    _meals = sqlInterface.GetItemsBasedOnAttribute("meals", "userId", userId)
    return _meals 

def CalculateCaloriesBurned(workoutType, duration):
    print("This hasn't been implemented yet")