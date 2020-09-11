from random import choice


class Lottery:
    """Represent a Lottery selection."""
    def __init__(self, *ticket):
        """Initialize arguments."""
        self.ticket = list(ticket)
        self.options = (4, 2, 6, 8, 4, 1, 0, 7, 9, 4, "c", "i", "g", "m")
        self.counter = 0
        self.winner = []

    def find_match(self):
        """Find attempts to won."""
        while True:
            self.winner = []
            for selection in range(4):
                self.winner.append(choice(self.options))

            if self.winner != self.ticket:
                self.counter += 1
            else:
                print("\nCongratulations, you won!")
                print(f"The number of attempts were {self.counter}")
                break


# Instance to introduce the ticket.
my_ticket = Lottery(7, "c", 4, "i")
my_ticket.find_match()
print(my_ticket.winner)
