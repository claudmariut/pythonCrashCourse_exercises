# A tuple is similar to a list but its values are immutables. It is expressed using parentheses.
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

my_t = (3,)  # We can also define tuples with one element, although it does not make sense to do it often.
print(my_t[0])

# We can loop over all the values in a tuple.
for dimension in dimensions:
    print(dimension)

# We can reassign values to a variable to change the values of a tuple.
dimensions = (200, 50)
print('Original dimensions:')
for dimension in dimensions:
    print(dimension)
dimensions = (400, 100)
print('\nModified dimensions')
for dimension in dimensions:
    print(dimension)
    





