class Employee:
    """Represent information about an employee"""

    def __init__(self, first, last, salary):
        """Initialize attributes"""
        self.first = first
        self.last = last
        self.salary = salary

    def give_raise(self, adds=5000):
        """Adds a raise to the annual salary"""
        self.salary += adds

