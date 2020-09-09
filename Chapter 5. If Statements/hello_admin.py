# 1
usernames = []

if usernames:
    for user in usernames:
        if user == 'admin':
            print(f'Hello {user}, would you like to see a status report?')
        else:
            print(f'Hello {user.title()}, thank you for logging in again.')
else:
    print('We need to find some users!')

# 2
current_users = ['luke', 'john', 'sabina', 'mary', 'spencer']
new_users = ['josh', 'elena', 'mary', 'james', 'john']

for new_user in new_users:
    if new_user in current_users or new_user.lower() in current_users\
            or new_user.upper() in current_users or new_user.title() in current_users:
        print(f'The username {new_user} is not available. '
              f'You will have to enter a new username')
    else:
        print(f'The username {new_user} is available.')




