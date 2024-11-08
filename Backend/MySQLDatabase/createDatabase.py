from xml.dom.expatbuilder import ParseEscape
import mysql.connector
import MySQLInterface

sqlInterface = MySQLInterface.MySQLInterface("localhost", "root", "*tr5d7Ka9q", "AIHealthAndFitnessDatabase2");

sqlInterface.ConnectToDatabase()

#Creates a user and gives them an email and password
#sqlInterface.AddItem("user", ("email", "password"), ("matthiasharvey2006@gmai.com", "password123"))

#sets a specific users weight
#sqlInterface.SetItemAttribute("user", "weight", 143.13, 1)

#gets the entirety of the user table and prints off the results
#results = sqlInterface.GetTable("user")
#for x in results:
    #print(x)


#IMPORTANT: ONLY RUN THE BELOW CODE ONCE TO CREATE THE DATABASE
#def CreateDatabase():
#mydb = mysql.connector.connect(
#        host="localhost",
#        user="root",
#        password="*tr5d7Ka9q",
#        database="AIHealthAndFitnessDatabase2"
#    )
#sqlInterface = mydb.cursor()

#sqlInterface.execute("CREATE DATABASE AIHealthAndFitnessDatabase2")

#sqlInterface.execute("CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), sex INT, age INT, height DECIMAL(10, 2), weight DECIMAL(10, 2), diabetes BOOL, fitnessGoal INT, email VARCHAR(255), password VARCHAR(255))")

#sqlInterface.execute("CREATE TABLE workouts (id INT AUTO_INCREMENT PRIMARY KEY, userId INT,FOREIGN KEY (userID) REFERENCES users(id), workoutType VARCHAR(255), caloriesBurned INT, duration TIME, date DATE)")
#sqlInterface.execute("CREATE TABLE exercises (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), type VARCHAR(255), bodyPart VARCHAR(255), equipment VARCHAR(255))")
#sqlInterface.execute("CREATE TABLE workoutSets (id INT AUTO_INCREMENT PRIMARY KEY, workoutName VARCHAR(255), exerciseID INT, FOREIGN KEY (exerciseID) REFERENCES exercises(id), reps INT, weight INT)")

#sqlInterface.execute("CREATE TABLE interactionLogs (id INT AUTO_INCREMENT PRIMARY KEY, userID INT, FOREIGN KEY (userID) REFERENCES users(id),message VARCHAR(255), response VARCHAR(255), dateAndTime DATETIME)")

#sqlInterface.execute("CREATE TABLE meals (id INT AUTO_INCREMENT PRIMARY KEY, userID INT,FOREIGN KEY (userID) REFERENCES users(id), mealType VARCHAR(255), calories INT, protien INT, carbs INT, fat INT, date DATE)")
