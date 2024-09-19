#imports
import tensorflow as tf
from tensorflow.keras import layers, models
from sklearn.model_selection import train_test_split
import numpy as np

#Preparing the data
# Replace these with your actual data
inputs = np.array([...])  # Shape: (num_samples, num_features). This is a 2-d array with rows people and columns information about them (weight, activity level, target weight, etc)
outputs = np.array([...]) # Shape: (num_samples, ). The current code only outputs one number per person so there is not second part, but I'm pretty sure this can be easily changed to be a 2-d array

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(inputs, outputs, test_size=0.2, random_state=42)

#Building the Neural Network Model
model = keras.Sequential([
    keras.layers.Dense(64, activation='relu', input_shape=(inputs,shape[1],)),  # Input layer + first hidden layer
    keras.layers.Dense(32, activation='relu'),  # Second hidden layer
    keras.layers.Dense(outputs,shape[1], activation='softmax')  # Output layer
])


#Compiling the Model
model.compile(optimizer='adam', loss='mse', metrics=['mae'])#idk if the metrics thing will work its not in the documentation but neither is the compile method (even thoughj it shows up in the examples in the documentation). Nevermid I found it.

#Training The Model
history = model.fit(X_train, y_train, epochs=100, batch_size=32, validation_data=(X_test, y_test))

#Evaluating the Model
loss, mae = model.evaluate(X_test, y_test)
print(f"Test Loss: {loss}")
print(f"Test MAE: {mae}")

#Using the Model
new_data = np.array([[...]])  # Replace with new user data
predictions = model.predict(new_data)
print(f"Predicted Output: {predictions}")

#Saving and Loading
# Create the artifact
model.export("path/to/location")

# Later, in a different process/environment...
reloaded_artifact = tf.saved_model.load("path/to/location")
predictions = reloaded_artifact.serve(input_data)
