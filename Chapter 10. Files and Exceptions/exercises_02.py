# 1 It creates a txt with the user input name.
"""
name = input("Enter your name: ")
filename = "text_files/guest.txt"

with open(filename, 'w') as file_object:
    file_object.write(f"{name.title()}\n")
"""

# 2
filename = "text_files/guest_book.txt"

while True:
    name = input("Enter your name: ")
    print(f"{name.title()}, thank you for your visit!")
    with open(filename, 'a') as file_object:
        file_object.write(f"{name.title()}\n")
    decision = input("\nDo you want to continue? y/n: ")
    if decision == 'n':
        break


