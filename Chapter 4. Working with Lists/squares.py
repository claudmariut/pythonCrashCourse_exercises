# In python ** represents exponents.
squares = []
for square in range(1, 11):
    square = square ** 2
    squares.append(square)

print(f'\n {squares}')

# We can append each new value directly to the list.
squares = []
for square in range(1, 11):
    squares.append(square**2)

print(f'\n {squares}')

# List comprehension.
squares = [x**2 for x in range(1, 11)]  # It is like [do this, for each this,
# in this range]
print(f'\n{squares}')

numbers = [x for x in range(1, 101)]
print(numbers)