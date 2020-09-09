prompt = '\nTell me something, and I will repeat it back to you:'
prompt += '\nEnter "quit", to end the program. '

# We need this empty string in the variable so python has something to check
# at first.
message = ''
list = []
while message != 'quit':
    message = input(prompt)
    # We introduce this if statement so the program does not display the 'quit'
    if message != 'quit':
        print(message)

