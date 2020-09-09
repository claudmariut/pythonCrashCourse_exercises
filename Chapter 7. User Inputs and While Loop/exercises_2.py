# 1
pizza_toppings = input('Enter a series of pizza toppings you would like:\n')
topping = pizza_toppings
while topping != 'quit':
    if topping != 'quit':
        print(f'{topping.title()} added.')
        topping = input('\nEnter "quit" when you are done: ')

# 2
age = int(input('Enter your age: \n'))
if age < 3:
    print('The ticket is free.')
elif age < 12:
    print('The ticket is $10.')
else:
    print('The ticket is $15.')

# 3
# 1
pizza_toppings = input('Enter a series of pizza toppings you would like:\n')
topping = pizza_toppings
active = True
while active:
    if topping != 'quit':
        print(f'{topping.title()} added.')
        topping = input('\nEnter "quit" when you are done: ')
    else:
        # We can use either break or "active = False"
        break
