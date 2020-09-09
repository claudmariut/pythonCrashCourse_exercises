bicycles = ['trek', 'cannondale', 'redline', 'specializad']  # Square brackets [] indicate a list.
print(bicycles)

print(bicycles[0])  # To access an element from a list we use square brackets as an index pf the list starting form 0.
print(bicycles[0].title())  # First item is in position 0 for Python.
print(bicycles[1])
print(bicycles[3])
print(bicycles[-1])  # Returns last item on a list.
print(bicycles[-3])  # Returns third item form the end of the list.

# We can use individual values from a list and include them in other variables or messages.
message = f'My first bicycle was a {bicycles[0].title()}.'  # f-sting method using a list.
print(message)




