import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """Test for 'name_function.py"""

    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name("janis", "joplin")  # Try section.
        self.assertEqual(formatted_name, "Janis Joplin")  # Test section.

    def test_first_middle_last_name(self):
        """Do names like 'Wolfgang Amadeus Mozart work?"""
        formatted_name = get_formatted_name("wolfgang", "mozart", "amadeus")
        self.assertEqual(formatted_name, "Wolfgang Amadeus Mozart")


if __name__ == "__main__":  # If we are running the file from the source.
    unittest.main()  # This run our tests.



