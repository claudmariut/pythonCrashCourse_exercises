first_name = 'claudiu'
last_name = 'mariutanu'
full_name = '{0} {1}'.format(first_name, last_name)  # Format Method
print(full_name)

full_name = f'{first_name} {last_name}'  # f-string
print(full_name)

print(f'Hello, {full_name.title()}!')  # f-string combined with title method.

message = f'Hello, {full_name.title()}!'
print(message)
