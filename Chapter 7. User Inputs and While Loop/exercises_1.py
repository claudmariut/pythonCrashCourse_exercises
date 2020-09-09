# 1
rental_car = input('What kind of rental cat would you like? ')

print(f'Let me see if I can find you a {rental_car.title()}.')

# 2
seating = int(input('How many people are in your dinner group? '))

if seating > 8:
    print('You will have to wait for a table.')
else:
    print('Your table is ready.')

# 3
multiples = int(input('Enter a number and I will tell you whether is'
                      ' multiple of 10 or not: '))

if multiples % 10 == 0:
    print(f'The number {multiples} is a multiple of 10.')
else:
    print(f'The number {multiples} is not a multiple of 10.')