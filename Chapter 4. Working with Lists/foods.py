my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]  # To copy an entire list. We have to use slicing
# always. If not, the list is applied to
# both variables.
print('My favorite foods are:')
for food in my_foods:
    print(food)
print("\n My friend's favorite foods are:")
for food in friend_foods:
    print(food)

my_foods.append('cannoli')
friend_foods.append('ice cream')
print('My favorite foods are:')
print(my_foods)
print("\n My friend's favorite foods are:")
print(friend_foods)

