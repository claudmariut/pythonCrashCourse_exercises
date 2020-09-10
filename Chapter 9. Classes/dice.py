from random import randint
"""Represent results from rolling a dice"""


class Dice:
    """Initialize attributes."""
    def __init__(self, sides=6):
        self.sides = sides

    def roll_dice(self, num_rolls=10):
        """
        Rolls the dice a certain amount of times and displays a random
        number between 1 and the number of sides.
        """
        print(f"\nResults of rolling a {self.sides} sided dice"
              f" {num_rolls} times:")
        for roll in range(num_rolls):
            print(randint(1, self.sides))


# Create instances. 6 sided dice. Roll 10 times.
six_dice = Dice()
six_dice.roll_dice()

ten_dice = Dice(10)
ten_dice.roll_dice()

twenty_dice = Dice(20)
twenty_dice.roll_dice()



