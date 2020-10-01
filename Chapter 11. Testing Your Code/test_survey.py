import unittest
from survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    """Test for the class AnonymousSurvey"""

    def setUp(self):
        """
        Create a survey and set of responses for use in all test methods.
        """
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)  # Instance as an attribute.
        self.responses = ["English", "Spanish", "Mandarin"]

    def test_store_single_response(self):
        """Test that a single response is stored properly"""
        self.my_survey.store_responses(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        """Test that three individual responses store properly"""
        for response in self.responses:
            self.my_survey.store_responses(response)
            self.assertIn(response, self.my_survey.responses)


if __name__ == "__main__":
    unittest.main()

