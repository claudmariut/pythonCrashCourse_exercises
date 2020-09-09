# The input function allow us to insert user input from a prompt. We can assign
# the user's input ot a variable to work with it later.
# Everything is considered a string using just the input() function.
message = input('Tell me something, and I will repeat it back to you: ')
print(message)

name = input('Please enter your name: ')
print(f'Hello {name.title()}!')

# We can write prompts that are longer than one line. We can assign the prompt
# to a variable:
prompt = 'If you tell us who you are, we can personalize the messages you see.'
prompt += '\nWhat is your name? '

name = input(prompt)
print(f'\nHello, {name.title()}!')
