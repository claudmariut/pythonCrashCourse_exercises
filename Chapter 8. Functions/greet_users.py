import numpy as np


# Passing a list to a function. The parameter refers to a list.
def greet_users(names):
    """Print a simple greeting to each user in the list"""
    for name in names:
        print(f"Hello, {name}!")


# We can use as well set, tuples and arrays.
usernames = ['claudiu', 'iemina', 'blanca']
greet_users(usernames)


