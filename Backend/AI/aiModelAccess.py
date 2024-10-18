import tensorflow as tf
from tensorflow.keras import Model, Input

from pathlib import Path


#print(model_save_path)
def LoadModel(modelName):
    current_file_path = Path(__file__).resolve()
    current_directory = current_file_path.parent

    model_save_path = f"{str(current_directory)}\{modelName}.keras"
    reloaded_model = tf.keras.models.load_model(model_save_path, custom_objects=None, compile=True, safe_mode=True)
    return reloaded_model

def GetWorkoutType(userData):
    model = LoadModel("fitnessTypeModel")
    predictions = model.predict(userData)
    return predictions

def GetExercises(userData):
    model = LoadModel("exercisesModel")
    predictions = model.predict(userData)
    return predictions