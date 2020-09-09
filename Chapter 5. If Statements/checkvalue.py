# The key-word "in" is used to check if a value is in a list.
requested_toppings = ['mushrooms', 'onions', 'pineapple']
if 'mushrooms' in requested_toppings:
    print(True)
else:
    print(False)

if 'pepperoni' in requested_toppings:
    print(True)
else:
    print(False)

# The key-wod "not in" is used to check if  value is not in a list.
banned_users = ['andrew', 'carolina', 'david']
if 'marie' not in banned_users:
    print('You can comment in the page')
else:
    print('You are banned')

# Sometimes is important to use multiple if statements only when more
# conditions could be true. Test keeps going regardless it passes each time.
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print('Adding mushrooms.')
if 'pepperoni' in requested_toppings:
    print('Adding pepperoni.')
if 'extra cheese' in requested_toppings:
    print('Adding extra cheese.')

print('\nFinished making your pizza!')

requested_toppings = []
if requested_toppings:  # This if statement passes True if there is at least
    # one item in the list.
    for requested_topping in requested_toppings:
        print(f'Adding {requested_topping}.')
    print('\nFinished making your pizza!')
else:
    print('Are you sure you want a plain pizza?')

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni',
                      'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f'Adiing {requested_topping}.')
    else:
        print(f'Sorry, we do not have {requested_topping}.')

print('\nFinished making your pizza!')







