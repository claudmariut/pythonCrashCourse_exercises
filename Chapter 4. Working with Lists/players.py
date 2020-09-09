players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])  # This allow us to slice. From first argument to one position before last argument. 0 to 2nd index.
print(players[1:4])  # This would show us the second, third, and fourth element. 1 to 3rd index
print(players)  # Slicing this way does not affect the original list.

print(players[:4])  # Omitting the first argument, it start from the beginning. 0 to 3 index. 1 to 4th position.
print(players[2:])  # Index 2 to the end. From third element to the end.
print(players[-2:])  # To display the last two indexes.

print('Here are the first three players on my team:')
for player in players[:3]:
    print(player.title())







