# We use int() function to treat an input as an integer.
height = input('How tall are you, in inches? ')
height = int(height)

if height >= 48:
    print('\nYou are tall enough to ride!')
else:
    print('\nYou will be able to ride when you are a little older.')

# The modulo operator '%', divides one number by another and returns the
# remainder.
# We can conver the input directly from the input.
number = int(input('Enter a number, and I will tell you if it is even'
                   ' or odd: '))

if number % 2 == 0:
    print(f'The number {number} is even.')
else:
    print(f'The number {number} is odd.')