import json


def get_stored_username():
    """Get stored username if available"""
    filename = "text_files/username.json"
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_user():
    """Prompt for a new username"""
    username = input("\nWhat is your name? ")
    filename = "text_files/username.json"
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username


def get_new_password():
    """Prompt new user for a password"""
    while True:
        password = input("Enter a new password: ")
        password_ver = input("Enter the password again: ")
        if password == password_ver:
            print("Your password was set.")
            break
        else:
            print("The password does not match!\n")

    filename = "text_files/password.json"
    with open(filename, 'w') as f:
        json.dump(password, f)
    return password


def get_stored_password():
    """Get password from the user to verify"""
    filename = "text_files/password.json"
    try:
        with open(filename) as f:
            password = json.load(f)
    except FileNotFoundError:
        get_new_password()
    else:
        return password


def verifying_user(username):
    """Verifies if the correct user"""
    while True:
        verify = input(f"Verifying user: Are you {username}? (y/n) ")
        if verify == "y":
            return True
        elif verify == "n":
            return False
        else:
            print("Invalid Option.\n")


def verifying_password(password):
    """Verifies password"""
    while True:
        password_ver = input("Enter your password press 'q' to quit: ")
        if password_ver == password:
            return True
        if password_ver == 'q':
            break
        else:
            print("Incorrect password!\n")


def greet_user():
    """Greet the user by name"""
    username = get_stored_username()
    password = get_stored_password()
    if username:
        if verifying_user(username):
            if verifying_password(password):
                print(f"\nWelcome back, {username}!\n")
        else:
            username = get_new_user()
            password = get_new_password()
            print(f"\nWe'll remember you when you come back, {username}!\n")
    else:
        username = get_new_user()
        password = get_new_password()
        print(f"\nWe'll remember you when you come back, {username}!\n")


greet_user()
