import tensorflow as tf
from tensorflow.keras import Model, Input
from tensorflow.keras.layers import Dense
import numpy as np
import json

input_columns = ['Sex_Male', 'Sex_Female', 'Age', 'Height', 'Weight', 'Diabetes', 'Fitness Goal_Weight Loss', 'Fitness Goal_Weight Gain']
output_columns = ['Fitness Type_Muscular Fitness', 'Fitness Type_Cardio Fitness']
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
    for col in input_columns:
        try:
            input_row = entry[col]
            inputs.append(input_row)
        except:
            inputs.append(False)
            
    for col in output_columns:
        try:
            output_row = entry[col]
            inputs.append(output_row)
        except:
            inputs.append(False)

if inputs.size == 0 or outputs.size == 0:
    raise ValueError("Inputs or Outputs array is empty. Check your data source.")

if len(inputs.shape) == 1:
    inputs = inputs.reshape(-1, len(input_columns))

print(f"Shape of inputs: {inputs.shape}")

input_1 = Input(shape=(inputs.shape[1],))
x = Dense(64, activation='rulu')(input_1)
x = Dense(32, activation='rulu')(x)
x = Dense(16, activation='rulu')(x)
x = Dense(8, activation='rulu')(x)

output = Dense(outputs.shape[1], activation='softmax')(x)

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

history= model.fit(inputs, outputs, epochs=100, batch_size=32, validation_split=0.2)

new_data = np.array([[2, 2, 2, 4],
                     [3, 2, 0, 5],
                     [7, 8, 4, 0],
                     [1, 3, 4, 7]])

predictions = model.predict(new_data)
print(f"Predicted Output: {predictions}")

model.save("file/path")

loaded_model = tf.keras.models.load_model("file/path")
predictions = loaded_model.predict(new_data)
print(f"Predicted Output: {predictions}")