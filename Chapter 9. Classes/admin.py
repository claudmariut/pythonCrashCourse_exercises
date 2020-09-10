from user import User
"""A child classes that represent the admin of the database."""


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



