"""Return values are very useful to work with a value after passing the
function. We need to assign the return value to a variable, and then we have
freedom to work with it."""
users = []  # List in which we append every return value from the call function


def formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return users.append(full_name.title())


formatted_name("claudiu", "mariutanu")  # This appends the formatted name
formatted_name("iemina", "grecea")
formatted_name("nicoleta", "grecea")
formatted_name("viorel", "grecea")

print(users)  # Print the list with all the names.


# We can make an argument optional. We set an empty string as default value.
def formatted_name(first_name, last_name, middle_name=""):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return users.append(full_name.title())


formatted_name("emina", "mariutanu")
formatted_name("blanca", "mariutanu", "maria")

print(users)


