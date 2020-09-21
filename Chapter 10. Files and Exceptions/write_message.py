filename = "text_files/programming.txt"

with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("Hello World!\n")

with open(filename, 'a') as file_object:
    file_object.write("I am appending new values.\n")
    file_object.write("I love finding meaning in large datasets.\n")

