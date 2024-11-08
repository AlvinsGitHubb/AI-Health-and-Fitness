from asyncio.windows_events import NULL
from MySQLDatabase import user, MySQLInterface, workoutManager, mealManager
from AI import aiModelAccess, openAPIIntegration
from datetime import datetime, timedelta

sqlInterface = MySQLInterface.MySQLInterface("localhost", "root", "*tr5d7Ka9q", "AIHealthAndFitnessDatabase2");
sqlInterface.ConnectToDatabase()

#ALL OF THIS CODE THAT IS CURRENTLY IN MAIN IS JUST FOR TESTING AND MAKING SURE THAT ALL OF THE FUNCTIONS I MADE WORK IT WILL NOT BE PART OF THE FINAL PROJECT
userId = -1
while userId == -1:
    option = input("Create Account (0), Login (1), or quit (2): ")
    if option == "0":
        email = input("Please enter an email: ")
        password = input("Please input a password: ")

        userId = user.CreateAccount(sqlInterface, email, password)
        print(f"Account successfully created and loggd in. Your user ID is: {userId}")
    elif option == "1":
        email  = input("Enter your email: ")
        password = input("Enter your password: ")
        
        userId = user.Login(sqlInterface, email, password)
        if userId >= 0:
            print(f"You have successfully logged in. Your user ID is: {userId}")
        else:
            print("Invalid username or password!")
    elif option == "2":
        break
    else:
        print("Invalid Option")

if userId != -1:
    while True:
        option = input("What would you like to do? View User Data(0), Update User Data(1), Log Workout(2), View Workouts(3), Log Meal(4), View Meals(5), Speak With Chatbot(6), Get Exercice Recommendation(7), Get Meal Recommendation(8), Logout (9): ")
        if option == "0":
            _user = user.GetUserAttributes(sqlInterface, userId)
            for x in _user:
                print(x)
        elif option == "1":
            toChange = input("What value would you like to update? name, sex, age, height, weight, diabetes, fitnessGoal: ")
            toChangeTo = input("What would you like to change that value to?: ")
            user.SetUserAttribute(sqlInterface, toChange, toChangeTo, userId)
        elif option == "2":
            workoutType = input("What type of workout did you do?: ")
            duration = input("How long was your workout (in minutes)?: ")
            date = input("What day did you do your workout? (YYYY-MM-DD): ")
            sets = []
            while True:
                print("Adding a set.")
                exerciseId = input("Enter an exerciseId: ")
                reps = input("How many reps did you do?: ")
                weight = input ("How much weight did you use?: ")
                sets.append((exerciseId, reps, weight))
                cont = input("Do you want to add another set? No(0), Yes(1): ")
                if cont == "0":
                    break

            workoutManager.LogWorkout(sqlInterface, userId, workoutType, 0, duration, date, sets)
        elif option == "3":
            _workouts = workoutManager.GetWorkouts(sqlInterface, userId)
            for x in _workouts:
                print(x[0])
                if x[1] != NULL:
                    for y in x[1]:
                        print(y)
        elif option == "4":
            mealType = input("What type of meal did you have?: ")
            calories = input("How many calories were in the meal?: ")
            protein = input("How much protein was in the meal?: ")
            carbs = input("How much carbs was in the meal?: ")
            fat = input("How much fat was in the meal?: ")
            date = input("What day did you eat the meal? (YYYY-MM-DD): ")
            mealManager.LogMeal(sqlInterface, userId, mealType, calories, protein, carbs, fat, date)
        elif option == "5":
            _meals = mealManager.GetMeals(sqlInterface, userId)
            for x in _meals:
                print(x)
        elif option == "6":
            userMessage = input("What would you like to say to the chat bot?: ")
            chatBotMessage = openAPIIntegration.MessageChatBot(userMessage)
            print(chatBotMessage)
        elif option == "7":
            userData = user.GetUserAttributesForAI(sqlInterface, userId)
            workoutType = aiModelAccess.GetWorkoutType(userData)
            exercises = aiModelAccess.GetExercises(userData)
            print(f"{workoutType}, {exercises}")
            recommendation = openAPIIntegration.GetWorkoutRecommendation(workoutType, exercises)
            print(recommendation.content)
        elif option == "8":
            print("Not yet implemented")
        elif option == "9":
            break