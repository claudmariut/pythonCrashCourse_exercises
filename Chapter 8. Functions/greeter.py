# Functions are helpful to perform different tasks.
def greet():
    # Triple quotes indicates a docstring. (What the function task is)
    """Display a simple greeting"""
    print('Hello!')


greet()


# We can pass information to a Function. The information to calle a function
#  are called arguments. The variables are called parameters.
def greet_user(username):
    """Display a simple greeting"""
    print(f'Hello, {username.title()}!')

# We introduce the argument. The argument is assigned to the parameter.
greet_user('clau')
