# List with people invited to the dinner.
guest_list = ['iemina', 'andres', 'viorel', 'nicoleta']

# Print a message to each person. Longest way.
print(
    f'\tDear {guest_list[0].title()},\nI am happy to invite you to a dinner at my place this Saturday evening at 7pm.')
print(
    f'\tDear {guest_list[1].title()},\nI am happy to invite you to a dinner at my place this Saturday evening at 7pm.')
print(
    f'\tDear {guest_list[2].title()},\nI am happy to invite you to a dinner at my place this Saturday evening at 7pm.')
print(
    f'\tDear {guest_list[3].title()},\nI am happy to invite you to a dinner at my place this Saturday evening at 7pm.')

# Shorter but more complex way.
for each in guest_list:
    print(f'\tDear {each.title()},\nI am happy to invite you to a dinner at my place this Saturday evening at 7pm.')

# Changing guest list.
guest_list[2] = 'claudiu'
print(guest_list)
for each in guest_list:
    print(f'\tDear {each.title()},\nI am happy to invite you to a dinner at my place this Saturday evening at 7pm.')

# More guests.
print('A bigger table has been found')
guest_list.insert(0, 'viorel')
guest_list.insert(2, 'blanca')
guest_list.append('sorina')
guest_list.append('tiberiu')
print(guest_list)
for each in guest_list:
    print(f'\tDear {each.title()},\nI am happy to invite you to a dinner at my place this Saturday evening at 7pm.')

# Shrinking guest list.
print('I am sorry to inform you that I can only invite two guests')
print(len(guest_list))
# Longer way.
guest_1 = guest_list.pop()
guest_2 = guest_list.pop()
guest_3 = guest_list.pop()
guest_4 = guest_list.pop()
guest_5 = guest_list.pop()
guest_6 = guest_list.pop()
print(f'\tDear {guest_1.title()},\nI am sorry I can not invite you to dinner.')
print(f'\tDear {guest_2.title()},\nI am sorry I can not invite you to dinner.')
print(f'\tDear {guest_3.title()},\nI am sorry I can not invite you to dinner.')
print(f'\tDear {guest_4.title()},\nI am sorry I can not invite you to dinner.')
print(f'\tDear {guest_5.title()},\nI am sorry I can not invite you to dinner.')
print(f'\tDear {guest_6.title()},\nI am sorry I can not invite you to dinner.')
print(guest_list)

# Shorter way.
guest_list = ['viorel', 'iemina', 'blanca', 'andres', 'claudiu', 'nicoleta', 'sorina', 'tiberiu']
while len(guest_list)>2:
    guest_removed = guest_list.pop()
    print(f'\tDear {guest_removed.title()},\nI am sorry I can not invite you to dinner.')
print(guest_list)

for x in range(len(guest_list)):
    del guest_list[0]
    print(guest_list)

print(len(guest_list))




