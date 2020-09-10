from restaurant import Restaurant, IceCreamStand

restaurant = Restaurant("Seventh Taste", "Veggie")
restaurant.describe_restaurant()
restaurant.set_number_served(345)
restaurant.increment_number_served(15)

# Make an instance of the subclass. Inherited from the parent class.
my_ice_cream = IceCreamStand("Straciatella", "Ice-cream")
my_ice_cream.describe_restaurant()
my_ice_cream.get_flavors()

