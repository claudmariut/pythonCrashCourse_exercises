# Nesting means to store multiple dictionaries in a list, or a list of items
# as a value in a dictionary.

# A list of dictionaries.
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# To create a list full of aliens of the same characteristics(same
# dictionaries):
aliens = []
for x in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print('...')

# Show how many aliens we have been created.
print(f'\nTotal number of aliens: {len(aliens)}')  # Each alien has the same
# characteristics but python considers each one a different object.

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

for alien in (aliens[:5]):
    print(alien)




