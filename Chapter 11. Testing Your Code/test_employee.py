import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    """Test for Employee"""

    def setUp(self):
        """Initialize instance of tested class as attribute for test methods"""
        self.employee = Employee("Claudiu", "Mariutanu", 95000)

    def test_give_default_raise(self):
        """Test that the default raise is properly added"""
        self.employee.give_raise()
        self.assertEqual(100000, self.employee.salary)

    def test_give_custom_raise(self):
        """Test that a custom raise is properly added"""
        self.employee.give_raise(7000)
        self.assertEqual(102000, self.employee.salary)


if __name__ == "__main__":
    unittest.main()

