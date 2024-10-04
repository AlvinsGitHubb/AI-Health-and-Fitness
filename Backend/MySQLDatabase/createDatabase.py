from xml.dom.expatbuilder import ParseEscape
import mysql.connector
import main
import MySQLInterface

sqlinterface = main.GetSQLInterface()

#Creates a user and gives them an email and password
#sqlInterface.AddItem("user", ("email", "password"), ("matthiasharvey2006@gmai.com", "password123"))

#sets a specific users weight
#sqlInterface.SetItemAttribute("user", "weight", 143.13, 1)

#gets the entirety of the user table and prints off the results
#results = sqlInterface.GetTable("user")
#for x in results:
    #print(x)


#IMPORTANT: ONLY RUN THE BELOW CODE ONCE TO CREATE THE DATABASE

#mycursor = sqlInterface.mydb.cursor()

#mycursor.execute("CREATE DATABASE AIHealthAndFitnessDatabase")

#mycursor.execute("CREATE TABLE user (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT, height DECIMAL(10, 2), weight DECIMAL(4, 2), gender VARCHAR(255), email VARCHAR(255), password VARCHAR(255))")

#mycursor.execute("CREATE TABLE workout (id INT AUTO_INCREMENT PRIMARY KEY, userID INT, workoutType VARCHAR(255), caloriesBurned INT, duration TIME, date DATE)")
#mycursor.execute("CREATE TABLE workout_set (id INT AUTO_INCREMENT PRIMARY KEY, workoutID INT, exerciseID INT, reps INT, weight INT)")
#mycursor.execute("CREATE TABLE exercise (id INT AUTO_INCREMENT PRIMARY KEY, muscleGroup VARCHAR(255), caloriesBurned DECIMAL(10, 3))")

#mycursor.execute("CREATE TABLE goal (id INT AUTO_INCREMENT PRIMARY KEY, userID INT, goal VARCHAR(255), progress DECIMAL(10, 10), deadline DATE)")

#mycursor.execute("CREATE TABLE interactionLog (id INT AUTO_INCREMENT PRIMARY KEY, userID INT, message VARCHAR(255), response VARCHAR(255), dateAndTime DATETIME)")

#mycursor.execute("CREATE TABLE meal (id INT AUTO_INCREMENT PRIMARY KEY, userID INT, mealType VARCHAR(255), calories INT, protien INT, carbs INT, fat INT, date DATE)")
