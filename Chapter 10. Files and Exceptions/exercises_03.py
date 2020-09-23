# 1, 2
"""
print("Enter two numbers and I will give you the sum.")
a = input("Enter the first number: ")
b = input("Enter the second number: ")

while True:
    try:
        sum = int(a) + int(b)
    except ValueError:
        print("\nThe values were not correct, try again.")
        a = input("Enter the first number: ")
        b = input("Enter the second number: ")
    else:
        print(sum)
        break
"""
# 3
filename = "text_files/marktwain.txt"

try:
    with open(filename) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    print("Sorry, the file was not found.")
else:
    print(contents.lower().count("the "))

