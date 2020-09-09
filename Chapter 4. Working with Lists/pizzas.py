pizzas = ['cheese', 'margherita', 'vegetarian']

for pizza in pizzas:
    print(f'I like {pizza} pizza.')

print('\nI really love pizza!')

friend_pizzas = pizzas[:]
pizzas.append('hawaian')
friend_pizzas.append('chicken')
print('My favorite pizzas are:')
for pizza in pizzas:
    print(pizza)
print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)


