# 1
# Store all the content in a single string and print it out.
with open("text_files/learning_python.txt") as file_object:
    contents = file_object.read()  # Create string.
    print(contents.strip())  # To remove last \n

# Iterate through the file object.
with open("text_files/learning_python.txt") as file_object:
    for line in file_object:  # Iterate in the object.
        print(line.strip())  # To remove each \n at the end.

# Create a list and then work with it.
with open("text_files/learning_python.txt") as file_object:
    lines = file_object.readlines()

for line in lines:
    line = line.replace("Python", "Java")
    print(line.strip())

# 2
contents = contents.replace("Python", "C++")
print(contents.strip())









