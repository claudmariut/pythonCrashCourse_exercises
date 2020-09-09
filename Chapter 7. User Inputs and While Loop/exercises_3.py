# 1, 2
sandwich_orders = ['tuna', 'pastrami', 'veggie', 'pastrami', 'chicken', 'beef',
                   'pastrami', 'turkey']
finished_sandwiches = []

print('The deli has run out of pastrami.\n')

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich_order = sandwich_orders.pop()
    print(f'I made your {sandwich_order} sandwich.')
    finished_sandwiches.append(sandwich_order)

print('\nAll these sandwiches have been made:')
for finished in finished_sandwiches:
    print(f'{finished.title()} sandwich.')

# 3
vacations = {}
poll_active = True

while poll_active:
    name = input('\nWhat is your name? ')
    place = input('Which place would you like to go on vacation? ').split()

    vacations[name] = place

    repeat = input('Would you like to let another person to take the poll? '
                   '(yes/no) ')

    if repeat == 'no':
        poll_active = False

print(vacations)

print('\nHere are the poll results:')
for name, place in vacations.items():
    if len(place) > 1:
        print(f'{name.title()} would like to go to ', end='')
        for single_place in place:
            if single_place != place[-1]:
                print(f'{single_place.title()}, ', end='')
            else:
                print(f'and {single_place.title()}.')
    else:
        print(f'{name.title()} would like to go to {place} in '
              f'vacation.')


