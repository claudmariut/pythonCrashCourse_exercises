from admin import User, Admin

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
