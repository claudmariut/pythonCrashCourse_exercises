class Restaurant:
    """Building a restaurant."""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Display the name and type of restaurant."""
        vowels = ("A", "E", "I", "O", "U")
        if self.cuisine_type[0] in vowels:
            print(f"\n{self.restaurant_name} is an {self.cuisine_type} "
                  f"restaurant.")

        else:
            print(f"\n{self.restaurant_name} is a {self.cuisine_type} "
                  f"restaurant.")

    def open_restaurant(self):
        """Displays that the restaurant is open."""
        print(f"\nThe restaurant {self.restaurant_name} is open!")

    def set_number_served(self, customers_served):
        """This function allow us to set the number of served customers"""
        self.number_served = customers_served
        print(f"\nThe restaurant has served {self.number_served} customers.")

    def increment_number_served(self, increment_served):
        """Let us increment the number of people being served"""
        if increment_served >= 0:
            self.number_served += increment_served
            print(f"\nThe current total of served people is "
                  f"{self.number_served}")

        else:
            print("\nYou can not introduce negative values")


class IceCreamStand(Restaurant):
    """Representation of a restaurant, specific to an Ice Cream Stand"""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes from the parent class."""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["chocolate", "strawberry", "lemon",
                        "peanut", "vanilla", "mango"]

    def get_flavors(self):
        print("\nHere is a list with all the flavours:")
        for flavor in self.flavors:
            print(f"\t-{flavor.title()}")


restaurant = Restaurant("Seventh Taste", "Veggie")
restaurant.describe_restaurant()
restaurant.set_number_served(345)
restaurant.increment_number_served(15)

# Make an instance of the subclass. Inherited from the parent class.
my_ice_cream = IceCreamStand("Straciatella", "Ice-cream")
my_ice_cream.describe_restaurant()
my_ice_cream.get_flavors()





