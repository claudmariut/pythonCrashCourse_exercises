# Creating and Using a Class
class Dog:
    """A simple attempt to model a dog."""
    # method called automatically in the instance. self = object
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name  # Parameter name assigned to a variable/attribute.
        self.age = age

    def introducing(self):
        """Displays the name and age of the dog"""
        print(f"My dog's name is {self.name}.")
        print(f"My dog is {self.age} years old.")

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")


# Making an instance from a Class.
my_dog = Dog("Willie", 6)
my_dog.sit()
my_dog.roll_over()

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

your_dog = Dog("Lucy", 3)

your_dog.introducing()

