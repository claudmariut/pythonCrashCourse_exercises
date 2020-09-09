# Importing a function from a module (.py file). Same directory.
# If we use import, it imports all the functions from the module.
import pizza

pizza.make_pizza(12, "cheese", "pepperoni")  # Declare module module_name.

# We can import the function directly from the module.
from pizza import make_pizza

make_pizza(6, "mozzarela", "eggs")  # Omit the module_name call.

# Using as to give a function an alias.
from pizza import make_pizza as mp

mp(18, "provolone", "lettuce", "pineapple")

"""Syntax is from module_name import function_name as fn"""

# Using as to give a module an alias.

import pizza as p

# We use to call the module, and then the function we want. Similar to Numpy.
# (import numpy as np. It imports the module numpy as np. then we choose the
# function we want to use)
p.make_piza(12, "apple", "raspberry")

# Import all functions in a module.

from pizza import *

make_pizza(7, "hello")




