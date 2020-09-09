# Is is useful to use a dictionary to store one kind of information about many
# objects. We can use a different way of store the key-value pairs.
favorite_lenguages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

lenguage = favorite_lenguages['sarah'].title()
print(f"Sarah's favorite lenguage is {lenguage}.")

# We can loop through all the dictionary to print the results of the poll.
for name, lenguage in favorite_lenguages.items():
    print(f"{name.title()}'s favorite lenguage is {lenguage.title()}")

# To access only the keys in a dictionary we use the .key() method.
# We can loop, use sorted() function and create a list with only the keys.
for name in sorted(favorite_lenguages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

# To access only the values in a dictionary we use the .values() method in the
# same way as we used .keys().
print('\nThe following lenguages have been mentioned:')
for lenguage in favorite_lenguages.values():
    print(lenguage.title())

# The .set() method creates or displays a new list of unique items from another
# list. Without repeating the same items again.
print('\nThe following lenguages have been mentioned:')
for lenguage in set(sorted(favorite_lenguages.values())):
    print(lenguage.title())

poll = ['iemina', 'sarah', 'claudio', 'edward']
for person in poll:
    if person in favorite_lenguages.keys():
        print(f'{person.title()}, thank you for taking the poll')
    else:
        print(f'{person.title()}, you should take the poll')


favorite_lenguages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }
# In order to loop through a value that is a list, all the values have to be
# inside a list.
for name, languages in favorite_lenguages.items():
    if len(languages) > 1:
        print(f"\n{name.title()}'s favorite languages are:")
    else:
        print(f"\n{name.title()}'s favorite languages is:")
    for language in languages:
        print(f'\t{language.title()}')

