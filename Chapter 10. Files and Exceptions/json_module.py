import json

numbers = [1, 2, 3, 4, 5]

filename = "text_files/numbers.json"
with open(filename, 'w') as f:
    json.dump(numbers, f)  # Store numbers data structure into the file object.

filename = "text_files/numbers.json"
with open(filename) as f:
    numbers = json.load(f)  # Load the data structure into the variable.

print(numbers)
