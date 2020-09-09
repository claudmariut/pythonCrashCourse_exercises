# We can create a list inside a dictionary. For example:
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }

# Summarize the order
print(f"You ordered a {pizza['crust']}-crust pizza with the following "
      f"toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")

