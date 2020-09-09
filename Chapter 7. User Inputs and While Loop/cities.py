prompt = '\nPlease enter the name of a city you have visite:'
prompt += '\n(Enter "quit" when you are finished.) '

while True:
    city = input(prompt)
    # Break is used to exit a loop, so the code afterward is omitted.
    if city == 'quit':
        break
    else:
        print(f'I would love to go to {city.title()}!')

