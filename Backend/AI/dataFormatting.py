import json

#Step 1: Open the file and load the JSON data
with open('gymrecommendations.json', 'r') as file:
    data = json.load(file)

for item in data:  # Assuming 'data' is a list of dictionaries
    if item['Diabetes'] == "No":
        item['Diabetes'] = False
    else:
        item['Diabetes'] = True

#Step 3: Save the modified data back to the file
with open('gymrecommendations.json', 'w') as file:
    json.dump(data, file, indent=4)  # Nice formatting with that indent, bro