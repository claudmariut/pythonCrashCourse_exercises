# 1 ,2
def make_shirt(size="l", message="I love Python"):
    print(f"\nThe size of the shirt is: {size.title()}")
    print(f"The message printed is: {message}.")


make_shirt("m", "I am a hacker")
make_shirt(size="s", message="I am in love with you")
make_shirt()
make_shirt("xl")
make_shirt(message="Hello world!")


# 3
def describe_city(name_city, country_city="spain"):
    print(f"\n{name_city.title()} is in {country_city.title()}.")


describe_city("zaragoza")
describe_city("paris", "france")
describe_city(name_city="barcelona")