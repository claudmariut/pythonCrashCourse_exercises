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


class Admin(User):
    """Administrator profile from users."""
    def __init__(self, first_name, last_name, age, occupation):
        """Initialize attributes from parent class"""
        super().__init__(first_name, last_name, age, occupation)
        self.privilegesClass = Privileges()


class Privileges:
    """Privileges specific class"""
    def __init__(self):
        self.privileges = ["can delete post", "can ban user",
                           "can add post"]

    def show_privileges(self):
        """Display a list with the privileges of the admin."""
        print("\nHere is a list with the admin privileges:")
        for privilege in self.privileges:
            print(f"\t-{privilege}")


# Create instances
user_1 = User("Iemina", 'Grecea', 20, 'student')

user_1.describe_user()
user_1.greet_user()

user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()  # The account blocks on the third attempt.
user_1.reset_login_attempts()  # The account resets.
user_1.increment_login_attempts()  # First Attempt.
print(user_1.login_attempts)

# Create instance in the child class.
admin_user = Admin("claudiu", "mariutanu", 24, "student")
admin_user.describe_user()
# Instance as an attribute. We access the methods of the privileges Class
# through the attribute.
admin_user.privilegesClass.show_privileges()


