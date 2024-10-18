import tensorflow as tf
from tensorflow.keras import Model, Input

from pathlib import Path


#print(model_save_path)
def LoadModel(modelName):
    current_file_path = Path(__file__).resolve()
    current_directory = current_file_path.parent

    model_save_path = f"{str(current_directory)}\{modelName}"
    reloaded_model = tf.saved_model.load(f"{model_save_path}")
    return reloaded_model

def GetWorkoutType(userData):
    model = LoadModel("fitnessTypeModel")
    predictions = model.predict(userData)
    return predictions

def GetExercises(userData):
    model = LoadModel("exercisesModel")
    predictions = model.predict(userData)
    return predictions