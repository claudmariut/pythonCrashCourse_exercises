with open("text_files/pi_digits.txt") as file_object:
    contents = file_object.read()  # Save a ling string.

print(contents.rstrip())

# Open a file from another directory.
path = "/home/claumariut/Documents/documentation/git commands.txt"
with open(path) as file_object:
    for line in file_object:
        print(line.rstrip())  # Because python reads a newline at the end.

# Stored the content of a file in a list.
with open(path) as file_object:
    lines = file_object.readlines()  # Save a list with string/line

# lines is a list containing each line of the file.
print(type(lines))
for line in lines:
    print(line.rstrip())

# Working with file content.
with open("text_files/pi_digits.txt") as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()  # We use .strip() method to remove \n, and \t.

print(pi_string)
print(len(pi_string))








