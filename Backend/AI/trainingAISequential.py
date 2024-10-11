#imports
import tensorflow as tf
from tensorflow.keras import layers, models, saving
import numpy as np

inputs = np.array([...])  # Shape: (num_samples, num_features). This is a 2-d array with rows people and columns information about them (weight, activity level, target weight, etc)
outputs = np.array([...]) # Shape: (num_samples, ). The current code only outputs one number per person so there is not second part, but I'm pretty sure this can be easily changed to be a 2-d array

#Building the Neural Network Model. Layers should be edited to be better probably because they suck right now.
model = models.Sequential([
    layers.Dense(64, activation='relu', input_shape=(inputs.shape[1],)),  # Input layer + first hidden layer
    layers.Dense(32, activation='relu'),  # Second hidden layer
    layers.Dense(16, activation='relu'),  # Third hidden layer
    layers.Dense(8, activation='relu'),  # Fourth hidden layer
    layers.Dense(outputs.shape[1], activation='softmax')  # Output layer
])


#Compiling the Model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])#idk if the metrics thing will work its not in the documentation but neither is the compile method (even thoughj it shows up in the examples in the documentation). Nevermid I found it.

#Training The Model
history = model.fit(inputs, outputs, epochs=100, batch_size=32, validation_split=0.2) #validation_data=(X_test, y_test))

#Using the Model
new_data = np.array([[2, 2, 2, 4],
                     [3, 2, 0, 5],
                     [7, 8, 4, 0],
                     [1, 3, 4, 7]])  # Replace with new user data
predictions = model.predict(new_data)
print(f"Predicted Output: {predictions}")

#Saving and Loading
model.save("file/path")

loaded_model = saving.load_model("file/path")

predictions = loaded_model.predict(new_data)
print(f"Predicted Output: {predictions}")
