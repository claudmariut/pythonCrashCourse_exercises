"""A class to represent a user database."""


class User:
    """Collect data to create a person"""
    def __init__(self, first_name, last_name, age, occupation):
        self.first = first_name
        self.last = last_name
        self.age = age
        self.occupation = occupation
        self.login_attempts = 0

    def describe_user(self):
        """Displays a description of the user"""
        print(f"\n{(id(self))}'s user full name is {self.first} {self.last}")
        print(f"The user age is {self.age}, and the occupation is"
              f" {self.occupation}")

    def greet_user(self):
        """Welcomes the user"""
        print(f"\nWelcome again {self.first}!")

    def increment_login_attempts(self):
        """Increments the number of login attempts by 1"""
        if self.login_attempts == 2:
            print("\nThe account has been blocked.")
            self.login_attempts += 1

        else:
            self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset counter of login attempts"""
        self.login_attempts = 0
