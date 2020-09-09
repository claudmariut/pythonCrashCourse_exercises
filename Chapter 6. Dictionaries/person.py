# 1
person = {'first_name': 'Iemina', 'last_name': 'Grecea', 'age': 20, 'city':
          'Hot Springs'}
print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])

# 2
favorite_numbers = {
    'Iemina': 3,
    'Nicoleta': 7,
    'Vio': 8,
    'Andres': 1,
    'Claudio': 0
    }

print(f"\nIemina favorite number is {favorite_numbers['Iemina']}")
print(f"Nicoleta favorite number is {favorite_numbers['Nicoleta']}")
print(f"Vio favorite number is {favorite_numbers['Vio']}")
print(f"Andres favorite number is {favorite_numbers['Andres']}")
print(f"Claudio favorite number is {favorite_numbers['Claudio']}")

# 3
meaning = {
    'list': 'A list is used to store either integers, string, or both values',
    'tuple': 'A tuple is similar to a list , but its values are immutable',
    'array': 'An array is a list with only a tipe of data',
    'set': 'A set only contains unique items without repetition'
    }

for word, definition in meaning.items():
    print(f'\n{word.title()}:')
    print(definition)

