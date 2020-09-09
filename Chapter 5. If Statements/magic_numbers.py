answer = 17

if answer != 42:
    print('That is not the correct answer. Please, try again!')
else:
    print('Congratulations, that is the correct answer')

# We can use "and" to check multiple conditions. Both have to pass.
age_0 = 18
age_1 = 21
if age_0 <= 20 and age_1 <= 20:
    print('Both ages are less or equal to 20')
else:
    print('False')  # It will print false because not both conditions passed.

# We can also use "or" for multiple conditions, it will pass while one of the
# conditions passes.
if age_0 <=20 or age_1 <= 20:
    print('True')  # It will print true because one conditions passes.
else:
    print('False')

