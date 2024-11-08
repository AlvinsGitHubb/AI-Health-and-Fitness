from . import MySQLInterface

def LogWorkout(sqlInterface, userId, workoutType, caloriesBurned, duration, date, sets):
     sqlInterface.AddItem("workouts", ("userId", "workoutType", "caloriesBurned", "duration", "date"), (userId, workoutType, caloriesBurned, duration, date))
     workoutId = sqlInterface.GetLastInsertId()
     for x in sets:
         LogSet(sqlInterface, workoutId, x[0], x[1], x[2])

def LogSet(sqlInterface, workoutId, exerciseId, reps, weight):
    sqlInterface.AddItem("workoutSets", ("workoutId", "exerciseId", "reps", "weight"), (workoutId, exerciseId, reps, weight))

def GetWorkouts(sqlInterface, userId):
    _workouts = sqlInterface.GetItemsBasedOnAttribute("workouts", "userId", userId)
    workouts = []
    for x in _workouts:
        _sets = GetSets(sqlInterface, x[0])
        workouts.append((x, _sets))
    return workouts #This is a list where the first value (workouts[0]) is the wokrout details and the second value (workouts[1]) is a list of workout set details

def GetSets(sqlInterface, workoutId):
    _sets = sqlInterface.GetItemsBasedOnAttribute("workoutSets", "workoutId", workoutId)
    return _sets

def CalculateCaloriesBurned(workoutType, duration):
    print("This hasn't been implemented yet")