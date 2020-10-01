import unittest
from city_functions import get_city_country


class CityTestCase(unittest.TestCase):
    """Test for city_functions.py"""

    def test_city_country(self):
        """Do values as 'santiago', and 'chile' work?"""
        formatted_out = get_city_country("santiago", "chile")
        self.assertEqual(formatted_out, "Santiago, Chile")

    def test_city_country_population(self):
        """Do values as 'santiago', 'chile', and '50000000' work?"""
        formatted_out = get_city_country("santiago", "chile", "5000000")
        self.assertEqual(formatted_out, "Santiago, Chile - Population 5000000")


if __name__ == "__main__":
    unittest.main()

