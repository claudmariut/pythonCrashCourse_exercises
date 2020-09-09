print('Python')  # Whitespace refers to any nonprinting character, such as spaces, tabs, and end-o-line symbols.
print('\tPython')  # \t is used to add a tab.

print('Languages:\nPython\nC\nJavaScript')  # \n is used to add a newline.

print('Languages:\n\tPython\n\tC\n\tJavaScript')  # \n\t to combine them.

favorite_language = 'python '
favorite_language = favorite_language.rstrip()  # .rstrip() method eliminates right whitespace.
print(favorite_language)

favorite_language = ' python'
favorite_language = favorite_language.lstrip()  # .lstrip() method eliminates left whitespace.
print(favorite_language)

favorite_language = ' python '
favorite_language = favorite_language.strip()  # .strip() method eliminates both sides whitespace.
print(favorite_language)

full_name = input('What is your full name?: ')
full_name = full_name.strip()
print(f'Your full name is {full_name.title()}')
# The user input value string is changed with the .strip() method. Then, the .title() method is applied to the final
# value for print.

