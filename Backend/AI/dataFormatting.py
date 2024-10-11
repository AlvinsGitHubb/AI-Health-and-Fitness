import json

#Step 1: Open the file and load the JSON data
with open('gymrecommendations.json', 'r') as file:
    data = json.load(file)

#types_ = []
itemName = "Exercises"
for item in data:  # Assuming 'data' is a list of dictionaries
    #if item[itemName] not in types_:
        #types_.append(item[itemName])
        #print(item[itemName])
    if item[itemName] == 'Squats, deadlifts, bench presses, and overhead presses':
        item[itemName] = 0
    else:
        item[itemName] = 1

#Step 3: Save the modified data back to the file
with open('gymrecommendations.json', 'w') as file:
    json.dump(data, file, indent=4)