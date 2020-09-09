# Passing an arbitrary number of arguments.
"""The "*" before the parameter, tells python to store all the values in the
argument as tuple named as the parameter."""


# Positional argument first and arg* last, if not, we use keywords in the call.
def make_pizza(size, *toppings):  # *args
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

# We can add more arguments to an arbitrary number but we have to use a key.



