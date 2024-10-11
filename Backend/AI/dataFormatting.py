import json
import pandas as pd

#Step 1: Open the file and load the JSON data
with open('gymrecommendations.json', 'r') as file:
    data = json.load(file)

#for item in data:  # Assuming 'data' is a list of dictionaries
    

#Step 3: Save the modified data back to the file
#with open('gymrecommendations.json', 'w') as file:
#    json.dump(data, file, indent=4)

json_data = data[0]

# Load the JSON into a DataFrame
df = pd.DataFrame([json_data])

# One-hot encode the 'Sex' column
one_hot_encoded = pd.get_dummies(df['Sex'])

# Add the one-hot encoded columns to your DataFrame
df = pd.concat([df, one_hot_encoded], axis=1)

json_result = df.to_json(orient='records', indent=4)

# Check it out
#print(one_hot_encoded)

with open('oneHotEncodedGymRecommendations.json', 'w') as file:
    json.dump(json_result, file, indent=4)