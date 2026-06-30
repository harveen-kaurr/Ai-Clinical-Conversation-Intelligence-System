import unittest

from services.ai_service import AIService


class TestAIService(unittest.TestCase):

    def test_validation_success(self):

        AIService.validate_analysis(
            {
                "conversation_id": "123",
                "transcript": "hello"
            }
        )

    def test_validation_failure(self):

        with self.assertRaises(
            ValueError
        ):

            AIService.validate_analysis(
                {
                    "conversation_id": ""
                }
            )


if __name__ == "__main__":
    unittest.main()