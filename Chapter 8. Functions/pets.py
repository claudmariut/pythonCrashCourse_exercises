"""Positional arguments. Each argument in the function call, must match, in
the same order, the parameters of the function definition."""


def describe_pet(animal_type, pet_name):
    """Describe information about a pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}")


describe_pet("hamster", "harry")

"""Multiple function Calls. This is an efficient way to do a task in a single
line. The order of the arguments matters. Be careful with that."""
describe_pet("dog", "spencer")

"""A keyword argument is a name-value pair. This allow us to avoid that an
argument is wrongly paired with a parameter. This is useful if we use
a lot of arguments."""
describe_pet(pet_name="tommy", animal_type="dog")

"""We can define a default value for any parameter in a function. If the
argument is omitted in the function call, then python sets that value to 
the default parameter value. Default values have to go at the end."""


def person(name, gender="male"):
    print(f"\nMy name is {name.title()}.")
    print(f"I am a {gender}.")


person("claudiu")






