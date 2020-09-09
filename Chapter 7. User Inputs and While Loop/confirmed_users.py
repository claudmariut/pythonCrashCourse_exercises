# Is best to use a while loop to modify a list or a dictionary than a for.
unconfirmed_users = ['alice', 'brian', 'candance']
confirmed_users = []
# We move items from a list to another using a while loop.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f'Verifying user: {current_user.title()}')
    confirmed_users.append(current_user)

print('\nThe following users have been confirmed:')
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# We can use a while loop and the remove method to remove all instances of a
# specific value from a list. The method alone only removes the first instance.
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)
