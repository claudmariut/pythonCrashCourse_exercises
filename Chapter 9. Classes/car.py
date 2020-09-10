"""A class that can be used to represent a gas and electric cars."""


class Car:
    """A simple attempt to represent a car"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  # Default value for an attribute.
        self.sizeTank = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage """
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to a given mileage.
        Reject the change if it attempts to roll the odometer back
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading"""
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("The number of miles can not be negative")

    def gas_tank_size(self, tank_size):
        """Prints a statement with the size of the tank"""
        self.sizeTank = tank_size
        print(f"The size of the tank is: {self.sizeTank} liters.")


class Battery:
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=75):
        self.battery_size = battery_size
        self.range = 260

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides"""
        if self.battery_size == 75:
            self.range = 260
        elif self.battery_size == 100:
            self.range = 315

        print(f"This car can go about {self.range} miles on a full charge.")

    def upgrade_battery(self):
        """Updates the battery size to 100"""
        self.battery_size = 100


# Child class. Always in the same file and after the parent class.
class ElectricCar(Car):
    """Representation aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """
        Initialize attributes from the parent class.
        Then initialize attributes specific to an Electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery(75)  # We pass an instance as an argument.

    def gas_tank_size(self, tank_size=None):
        """Electrics cars don't have gas tanks."""
        print("This car does not need a gas tank!")





