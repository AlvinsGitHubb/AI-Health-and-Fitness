import tensorflow as tf
from tensorflow.keras import Model, Input
from tensorflow.keras.layers import Dense
import numpy as np
import json
import datetime
import os

input_columns = ['Sex_Male', 'Sex_Female', 'Age', 'Height', 'Weight', 'Diabetes', 'Fitness Goal_Weight Loss', 'Fitness Goal_Weight Gain']
#For Fitness Type: output_columns = ['Fitness Type_Muscular Fitness', 'Fitness Type_Cardio Fitness']
output_columns = ['Exercises_Squats, deadlifts, bench presses, and overhead presses', 
                  'Exercises_Squats, yoga, deadlifts, bench presses, and overhead presses', 
                  'Exercises_Brisk walking, cycling, swimming, running , or dancing.',
                  'Exercises_Walking, Yoga, Swimming.',
 	              'Exercises_brisk walking, cycling, swimming, or dancing.']
#Array of the names of colums to have in input
#Read Json file
#Iterate through values in 2darray file and make a new Json file but only including the columns in the origional array
#This new file is the inputs
#Do the same for outputs

with open('oneHotEncodedGymRecommendations.json', 'r') as file:
    data = json.load(file)

inputs = []
outputs = []

for entry in data:
    input_row = []
    for col in input_columns:
        try:
            input_column = entry[col]
            input_row.append(input_column)
        except:
            input_row.append(False)
    inputs.append(input_row)
    
    output_row = []
    for col in output_columns:
        try:
            output_column = entry[col]
            output_row.append(output_column)
        except:
            output_row.append(False)
    outputs.append(output_row)

#print("-----INPUTS 1------")
#print(inputs)
#print("-----OUTPUTS 1------")
#print(outputs)

inputs = np.array(inputs, dtype=np.float32)
outputs = np.array(outputs, dtype=np.float32) 

#print("-----INPUTS 2------")
#print(inputs)
#print("-----OUTPUTS 2------")
#print(outputs)

if inputs.size == 0 or outputs.size == 0:
    raise ValueError("Inputs or Outputs array is empty. Check your data source.")

if len(inputs.shape) == 1:
    inputs = inputs.reshape(-1, len(input_columns))

print(f"Shape of inputs: {inputs.shape}")
print(f"Shape of outputs: {outputs.shape}")

input_1 = Input(shape=(inputs.shape[1],))
x = Dense(64, activation='relu')(input_1)
x = Dense(32, activation='relu')(x)
x = Dense(16, activation='relu')(x)
x = Dense(8, activation='relu')(x)

output = Dense(outputs.shape[1], activation='softmax')(x)

model = Model(inputs=input_1, outputs=output)

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

history= model.fit(inputs, outputs, epochs=150, batch_size=32, validation_split=0.2)

#new_data = np.array([[2, 2, 2, 4],
 #                    [3, 2, 0, 5],
  #                   [7, 8, 4, 0],
   #                  [1, 3, 4, 7]])

#predictions = model.predict(new_data)

#print(f"Predicted Output: {predictions}")

timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
model_save_path = f"W:\\GitHub\\Ai Health and Fitness\\AI-Health-and-Fitness\\Backend\\AI\\fitness_model_{timestamp}"
print(model_save_path)

model.export(str(model_save_path))

#loaded_model = tf.keras.models.load_model(f"{model_save_path}//saved_model.pb")
predictions = model.predict(inputs)
print(f"Predicted Output: {predictions}")