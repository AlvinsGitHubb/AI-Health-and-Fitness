import tensorflow as tf
from tensorflow.keras import Model, Input
from tensorflow.keras.models import load_model
import numpy as np

from pathlib import Path

#Keys for what the outputs of the AI means.
workoutTypeArray = ['Fitness Type_Muscular Fitness', 'Fitness Type_Cardio Fitness']
    #For Fitness Type
exercisesArray = ['Exercises_Squats, deadlifts, bench presses, and overhead presses', 
                  'Exercises_Squats, yoga, deadlifts, bench presses, and overhead presses', 
                  'Exercises_Brisk walking, cycling, swimming, running , or dancing.',
                  'Exercises_Walking, Yoga, Swimming.',
 	              'Exercises_brisk walking, cycling, swimming, or dancing.']

#print(model_save_path)
def LoadModel(modelName):
    current_file_path = Path(__file__).resolve()
    current_directory = current_file_path.parent
    model_save_path = f"{str(current_directory)}\\{modelName}.keras"
    
    reloaded_model = load_model(f"{model_save_path}")
    return reloaded_model

def ReformatUserData(userData):
    input = []
    input_row = []

    for entry in userData:
        input_row.append(entry)
    
    input.append(input_row)

    input = np.array(input, dtype=np.float32)

    if input.size == 0:
        raise ValueError("Inputs or Outputs array is empty. Check your data source.")
    
    return input

def GetPredictions(userData, modelName):
    input = ReformatUserData(userData)
    model = LoadModel(modelName)
    predictions = model.predict(input)
    return predictions

def ReformatOutputToText(output, textArray):
    x = 0
    max = 0;
    for y in range(0, output.size):
        if output[y] > max:
            max = output[y]
            x = y
    return textArray[x]

def GetWorkoutType(userData):
    predictions = GetPredictions(userData, "fitnessTypeModel")
    return ReformatOutputToText(predictions[0], workoutTypeArray)

def GetExercises(userData):
    predictions = GetPredictions(userData, "exercisesModel")
    return ReformatOutputToText(predictions[0], exercisesArray)