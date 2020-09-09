"""We can create a dictionary and add as many arguments we want, we use =None
parameter, which does not have a default value, so it is set to False as
default."""


def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {"first": first_name, "last": last_name}
    if age:
        person["age"] = age
    return person


musician = build_person("jimi", "hendrix", age=27)
print(musician)



