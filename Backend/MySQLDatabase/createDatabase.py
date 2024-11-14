import mysql.connector
import MySQLInterface

# Define MySQL connection details
sqlInterface = MySQLInterface.MySQLInterface("localhost", "root", "Alvin2003$", "AIHealthAndFitnessDatabase2")
sqlInterface.ConnectToDatabase()

# Uncomment these lines if the tables are already created, or if you're testing other functionality:
# Creates a user and gives them an email and password
sqlInterface.AddItem("user", ("email", "password"), ("matthiasharvey2006@gmai.com", "password123"))

# Sets a specific user's weight
sqlInterface.SetItemAttribute("user", "weight", 143.13, 1)

# Gets the entirety of the user table and prints off the results
results = sqlInterface.GetTable("user")
for x in results:
    print(x)

# Function to create the database and tables
def CreateDatabase():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Alvin2003$"  # Update this password if needed
    )
    cursor = mydb.cursor()
    
    # Create database
    #cursor.execute("CREATE DATABASE IF NOT EXISTS AIHealthAndFitnessDatabase2")
    
    # Connect to the new database
    mydb.database = "AIHealthAndFitnessDatabase2"
    
    # Create tables
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), sex INT, age INT, height DECIMAL(10, 2), weight DECIMAL(10, 2), diabetes BOOL, fitnessGoal INT, email VARCHAR(255), password VARCHAR(255))")
    cursor.execute("CREATE TABLE IF NOT EXISTS workouts (id INT AUTO_INCREMENT PRIMARY KEY, userId INT, FOREIGN KEY (userId) REFERENCES users(id), workoutType VARCHAR(255), caloriesBurned INT, duration TIME, date DATE)")
    cursor.execute("CREATE TABLE IF NOT EXISTS exercises (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), type VARCHAR(255), bodyPart VARCHAR(255), equipment VARCHAR(255))")
    cursor.execute("CREATE TABLE IF NOT EXISTS workoutSets (id INT AUTO_INCREMENT PRIMARY KEY, workoutId INT, FOREIGN KEY (workoutId) REFERENCES workouts(id), exerciseID INT, FOREIGN KEY (exerciseID) REFERENCES exercises(id), reps INT, weight INT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS interactionLogs (id INT AUTO_INCREMENT PRIMARY KEY, userID INT, FOREIGN KEY (userID) REFERENCES users(id), message VARCHAR(255), response VARCHAR(255), dateAndTime DATETIME)")
    cursor.execute("CREATE TABLE IF NOT EXISTS meals (id INT AUTO_INCREMENT PRIMARY KEY, userID INT, FOREIGN KEY (userID) REFERENCES users(id), mealType VARCHAR(255), calories INT, protein INT, carbs INT, fat INT, date DATE)")

    # Commit and close
    mydb.commit()
    cursor.close()
    mydb.close()

# Call CreateDatabase only once, when setting up the database initially
CreateDatabase()
