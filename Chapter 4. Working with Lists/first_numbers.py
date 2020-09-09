# range() function is useful to generate a series of numbers.
for value in range(1, 5):  # The value starts at 1 and stops at the second value in range (5). It stops there.
    print(value)

for value in range(5):  # When there is only one argument, it starts with 0 until the argument value and stops.
    print(value)

numbers = list(range(1, 5))
print(numbers)

even = list(range(2, 11, 2))  # We can a third argument in a range() function as a step value that skips.
print(f'\n{even}')

odd = list(range(1, 12, 2))
print(f'\n{odd}')






