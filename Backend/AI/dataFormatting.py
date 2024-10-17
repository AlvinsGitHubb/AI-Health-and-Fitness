import json
import pandas as pd

#Step 1: Open the file and load the JSON data
with open('gymrecommendations.json', 'r') as file:
    data = json.load(file)

#for item in data:  # Assuming 'data' is a list of dictionaries
    

#Step 3: Save the modified data back to the file
#with open('gymrecommendations.json', 'w') as file:
#    json.dump(data, file, indent=4)
valuesToOneHotEncode = ['Sex', 'Fitness Goal', 'Fitness Type', 'Exercises', 'Equipment', 'Diet']

final_result = []
j = 0

for json_data in data:

    # Load the JSON into a DataFrame
    df = pd.DataFrame([json_data])

    for value in valuesToOneHotEncode:
        one_hot_encoded = pd.get_dummies(df[value], prefix=value)

        col_index = df.columns.get_loc(value)

        df = df.drop(columns=[value])

        for i, col in enumerate(one_hot_encoded.columns):
            df.insert(col_index + i, col, one_hot_encoded[col])

    #json_result = df.to_json(orient='records', indent=4)
    #final_result += json_result
    final_result.append(df.to_dict(orient='records')[0])  # Convert to dictionary and take the first entry
    j += 1
    print(j)

# Check it out
#print(one_hot_encoded)

with open('oneHotEncodedGymRecommendations.json', 'w') as file:
    json.dump(final_result, file, indent=4)