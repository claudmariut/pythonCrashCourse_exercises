alien_0 = {'color': 'green', 'speed': 'slow'}
# print(alien_0['points'])

# To avoid this error above we can use the .get() method to assign a default
# value to a key, if this does not exist.

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)

alien_0['points'] = 5
print(alien_0['points'])
