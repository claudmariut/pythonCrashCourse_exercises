motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# To change the value of an element from the list.
motorcycles[0] = 'ducati'
print(motorcycles)

# To add a new element to the end of the list we use the method .append(new element).
motorcycles.append('honda')
print(motorcycles)

# We can add all the elements in a list form the beginning.
motorcycles = []
print(motorcycles)
motorcycles.append('ducati')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
motorcycles.append('honda')
print(motorcycles)

# To insert a new element to the list we use the method .insert(place, new element)
motorcycles = ['yamaha', 'suzuki', 'honda']
print(motorcycles)
motorcycles.insert(0, 'ducati')
print(motorcycles)

# To remove an item from the list we use the del statement.
del motorcycles[0]  # We need to know the position of the element.
print(motorcycles)

# We can also remove the last item from a list using the .pop() method, and store that value.
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

motorcycles.insert(0, popped_motorcycles)  # Here we use the removed last element and inserted again in other place.
print(motorcycles)

# We can use the .pop(place) method to remove and stored whatever element form a list.
print(f'The first motorcycle that broke was a {motorcycles[1].title()}.')  # Here we print a message with the element in the
# list.
motorcycle_broken = motorcycles.pop(1)
print(motorcycles)
print(f'The first motorcycle that broke was a {motorcycle_broken.title()}.')  # Here we print a message with the popped
# element.

# To remove an element that only we know the value we use the .remove(element) method.
print(motorcycles)
motorcycles.remove('suzuki')
print(motorcycles)

# We can also use .remove() method to remove elements from a list that already had a variable.
too_expensive = 'honda'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f'\nA {too_expensive.title()} is too expensive for me.')

# .remove() method only removes the first occurrence of the element in the list. We need to create a look to make sure
# we remove all the items with that value.


