names = ['tiberiu', 'sorina', 'blanca', 'claudiu']
print(names[0].title())
print(names[1].title())
print(names[2].title())
print(names[3].title())

print(f'Our family are: {names[0].title()}, {names[1].title()}, {names[2].title()}, {names[3].title()}.')

print(f'I love you {names[0].title()}')
print(f'I love you {names[1].title()}')
print(f'I love you {names[2].title()}')
print(f'I love you {names[3].title()}')

cars = ['Honda', 'Hyundai', 'Tesla']
print(f'My first car was a {cars[0].title()}.')
print(f'The las summer I bought a {cars[1].title()}, it was my own first car.')
print(f'In the future, I would like to buy a {cars[2].title()}.')

# We can add values to the list with the .append() method. The added value is inside the parentheses.
names.append(input('Introduce el nombre del nuevo miembro familiar: '))
print(names)

