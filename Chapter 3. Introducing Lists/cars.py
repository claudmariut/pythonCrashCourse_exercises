cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()  # .sort() method changes the order of the list in alphabetical order. It is irreversible.
print(cars)

# We can change sort the list in reverse alphabetical by using the argument reverse=True in the .sort() method.
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

# The sorted() function is used only to display the list in alphabetical order but the original list is not affected.
cars = ['bmw', 'audi', 'toyota', 'subaru']
print('\nHere is the original list:')
print(cars)
print('\nHere is the sorted list:')
print(sorted(cars))
print('\nHere is the original list again:')
print(cars)

# We can also display the list in reverse alphabetical order using the argument reverse=True in the sorted() function.
print('\nHere is the reverse sorted list:')
print(sorted(cars, reverse=True))

# Besides the sort() method and sorted() function, we can display the list reversed, not in alphabetical order by using
# the method reverse().
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()
print(cars)  # We can reverse the function again to get the same original list.

# To find the length of a list we use the len() function.
print(len(cars))

