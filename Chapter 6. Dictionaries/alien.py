# Dictionaries are unordered sets of data. The items in a dictionary are
# accessed by keys, not via their position.
from turtle import color

alien_0 = {'color': 'green'}  # We use {} braces and key-value pairs.
print(alien_0['color'])  # The key color stores the value 'green'.

# We can have unlimited number of key-value pairs. Separated by commas.
alien_0 = {'color': 'green', 'points': 5}
new_points = alien_0['points']
print(f'\nYou just earned {new_points} points!')

# To add new items. In the order they were created.
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print('\n', alien_0)

# To change the value of a key item. When accesing to values in a dictionary
# we have to use double quotations marks!!
alien_0 = {'color': 'green'}
print(f"\nThe alien is {alien_0['color']}.")
alien_0 = {'color': 'yellow'}
print(f"The alien is now {alien_0['color']}.")

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'fast'}
print(f"\nOriginal position: {alien_0['x_position']}")

# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3

# The new position is the old position plus the increment.
alien_0['x_position'] += x_increment
print(f"New position: {alien_0['x_position']}")

# We can remove an item from a dictionary using the del statement with the key.
# del and pop only work with index position or key. remove works with value.
del alien_0['x_position']
print(alien_0)
