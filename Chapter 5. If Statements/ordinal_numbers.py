numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numbers:
    if number == 1:
        print(f'{number}st', end=',')
    elif number == 2:
        print(f'{number}nd', end=',')
    elif number == 3:
        print(f'{number}rd', end=',')
    elif number != numbers[-1]:
        print(f'{number}th', end=',')
    else:
        print(f'and {number}th.')